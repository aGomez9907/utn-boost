"""Tests del circuito manual: pins del tablero, promociones, recursadas y tablero.html."""

from __future__ import annotations

import json
import unittest
from dataclasses import replace
from datetime import date

from .. import correr
from ..finales import planificar
from ..modelo import PlanManual, parsear_materias, parsear_plan_manual
from ..proyeccion import proyectar
from ..tablero import a_tablero_html, construir_payload
from .base import FIXTURES, CasoConDatos


def con_plan_manual(datos, **kwargs):
    return replace(datos, plan_manual=PlanManual(**kwargs))


def con_intentos(datos, codigo: str, intentos: int):
    crudo = json.loads((FIXTURES / "estado.json").read_text(encoding="utf-8"))
    for item in crudo["subjects"]:
        if item["code"] == codigo:
            item["intentosFinal"] = intentos
    return replace(datos, materias=parsear_materias(crudo, datos.config))


class TestParseoPlanManual(unittest.TestCase):
    def test_parseo_completo(self):
        manual = parsear_plan_manual(
            {
                "generado": "2026-08-11",
                "cursadas": {"CD": "1C-2027"},
                "finales": {"AM2": "sep-2026"},
                "promociones": ["GG"],
                "intentosFinal": {"SySL": 2},
                "maxMateriasPorCuatrimestre": 4,
            }
        )
        self.assertEqual(manual.cursadas["CD"], "1C-2027")
        self.assertEqual(manual.max_materias, 4)
        self.assertFalse(manual.vacio)

    def test_vacio(self):
        self.assertTrue(parsear_plan_manual(None).vacio)
        self.assertTrue(parsear_plan_manual({}).vacio)


class TestPinsDeFinales(CasoConDatos):
    def test_final_fijado_cambia_de_mesa(self):
        """AM2 fijado a dic-2026: deja sep libre y aparece en diciembre como 'fijado'."""
        datos = con_plan_manual(self.datos, finales={"AM2": "dic-2026"})
        plan = planificar(datos)
        am2 = next(f for f in plan.finales if f.codigo == "AM2")
        self.assertEqual(am2.ventana_clave, "dic-2026")
        self.assertEqual(am2.origen, "fijado")
        self.assertEqual(plan.violaciones, [])
        # Y no quedó también en septiembre.
        self.assertEqual([f for f in plan.finales if f.codigo == "AM2"], [am2])

    def test_pin_imposible_se_reporta(self):
        """BD fijada a sep-2026 con AN cursando… BD está regularizada, puede. Usamos GG
        (cursando hasta fin de 2C): en sep todavía no cerró la cursada → violación."""
        datos = con_plan_manual(self.datos, finales={"GG": "sep-2026"})
        plan = planificar(datos)
        violacion = next(v for v in plan.violaciones if v["codigo"] == "GG")
        self.assertEqual(violacion["tipo"], "final-fijado-imposible")
        self.assertIn("cursada cierra", violacion["motivo"])
        self.assertNotIn("GG", [f.codigo for f in plan.finales if f.ventana_clave == "sep-2026"])

    def test_pin_a_mesa_inexistente(self):
        datos = con_plan_manual(self.datos, finales={"AM2": "enero-2027"})
        proy = proyectar(datos)
        violacion = next(v for v in proy.violaciones if v["donde"] == "enero-2027")
        self.assertEqual(violacion["tipo"], "mesa-desconocida")


class TestPinsDeCursadas(CasoConDatos):
    def test_cursada_fijada_se_respeta(self):
        """CD fijada a 1C-2027 (podría cursarse ya en 2C-2026 si hubiera cupo): espera."""
        datos = con_plan_manual(self.datos, cursadas={"CD": "1C-2027"})
        proy = proyectar(datos)
        periodo = next(p for p in proy.periodos if "CD" in p.nuevas)
        self.assertEqual(periodo.cuatrimestre.clave, "1C-2027")
        self.assertIn("CD", periodo.fijadas)
        self.assertEqual([v for v in proy.violaciones if v["codigo"] == "CD"], [])

    def test_cursada_fijada_sin_correlativas_se_reporta(self):
        """RD en 1C-2027 es ilegal (CD no estaría aprobada): se ejecuta pero se avisa."""
        datos = con_plan_manual(self.datos, cursadas={"RD": "1C-2027"})
        proy = proyectar(datos)
        violacion = next(v for v in proy.violaciones if v["codigo"] == "RD")
        self.assertEqual(violacion["tipo"], "cursada-fijada-sin-correlativas")
        periodo = next(p for p in proy.periodos if "RD" in p.nuevas)
        self.assertEqual(periodo.cuatrimestre.clave, "1C-2027")

    def test_max_materias_del_tablero(self):
        datos = con_plan_manual(self.datos, max_materias=3)
        proy = proyectar(datos)
        self.assertEqual(proy.max_materias, 3)
        for periodo in proy.periodos:
            self.assertLessEqual(len(periodo.cursa), 3)


class TestPromocion(CasoConDatos):
    def test_promocion_evita_el_final(self):
        """GG marcada promoción: aprueba al cerrar la cursada, sin final en ninguna mesa."""
        datos = con_plan_manual(self.datos, promociones=("GG",))
        proy = proyectar(datos)
        self.assertNotIn("GG", [f.codigo for f in proy.finales])
        periodo = next(p for p in proy.periodos if "GG" in p.promociona)
        self.assertEqual(periodo.cuatrimestre.clave, "2C-2026")
        self.assertTrue(proy.completa)

    def test_promocion_en_estado_json(self):
        """asumirPromocion en estado.json equivale a la marca del tablero."""
        crudo = json.loads((FIXTURES / "estado.json").read_text(encoding="utf-8"))
        for item in crudo["subjects"]:
            if item["code"] == "AN":
                item["asumirPromocion"] = True
        datos = replace(self.datos, materias=parsear_materias(crudo, self.datos.config))
        self.assertTrue(datos.promocion_asumida("AN"))
        plan = planificar(datos)
        self.assertNotIn("AN", [f.codigo for f in plan.finales])

    def test_regularizada_no_promociona(self):
        """La promoción se gana cursando: una ya regularizada (F2) no puede promocionar."""
        datos = con_plan_manual(self.datos, promociones=("F2",))
        self.assertFalse(datos.promocion_asumida("F2"))
        plan = planificar(datos)
        self.assertIn("F2", [f.codigo for f in plan.finales])


class TestRecursada(CasoConDatos):
    def test_agotada_no_rinde_y_se_recursa(self):
        """SySL con 4 intentos: no puede rendir; la proyección la recursa y después aprueba."""
        datos = con_intentos(self.datos, "SySL", 4)
        proy = proyectar(datos)
        recursada = next(p for p in proy.periodos if "SySL" in p.recursa)
        finales_sysl = [f for f in proy.finales if f.codigo == "SySL"]
        self.assertEqual(len(finales_sysl), 1)
        self.assertGreater(finales_sysl[0].fecha, recursada.fin)
        self.assertTrue(proy.completa)

    def test_agotada_queda_fuera_del_plan_de_finales(self):
        datos = con_intentos(self.datos, "SySL", 4)
        plan = planificar(datos)
        self.assertNotIn("SySL", [f.codigo for f in plan.finales])
        motivo = next(d for d in plan.descartadas if d["codigo"] == "SySL")
        self.assertIn("RECURSAR", motivo["motivo"])


class TestTablero(CasoConDatos):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.resultado = correr(cls.datos)
        cls.payload = construir_payload(cls.resultado)

    def test_payload_completo(self):
        claves = {"meta", "config", "materias", "correlativas", "cuatrimestres", "mesas", "parciales", "sugerencia", "pins"}
        self.assertTrue(claves.issubset(self.payload))
        self.assertEqual(len(self.payload["materias"]), 41)

    def test_sugerencia_consistente_con_proyeccion(self):
        """La sugerencia embebida ubica AM2 en sep-2026 y a CD en algún cuatrimestre."""
        self.assertEqual(self.payload["sugerencia"]["finales"]["AM2"], "sep-2026")
        self.assertIn("CD", self.payload["sugerencia"]["cursadas"])

    def test_mesas_tienen_fechas_de_llamados(self):
        dic = next(m for m in self.payload["mesas"] if m["clave"] == "dic-2026")
        self.assertEqual(len(dic["fechas"]), 3)
        oct_ = next(m for m in self.payload["mesas"] if m["clave"] == "oct-2026")
        self.assertTrue(oct_["especial"])

    def test_html_autocontenido(self):
        html = a_tablero_html(self.resultado)
        self.assertNotIn("__DATOS__", html)
        self.assertNotIn("__PLAN__", html)
        self.assertIn("AM2", html)
        self.assertIn("plan-manual.json", html)
        self.assertNotIn("http://", html)
        self.assertNotIn("https://cdn", html)

    def test_payload_es_json_serializable(self):
        texto = json.dumps(self.payload, ensure_ascii=False)
        self.assertIn("sep-2026", texto)


class TestDeterminismoConPins(CasoConDatos):
    def test_misma_entrada_mismo_plan(self):
        datos = con_plan_manual(
            self.datos, cursadas={"CD": "1C-2027"}, finales={"AM2": "dic-2026"}, promociones=("GG",)
        )
        primera = json.dumps(proyectar(datos).a_dict(), sort_keys=True)
        segunda = json.dumps(proyectar(datos).a_dict(), sort_keys=True)
        self.assertEqual(primera, segunda)


if __name__ == "__main__":
    unittest.main()
