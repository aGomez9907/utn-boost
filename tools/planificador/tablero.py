"""Tablero interactivo arrastrable: el editor visual del plan de carrera.

Genera `carrera/exports/tablero.html`, un HTML autocontenido (sin CDN, offline)
donde se arrastran cursadas a cuatrimestres y finales a mesas. El tablero
valida en vivo correlativas, cupos, promociones e intentos, y exporta
`plan-manual.json` para que el motor respete lo fijado en la próxima corrida.

La plantilla vive en `plantilla_tablero.html` (mismo directorio); acá solo se
arma el payload de datos y se inyecta. Toda la información sale del motor:
el JS del tablero re-valida las mismas reglas para dar feedback inmediato,
pero la corrida "oficial" sigue siendo la de `tools.planificador.cli plan`.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path

from .modelo import Cuatrimestre, DatosCarrera
from .proyeccion import Proyeccion, proyectar
from .reglas import (
    cuatrimestre_de,
    fin_cuatrimestre,
    horas_esfuerzo,
    inicio_cuatrimestre,
    preparacion,
    ventanas_efectivas,
)
from .salidas import Resultado

PLANTILLA = Path(__file__).parent / "plantilla_tablero.html"


def _horizonte(datos: DatosCarrera, sugerencia: Proyeccion) -> date:
    """Hasta cuándo mostrar cuatrimestres y mesas en el tablero."""
    hoy = datos.calendario.hoy
    tope = date(hoy.year + 4, 12, 31)
    if sugerencia.graduacion:
        tope = max(tope, date(sugerencia.graduacion.year + 1, 12, 31))
    return tope


def construir_payload(resultado: Resultado) -> dict:
    """Arma el JSON que consume el JS del tablero."""
    datos = resultado.datos
    config = datos.config
    hoy = datos.calendario.hoy

    # La sugerencia es el plan del motor SIN pins: es el estado "restaurar".
    sugerencia = proyectar(datos, resultado.grafo, usar_pins=False)
    tope_fecha = _horizonte(datos, sugerencia)

    # -- cuatrimestres del horizonte --------------------------------------
    actual, _ = cuatrimestre_de(hoy, config)
    cuatrimestres = []
    cursor: Cuatrimestre = actual
    while inicio_cuatrimestre(cursor, config) <= tope_fecha:
        inicio = inicio_cuatrimestre(cursor, config)
        fin = fin_cuatrimestre(cursor, config)
        cuatrimestres.append(
            {
                "clave": cursor.clave,
                "etiqueta": cursor.etiqueta,
                "numero": cursor.numero,
                "inicio": inicio.isoformat(),
                "fin": fin.isoformat(),
                "abierta": inicio >= hoy,
                "enCurso": inicio <= hoy <= fin,
            }
        )
        cursor = cursor.siguiente()

    # -- mesas (declaradas + estimadas) -----------------------------------
    mesas = [
        {
            "clave": v.clave,
            "id": v.id,
            "desde": v.desde.isoformat(),
            "hasta": v.hasta.isoformat(),
            "llamados": v.llamados,
            "especial": v.especial,
            "estimada": v.estimada,
            "candidatas": list(v.candidatas),
            "fechas": [f.isoformat() for f in v.fechas_de_llamados()],
        }
        for v in ventanas_efectivas(datos.calendario, config, tope_fecha)
        if v.hasta >= hoy
    ]

    # -- materias ---------------------------------------------------------
    cierre_actual = fin_cuatrimestre(actual, config).isoformat()
    materias = []
    for m in datos.materias:
        horas, _ = horas_esfuerzo(m, config)
        prep = preparacion(m, hoy + timedelta(days=90), config)  # solo por los días
        materias.append(
            {
                "codigo": m.codigo,
                "nombre": m.nombre,
                "nivel": m.nivel,
                "estado": m.estado,
                "nota": m.nota,
                "anio": m.anio,
                "anual": m.es_anual,
                "electiva": m.electiva,
                "slug": m.slug,
                "intentos": m.intentos_final,
                "promocionable": m.promocionable,
                "asumirPromocion": m.asumir_promocion or (m.codigo in datos.plan_manual.promociones),
                "horas": horas,
                "prepDias": prep.dias_calendario,
                "cierreActual": cierre_actual if m.estado == "cursando" else None,
            }
        )

    # -- sugerencia del motor ---------------------------------------------
    sugerencia_cursadas: dict[str, str] = {}
    sugerencia_finales: dict[str, str] = {}
    for periodo in sugerencia.periodos:
        for codigo in periodo.nuevas:
            sugerencia_cursadas.setdefault(codigo, periodo.cuatrimestre.clave)
        for final in periodo.finales:
            sugerencia_finales.setdefault(final.codigo, final.ventana_clave)

    return {
        "meta": {
            "plan": datos.plan,
            "carrera": datos.carrera,
            "hoy": hoy.isoformat(),
        },
        "config": {
            "maxMaterias": datos.plan_manual.max_materias or config.max_materias_por_cuatrimestre,
            "anualArranca": int(config.cursada["anual_empieza_en_cuatrimestre"]),
            "intentosMaximo": int(config.intentos["maximo"]),
            "intentosAvisoDesde": int(config.intentos["aviso_desde"]),
            "diasMinEntreFinales": int(config.finales["dias_minimos_entre_finales"]),
            "parcialAntes": int(config.finales["bloqueo_parcial_dias_antes"]),
            "parcialDespues": int(config.finales["bloqueo_parcial_dias_despues"]),
        },
        "materias": materias,
        "correlativas": [
            {
                "codigo": corr.codigo,
                "reg": list(corr.requiere_regularizadas),
                "apr": list(corr.requiere_aprobadas),
            }
            for corr in datos.correlativas.values()
        ],
        "cuatrimestres": cuatrimestres,
        "mesas": mesas,
        "parciales": [
            {"codigo": p.codigo, "nombre": p.nombre, "numero": p.numero, "fecha": p.fecha.isoformat()}
            for p in datos.calendario.parciales
        ],
        "sugerencia": {"cursadas": sugerencia_cursadas, "finales": sugerencia_finales},
        "pins": None if datos.plan_manual.vacio else datos.plan_manual.a_dict(),
    }


def a_tablero_html(resultado: Resultado) -> str:
    """Renderiza el tablero con el payload embebido (autocontenido)."""
    datos = resultado.datos
    payload = json.dumps(construir_payload(resultado), ensure_ascii=False)
    # Que ningún contenido pueda cerrar el <script> que lo embebe.
    payload = payload.replace("</", "<\\/")
    plantilla = PLANTILLA.read_text(encoding="utf-8")
    return (
        plantilla.replace("__DATOS__", payload)
        .replace("__PLAN__", datos.plan)
        .replace("__CARRERA__", datos.carrera)
        .replace("__HOY__", datos.calendario.hoy.isoformat())
    )
