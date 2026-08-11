"""Reglas del reglamento (paramétricas): regularidad, esfuerzo, cuatrimestres, electivas.

Todo lo que la facultad define y varía entre reglamentos vive acá y sale de
`Config`. Ninguna regla está hardcodeada: los defaults están documentados en
`carrera/datos/config.json` y en `carrera/CARRERA.md`.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import date, timedelta

from .modelo import Calendario, Config, Cuatrimestre, DatosCarrera, Materia, Ventana

# --------------------------------------------------------------------------
# Vigencia de la regularidad (regla 3)
#
# En el reglamento vigente la regularidad NO vence (modo "no_vence", el
# default). El modo "anios" queda implementado y parametrizable por si la
# regla cambia o el sistema se usa en otra facultad.
# --------------------------------------------------------------------------

VIGENTE = "vigente"
POR_VENCER = "por-vencer"
VENCIDA = "vencida"
DESCONOCIDA = "desconocida"
NO_APLICA = "no-aplica"


@dataclass(frozen=True)
class EstadoRegularidad:
    codigo: str
    situacion: str  # vigente | por-vencer | vencida | desconocida | no-aplica
    vence: date | None = None
    dias_restantes: int | None = None
    supuesto: str | None = None

    @property
    def urgente(self) -> bool:
        return self.situacion in (POR_VENCER, VENCIDA)

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "situacion": self.situacion,
            "vence": self.vence.isoformat() if self.vence else None,
            "diasRestantes": self.dias_restantes,
            "supuesto": self.supuesto,
        }


def vencimiento_regularidad(materia: Materia, config: Config) -> tuple[date | None, str | None]:
    """Fecha de vencimiento de la regularidad (solo en modo "anios").

    En modo "no_vence" no hay fecha. En modo "anios": si la materia trae
    `regularidadHasta` se usa ese dato (es un hecho); si no, se calcula desde
    el AÑO de la cursada + `vigencia_regularidad.anios`, arrancando en
    `referencia_mes_dia` (por defecto, fin de ese año).
    """
    cfg = config.vigencia
    if cfg.get("modo") == "no_vence":
        return None, "la regularidad no vence (vigencia_regularidad.modo = no_vence)"
    if materia.regularidad_hasta:
        return materia.regularidad_hasta, "fecha declarada en estado.json"
    if materia.anio is None:
        return None, None
    if cfg.get("modo") != "anios":
        return None, f"modo de vigencia '{cfg.get('modo')}' no implementado"
    mes, dia = str(cfg["referencia_mes_dia"]).split("-")
    inicio = date(int(materia.anio), int(mes), int(dia))
    try:
        vence = inicio.replace(year=inicio.year + int(cfg["anios"]))
    except ValueError:  # 29/02
        vence = inicio.replace(year=inicio.year + int(cfg["anios"]), day=28)
    return vence, (
        f"supuesto: {cfg['anios']} años desde el {cfg['referencia_mes_dia']} de {materia.anio} "
        "(configurable en config.json → vigencia_regularidad)"
    )


def estado_regularidad(materia: Materia, hoy: date, config: Config) -> EstadoRegularidad:
    if materia.estado == "aprobada":
        return EstadoRegularidad(materia.codigo, NO_APLICA)
    if materia.estado not in ("regularizada", "cursando"):
        return EstadoRegularidad(materia.codigo, NO_APLICA)
    if materia.estado == "cursando":
        return EstadoRegularidad(
            materia.codigo, VIGENTE, None, None, "cursando: la regularidad arranca al cerrar la cursada"
        )
    vence, supuesto = vencimiento_regularidad(materia, config)
    if vence is None and config.vigencia.get("modo") == "no_vence":
        return EstadoRegularidad(materia.codigo, VIGENTE, None, None, supuesto)
    if vence is None:
        return EstadoRegularidad(materia.codigo, DESCONOCIDA, None, None, "falta el año de la cursada")
    dias = (vence - hoy).days
    aviso = int(config.vigencia["aviso_por_vencer_dias"])
    if dias < 0:
        situacion = VENCIDA
    elif dias <= aviso:
        situacion = POR_VENCER
    else:
        situacion = VIGENTE
    return EstadoRegularidad(materia.codigo, situacion, vence, dias, supuesto)


def regularidades(datos: DatosCarrera) -> list[EstadoRegularidad]:
    """Estado de regularidad de todas las materias regularizadas, más urgente primero."""
    hoy = datos.calendario.hoy
    salida = [
        estado_regularidad(m, hoy, datos.config)
        for m in datos.materias
        if m.estado in ("regularizada", "cursando")
    ]
    return sorted(
        salida,
        key=lambda e: (e.dias_restantes if e.dias_restantes is not None else 10**6, e.codigo),
    )


def antiguedad_regularidad(materia: Materia, hoy: date) -> int | None:
    """Años (enteros, aproximados) desde que se regularizó la materia.

    Solo tenemos el AÑO de cursada, así que es una cuenta gruesa. Sirve como
    señal de decaimiento: una regularidad de hace 6 años no vence, pero el
    contenido está más olvidado y conviene sacársela de encima antes.
    """
    if materia.estado != "regularizada" or materia.anio is None:
        return None
    return max(0, hoy.year - int(materia.anio))


# --------------------------------------------------------------------------
# Intentos de final (regla real: 4 desaprobados → recursar)
# --------------------------------------------------------------------------

INTENTOS_OK = "ok"
INTENTOS_ATENCION = "atencion"
INTENTOS_ULTIMA_CHANCE = "ultima-chance"
INTENTOS_AGOTADO = "agotado"


@dataclass(frozen=True)
class EstadoIntentos:
    codigo: str
    usados: int
    maximo: int
    situacion: str  # ok | atencion | ultima-chance | agotado

    @property
    def restantes(self) -> int:
        return max(0, self.maximo - self.usados)

    @property
    def mensaje(self) -> str:
        if self.situacion == INTENTOS_AGOTADO:
            return (
                f"{self.usados} de {self.maximo} intentos usados: hay que RECURSAR la materia"
            )
        if self.situacion == INTENTOS_ULTIMA_CHANCE:
            return f"{self.usados} de {self.maximo} intentos usados: el próximo es el ÚLTIMO"
        if self.situacion == INTENTOS_ATENCION:
            return f"{self.usados} de {self.maximo} intentos usados: quedan {self.restantes}"
        return f"sin intentos usados ({self.maximo} disponibles)"

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "usados": self.usados,
            "maximo": self.maximo,
            "restantes": self.restantes,
            "situacion": self.situacion,
            "mensaje": self.mensaje,
        }


def estado_intentos(codigo: str, usados: int, config: Config) -> EstadoIntentos:
    """Clasifica los intentos de final usados contra el tope configurado."""
    cfg = config.intentos
    maximo = int(cfg["maximo"])
    aviso_desde = int(cfg["aviso_desde"])
    if usados >= maximo:
        situacion = INTENTOS_AGOTADO
    elif usados == maximo - 1:
        situacion = INTENTOS_ULTIMA_CHANCE
    elif usados >= aviso_desde:
        situacion = INTENTOS_ATENCION
    else:
        situacion = INTENTOS_OK
    return EstadoIntentos(codigo, usados, maximo, situacion)


def intentos_de_materia(materia: Materia, config: Config) -> EstadoIntentos:
    return estado_intentos(materia.codigo, materia.intentos_final, config)


# --------------------------------------------------------------------------
# Esfuerzo de preparación (funcionalidad A)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Preparacion:
    """Ventana de preparación calculada hacia atrás desde la fecha del final."""

    codigo: str
    horas: float
    dias_utiles: int
    dias_calendario: int
    inicio: date
    fin: date  # el día del examen
    origen_horas: str

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "horas": self.horas,
            "diasUtiles": self.dias_utiles,
            "diasCalendario": self.dias_calendario,
            "inicio": self.inicio.isoformat(),
            "examen": self.fin.isoformat(),
            "origenHoras": self.origen_horas,
        }


def horas_esfuerzo(materia: Materia, config: Config) -> tuple[float, str]:
    """Horas estimadas para preparar el final + de dónde salió el número."""
    por_materia = config.esfuerzo.get("horas_por_materia", {})
    if materia.codigo in por_materia:
        return float(por_materia[materia.codigo]), "override por materia (config.json)"
    por_nivel = config.esfuerzo["horas_por_nivel"]
    horas = por_nivel.get(str(materia.nivel), por_nivel.get(materia.nivel))
    if horas is None:
        horas = max(float(v) for v in por_nivel.values())
        return float(horas), f"sin default para nivel {materia.nivel}: se usó el máximo"
    return float(horas), f"default por nivel {materia.nivel} (config.json)"


def preparacion(materia: Materia, fecha_examen: date, config: Config) -> Preparacion:
    """Calcula hacia atrás desde el examen cuándo hay que empezar a estudiar."""
    horas, origen = horas_esfuerzo(materia, config)
    cfg = config.esfuerzo
    horas_dia = float(cfg["horas_por_dia"]) or 1.0
    dias_utiles = max(math.ceil(horas / horas_dia), int(cfg["dias_minimos_preparacion"]))
    utiles_semana = max(1, min(7, int(cfg["dias_utiles_por_semana"])))
    dias_calendario = math.ceil(dias_utiles * 7 / utiles_semana)
    return Preparacion(
        codigo=materia.codigo,
        horas=horas,
        dias_utiles=dias_utiles,
        dias_calendario=dias_calendario,
        inicio=fecha_examen - timedelta(days=dias_calendario),
        fin=fecha_examen,
        origen_horas=origen,
    )


# --------------------------------------------------------------------------
# Cuatrimestres y ventanas (reglas 4 y 5)
# --------------------------------------------------------------------------


def _md(config: Config, numero: int, extremo: int) -> tuple[int, int]:
    texto = config.rango_cuatrimestre(numero)[extremo]
    mes, dia = texto.split("-")
    return int(mes), int(dia)


def inicio_cuatrimestre(cuatri: Cuatrimestre, config: Config) -> date:
    mes, dia = _md(config, cuatri.numero, 0)
    return date(cuatri.anio, mes, dia)


def fin_cuatrimestre(cuatri: Cuatrimestre, config: Config) -> date:
    mes, dia = _md(config, cuatri.numero, 1)
    return date(cuatri.anio, mes, dia)


def cuatrimestre_de(fecha: date, config: Config) -> tuple[Cuatrimestre, bool]:
    """Cuatrimestre al que pertenece una fecha y si está dentro del dictado.

    Fuera de los rangos de dictado devuelve el cuatrimestre que viene (que es lo
    que importa para planificar), con `en_curso=False`.
    """
    for numero in (1, 2):
        cuatri = Cuatrimestre(fecha.year, numero)
        if inicio_cuatrimestre(cuatri, config) <= fecha <= fin_cuatrimestre(cuatri, config):
            return cuatri, True
    primero = Cuatrimestre(fecha.year, 1)
    if fecha < inicio_cuatrimestre(primero, config):
        return primero, False
    segundo = Cuatrimestre(fecha.year, 2)
    if fecha < inicio_cuatrimestre(segundo, config):
        return segundo, False
    return Cuatrimestre(fecha.year + 1, 1), False


def cuatrimestres_desde(cuatri: Cuatrimestre, cantidad: int) -> list[Cuatrimestre]:
    salida = [cuatri]
    for _ in range(cantidad - 1):
        salida.append(salida[-1].siguiente())
    return salida


def ventanas_efectivas(calendario: Calendario, config: Config, hasta: date) -> list[Ventana]:
    """Ventanas declaradas + ventanas estimadas por plantilla hasta `hasta`.

    Las declaradas mandan: las estimadas solo se generan DESPUÉS de la última
    ventana cargada por el usuario, así nunca duplican ni pisan un dato real.
    """
    declaradas = list(calendario.ventanas)
    corte = max((v.hasta for v in declaradas), default=calendario.hoy)
    plantilla = config.datos["ventanas_tipicas"]["plantilla"]
    estimadas: list[Ventana] = []
    for anio in range(corte.year, hasta.year + 2):
        for item in plantilla:
            mes_d, dia_d = (int(x) for x in str(item["desde"]).split("-"))
            mes_h, dia_h = (int(x) for x in str(item["hasta"]).split("-"))
            desde = date(anio, mes_d, dia_d)
            fin = date(anio, mes_h, dia_h)
            if fin < desde:  # la ventana cruza el año (p. ej. dic → feb)
                fin = date(anio + 1, mes_h, dia_h)
            if desde <= corte or desde > hasta:
                continue
            estimadas.append(
                Ventana(
                    id=str(item["id"]),
                    desde=desde,
                    hasta=fin,
                    llamados=int(item.get("llamados", 1)),
                    estimada=True,
                    especial=bool(item.get("especial", False)),
                )
            )
    return sorted(declaradas + estimadas, key=lambda v: (v.desde, v.id))


def fecha_de_examen(ventana: Ventana, indice_llamado: int, config: Config) -> date:
    """Fecha concreta del final dentro de la ventana, según el llamado asignado."""
    fechas = ventana.fechas_de_llamados()
    if config.finales.get("dia_en_ventana") == "fin":
        fechas = list(reversed(fechas))
    return fechas[min(indice_llamado, len(fechas) - 1)]


def cupo_de_ventana(ventana: Ventana, config: Config) -> int:
    tope = config.finales.get("max_por_ventana")
    if tope is None:
        return max(1, ventana.llamados)
    return max(1, int(tope))


# --------------------------------------------------------------------------
# Electivas (regla 6)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class RequisitoElectivas:
    nivel: int
    requeridas: float
    acumuladas: float

    @property
    def falta(self) -> float:
        return max(0.0, self.requeridas - self.acumuladas)

    @property
    def cumple(self) -> bool:
        return self.acumuladas >= self.requeridas

    def a_dict(self) -> dict:
        return {
            "nivel": self.nivel,
            "requeridas": self.requeridas,
            "acumuladas": self.acumuladas,
            "falta": self.falta,
            "cumple": self.cumple,
        }


@dataclass(frozen=True)
class ResumenElectivas:
    aprobadas: tuple[str, ...]
    horas_aprobadas: float
    horas_en_curso: float
    requisitos: tuple[RequisitoElectivas, ...]
    aviso_unidades: str | None = None

    def a_dict(self) -> dict:
        return {
            "aprobadas": list(self.aprobadas),
            "horasAprobadas": self.horas_aprobadas,
            "horasEnCurso": self.horas_en_curso,
            "requisitos": [r.a_dict() for r in self.requisitos],
            "avisoUnidades": self.aviso_unidades,
        }


def resumen_electivas(datos: DatosCarrera) -> ResumenElectivas:
    """Horas de electivas acumuladas vs. requeridas por nivel."""
    electivas = [m for m in datos.materias if m.electiva]
    aprobadas = [m for m in electivas if m.estado == "aprobada"]
    en_curso = [m for m in electivas if m.estado in ("regularizada", "cursando")]
    total = sum(m.horas_electiva for m in aprobadas)
    requisitos = tuple(
        RequisitoElectivas(nivel, datos.config.horas_requeridas_electivas(nivel), total)
        for nivel in datos.config.niveles_con_electivas()
    )
    valores = sorted({m.horas_electiva for m in electivas if m.horas_electiva}, reverse=True)
    aviso = None
    if len(valores) > 1 and valores[0] >= 10 * valores[-1]:
        aviso = (
            "las horas cargadas mezclan escalas ("
            + ", ".join(f"{m.codigo}={m.horas_electiva:g}" for m in electivas if m.horas_electiva)
            + "): parecen horas totales vs. horas semanales. Unificá el criterio en estado.json "
            "antes de confiar en el acumulado"
        )
    return ResumenElectivas(
        aprobadas=tuple(m.codigo for m in aprobadas),
        horas_aprobadas=total,
        horas_en_curso=sum(m.horas_electiva for m in en_curso),
        requisitos=requisitos,
        aviso_unidades=aviso,
    )
