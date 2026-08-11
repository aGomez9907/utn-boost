"""Tests del DAG: disponibilidad, impacto, topología y validación de datos."""

from __future__ import annotations

import unittest

from ..grafo import validar
from ..modelo import EstadoAcademico
from .base import CasoConDatos


class TestDisponibilidad(CasoConDatos):
    def test_f2_requiere_am1_y_f1_regularizadas(self):
        """Hecho del enunciado: F2 requiere AM1+F1 al menos regularizadas."""
        corr = self.datos.correlativa("F2")
        self.assertEqual(set(corr.requiere_regularizadas), {"AM1", "F1"})
        self.assertEqual(corr.requiere_aprobadas, ())
        # Con AM1 y F1 aprobadas (≥ regularizada), F2 cumple.
        disp = self.grafo.disponibilidad("F2", self.datos.estado_inicial())
        self.assertTrue(disp.puede)

    def test_hoy_no_hay_nada_cursable(self):
        """Con el estado del enunciado, ninguna bloqueada cumple correlativas aún."""
        self.assertEqual(self.grafo.cursables(self.datos.estado_inicial()), [])

    def test_sim_bloqueada_por_am2_no_aprobada(self):
        disp = self.grafo.disponibilidad("Sim", self.datos.estado_inicial())
        self.assertFalse(disp.puede)
        self.assertIn("AM2", disp.faltan_aprobar)
        self.assertEqual(disp.faltan_regularizar, ())  # PyE ya está aprobada

    def test_aprobar_am2_habilita_sim(self):
        """Aprobado AM2, Sim pasa a cursable (PyE ya estaba aprobada)."""
        estado = self.datos.estado_inicial()
        estado.marcar("AM2", "aprobada")
        self.assertIn("Sim", self.grafo.cursables(estado))

    def test_rd_necesita_ssoo_y_cd_regularizadas(self):
        estado = self.datos.estado_inicial()
        disp = self.grafo.disponibilidad("RD", estado)
        self.assertFalse(disp.puede)
        self.assertIn("CD", disp.faltan_regularizar)  # CD ni se cursó
        self.assertNotIn("SSOO", disp.faltan_regularizar)  # SSOO ya está regularizada

    def test_tras_2c2026_se_habilitan_las_de_1c2027(self):
        """Aprobando AM2, F2, AdC, SySL, SSOO, AN y BD (los finales proyectados
        de acá a marzo), quedan cursables CD, IO, IyCS, SI, Sim y TpA."""
        estado = self.datos.estado_inicial()
        for codigo in ("AM2", "F2", "AdC", "SySL", "SSOO", "AN", "BD"):
            estado.marcar(codigo, "aprobada")
        cursables = set(self.grafo.cursables(estado))
        self.assertEqual(cursables, {"CD", "IO", "IyCS", "SI", "Sim", "TpA"})


class TestImpacto(CasoConDatos):
    def test_aprobar_adc_desbloquea_cd(self):
        impacto = self.grafo.impacto("AdC", self.datos.estado_inicial())
        self.assertIn("CD", impacto.inmediatas)  # F1 ya aprobada: solo faltaba AdC

    def test_impacto_transitivo_de_adc_llega_a_pfinal(self):
        impacto = self.grafo.impacto("AdC", self.datos.estado_inicial())
        # CD → RD → PFinal/PPS/SSI cuelgan aguas abajo de AdC.
        for lejana in ("RD", "PFinal", "PPS", "SSI"):
            self.assertIn(lejana, impacto.transitivas)

    def test_gg_no_desbloquea_nada(self):
        impacto = self.grafo.impacto("GG", self.datos.estado_inicial())
        self.assertEqual(impacto.puntaje, 0)


class TestTopologia(CasoConDatos):
    def test_es_dag(self):
        self.assertEqual(self.grafo.ciclos(), [])

    def test_orden_topologico_respeta_correlativas(self):
        orden = self.grafo.orden_topologico()
        posicion = {codigo: i for i, codigo in enumerate(orden)}
        for codigo in self.grafo.codigos():
            for previa in self.grafo.predecesoras(codigo):
                self.assertLess(
                    posicion[previa], posicion[codigo],
                    f"{previa} debería ir antes que {codigo}",
                )

    def test_pfinal_es_terminal_y_profundo(self):
        self.assertIn("PFinal", self.grafo.terminales())
        niveles = self.grafo.niveles_topologicos()
        self.assertEqual(max(niveles.values()), niveles["PFinal"])

    def test_cadena_critica_hacia_pfinal(self):
        """El camino pendiente más largo pasa por CD → RD → PFinal."""
        cadena = self.grafo.cadena_mas_larga("PFinal", self.datos.estado_inicial())
        self.assertEqual(cadena[-1], "PFinal")
        self.assertIn("RD", cadena)
        self.assertIn("CD", cadena)


class TestValidacion(CasoConDatos):
    def test_datos_del_enunciado_no_tienen_errores(self):
        resultado = validar(self.datos)
        self.assertTrue(resultado.ok, [p.mensaje for p in resultado.errores])

    def test_detecta_cdd_incoherente(self):
        """CdD figura aprobada pero sus correlativas no: el validador avisa."""
        resultado = validar(self.datos)
        self.assertTrue(any(p.codigo == "CdD" for p in resultado.avisos))

    def test_detecta_escalas_mezcladas_en_electivas(self):
        resultado = validar(self.datos)
        self.assertTrue(any(p.codigo == "electivas" for p in resultado.avisos))


class TestEstadoAcademico(unittest.TestCase):
    def test_marcar_nunca_retrocede(self):
        estado = EstadoAcademico(estados={"X": "aprobada"})
        estado.marcar("X", "regularizada")
        self.assertEqual(estado.estado("X"), "aprobada")

    def test_desconocida_es_bloqueada(self):
        estado = EstadoAcademico(estados={})
        self.assertEqual(estado.estado("Nada"), "bloqueada")


if __name__ == "__main__":
    unittest.main()
