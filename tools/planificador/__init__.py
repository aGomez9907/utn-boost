"""Planificador de carrera (finales + cursada futura) de utn-boost.

Motor puro y determinista, separado de toda presentación:

    modelo.py      → dominio + carga de los 3 inputs + config con defaults
    grafo.py       → DAG de correlativas: disponibilidad, impacto, topología
    reglas.py      → reglamento paramétrico: regularidad, esfuerzo, ventanas, electivas
    scoring.py     → prioridad explicable de finales
    finales.py     → funcionalidad A: qué rendir en cada ventana + conflictos
    proyeccion.py  → funcionalidad C: cursada multi-año + graduación + escenarios
    objetivos.py   → funcionalidad D: targets del usuario validados contra el grafo
    salidas.py     → funcionalidad E: JSON, Markdown, .ics
    cli.py         → capa de presentación (argparse)

Uso programático:

    from tools.planificador import cargar, correr
    resultado = correr(cargar("carrera/datos"))
"""

from __future__ import annotations

from .finales import planificar
from .grafo import Grafo, validar
from .modelo import Config, DatosCarrera, cargar
from .objetivos import validar_objetivos
from .proyeccion import escenarios, proyectar
from .reglas import regularidades, resumen_electivas
from .salidas import Resultado, a_ics, a_json, a_markdown
from .scoring import ranking

__all__ = [
    "cargar",
    "correr",
    "Config",
    "DatosCarrera",
    "Grafo",
    "Resultado",
    "a_ics",
    "a_json",
    "a_markdown",
]


def correr(datos: DatosCarrera, max_materias: int | None = None) -> Resultado:
    """Corrida completa: valida, planifica finales, rankea, proyecta y evalúa targets."""
    grafo = Grafo(datos)
    validacion = validar(datos)
    plan_finales = planificar(datos, grafo)
    fechas = {f.codigo: f.fecha for f in plan_finales.finales}
    orden = ranking(datos, grafo, datos.estado_inicial(), fechas)
    proyeccion = proyectar(datos, grafo, max_materias=max_materias)
    lista_escenarios = escenarios(datos, grafo=grafo)
    veredictos = validar_objetivos(datos, grafo, proyeccion)
    return Resultado(
        datos=datos,
        validacion=validacion,
        plan_finales=plan_finales,
        ranking=orden,
        proyeccion=proyeccion,
        escenarios=lista_escenarios,
        veredictos=veredictos,
        regularidades=regularidades(datos),
        electivas=resumen_electivas(datos),
        grafo=grafo,
    )
