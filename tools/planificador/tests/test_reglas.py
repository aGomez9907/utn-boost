"""Tests del reglamento paramétrico: regularidad, intentos, esfuerzo, ventanas, electivas."""

from __future__ import annotations

import unittest
from datetime import date

from ..modelo import Config, Cuatrimestre
from ..reglas import (
    INTENTOS_AGOTADO,
    INTENTOS_ATENCION,
    INTENTOS_OK,
    INTENTOS_ULTIMA_CHANCE,
    POR_VENCER,
    VENCIDA,
    VIGENTE,
    antiguedad_regularidad,
    cuatrimestre_de,
    estado_intentos,
    estado_regularidad,
    fin_cuatrimestre,
    horas_esfuerzo,
    inicio_cuatrimestre,
    preparacion,
    resumen_electivas,
    ventanas_efectivas,
)
from .base import CasoConDatos


class TestVigenciaRegularidad(CasoConDatos):
    """Regla confirmada: la regularidad NO vence. El modo 'anios' queda paramétrico."""

    def test_default_no_vence(self):
        """AdC se regularizó en 2020 y sigue vigente: acá la regularidad no vence."""
        reg = estado_regularidad(self.datos.materia("AdC"), date(2026, 8, 11), self.datos.config)
        self.assertEqual(reg.situacion, VIGENTE)
        self.assertIsNone(reg.vence)
        self.assertIn("no vence", reg.supuesto)

    def test_modo_anios_sigue_disponible(self):
        """Si otra facultad vence regularidades, el modo 'anios' reproduce la regla."""
        config = self.datos.config.con(vigencia_regularidad={"modo": "anios", "anios": 5})
        reg = estado_regularidad(self.datos.materia("AdC"), date(2026, 8, 11), config)
        self.assertEqual(reg.situacion, VENCIDA)  # 2020 + 5 = 2025-12-31
        self.assertEqual(reg.vence, date(2025, 12, 31))
        reg_sysl = estado_regularidad(self.datos.materia("SySL"), date(2026, 8, 11), config)
        self.assertEqual(reg_sysl.situacion, POR_VENCER)

    def test_fecha_declarada_pisa_el_supuesto_en_modo_anios(self):
        from dataclasses import replace

        config = self.datos.config.con(vigencia_regularidad={"modo": "anios"})
        materia = replace(self.datos.materia("AdC"), regularidad_hasta=date(2027, 3, 1))
        reg = estado_regularidad(materia, date(2026, 8, 11), config)
        self.assertEqual(reg.vence, date(2027, 3, 1))
        self.assertEqual(reg.supuesto, "fecha declarada en estado.json")

    def test_cursando_no_tiene_vencimiento(self):
        reg = estado_regularidad(self.datos.materia("AN"), date(2026, 8, 11), self.datos.config)
        self.assertEqual(reg.situacion, VIGENTE)
        self.assertIsNone(reg.vence)

    def test_antiguedad_de_regularidad(self):
        """AdC (2020) tiene ~6 años de antigüedad; F2 (2025), 1; y una aprobada, None."""
        hoy = date(2026, 8, 11)
        self.assertEqual(antiguedad_regularidad(self.datos.materia("AdC"), hoy), 6)
        self.assertEqual(antiguedad_regularidad(self.datos.materia("F2"), hoy), 1)
        self.assertIsNone(antiguedad_regularidad(self.datos.materia("AM1"), hoy))


class TestIntentosDeFinal(CasoConDatos):
    """Regla confirmada: 4 finales desaprobados → recursar."""

    def test_escala_de_situaciones(self):
        config = self.datos.config
        self.assertEqual(estado_intentos("X", 0, config).situacion, INTENTOS_OK)
        self.assertEqual(estado_intentos("X", 1, config).situacion, INTENTOS_OK)
        self.assertEqual(estado_intentos("X", 2, config).situacion, INTENTOS_ATENCION)
        self.assertEqual(estado_intentos("X", 3, config).situacion, INTENTOS_ULTIMA_CHANCE)
        self.assertEqual(estado_intentos("X", 4, config).situacion, INTENTOS_AGOTADO)

    def test_maximo_configurable(self):
        config = self.datos.config.con(intentos_final={"maximo": 3, "aviso_desde": 1})
        self.assertEqual(estado_intentos("X", 2, config).situacion, INTENTOS_ULTIMA_CHANCE)
        self.assertEqual(estado_intentos("X", 3, config).situacion, INTENTOS_AGOTADO)

    def test_mensaje_de_recursado(self):
        intentos = estado_intentos("SySL", 4, self.datos.config)
        self.assertIn("RECURSAR", intentos.mensaje)
        self.assertEqual(intentos.restantes, 0)


class TestEsfuerzo(CasoConDatos):
    def test_default_por_nivel(self):
        horas, origen = horas_esfuerzo(self.datos.materia("AM2"), self.datos.config)
        self.assertEqual(horas, 40.0)  # nivel 2
        self.assertIn("nivel 2", origen)

    def test_override_por_materia(self):
        config = self.datos.config.con(esfuerzo={"horas_por_materia": {"AM2": 60}})
        horas, origen = horas_esfuerzo(self.datos.materia("AM2"), config)
        self.assertEqual(horas, 60.0)
        self.assertIn("override", origen)

    def test_preparacion_hacia_atras(self):
        """40 h a 3 h/día = 14 días útiles → 17 de calendario (6 útiles/semana)."""
        prep = preparacion(self.datos.materia("AM2"), date(2026, 9, 22), self.datos.config)
        self.assertEqual(prep.dias_utiles, 14)
        self.assertEqual(prep.dias_calendario, 17)
        self.assertEqual(prep.inicio, date(2026, 9, 5))
        self.assertEqual(prep.fin, date(2026, 9, 22))

    def test_minimo_de_dias(self):
        """Aunque el esfuerzo sea bajito, hay un piso de días de preparación."""
        config = self.datos.config.con(esfuerzo={"horas_por_nivel": {"5": 3}})
        prep = preparacion(self.datos.materia("GG"), date(2026, 12, 1), config)
        self.assertGreaterEqual(prep.dias_utiles, 5)


class TestCuatrimestres(CasoConDatos):
    def test_hoy_cae_en_2c_2026(self):
        cuatri, en_curso = cuatrimestre_de(date(2026, 8, 11), self.datos.config)
        self.assertEqual(cuatri, Cuatrimestre(2026, 2))
        self.assertTrue(en_curso)

    def test_enero_apunta_al_1c_siguiente(self):
        cuatri, en_curso = cuatrimestre_de(date(2027, 1, 15), self.datos.config)
        self.assertEqual(cuatri, Cuatrimestre(2027, 1))
        self.assertFalse(en_curso)

    def test_limites_de_dictado(self):
        cuatri = Cuatrimestre(2027, 1)
        self.assertEqual(inicio_cuatrimestre(cuatri, self.datos.config), date(2027, 3, 1))
        self.assertEqual(fin_cuatrimestre(cuatri, self.datos.config), date(2027, 7, 15))

    def test_parseo_de_claves(self):
        self.assertEqual(Cuatrimestre.desde_clave("1C-2027"), Cuatrimestre(2027, 1))
        self.assertEqual(Cuatrimestre.desde_clave("2c 2028"), Cuatrimestre(2028, 2))


class TestVentanas(CasoConDatos):
    def test_estimadas_no_pisan_las_declaradas(self):
        """Las ventanas por plantilla arrancan DESPUÉS de la última declarada."""
        ventanas = ventanas_efectivas(self.datos.calendario, self.datos.config, date(2027, 12, 31))
        declaradas = [v for v in ventanas if not v.estimada]
        estimadas = [v for v in ventanas if v.estimada]
        self.assertEqual(len(declaradas), 3)  # sep, oct, dic 2026
        ultima_declarada = max(v.hasta for v in declaradas)
        for ventana in estimadas:
            self.assertGreater(ventana.desde, ultima_declarada)

    def test_primera_estimada_es_feb_mar_2027(self):
        """Después de dic 2026 (última declarada) sigue la mesa feb-mar 2027 de la plantilla."""
        ventanas = ventanas_efectivas(self.datos.calendario, self.datos.config, date(2027, 12, 31))
        primera = next(v for v in ventanas if v.estimada)
        self.assertEqual((primera.id, primera.anio), ("feb-mar", 2027))
        self.assertEqual(primera.desde, date(2027, 2, 10))
        self.assertEqual(primera.llamados, 3)

    def test_plantilla_trae_el_ciclo_completo_utn(self):
        """Un año estimado entero tiene las 8 mesas del calendario académico real."""
        ventanas = ventanas_efectivas(self.datos.calendario, self.datos.config, date(2027, 12, 31))
        de_2027 = [v.id for v in ventanas if v.estimada and v.anio == 2027]
        self.assertEqual(
            de_2027, ["feb-mar", "abril", "mayo", "jul-1", "jul-2", "sep", "oct", "dic"]
        )

    def test_mesas_especiales_marcadas(self):
        """abril y octubre son mesas especiales (pocas materias aplican)."""
        ventanas = ventanas_efectivas(self.datos.calendario, self.datos.config, date(2027, 12, 31))
        especiales = {v.id for v in ventanas if v.estimada and v.anio == 2027 and v.especial}
        self.assertEqual(especiales, {"abril", "oct"})
        # Y la declarada de oct 2026 también viene marcada desde calendario.json.
        self.assertTrue(self.datos.calendario.ventana("oct").especial)

    def test_llamados_repartidos_en_la_ventana(self):
        ventana = self.datos.calendario.ventana("dic")
        fechas = ventana.fechas_de_llamados()
        self.assertEqual(len(fechas), 3)
        self.assertEqual(fechas[0], date(2026, 12, 1))
        self.assertEqual(fechas[-1], date(2026, 12, 22))

    def test_clave_estable_de_mesa(self):
        self.assertEqual(self.datos.calendario.ventana("sep").clave, "sep-2026")


class TestElectivas(CasoConDatos):
    def test_acumulado_y_requisitos(self):
        resumen = resumen_electivas(self.datos)
        self.assertEqual(resumen.horas_aprobadas, 46.0)  # 40 + 3 + 3
        self.assertEqual(set(resumen.aprobadas), {"ELEC_QA", "ELEC_UX", "ELEC_TH"})
        for requisito in resumen.requisitos:  # 6/12/24 → todas cubiertas
            self.assertTrue(requisito.cumple)

    def test_avisa_escalas_mezcladas(self):
        resumen = resumen_electivas(self.datos)
        self.assertIsNotNone(resumen.aviso_unidades)

    def test_requisitos_configurables(self):
        config = self.datos.config.con(electivas={"horas_requeridas_por_nivel": {"5": 100}})
        datos = self.datos.con_config(config)
        resumen = resumen_electivas(datos)
        requisito = next(r for r in resumen.requisitos if r.nivel == 5)
        self.assertFalse(requisito.cumple)
        self.assertEqual(requisito.falta, 54.0)


if __name__ == "__main__":
    unittest.main()
