"""Grafo de correlatividades (DAG): disponibilidad, impacto y orden topológico.

Motor puro: funciones deterministas sobre `DatosCarrera` + `EstadoAcademico`.
Nada de fechas ni de presentación acá — solo la estructura del plan de estudios.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .modelo import Correlativa, DatosCarrera, EstadoAcademico, Materia


@dataclass(frozen=True)
class Disponibilidad:
    """Resultado de evaluar si una materia se puede cursar."""

    codigo: str
    puede: bool
    faltan_regularizar: tuple[str, ...] = ()
    faltan_aprobar: tuple[str, ...] = ()

    @property
    def faltantes(self) -> tuple[str, ...]:
        return self.faltan_regularizar + self.faltan_aprobar

    def motivo(self) -> str:
        if self.puede:
            return "cumple todas las correlativas"
        partes = []
        if self.faltan_regularizar:
            partes.append("falta regularizar " + ", ".join(self.faltan_regularizar))
        if self.faltan_aprobar:
            partes.append("falta aprobar " + ", ".join(self.faltan_aprobar))
        return "; ".join(partes)

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "puede": self.puede,
            "faltanRegularizar": list(self.faltan_regularizar),
            "faltanAprobar": list(self.faltan_aprobar),
            "motivo": self.motivo(),
        }


@dataclass(frozen=True)
class Impacto:
    """Cuántas materias destraba aprobar una materia dada."""

    codigo: str
    inmediatas: tuple[str, ...] = ()  # pasan a cursables apenas se apruebe esta
    directas: tuple[str, ...] = ()  # la tienen como correlativa directa
    transitivas: tuple[str, ...] = ()  # todo lo que cuelga aguas abajo (pendiente)

    @property
    def puntaje(self) -> int:
        """Peso combinado: lo inmediato vale más que lo lejano."""
        return 3 * len(self.inmediatas) + 2 * len(self.directas) + len(self.transitivas)

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "inmediatas": list(self.inmediatas),
            "directas": list(self.directas),
            "transitivas": list(self.transitivas),
            "puntaje": self.puntaje,
        }


class Grafo:
    """DAG de correlatividades del plan."""

    def __init__(self, datos: DatosCarrera):
        self.datos = datos
        self.materias: dict[str, Materia] = datos.por_codigo()
        self.correlativas: dict[str, Correlativa] = {
            codigo: datos.correlativa(codigo) for codigo in self.materias
        }
        self._niveles: dict[str, int] | None = None
        # Aristas inversas: materia → materias que dependen de ella.
        self._dependientes_reg: dict[str, list[str]] = {c: [] for c in self.materias}
        self._dependientes_apr: dict[str, list[str]] = {c: [] for c in self.materias}
        for codigo, corr in self.correlativas.items():
            for req in corr.requiere_regularizadas:
                if req in self._dependientes_reg:
                    self._dependientes_reg[req].append(codigo)
            for req in corr.requiere_aprobadas:
                if req in self._dependientes_apr:
                    self._dependientes_apr[req].append(codigo)

    # -- estructura -------------------------------------------------------

    def codigos(self) -> list[str]:
        return sorted(self.materias)

    def predecesoras(self, codigo: str) -> tuple[str, ...]:
        corr = self.correlativas.get(codigo)
        if corr is None:
            return ()
        vistas: list[str] = []
        for req in corr.todas:
            if req in self.materias and req not in vistas:
                vistas.append(req)
        return tuple(vistas)

    def dependientes(self, codigo: str) -> tuple[str, ...]:
        """Materias que tienen a `codigo` como correlativa (de cualquier tipo)."""
        juntas = dict.fromkeys(
            self._dependientes_reg.get(codigo, []) + self._dependientes_apr.get(codigo, [])
        )
        return tuple(sorted(juntas))

    def dependientes_por_aprobacion(self, codigo: str) -> tuple[str, ...]:
        return tuple(sorted(self._dependientes_apr.get(codigo, [])))

    # -- disponibilidad ---------------------------------------------------

    def disponibilidad(self, codigo: str, estado: EstadoAcademico) -> Disponibilidad:
        """¿Se puede CURSAR `codigo` con este estado académico?

        Regla 1: todas las `requiresRegularized` en al menos `regularizada` y
        todas las `requiresApproved` en `aprobada`.
        """
        corr = self.correlativas.get(codigo)
        if corr is None:
            return Disponibilidad(codigo, True)
        faltan_reg = tuple(
            req for req in corr.requiere_regularizadas if not estado.al_menos(req, "regularizada")
        )
        faltan_apr = tuple(
            req for req in corr.requiere_aprobadas if not estado.al_menos(req, "aprobada")
        )
        return Disponibilidad(codigo, not (faltan_reg or faltan_apr), faltan_reg, faltan_apr)

    def cursables(self, estado: EstadoAcademico) -> list[str]:
        """Materias todavía no arrancadas que ya cumplen correlativas."""
        return [
            codigo
            for codigo in self.codigos()
            if estado.estado(codigo) == "bloqueada"
            and self.disponibilidad(codigo, estado).puede
        ]

    def rendibles(self, estado: EstadoAcademico, incluir_cursando: bool = False) -> list[str]:
        """Materias que pueden rendir final: regularizadas (regla 2).

        Con `incluir_cursando` suma las que están cursando, asumiendo que
        aprueban la cursada antes de la fecha del final.
        """
        objetivo = ("regularizada",) + (("cursando",) if incluir_cursando else ())
        return [c for c in self.codigos() if estado.estado(c) in objetivo]

    # -- impacto ----------------------------------------------------------

    def impacto(self, codigo: str, estado: EstadoAcademico) -> Impacto:
        """Qué destraba aprobar `codigo`, desde el estado actual."""
        hipotetico = estado.copia()
        hipotetico.marcar(codigo, "aprobada")

        inmediatas = tuple(
            dep
            for dep in self.dependientes(codigo)
            if estado.estado(dep) == "bloqueada"
            and not self.disponibilidad(dep, estado).puede
            and self.disponibilidad(dep, hipotetico).puede
        )
        directas = tuple(
            dep for dep in self.dependientes(codigo) if not estado.al_menos(dep, "aprobada")
        )

        # Cierre transitivo aguas abajo, quedándose con lo que sigue pendiente.
        pendientes: list[str] = []
        vistas = {codigo}
        cola = list(self.dependientes(codigo))
        while cola:
            actual = cola.pop(0)
            if actual in vistas:
                continue
            vistas.add(actual)
            if not estado.al_menos(actual, "aprobada"):
                pendientes.append(actual)
            cola.extend(self.dependientes(actual))
        return Impacto(codigo, inmediatas, directas, tuple(sorted(pendientes)))

    # -- orden topológico -------------------------------------------------

    def niveles_topologicos(self) -> dict[str, int]:
        """Profundidad en el DAG: 0 = sin correlativas, n = camino más largo.

        No es el "nivel" del plan de estudios (ese viene dado), sino la capa
        real que impone el grafo.
        """
        if self._niveles is not None:
            return self._niveles
        nivel: dict[str, int] = {}
        pendientes = set(self.codigos())
        vuelta = 0
        while pendientes:
            listas = [
                c
                for c in sorted(pendientes)
                if all(p in nivel for p in self.predecesoras(c) if p in self.materias)
            ]
            if not listas:  # queda un ciclo: lo cortamos para no colgarnos
                for c in sorted(pendientes):
                    nivel[c] = vuelta
                break
            for c in listas:
                previos = [nivel[p] for p in self.predecesoras(c) if p in nivel]
                nivel[c] = max(previos) + 1 if previos else 0
            pendientes -= set(listas)
            vuelta += 1
        self._niveles = nivel
        return nivel

    def orden_topologico(self) -> list[str]:
        niveles = self.niveles_topologicos()
        return sorted(self.codigos(), key=lambda c: (niveles[c], self.materias[c].nivel, c))

    def ciclos(self) -> list[list[str]]:
        """Detecta ciclos (el plan debería ser un DAG)."""
        estado: dict[str, int] = {}  # 0 sin visitar, 1 en camino, 2 cerrado
        encontrados: list[list[str]] = []

        def visitar(nodo: str, camino: list[str]) -> None:
            estado[nodo] = 1
            for previo in self.predecesoras(nodo):
                if estado.get(previo, 0) == 0:
                    visitar(previo, camino + [previo])
                elif estado.get(previo) == 1:
                    corte = camino.index(previo) if previo in camino else 0
                    encontrados.append(camino[corte:] + [previo])
            estado[nodo] = 2

        for codigo in self.codigos():
            if estado.get(codigo, 0) == 0:
                visitar(codigo, [codigo])
        return encontrados

    # -- cadena crítica ---------------------------------------------------

    def cadena_mas_larga(self, codigo: str, estado: EstadoAcademico) -> list[str]:
        """Cadena de materias PENDIENTES más larga que hay que hacer antes de `codigo`.

        Es el piso teórico de cuatrimestres para llegar a esa materia: cada
        eslabón necesita al menos un cuatrimestre (regularizar habilita al
        siguiente cuatrimestre; aprobar, la ventana de finales inmediata).
        """
        memo: dict[str, list[str]] = {}

        def resolver(actual: str) -> list[str]:
            if actual in memo:
                return memo[actual]
            memo[actual] = []  # corta ciclos
            if estado.al_menos(actual, "aprobada"):
                memo[actual] = []
                return memo[actual]
            mejor: list[str] = []
            for previo in self.predecesoras(actual):
                if estado.al_menos(previo, "aprobada"):
                    continue
                # Si ya está regularizada solo falta el final: no suma cuatrimestre de cursada.
                candidata = resolver(previo)
                if estado.estado(previo) not in ("regularizada", "cursando"):
                    candidata = candidata + [previo]
                if len(candidata) > len(mejor):
                    mejor = candidata
            memo[actual] = mejor
            return mejor

        cadena = resolver(codigo)
        if not estado.al_menos(codigo, "regularizada"):
            cadena = cadena + [codigo]
        return cadena

    def terminales(self) -> list[str]:
        """Materias de las que no depende ninguna otra (típicamente PFinal/PPS)."""
        return [c for c in self.codigos() if not self.dependientes(c)]


# --------------------------------------------------------------------------
# Validación estructural de los datos
# --------------------------------------------------------------------------


@dataclass
class Problema:
    """Inconsistencia detectada en los datos de entrada."""

    nivel: str  # error | aviso
    codigo: str
    mensaje: str

    def a_dict(self) -> dict:
        return {"nivel": self.nivel, "codigo": self.codigo, "mensaje": self.mensaje}


@dataclass
class Validacion:
    problemas: list[Problema] = field(default_factory=list)

    @property
    def errores(self) -> list[Problema]:
        return [p for p in self.problemas if p.nivel == "error"]

    @property
    def avisos(self) -> list[Problema]:
        return [p for p in self.problemas if p.nivel == "aviso"]

    @property
    def ok(self) -> bool:
        return not self.errores

    def a_dict(self) -> dict:
        return {
            "ok": self.ok,
            "errores": [p.a_dict() for p in self.errores],
            "avisos": [p.a_dict() for p in self.avisos],
        }


def validar(datos: DatosCarrera) -> Validacion:
    """Chequea coherencia entre los tres inputs antes de planificar nada."""
    v = Validacion()
    grafo = Grafo(datos)
    codigos = set(grafo.materias)

    # 1. Correlativas que apuntan a materias inexistentes.
    for codigo, corr in datos.correlativas.items():
        if codigo not in codigos:
            v.problemas.append(
                Problema("error", codigo, f"correlativas.json define '{codigo}', que no está en estado.json")
            )
        for req in corr.todas:
            if req not in codigos:
                v.problemas.append(
                    Problema("error", codigo, f"requiere '{req}', que no existe en estado.json")
                )

    # 2. Ciclos.
    for ciclo in grafo.ciclos():
        v.problemas.append(
            Problema("error", ciclo[0], "ciclo de correlativas: " + " → ".join(ciclo))
        )

    # 3. Estados incoherentes con las correlativas (aprobada sin correlativas aprobadas).
    estado = datos.estado_inicial()
    for codigo in grafo.codigos():
        if estado.al_menos(codigo, "regularizada"):
            disp = grafo.disponibilidad(codigo, estado)
            if not disp.puede:
                v.problemas.append(
                    Problema(
                        "aviso",
                        codigo,
                        f"figura como {estado.estado(codigo)} pero {disp.motivo()} "
                        "(equivalencia, excepción o dato viejo: revisá)",
                    )
                )

    # 4. Ventanas del calendario con candidatas que no se pueden rendir.
    for ventana in datos.calendario.ventanas:
        for candidata in ventana.candidatas:
            if candidata not in codigos:
                v.problemas.append(
                    Problema("error", candidata, f"la ventana '{ventana.id}' lista una materia inexistente")
                )
            elif not estado.al_menos(candidata, "regularizada") and estado.estado(candidata) != "cursando":
                v.problemas.append(
                    Problema(
                        "aviso",
                        candidata,
                        f"la ventana '{ventana.id}' la lista como candidata pero está "
                        f"'{estado.estado(candidata)}' (para rendir final hay que estar regularizada)",
                    )
                )

    # 5. Parciales de materias que no están cursando.
    for parcial in datos.calendario.parciales:
        if parcial.codigo not in codigos:
            v.problemas.append(
                Problema("error", parcial.codigo, "hay parciales de una materia que no existe en estado.json")
            )
        elif estado.estado(parcial.codigo) != "cursando":
            v.problemas.append(
                Problema(
                    "aviso",
                    parcial.codigo,
                    f"tiene parciales cargados pero su estado es '{estado.estado(parcial.codigo)}'",
                )
            )

    # 6. Contadores declarados vs. reales.
    declarado = (datos.resumen_declarado or {}).get("counts", {})
    if declarado:
        for clave, estado_real in (
            ("aprobadas", "aprobada"),
            ("regularizadas", "regularizada"),
            ("cursando", "cursando"),
            ("bloqueadas", "bloqueada"),
        ):
            esperado = declarado.get(clave)
            real = sum(1 for m in datos.materias if m.estado == estado_real)
            if esperado is not None and int(esperado) != real:
                v.problemas.append(
                    Problema(
                        "aviso",
                        "-",
                        f"summary.counts.{clave} dice {esperado} y en subjects hay {real}",
                    )
                )
        total = declarado.get("total")
        if total is not None and int(total) != len(datos.materias):
            v.problemas.append(
                Problema("aviso", "-", f"summary.counts.total dice {total} y hay {len(datos.materias)} materias")
            )

    # 7. Referencias del plan manual (tablero) a materias inexistentes.
    manual = datos.plan_manual
    referencias = (
        list(manual.cursadas)
        + list(manual.finales)
        + list(manual.promociones)
        + list(manual.intentos)
    )
    for codigo in dict.fromkeys(referencias):
        if codigo not in codigos:
            v.problemas.append(
                Problema(
                    "error",
                    codigo,
                    "plan-manual.json lo menciona pero no existe en estado.json",
                )
            )
    for codigo in manual.promociones:
        if codigo in codigos and datos.materia(codigo).estado in ("regularizada", "aprobada"):
            v.problemas.append(
                Problema(
                    "aviso",
                    codigo,
                    "está marcada como promoción pero su cursada ya cerró: la promoción se "
                    "gana durante la cursada (solo vale si la recursás)",
                )
            )

    # 8. Unidades sospechosas en horas de electivas.
    horas = sorted({m.horas_electiva for m in datos.materias if m.electiva and m.horas_electiva}, reverse=True)
    if len(horas) > 1 and horas[0] >= 10 * horas[-1]:
        v.problemas.append(
            Problema(
                "aviso",
                "electivas",
                f"las horas de electivas mezclan escalas ({', '.join(str(h) for h in horas)}): "
                "parecen totales vs. semanales. Unificá el criterio o el acumulado no significa nada",
            )
        )

    return v
