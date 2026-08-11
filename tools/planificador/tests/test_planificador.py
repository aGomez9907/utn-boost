"""Tests de las funcionalidades A-E con la data del enunciado (§5)."""

from __future__ import annotations

import unittest
from datetime import date

from .. import correr
from ..finales import planificar
from ..objetivos import ALCANZABLE, INALCANZABLE, validar_objetivos
from ..proyeccion import escenarios, proyectar
from ..salidas import a_ics, a_json, a_markdown
from ..scoring import calcular, ranking
from .base import CasoConDatos


class TestPlanFinales(CasoConDatos):
    """Funcionalidad A + hechos conocidos del §5."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.plan = planificar(cls.datos, cls.grafo)
        cls.por_codigo = {f.codigo: f for f in cls.plan.finales}

    def test_am2_va_a_septiembre(self):
        final = self.por_codigo["AM2"]
        self.assertEqual(final.fecha, date(2026, 9, 22))
        self.assertEqual(final.origen, "declarado")

    def test_f2_va_a_octubre(self):
        self.assertEqual(self.por_codigo["F2"].fecha, date(2026, 10, 26))

    def test_adc_va_a_diciembre(self):
        final = self.por_codigo["AdC"]
        self.assertEqual(final.ventana, "dic 2026")
        self.assertEqual(final.fecha, date(2026, 12, 1))  # primer llamado

    def test_preparacion_hacia_atras_desde_el_examen(self):
        for final in self.plan.finales:
            self.assertLess(final.preparacion.inicio, final.fecha)
            self.assertEqual(final.preparacion.fin, final.fecha)

    def test_an_solo_entra_despues_del_cierre_de_cursada(self):
        """AN está cursando (cierra 2026-11-30): no puede rendir en sep/oct,
        sí en el llamado de diciembre."""
        if "AN" in self.por_codigo:
            self.assertGreaterEqual(self.por_codigo["AN"].fecha, date(2026, 12, 1))

    def test_detecta_choque_con_parcial(self):
        """Preparar AdC (desde el 13/11) pisa el 2º parcial de GG (16/11) y el
        de AN (24/11): el conflicto tiene que estar declarado."""
        tipos = {(c.tipo, frozenset(c.involucra)) for c in self.plan.conflictos}
        self.assertIn(("choque-con-parcial", frozenset({"AdC", "GG"})), tipos)
        self.assertIn(("choque-con-parcial", frozenset({"AdC", "AN"})), tipos)

    def test_sin_conflictos_de_vencimiento(self):
        """Con el reglamento real (la regularidad no vence) no hay conflictos de vencimiento."""
        tipos = {c.tipo for c in self.plan.conflictos}
        self.assertNotIn("regularidad-vencida", tipos)
        self.assertNotIn("regularidad-por-vencer", tipos)

    def test_ultimo_intento_es_conflicto_alto(self):
        """Una materia con 3 de 4 intentos usados rinde, pero con alerta de último intento."""
        import json

        from ..modelo import cargar
        from .base import FIXTURES

        datos = cargar(FIXTURES)
        crudo = json.loads((FIXTURES / "estado.json").read_text(encoding="utf-8"))
        for item in crudo["subjects"]:
            if item["code"] == "SySL":
                item["intentosFinal"] = 3
        from ..modelo import DatosCarrera, parsear_materias

        materias = parsear_materias(crudo, datos.config)
        from dataclasses import replace

        datos = replace(datos, materias=materias)
        plan = planificar(datos)
        conflicto = next(c for c in plan.conflictos if c.tipo == "ultimo-intento")
        self.assertIn("SySL", conflicto.involucra)
        self.assertEqual(conflicto.severidad, "alta")

    def test_cupo_por_ventana(self):
        """sep y oct tienen 1 llamado → 1 materia; dic tiene 3 → hasta 3."""
        por_ventana: dict[str, int] = {}
        for final in self.plan.finales:
            por_ventana[final.ventana] = por_ventana.get(final.ventana, 0) + 1
        self.assertEqual(por_ventana.get("sep 2026"), 1)
        self.assertEqual(por_ventana.get("oct 2026 (esp.)"), 1)  # F2, candidata declarada
        self.assertLessEqual(por_ventana.get("dic 2026", 0), 3)

    def test_mesa_especial_no_se_llena_sola(self):
        """En oct (especial) entra F2 porque está declarada; el motor no suma sugeridas ahí."""
        de_oct = [f for f in self.plan.finales if f.ventana_clave == "oct-2026"]
        self.assertEqual([f.codigo for f in de_oct], ["F2"])
        self.assertEqual(de_oct[0].origen, "declarado")


class TestScoring(CasoConDatos):
    """Funcionalidad B: score explicable."""

    def test_desglose_suma_el_total(self):
        estado = self.datos.estado_inicial()
        score = calcular("SySL", self.datos, self.grafo, estado, date(2026, 12, 11))
        self.assertAlmostEqual(score.total, sum(c.aporte for c in score.componentes), places=5)
        self.assertEqual({c.nombre for c in score.componentes}, {"urgencia", "impacto", "proximidad", "esfuerzo"})

    def test_regularidad_vencida_da_urgencia_maxima(self):
        estado = self.datos.estado_inicial()
        score = calcular("AdC", self.datos, self.grafo, estado)
        urgencia = next(c for c in score.componentes if c.nombre == "urgencia")
        self.assertEqual(urgencia.normalizado, 1.0)

    def test_ranking_ordena_por_score(self):
        orden = ranking(self.datos, self.grafo, self.datos.estado_inicial())
        totales = [s.total for s in orden]
        self.assertEqual(totales, sorted(totales, reverse=True))

    def test_urgentes_arriba(self):
        """SySL y AdC (regularidades al límite) rankean sobre F2 y GG."""
        plan = planificar(self.datos, self.grafo)
        fechas = {f.codigo: f.fecha for f in plan.finales}
        orden = ranking(self.datos, self.grafo, self.datos.estado_inicial(), fechas)
        posicion = {s.codigo: i for i, s in enumerate(orden)}
        self.assertLess(posicion["SySL"], posicion["F2"])
        self.assertLess(posicion["AdC"], posicion["F2"])
        self.assertEqual(orden[-1].codigo, "GG")  # no desbloquea nada y sin apuro

    def test_pesos_configurables(self):
        """Con todo el peso en esfuerzo, gana la materia más barata."""
        config = self.datos.config.con(
            scoring={"pesos": {"urgencia": 0, "impacto": 0, "proximidad": 0, "esfuerzo": 1}}
        )
        datos = self.datos.con_config(config)
        orden = ranking(datos, self.grafo, datos.estado_inicial())
        self.assertEqual(orden[0].codigo, "GG")  # nivel 5 → 25 h, la más liviana


class TestProyeccion(CasoConDatos):
    """Funcionalidad C: cursada multi-año."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.proyeccion = proyectar(cls.datos, cls.grafo)

    def test_completa_la_carrera(self):
        self.assertTrue(self.proyeccion.completa)
        self.assertIsNotNone(self.proyeccion.graduacion)

    def test_respeta_el_cupo(self):
        for periodo in self.proyeccion.periodos:
            self.assertLessEqual(len(periodo.cursa), self.proyeccion.max_materias)

    def test_no_se_cursa_sin_correlativas(self):
        """Reconstruye la simulación y verifica que cada inscripción era legal."""
        estado = self.datos.estado_inicial()
        for periodo in self.proyeccion.periodos:
            for codigo in periodo.nuevas:
                disp = self.grafo.disponibilidad(codigo, estado)
                self.assertTrue(disp.puede, f"{codigo} en {periodo.cuatrimestre.etiqueta}: {disp.motivo()}")
                estado.marcar(codigo, "cursando")
            for codigo in periodo.regulariza:
                estado.marcar(codigo, "regularizada")
            for final in periodo.finales:
                self.assertIn(estado.estado(final.codigo), ("regularizada", "cursando"))
                estado.marcar(final.codigo, "aprobada")

    def test_no_inscribe_en_cuatrimestre_ya_empezado(self):
        """Hoy (11/08) el 2C 2026 ya arrancó: no puede haber inscripciones nuevas."""
        primero = self.proyeccion.periodos[0]
        self.assertEqual(primero.cuatrimestre.clave, "2C-2026")
        self.assertEqual(primero.nuevas, ())
        self.assertEqual(set(primero.cursa), {"AN", "GG"})  # hecho del §5

    def test_pfinal_es_anual_y_va_al_final(self):
        """PFinal ocupa dos cuatrimestres consecutivos y es lo último que se rinde."""
        con_pfinal = [p for p in self.proyeccion.periodos if "PFinal" in p.cursa]
        self.assertEqual(len(con_pfinal), 2)
        self.assertEqual(con_pfinal[0].cuatrimestre.numero, 1)  # arranca en 1C
        self.assertEqual(con_pfinal[0].cuatrimestre.siguiente(), con_pfinal[1].cuatrimestre)
        ultimo_final = max(self.proyeccion.finales, key=lambda f: f.fecha)
        self.assertEqual(ultimo_final.codigo, "PFinal")
        self.assertEqual(self.proyeccion.graduacion, ultimo_final.fecha)

    def test_pfinal_espera_sus_correlativas(self):
        """PFinal recién se cursa cuando IyCS+AdmSI+RD están regularizadas y
        Inglés2+DdS+DSI aprobadas (§5: 'muy lejos')."""
        arranque = next(p for p in self.proyeccion.periodos if "PFinal" in p.nuevas)
        self.assertGreaterEqual(arranque.cuatrimestre.anio, 2028)

    def test_escenarios_mas_materias_no_alarga(self):
        lista = escenarios(self.datos, [3, 4, 5], self.grafo)
        por_tope = {e.max_materias: e for e in lista}
        self.assertLessEqual(por_tope[5].cuatrimestres, por_tope[3].cuatrimestres)
        for escenario in lista:
            self.assertTrue(escenario.completa)

    def test_piso_teorico_menor_o_igual_que_lo_simulado(self):
        self.assertLessEqual(self.proyeccion.piso_teorico, self.proyeccion.cuatrimestres_restantes)


class TestObjetivos(CasoConDatos):
    """Funcionalidad D: targets."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.veredictos = {v.objetivo.id: v for v in validar_objetivos(cls.datos, cls.grafo)}

    def test_am2_en_septiembre_alcanzable(self):
        veredicto = self.veredictos["am2-septiembre"]
        self.assertEqual(veredicto.resultado, ALCANZABLE)

    def test_recibirse_2028_da_veredicto_con_motivo(self):
        veredicto = self.veredictos["recibirme-2028"]
        self.assertIn(veredicto.resultado, ("alcanzable", "ajustado"))
        self.assertIn("2028", veredicto.motivo)

    def test_target_imposible_explica_que_falta(self):
        """Cursar RD en 1C 2027 es imposible: CD ni se cursó todavía."""
        from ..modelo import Objetivo

        veredicto = validar_objetivos(
            self.datos,
            self.grafo,
            objetivos=[Objetivo(id="rd-ya", tipo="cursar", materia="RD", cuatrimestre="1C-2027")],
        )[0]
        self.assertEqual(veredicto.resultado, INALCANZABLE)
        self.assertTrue(any("CD" in paso for paso in veredicto.que_haria_falta))

    def test_recibirse_2027_inalcanzable_por_cadena_critica(self):
        from ..modelo import Objetivo

        veredicto = validar_objetivos(
            self.datos,
            self.grafo,
            objetivos=[Objetivo(id="ya", tipo="recibirme", antes_de=date(2027, 6, 30))],
        )[0]
        self.assertEqual(veredicto.resultado, INALCANZABLE)
        self.assertIn("cadena crítica", veredicto.motivo)


class TestSalidas(CasoConDatos):
    """Funcionalidad E: JSON, Markdown, ICS. Y determinismo del motor."""

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.resultado = correr(cls.datos)

    def test_json_estructurado(self):
        salida = a_json(self.resultado)
        for clave in ("planFinales", "ranking", "proyeccion", "escenarios", "objetivos", "electivas"):
            self.assertIn(clave, salida)
        codigos = [f["codigo"] for f in salida["planFinales"]["finales"]]
        self.assertIn("AM2", codigos)

    def test_markdown_tiene_secciones(self):
        md = a_markdown(self.resultado)
        for seccion in (
            "## Plan de finales",
            "## Qué preparar primero",
            "## Proyección de cursada",
            "## Objetivos declarados",
            "## Electivas",
        ):
            self.assertIn(seccion, md)

    def test_ics_tiene_finales_preparacion_y_parciales(self):
        ics = a_ics(self.resultado)
        self.assertIn("BEGIN:VCALENDAR", ics)
        self.assertIn("Final AM2", ics)
        self.assertIn("Arrancar AM2", ics)
        self.assertIn("GG P2", ics)

    def test_motor_determinista(self):
        """Dos corridas con la misma data producen el mismo JSON."""
        import json

        primera = json.dumps(a_json(correr(self.datos)), sort_keys=True)
        segunda = json.dumps(a_json(correr(self.datos)), sort_keys=True)
        self.assertEqual(primera, segunda)


if __name__ == "__main__":
    unittest.main()
