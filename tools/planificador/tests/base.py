"""Base común de los tests: carga la fixture congelada (la data del enunciado).

Las fixtures son una COPIA de carrera/datos/ al momento de escribir los tests:
editar los datos reales del alumno no rompe la suite.
"""

from __future__ import annotations

import unittest
from pathlib import Path

from ..grafo import Grafo
from ..modelo import DatosCarrera, cargar

FIXTURES = Path(__file__).parent / "fixtures"


class CasoConDatos(unittest.TestCase):
    """TestCase con la data del enunciado ya cargada."""

    datos: DatosCarrera
    grafo: Grafo

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.datos = cargar(FIXTURES)
        cls.grafo = Grafo(cls.datos)
