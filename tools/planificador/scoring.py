"""Score de prioridad de finales, con desglose explicable (funcionalidad B).

El número final no sirve solo: cada componente se devuelve con su valor crudo,
su normalización, su peso y cuánto aportó. Si el ranking sorprende, se puede
auditar sin leer el código.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from .grafo import Grafo
from .modelo import DatosCarrera, EstadoAcademico
from .reglas import (
    VENCIDA,
    antiguedad_regularidad,
    estado_intentos,
    estado_regularidad,
    horas_esfuerzo,
)


def _acotar(valor: float) -> float:
    return max(0.0, min(1.0, valor))


@dataclass(frozen=True)
class Componente:
    nombre: str
    crudo: str  # el dato real, legible ("vence en 142 días")
    normalizado: float  # 0..1
    peso: float

    @property
    def aporte(self) -> float:
        return round(self.normalizado * self.peso * 100, 1)

    def a_dict(self) -> dict:
        return {
            "nombre": self.nombre,
            "crudo": self.crudo,
            "normalizado": round(self.normalizado, 3),
            "peso": self.peso,
            "aporte": self.aporte,
        }


@dataclass(frozen=True)
class Score:
    codigo: str
    total: float
    componentes: tuple[Componente, ...]

    def explicacion(self) -> str:
        partes = [f"{c.nombre} {c.aporte:g}" for c in self.componentes]
        return f"{self.total:g}/100 = " + " + ".join(partes)

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "total": self.total,
            "explicacion": self.explicacion(),
            "componentes": [c.a_dict() for c in self.componentes],
        }


def _pesos(datos: DatosCarrera) -> dict[str, float]:
    crudos = dict(datos.config.scoring["pesos"])
    total = sum(float(v) for v in crudos.values()) or 1.0
    return {k: float(v) / total for k, v in crudos.items()}


def max_impacto(datos: DatosCarrera, grafo: Grafo, estado: EstadoAcademico) -> int:
    """Impacto más alto del plan: sirve de referencia para normalizar."""
    valores = [grafo.impacto(c, estado).puntaje for c in grafo.codigos()]
    return max(valores) if valores else 1


def calcular(
    codigo: str,
    datos: DatosCarrera,
    grafo: Grafo,
    estado: EstadoAcademico,
    fecha_examen: date | None = None,
    referencia_impacto: int | None = None,
) -> Score:
    """Score 0-100 de "qué tan prioritario es preparar este final ahora"."""
    config = datos.config
    materia = datos.materia(codigo)
    pesos = _pesos(datos)
    cfg = config.scoring
    hoy = datos.calendario.hoy

    # 1. Urgencia: qué tan caro es seguir postergando este final. La manda el
    #    driver más fuerte entre: intentos de final ya quemados (a 1 del límite
    #    de recursar = urgencia máxima), la antigüedad de la regularidad (no
    #    vence, pero el contenido se olvida) y — solo en modo "anios" — el
    #    vencimiento. El desglose dice cuál dominó.
    candidatos: list[tuple[float, str]] = []

    usados = estado.intentos_de(codigo) or materia.intentos_final
    intentos = estado_intentos(codigo, usados, config)
    if usados > 0:
        valor = _acotar(usados / max(1, intentos.maximo - 1))
        candidatos.append((valor, intentos.mensaje))

    antiguedad = antiguedad_regularidad(materia, hoy)
    if antiguedad is not None:
        horizonte_antiguedad = float(cfg.get("horizonte_antiguedad_anios", 6)) or 1.0
        valor = _acotar(antiguedad / horizonte_antiguedad)
        candidatos.append(
            (valor, f"regularizada hace ~{antiguedad} años ({materia.anio}): contenido a refrescar")
        )

    reg = estado_regularidad(materia, hoy, config)
    horizonte_urgencia = float(cfg["horizonte_urgencia_dias"])
    if reg.situacion == VENCIDA:
        candidatos.append((1.0, f"regularidad VENCIDA el {reg.vence}"))
    elif reg.dias_restantes is not None:
        candidatos.append(
            (_acotar(1 - reg.dias_restantes / horizonte_urgencia), f"vence {reg.vence} (en {reg.dias_restantes} días)")
        )

    if candidatos:
        urgencia, crudo_urgencia = max(candidatos, key=lambda par: par[0])
    elif materia.estado == "cursando":
        urgencia, crudo_urgencia = 0.2, "cursando: sin apuro propio todavía"
    else:
        urgencia, crudo_urgencia = 0.3, "sin año de cursada: no hay señal de urgencia"

    # 2. Impacto: cuántas materias destraba aprobarla.
    impacto = grafo.impacto(codigo, estado)
    referencia = referencia_impacto or max_impacto(datos, grafo, estado) or 1
    valor_impacto = _acotar(impacto.puntaje / referencia) if referencia else 0.0
    crudo_impacto = (
        f"{len(impacto.inmediatas)} inmediatas, {len(impacto.directas)} directas, "
        f"{len(impacto.transitivas)} aguas abajo"
    )
    if impacto.inmediatas:
        crudo_impacto += " → " + ", ".join(impacto.inmediatas)

    # 3. Proximidad: qué tan cerca está la ventana donde se puede rendir.
    horizonte_prox = float(cfg["horizonte_proximidad_dias"])
    if fecha_examen is not None:
        dias = (fecha_examen - hoy).days
        proximidad = _acotar(1 - dias / horizonte_prox)
        crudo_proximidad = f"final el {fecha_examen} (en {dias} días)"
    else:
        proximidad, crudo_proximidad = 0.0, "sin ventana asignada"

    # 4. Esfuerzo: barato primero (a igualdad de todo, se saca antes lo corto).
    horas, origen = horas_esfuerzo(materia, config)
    esfuerzo = _acotar(1 - horas / float(cfg["esfuerzo_maximo_horas"]))
    crudo_esfuerzo = f"{horas:g} h estimadas ({origen})"

    componentes = (
        Componente("urgencia", crudo_urgencia, urgencia, pesos.get("urgencia", 0)),
        Componente("impacto", crudo_impacto, valor_impacto, pesos.get("impacto", 0)),
        Componente("proximidad", crudo_proximidad, proximidad, pesos.get("proximidad", 0)),
        Componente("esfuerzo", crudo_esfuerzo, esfuerzo, pesos.get("esfuerzo", 0)),
    )
    total = round(sum(c.aporte for c in componentes), 1)
    return Score(codigo, total, componentes)


def ranking(
    datos: DatosCarrera,
    grafo: Grafo,
    estado: EstadoAcademico,
    fechas: dict[str, date] | None = None,
    codigos: list[str] | None = None,
) -> list[Score]:
    """Ordena los finales pendientes por prioridad (mayor score primero).

    Quedan afuera las materias con los intentos agotados (no pueden rendir:
    hay que recursarlas) y las que el plan asume promocionadas (no hay final).
    """
    if codigos is None:
        codigos = [
            c
            for c in grafo.rendibles(
                estado, incluir_cursando=bool(datos.config.finales["asumir_regulariza_cursando"])
            )
            if estado_intentos(c, estado.intentos_de(c), datos.config).situacion != "agotado"
            and not datos.promocion_asumida(c)
        ]
    referencia = max_impacto(datos, grafo, estado)
    scores = [
        calcular(c, datos, grafo, estado, (fechas or {}).get(c), referencia) for c in codigos
    ]
    return sorted(scores, key=lambda s: (-s.total, s.codigo))
