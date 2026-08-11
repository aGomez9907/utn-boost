"""Modelo de dominio del planificador de carrera.

Acá viven las estructuras de datos (materias, correlativas, calendario, config),
la carga/validación de los tres archivos de entrada y el snapshot de estado
académico que usa la simulación. Todo determinista y sin efectos de I/O más allá
de leer los JSON: es la base del motor puro.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Iterable

# --------------------------------------------------------------------------
# Estados y su orden (bloqueada < cursando < regularizada < aprobada)
# --------------------------------------------------------------------------

ESTADOS: tuple[str, ...] = ("bloqueada", "cursando", "regularizada", "aprobada")
ORDEN_ESTADO: dict[str, int] = {estado: i for i, estado in enumerate(ESTADOS)}

DURACIONES: tuple[str, ...] = ("cuatrimestral", "anual")


class ErrorDeDatos(Exception):
    """Los datos de entrada son inconsistentes al punto de no poder planificar."""


# --------------------------------------------------------------------------
# Entidades
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Materia:
    """Una materia del plan con su estado académico actual."""

    codigo: str
    nombre: str
    nivel: int
    estado: str
    nota: int | None = None
    anio: int | None = None
    electiva: bool = False
    horas_electiva: float = 0.0
    duracion: str = "cuatrimestral"
    slug: str | None = None  # carpeta en materias/ (para enganchar con las skills)
    regularidad_hasta: date | None = None  # solo se usa si vigencia.modo = "anios"
    intentos_final: int = 0  # finales ya rendidos y desaprobados de esta materia
    promocionable: bool | None = None  # la cátedra ofrece promoción (None = sin dato)
    asumir_promocion: bool = False  # el plan asume que promociona (sin final)

    @property
    def es_anual(self) -> bool:
        return self.duracion == "anual"

    def al_menos(self, estado: str) -> bool:
        return ORDEN_ESTADO[self.estado] >= ORDEN_ESTADO[estado]


@dataclass(frozen=True)
class Correlativa:
    """Requisitos para poder CURSAR una materia."""

    codigo: str
    requiere_regularizadas: tuple[str, ...] = ()
    requiere_aprobadas: tuple[str, ...] = ()

    @property
    def todas(self) -> tuple[str, ...]:
        return self.requiere_regularizadas + self.requiere_aprobadas


@dataclass(frozen=True)
class Ventana:
    """Ventana (turno o mesa) de exámenes finales."""

    id: str
    desde: date
    hasta: date
    llamados: int = 1
    candidatas: tuple[str, ...] = ()
    estimada: bool = False  # True = generada por plantilla, no declarada por el usuario
    especial: bool = False  # mesa especial: pocas materias aplican, no se auto-asigna

    @property
    def anio(self) -> int:
        return self.desde.year

    @property
    def clave(self) -> str:
        """Identificador estable entre corridas ('sep-2026'): lo usan los pins."""
        return f"{self.id}-{self.anio}"

    @property
    def etiqueta(self) -> str:
        sufijos = [s for s in ("esp." if self.especial else "", "est." if self.estimada else "") if s]
        return f"{self.id} {self.anio}" + (f" ({', '.join(sufijos)})" if sufijos else "")

    def fechas_de_llamados(self) -> list[date]:
        """Reparte los llamados de la ventana entre `desde` y `hasta`.

        Con 1 llamado devuelve `desde`; con N > 1, N fechas equiespaciadas
        (la primera en `desde`, la última en `hasta`).
        """
        if self.llamados <= 1:
            return [self.desde]
        span = (self.hasta - self.desde).days
        return [
            self.desde + timedelta(days=round(span * i / (self.llamados - 1)))
            for i in range(self.llamados)
        ]


@dataclass(frozen=True)
class Parcial:
    """Un parcial de una materia que se está cursando."""

    codigo: str
    nombre: str
    numero: int
    fecha: date

    @property
    def etiqueta(self) -> str:
        return f"{self.codigo} P{self.numero}"


@dataclass(frozen=True)
class Calendario:
    hoy: date
    ventanas: tuple[Ventana, ...] = ()
    parciales: tuple[Parcial, ...] = ()

    def ventana(self, id_ventana: str, anio: int | None = None) -> Ventana | None:
        for v in self.ventanas:
            if v.id == id_ventana and (anio is None or v.anio == anio):
                return v
        return None


@dataclass(frozen=True)
class Cuatrimestre:
    """Un cuatrimestre calendario (1C/2C de un año)."""

    anio: int
    numero: int  # 1 | 2

    @property
    def etiqueta(self) -> str:
        return f"{self.numero}C {self.anio}"

    @property
    def clave(self) -> str:
        return f"{self.numero}C-{self.anio}"

    def siguiente(self) -> "Cuatrimestre":
        if self.numero == 1:
            return Cuatrimestre(self.anio, 2)
        return Cuatrimestre(self.anio + 1, 1)

    def __lt__(self, otro: "Cuatrimestre") -> bool:
        return (self.anio, self.numero) < (otro.anio, otro.numero)

    @classmethod
    def desde_clave(cls, clave: str) -> "Cuatrimestre":
        """Parsea '1C-2027' / '2C2027' / '2027-1C'."""
        limpio = clave.strip().upper().replace(" ", "").replace("-", "").replace("_", "")
        for numero in (1, 2):
            marca = f"{numero}C"
            if marca in limpio:
                anio_txt = limpio.replace(marca, "")
                if anio_txt.isdigit() and len(anio_txt) == 4:
                    return cls(int(anio_txt), numero)
        raise ErrorDeDatos(f"No entiendo el cuatrimestre '{clave}' (usá '1C-2027').")


# --------------------------------------------------------------------------
# Configuración
# --------------------------------------------------------------------------

DEFAULTS: dict[str, Any] = {
    # La regularidad NO vence en este reglamento (dato confirmado por el usuario).
    # El modo "anios" queda disponible por si la regla cambia o para otra facultad.
    "vigencia_regularidad": {
        "modo": "no_vence",
        "anios": 5,
        "referencia_mes_dia": "12-31",
        "aviso_por_vencer_dias": 365,
        "bloquear_por_vencimiento": False,
    },
    # Regla real: 4 finales desaprobados de la misma materia → hay que recursarla.
    "intentos_final": {
        "maximo": 4,
        "aviso_desde": 2,
    },
    "esfuerzo": {
        "horas_por_nivel": {"1": 45, "2": 40, "3": 35, "4": 30, "5": 25},
        "horas_por_materia": {},
        "horas_por_dia": 3,
        "dias_utiles_por_semana": 6,
        "dias_minimos_preparacion": 5,
    },
    "finales": {
        "dia_en_ventana": "inicio",
        "max_por_ventana": None,
        "dias_minimos_entre_finales": 7,
        "bloqueo_parcial_dias_antes": 5,
        "bloqueo_parcial_dias_despues": 1,
        "asumir_regulariza_cursando": True,
        "asumir_aprueba_final": True,
        # Las mesas especiales (abril/octubre) aplican a pocas materias: el motor
        # no las llena solo; entran solo candidatas declaradas o pins del tablero.
        "usar_mesas_especiales": False,
    },
    "cursada": {
        "max_materias_por_cuatrimestre": 5,
        "anual_empieza_en_cuatrimestre": 1,
        "asumir_aprueba_cursada": True,
        # Default conservador: sin promoción salvo que la materia lo declare
        # (asumirPromocion en estado.json o promociones en plan-manual.json).
        "asumir_promocion": False,
    },
    "cuatrimestres": {
        "1": {"inicio": "03-01", "fin": "07-15"},
        "2": {"inicio": "08-01", "fin": "11-30"},
    },
    # Calendario académico real UTN (se repite todos los años; MM-DD).
    "ventanas_tipicas": {
        "plantilla": [
            {"id": "feb-mar", "desde": "02-10", "hasta": "03-06", "llamados": 3},
            {"id": "abril", "desde": "04-20", "hasta": "04-24", "llamados": 1, "especial": True},
            {"id": "mayo", "desde": "05-19", "hasta": "05-20", "llamados": 1},
            {"id": "jul-1", "desde": "07-13", "hasta": "07-18", "llamados": 1},
            {"id": "jul-2", "desde": "07-27", "hasta": "08-01", "llamados": 1},
            {"id": "sep", "desde": "09-22", "hasta": "09-23", "llamados": 1},
            {"id": "oct", "desde": "10-26", "hasta": "10-30", "llamados": 1, "especial": True},
            {"id": "dic", "desde": "12-01", "hasta": "12-22", "llamados": 3},
        ]
    },
    "electivas": {"horas_requeridas_por_nivel": {"3": 6, "4": 12, "5": 24}},
    "duracion_por_materia": {"PFinal": "anual"},
    "scoring": {
        "pesos": {"urgencia": 0.25, "impacto": 0.35, "proximidad": 0.25, "esfuerzo": 0.15},
        "horizonte_urgencia_dias": 1095,
        "horizonte_antiguedad_anios": 6,
        "horizonte_proximidad_dias": 365,
        "esfuerzo_maximo_horas": 60,
    },
    "horizonte": {
        "max_cuatrimestres": 24,
        "escenarios_materias_por_cuatrimestre": [3, 4, 5],
    },
    "objetivos": {
        "horas_por_dia_tope": 8,
        "max_materias_por_cuatrimestre_tope": 8,
    },
}


def _sin_comentarios(valor: Any) -> Any:
    """Saca las claves `_doc` / `_comentario` que usamos para documentar el JSON."""
    if isinstance(valor, dict):
        return {k: _sin_comentarios(v) for k, v in valor.items() if not k.startswith("_")}
    if isinstance(valor, list):
        return [_sin_comentarios(v) for v in valor]
    return valor


def _merge(base: dict[str, Any], encima: dict[str, Any]) -> dict[str, Any]:
    """Merge recursivo: `encima` pisa a `base` clave por clave."""
    salida = dict(base)
    for clave, valor in encima.items():
        if isinstance(valor, dict) and isinstance(salida.get(clave), dict):
            salida[clave] = _merge(salida[clave], valor)
        else:
            salida[clave] = valor
    return salida


@dataclass(frozen=True)
class Config:
    """Parámetros de reglas. Todo configurable, con defaults documentados."""

    datos: dict[str, Any] = field(default_factory=lambda: _sin_comentarios(DEFAULTS))

    @classmethod
    def desde_dict(cls, crudo: dict[str, Any] | None) -> "Config":
        base = _sin_comentarios(DEFAULTS)
        if not crudo:
            return cls(base)
        return cls(_merge(base, _sin_comentarios(crudo)))

    def con(self, **secciones: dict[str, Any]) -> "Config":
        """Devuelve una copia con algunas claves pisadas (para escenarios)."""
        return Config(_merge(self.datos, secciones))

    # -- accesos tipados --------------------------------------------------
    @property
    def vigencia(self) -> dict[str, Any]:
        return self.datos["vigencia_regularidad"]

    @property
    def intentos(self) -> dict[str, Any]:
        return self.datos["intentos_final"]

    @property
    def esfuerzo(self) -> dict[str, Any]:
        return self.datos["esfuerzo"]

    @property
    def finales(self) -> dict[str, Any]:
        return self.datos["finales"]

    @property
    def cursada(self) -> dict[str, Any]:
        return self.datos["cursada"]

    @property
    def scoring(self) -> dict[str, Any]:
        return self.datos["scoring"]

    @property
    def horizonte(self) -> dict[str, Any]:
        return self.datos["horizonte"]

    @property
    def max_materias_por_cuatrimestre(self) -> int:
        return int(self.cursada["max_materias_por_cuatrimestre"])

    def horas_requeridas_electivas(self, nivel: int) -> float:
        tabla = self.datos["electivas"]["horas_requeridas_por_nivel"]
        return float(tabla.get(str(nivel), tabla.get(nivel, 0)))

    def niveles_con_electivas(self) -> list[int]:
        tabla = self.datos["electivas"]["horas_requeridas_por_nivel"]
        return sorted(int(k) for k in tabla)

    def rango_cuatrimestre(self, numero: int) -> tuple[str, str]:
        cfg = self.datos["cuatrimestres"][str(numero)]
        return cfg["inicio"], cfg["fin"]


# --------------------------------------------------------------------------
# Snapshot de estado académico (lo que muta la simulación)
# --------------------------------------------------------------------------


@dataclass
class EstadoAcademico:
    """Foto mutable del estado de todas las materias en un instante dado.

    La simulación clona este objeto y lo va avanzando; el motor nunca toca las
    `Materia` originales (son inmutables).
    """

    estados: dict[str, str]
    regularizada_desde: dict[str, date] = field(default_factory=dict)
    aprobada_desde: dict[str, date] = field(default_factory=dict)
    intentos: dict[str, int] = field(default_factory=dict)  # finales desaprobados

    @classmethod
    def desde_materias(cls, materias: Iterable[Materia]) -> "EstadoAcademico":
        return cls(
            estados={m.codigo: m.estado for m in materias},
            intentos={m.codigo: m.intentos_final for m in materias if m.intentos_final},
        )

    def copia(self) -> "EstadoAcademico":
        return EstadoAcademico(
            estados=dict(self.estados),
            regularizada_desde=dict(self.regularizada_desde),
            aprobada_desde=dict(self.aprobada_desde),
            intentos=dict(self.intentos),
        )

    def intentos_de(self, codigo: str) -> int:
        return self.intentos.get(codigo, 0)

    def estado(self, codigo: str) -> str:
        return self.estados.get(codigo, "bloqueada")

    def al_menos(self, codigo: str, estado: str) -> bool:
        return ORDEN_ESTADO[self.estado(codigo)] >= ORDEN_ESTADO[estado]

    def marcar(self, codigo: str, estado: str, cuando: date | None = None) -> None:
        """Avanza el estado de una materia (nunca retrocede)."""
        if ORDEN_ESTADO[estado] < ORDEN_ESTADO[self.estado(codigo)]:
            return
        self.estados[codigo] = estado
        if cuando is not None:
            if estado == "regularizada":
                self.regularizada_desde.setdefault(codigo, cuando)
            elif estado == "aprobada":
                self.aprobada_desde.setdefault(codigo, cuando)
                self.regularizada_desde.setdefault(codigo, cuando)

    def codigos_en(self, estado: str) -> list[str]:
        return sorted(c for c, e in self.estados.items() if e == estado)


# --------------------------------------------------------------------------
# Bundle de datos + carga
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Objetivo:
    """Un target declarado por el usuario (funcionalidad D)."""

    id: str
    tipo: str  # aprobar | cursar | recibirme
    materia: str | None = None
    ventana: str | None = None
    cuatrimestre: str | None = None
    antes_de: date | None = None
    nota: str | None = None


@dataclass(frozen=True)
class PlanManual:
    """Decisiones fijadas a mano en el tablero (carrera/datos/plan-manual.json).

    Son *pins*: la simulación los respeta en vez de decidir sola, y reporta como
    violación todo pin que rompa una regla (correlativa, cupo, regularización).

      cursadas:    codigo → clave de cuatrimestre ("1C-2027")
      finales:     codigo → clave de mesa ("dic-2026", ver Ventana.clave)
      promociones: materias que se asume que promocionan (sin final)
      intentos:    codigo → finales ya desaprobados (pisa intentosFinal de estado.json)
    """

    cursadas: dict[str, str] = field(default_factory=dict)
    finales: dict[str, str] = field(default_factory=dict)
    promociones: tuple[str, ...] = ()
    intentos: dict[str, int] = field(default_factory=dict)
    max_materias: int | None = None
    generado: str | None = None

    @property
    def vacio(self) -> bool:
        return not (self.cursadas or self.finales or self.promociones or self.intentos)

    def a_dict(self) -> dict:
        return {
            "generado": self.generado,
            "cursadas": dict(self.cursadas),
            "finales": dict(self.finales),
            "promociones": list(self.promociones),
            "intentosFinal": dict(self.intentos),
            "maxMateriasPorCuatrimestre": self.max_materias,
        }


@dataclass(frozen=True)
class DatosCarrera:
    """Los tres inputs ya parseados + config + objetivos + plan manual."""

    plan: str
    carrera: str
    materias: tuple[Materia, ...]
    correlativas: dict[str, Correlativa]
    calendario: Calendario
    config: Config
    objetivos: tuple[Objetivo, ...] = ()
    plan_manual: PlanManual = field(default_factory=PlanManual)
    resumen_declarado: dict[str, Any] = field(default_factory=dict)

    def materia(self, codigo: str) -> Materia:
        for m in self.materias:
            if m.codigo == codigo:
                return m
        raise ErrorDeDatos(f"No existe la materia '{codigo}' en estado.json.")

    def existe(self, codigo: str) -> bool:
        return any(m.codigo == codigo for m in self.materias)

    def por_codigo(self) -> dict[str, Materia]:
        return {m.codigo: m for m in self.materias}

    def correlativa(self, codigo: str) -> Correlativa:
        return self.correlativas.get(codigo, Correlativa(codigo))

    def estado_inicial(self) -> EstadoAcademico:
        return EstadoAcademico.desde_materias(self.materias)

    def promocion_asumida(self, codigo: str) -> bool:
        """¿El plan asume que esta materia se promociona (sin final)?

        Solo aplica a materias `cursando` o todavía sin cursar: la promoción se
        gana con los parciales DURANTE la cursada; una ya regularizada solo
        puede aprobar por final. Lo activan `asumirPromocion` en estado.json,
        la lista `promociones` del plan manual, o el default global
        `cursada.asumir_promocion`.
        """
        materia = self.materia(codigo)
        if materia.estado not in ("cursando", "bloqueada"):
            return False
        return (
            materia.asumir_promocion
            or codigo in self.plan_manual.promociones
            or bool(self.config.cursada["asumir_promocion"])
        )

    def con_config(self, config: Config) -> "DatosCarrera":
        return replace(self, config=config)

    def con_hoy(self, hoy: date) -> "DatosCarrera":
        cal = Calendario(hoy=hoy, ventanas=self.calendario.ventanas, parciales=self.calendario.parciales)
        return replace(self, calendario=cal)


def _fecha(valor: Any, contexto: str) -> date:
    try:
        return date.fromisoformat(str(valor))
    except (TypeError, ValueError) as exc:
        raise ErrorDeDatos(f"Fecha inválida en {contexto}: {valor!r} (usá AAAA-MM-DD).") from exc


def parsear_materias(crudo: dict[str, Any], config: Config) -> tuple[Materia, ...]:
    duracion_cfg = config.datos["duracion_por_materia"]
    materias: list[Materia] = []
    for item in crudo.get("subjects", []):
        codigo = str(item["code"])
        estado = str(item.get("status", "bloqueada"))
        if estado not in ORDEN_ESTADO:
            raise ErrorDeDatos(
                f"Estado desconocido '{estado}' en {codigo}. Válidos: {', '.join(ESTADOS)}."
            )
        duracion = str(item.get("duration") or duracion_cfg.get(codigo, "cuatrimestral"))
        if duracion not in DURACIONES:
            raise ErrorDeDatos(f"Duración desconocida '{duracion}' en {codigo}.")
        vence = item.get("regularidadHasta")
        promocionable = item.get("promotable", item.get("promocionable"))
        materias.append(
            Materia(
                codigo=codigo,
                nombre=str(item.get("name", codigo)),
                nivel=int(item.get("level", 0)),
                estado=estado,
                nota=item.get("grade"),
                anio=item.get("year"),
                electiva=bool(item.get("elective", False)),
                horas_electiva=float(item.get("electiveHours") or 0),
                duracion=duracion,
                slug=item.get("slug"),
                regularidad_hasta=_fecha(vence, f"{codigo}.regularidadHasta") if vence else None,
                intentos_final=int(item.get("intentosFinal") or 0),
                promocionable=None if promocionable is None else bool(promocionable),
                asumir_promocion=bool(item.get("asumirPromocion", False)),
            )
        )
    if not materias:
        raise ErrorDeDatos("estado.json no tiene materias (`subjects` vacío).")
    return tuple(materias)


def parsear_correlativas(crudo: list[dict[str, Any]]) -> dict[str, Correlativa]:
    salida: dict[str, Correlativa] = {}
    for item in crudo:
        codigo = str(item["code"])
        salida[codigo] = Correlativa(
            codigo=codigo,
            requiere_regularizadas=tuple(item.get("requiresRegularized", []) or ()),
            requiere_aprobadas=tuple(item.get("requiresApproved", []) or ()),
        )
    return salida


def parsear_calendario(crudo: dict[str, Any]) -> Calendario:
    ventanas = [
        Ventana(
            id=str(v["id"]),
            desde=_fecha(v["from"], f"ventana {v.get('id')}"),
            hasta=_fecha(v.get("to", v["from"]), f"ventana {v.get('id')}"),
            llamados=int(v.get("calls", 1)),
            candidatas=tuple(v.get("candidateSubjects", []) or ()),
            especial=bool(v.get("special", v.get("especial", False))),
        )
        for v in crudo.get("finalExamWindows", [])
    ]
    parciales = [
        Parcial(
            codigo=str(m["code"]),
            nombre=str(m.get("name", m["code"])),
            numero=int(examen.get("n", i + 1)),
            fecha=_fecha(examen["date"], f"parcial de {m.get('code')}"),
        )
        for m in crudo.get("midterms", [])
        for i, examen in enumerate(m.get("exams", []))
    ]
    return Calendario(
        hoy=_fecha(crudo.get("today", date.today().isoformat()), "calendario.today"),
        ventanas=tuple(sorted(ventanas, key=lambda v: (v.desde, v.id))),
        parciales=tuple(sorted(parciales, key=lambda p: (p.fecha, p.codigo))),
    )


def parsear_plan_manual(crudo: dict[str, Any] | None) -> PlanManual:
    if not crudo:
        return PlanManual()
    tope = crudo.get("maxMateriasPorCuatrimestre")
    return PlanManual(
        cursadas={str(k): str(v) for k, v in (crudo.get("cursadas") or {}).items()},
        finales={str(k): str(v) for k, v in (crudo.get("finales") or {}).items()},
        promociones=tuple(crudo.get("promociones") or ()),
        intentos={str(k): int(v) for k, v in (crudo.get("intentosFinal") or {}).items()},
        max_materias=int(tope) if tope else None,
        generado=crudo.get("generado"),
    )


def parsear_objetivos(crudo: list[dict[str, Any]] | None) -> tuple[Objetivo, ...]:
    if not crudo:
        return ()
    salida = []
    for i, item in enumerate(crudo):
        antes = item.get("antesDe") or item.get("antes_de")
        salida.append(
            Objetivo(
                id=str(item.get("id", f"objetivo-{i + 1}")),
                tipo=str(item["tipo"]),
                materia=item.get("materia"),
                ventana=item.get("ventana"),
                cuatrimestre=item.get("cuatrimestre"),
                antes_de=_fecha(antes, "objetivo.antesDe") if antes else None,
                nota=item.get("nota"),
            )
        )
    return tuple(salida)


def _leer_json(ruta: Path, obligatorio: bool = True) -> Any:
    if not ruta.exists():
        if obligatorio:
            raise ErrorDeDatos(f"Falta el archivo {ruta}.")
        return None
    try:
        return json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ErrorDeDatos(f"{ruta} no es JSON válido: {exc}") from exc


def cargar(directorio: Path | str) -> DatosCarrera:
    """Carga los tres inputs (+ config, objetivos y plan manual) desde una carpeta."""
    base = Path(directorio)
    crudo_estado = _leer_json(base / "estado.json")
    crudo_correlativas = _leer_json(base / "correlativas.json")
    crudo_calendario = _leer_json(base / "calendario.json")
    config = Config.desde_dict(_leer_json(base / "config.json", obligatorio=False))
    objetivos = parsear_objetivos(_leer_json(base / "objetivos.json", obligatorio=False))
    plan_manual = parsear_plan_manual(_leer_json(base / "plan-manual.json", obligatorio=False))

    materias = parsear_materias(crudo_estado, config)
    if plan_manual.intentos:
        # Los intentos anotados en el tablero pisan los de estado.json.
        materias = tuple(
            replace(m, intentos_final=plan_manual.intentos[m.codigo])
            if m.codigo in plan_manual.intentos
            else m
            for m in materias
        )

    return DatosCarrera(
        plan=str(crudo_estado.get("plan", "")),
        carrera=str(crudo_estado.get("career", "")),
        materias=materias,
        correlativas=parsear_correlativas(crudo_correlativas),
        calendario=parsear_calendario(crudo_calendario),
        config=config,
        objetivos=objetivos,
        plan_manual=plan_manual,
        resumen_declarado=crudo_estado.get("summary", {}) or {},
    )
