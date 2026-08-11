"""Salidas del planificador: JSON estructurado, plan.md legible y calendario .ics.

El JSON es para integrar con otras apps (funcionalidad E); el Markdown es la
vista canónica dentro del repo (misma filosofía que estrategia.md/plan.md de
cada materia); el .ics agrega preparación, finales y parciales a cualquier
calendario.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta

from .finales import PlanFinales
from .grafo import Grafo, Validacion
from .modelo import DatosCarrera
from .objetivos import Veredicto
from .proyeccion import Escenario, Proyeccion
from .reglas import (
    EstadoRegularidad,
    ResumenElectivas,
    antiguedad_regularidad,
    intentos_de_materia,
    regularidades,
    resumen_electivas,
)
from .scoring import Score

VERSION = "2.0"


@dataclass
class Resultado:
    """Todo lo que produce una corrida completa del planificador."""

    datos: DatosCarrera
    validacion: Validacion
    plan_finales: PlanFinales
    ranking: list[Score]
    proyeccion: Proyeccion
    escenarios: list[Escenario]
    veredictos: list[Veredicto]
    regularidades: list[EstadoRegularidad]
    electivas: ResumenElectivas
    grafo: Grafo


# --------------------------------------------------------------------------
# JSON estructurado
# --------------------------------------------------------------------------


def a_json(resultado: Resultado) -> dict:
    datos = resultado.datos
    estado = datos.estado_inicial()
    grafo = resultado.grafo
    return {
        "version": VERSION,
        "generado": datos.calendario.hoy.isoformat(),
        "plan": datos.plan,
        "carrera": datos.carrera,
        "validacion": resultado.validacion.a_dict(),
        "estadoActual": {
            "cursando": estado.codigos_en("cursando"),
            "regularizadas": estado.codigos_en("regularizada"),
            "cursablesAhora": grafo.cursables(estado),
            "rendiblesAhora": grafo.rendibles(estado, incluir_cursando=False),
        },
        "regularidades": [r.a_dict() for r in resultado.regularidades],
        "intentosFinal": [
            intentos_de_materia(m, datos.config).a_dict()
            for m in datos.materias
            if m.estado == "regularizada" or m.intentos_final
        ],
        "promocionesAsumidas": sorted(
            m.codigo for m in datos.materias if datos.promocion_asumida(m.codigo)
        ),
        "planManual": None if datos.plan_manual.vacio else datos.plan_manual.a_dict(),
        "electivas": resultado.electivas.a_dict(),
        "planFinales": resultado.plan_finales.a_dict(),
        "ranking": [s.a_dict() for s in resultado.ranking],
        "proyeccion": resultado.proyeccion.a_dict(),
        "escenarios": [e.a_dict() for e in resultado.escenarios],
        "objetivos": [v.a_dict() for v in resultado.veredictos],
    }


def escribir_json(resultado: Resultado, ruta) -> None:
    ruta.write_text(
        json.dumps(a_json(resultado), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


# --------------------------------------------------------------------------
# Markdown legible
# --------------------------------------------------------------------------

_EMOJI_VEREDICTO = {"alcanzable": "✅", "ajustado": "🟡", "inalcanzable": "❌"}
_EMOJI_SEVERIDAD = {"alta": "🔴", "media": "🟠", "baja": "🟡"}


def _fmt_fecha(valor: date | None) -> str:
    return valor.isoformat() if valor else "—"


def a_markdown(resultado: Resultado) -> str:
    datos = resultado.datos
    hoy = datos.calendario.hoy
    lineas: list[str] = []
    p = lineas.append

    p(f"# Plan de carrera — {datos.carrera}")
    p("")
    p(f"> Plan {datos.plan} · Generado el **{hoy}** · Motor `tools/planificador` v{VERSION}.")
    p("> Documento REGENERABLE: se rehace con `/carrera` (no editar a mano).")
    p("")

    # -- Validación ------------------------------------------------------
    if not resultado.validacion.ok or resultado.validacion.avisos:
        p("## ⚠️ Datos: cosas a revisar")
        p("")
        for problema in resultado.validacion.errores:
            p(f"- 🔴 **{problema.codigo}**: {problema.mensaje}")
        for problema in resultado.validacion.avisos:
            p(f"- 🟠 {problema.codigo}: {problema.mensaje}")
        p("")

    # -- Foto de hoy -----------------------------------------------------
    estado = datos.estado_inicial()
    grafo = resultado.grafo
    p("## Hoy")
    p("")
    cursando = estado.codigos_en("cursando")
    regularizadas = estado.codigos_en("regularizada")
    p(f"- **Cursando:** {', '.join(cursando) or '—'}")
    p(f"- **Con final pendiente (regularizadas):** {', '.join(regularizadas) or '—'}")
    p(f"- **Se podría anotar ya (cumple correlativas):** {', '.join(grafo.cursables(estado)) or '—'}")
    p("")

    # -- Regularidades e intentos ----------------------------------------
    modo_vigencia = datos.config.vigencia.get("modo", "no_vence")
    p("## Regularidades e intentos de final")
    p("")
    if modo_vigencia == "no_vence":
        p(
            "La regularidad **no vence** en este reglamento. Lo que sí corre: cada final "
            f"desaprobado suma un intento y al {datos.config.intentos['maximo']}º hay que **recursar**; "
            "y cuanto más vieja la cursada, más olvidado el contenido."
        )
        p("")
    p("| Materia | Cursada en | Hace | Intentos de final | Situación |")
    p("|---|---|---|---|---|")
    for materia in datos.materias:
        if materia.estado != "regularizada":
            continue
        intentos = intentos_de_materia(materia, datos.config)
        antiguedad = antiguedad_regularidad(materia, hoy)
        iconos = {"ok": "🟢", "atencion": "🟠", "ultima-chance": "🔴", "agotado": "🔴 RECURSAR"}
        situacion = f"{iconos.get(intentos.situacion, '❔')}"
        if intentos.situacion != "ok":
            situacion += f" {intentos.mensaje}"
        elif antiguedad is not None and antiguedad >= 4:
            situacion = f"🟠 contenido de hace {antiguedad} años: refrescar antes de rendir"
        p(
            f"| {materia.codigo} | {materia.anio or '—'} | "
            f"{f'~{antiguedad} años' if antiguedad is not None else '—'} | "
            f"{intentos.usados} de {intentos.maximo} | {situacion} |"
        )
    p("")
    if modo_vigencia != "no_vence":
        urgentes = [r for r in resultado.regularidades if r.situacion in ("por-vencer", "vencida")]
        for reg in resultado.regularidades:
            if reg.vence:
                p(f"- {reg.codigo}: vence el {_fmt_fecha(reg.vence)} ({reg.situacion}).")
        if urgentes:
            p("")
            p("**Prioridad:** " + ", ".join(r.codigo for r in urgentes) + " — rendilas antes del vencimiento.")
        p("")
    promovidas = sorted(m.codigo for m in datos.materias if datos.promocion_asumida(m.codigo))
    if promovidas:
        p(
            "✨ **Promociones asumidas (sin final):** "
            + ", ".join(promovidas)
            + " — si alguna promoción se cae, sacale la marca y recalculá."
        )
        p("")

    # -- Plan de finales -------------------------------------------------
    p("## Plan de finales")
    p("")
    p("| Ventana | Fecha | Materia | Prepará desde | Carga | Score | Origen |")
    p("|---|---|---|---|---|---|---|")
    for final in resultado.plan_finales.finales:
        prep = final.preparacion
        carga = f"{prep.horas:g} h (~{prep.dias_calendario} días)"
        origen = {"fijado": "📌 fijado", "declarado": "declarado"}.get(final.origen, "sugerido")
        ventana = final.ventana
        p(
            f"| {ventana} | **{final.fecha}** | {final.codigo} — {final.nombre} | "
            f"{prep.inicio} | {carga} | {final.score.total:g} | {origen} |"
        )
    if not resultado.plan_finales.finales:
        p("| — | — | *(sin finales asignables en las ventanas cargadas)* | — | — | — | — |")
    p("")
    for item in resultado.plan_finales.descartadas:
        p(f"- ⚠️ {item['codigo']} quedó fuera de la ventana '{item['ventana']}': {item['motivo']}.")
    if resultado.plan_finales.sin_ventana:
        p(
            "- Sin ventana asignada todavía: "
            + ", ".join(resultado.plan_finales.sin_ventana)
            + " (cargá más ventanas en `calendario.json` o entran en la proyección)."
        )
    p("")

    # -- Conflictos ------------------------------------------------------
    p("### Conflictos detectados")
    p("")
    if resultado.plan_finales.conflictos:
        for conflicto in resultado.plan_finales.conflictos:
            icono = _EMOJI_SEVERIDAD.get(conflicto.severidad, "🟡")
            p(f"- {icono} **{conflicto.tipo}** ({' + '.join(conflicto.involucra)}): {conflicto.mensaje}.")
            if conflicto.sugerencia:
                p(f"  - Sugerencia: {conflicto.sugerencia}.")
    else:
        p("- Ninguno con el calendario actual.")
    p("")

    # -- Pins del tablero con problemas ----------------------------------
    violaciones = resultado.plan_finales.violaciones + resultado.proyeccion.violaciones
    if violaciones:
        p("### ⚠️ Decisiones del tablero que rompen reglas")
        p("")
        p("El plan las respeta igual (mandás vos), pero quedan señaladas:")
        p("")
        for v in violaciones:
            p(f"- 🔴 **{v['codigo']}** en `{v['donde']}` ({v['tipo']}): {v['motivo']}.")
        p("")
        p("*Para resolverlas: movelas en el tablero (`exports/tablero.html`) y re-exportá `plan-manual.json`.*")
        p("")

    # -- Ranking ---------------------------------------------------------
    p("## Qué preparar primero (ranking explicado)")
    p("")
    p("| # | Materia | Score | Urgencia | Impacto | Proximidad | Esfuerzo |")
    p("|---|---|---|---|---|---|---|")
    for i, score in enumerate(resultado.ranking, 1):
        c = {comp.nombre: comp for comp in score.componentes}
        p(
            f"| {i} | **{score.codigo}** | **{score.total:g}** | "
            f"{c['urgencia'].aporte:g} | {c['impacto'].aporte:g} | "
            f"{c['proximidad'].aporte:g} | {c['esfuerzo'].aporte:g} |"
        )
    p("")
    p("<details><summary>Desglose completo de cada score</summary>")
    p("")
    for score in resultado.ranking:
        p(f"**{score.codigo}** → {score.total:g}/100")
        p("")
        for comp in score.componentes:
            p(f"- {comp.nombre} (peso {comp.peso:.2f}): {comp.crudo} → aporta {comp.aporte:g}")
        p("")
    p("</details>")
    p("")

    # -- Proyección ------------------------------------------------------
    proy = resultado.proyeccion
    p("## Proyección de cursada (cuatrimestre por cuatrimestre)")
    p("")
    if proy.graduacion:
        p(
            f"**Fecha estimada de graduación: {proy.graduacion}** "
            f"({proy.cuatrimestres_restantes} cuatrimestres, máx. {proy.max_materias} materias c/u)."
        )
    else:
        p(
            f"⚠️ La simulación no completó la carrera en el horizonte: quedan {', '.join(proy.pendientes)}."
        )
    p("")
    p(
        f"Piso teórico por correlativas: **{proy.piso_teorico} cuatrimestres** "
        f"(cadena crítica: {' → '.join(proy.cadena_critica) or '—'})."
    )
    p("")
    p("| Cuatrimestre | Cursa | Cierra cursada | Finales |")
    p("|---|---|---|---|")
    for periodo in proy.periodos:
        finales_txt = (
            "<br>".join(
                ("📌 " if f.origen == "fijado" else "")
                + f"{f.codigo} ({f.fecha}{', est.' if f.ventana_estimada else ''})"
                for f in periodo.finales
            )
            or "—"
        )

        def marca_cursa(codigo: str) -> str:
            partes = codigo
            if codigo in periodo.fijadas:
                partes = "📌 " + partes
            if codigo in periodo.recursa:
                partes += " (recursa)"
            return partes

        cursa_txt = ", ".join(marca_cursa(c) for c in periodo.cursa) or "—"
        cierra = [*periodo.regulariza, *(f"✨{c}" for c in periodo.promociona)]
        etiqueta = periodo.cuatrimestre.etiqueta
        if not periodo.inscripcion_abierta and periodo.nuevas == ():
            etiqueta += " *(en curso)*"
        p(f"| **{etiqueta}** | {cursa_txt} | {', '.join(cierra) or '—'} | {finales_txt} |")
    p("")
    p("Supuestos de la simulación: " + "; ".join(proy.supuestos) + ".")
    p("")

    # -- Escenarios ------------------------------------------------------
    p("### Escenarios (¿y si curso más/menos por cuatrimestre?)")
    p("")
    p("| Materias/cuatrimestre | Graduación | Cuatrimestres |")
    p("|---|---|---|")
    for escenario in resultado.escenarios:
        grad = _fmt_fecha(escenario.graduacion) if escenario.completa else "no termina en el horizonte"
        p(f"| {escenario.max_materias} | {grad} | {escenario.cuatrimestres} |")
    p("")

    # -- Objetivos -------------------------------------------------------
    if resultado.veredictos:
        p("## Objetivos declarados")
        p("")
        for veredicto in resultado.veredictos:
            icono = _EMOJI_VEREDICTO.get(veredicto.resultado, "❔")
            objetivo = veredicto.objetivo
            titulo = objetivo.id
            p(f"- {icono} **{titulo}** ({veredicto.resultado}): {veredicto.motivo}.")
            for paso in veredicto.que_haria_falta:
                p(f"  - → {paso}.")
        p("")

    # -- Electivas -------------------------------------------------------
    electivas = resultado.electivas
    p("## Electivas")
    p("")
    p(
        f"Acumuladas: **{electivas.horas_aprobadas:g} h** aprobadas"
        + (f" (+{electivas.horas_en_curso:g} h en curso)" if electivas.horas_en_curso else "")
        + f" — {', '.join(electivas.aprobadas) or 'ninguna'}."
    )
    p("")
    p("| Nivel | Requeridas | Acumuladas | Falta |")
    p("|---|---|---|---|")
    for req in electivas.requisitos:
        estado_txt = "✅" if req.cumple else f"faltan {req.falta:g} h"
        p(f"| {req.nivel} | {req.requeridas:g} h | {req.acumuladas:g} h | {estado_txt} |")
    p("")
    if electivas.aviso_unidades:
        p(f"⚠️ {electivas.aviso_unidades}.")
        p("")

    # -- Puente con el sistema de estudio --------------------------------
    con_slug = [f for f in resultado.plan_finales.finales if f.slug]
    if con_slug:
        p("## Siguiente paso en el sistema de estudio")
        p("")
        for final in con_slug:
            p(
                f"- **{final.codigo}** vive en `materias/{final.slug}/`: usá `/estrategia` y `/plan` "
                f"ahí para bajar este objetivo (final el {final.fecha}, arrancar el "
                f"{final.preparacion.inicio}) a un plan de días concreto."
            )
        sin_slug = [f for f in resultado.plan_finales.finales if not f.slug]
        if sin_slug:
            p(
                "- Sin carpeta de materia todavía: "
                + ", ".join(f.codigo for f in sin_slug)
                + " → `/nueva-materia` cuando arranque la preparación."
            )
        p("")

    # -- Tablero ---------------------------------------------------------
    p("## Ajustar el plan a mano")
    p("")
    p(
        "Abrí **`carrera/exports/tablero.html`**: arrastrás cursadas a cuatrimestres y "
        "finales a mesas, marcás promociones ✨ y anotás intentos, con validación en vivo. "
        "Al exportar te da `plan-manual.json`; guardalo en `carrera/datos/` y volvé a correr "
        "`/carrera` para que este plan respete lo que fijaste."
    )
    p("")

    p("---")
    p("")
    fuentes = "estado.json, correlativas.json, calendario.json, config.json, objetivos.json"
    if not datos.plan_manual.vacio:
        fuentes += ", plan-manual.json (pins del tablero)"
    p(f"*Generado el {hoy} desde `carrera/datos/` ({fuentes}). Regenerar con `/carrera`.*")
    p("")
    return "\n".join(lineas)


# --------------------------------------------------------------------------
# iCalendar (.ics)
# --------------------------------------------------------------------------


def _ics_escape(texto: str) -> str:
    return (
        texto.replace("\\", "\\\\").replace(";", "\\;").replace(",", "\\,").replace("\n", "\\n")
    )


def _evento_dia(uid: str, dia: date, resumen: str, descripcion: str, sello: str) -> list[str]:
    return [
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTAMP:{sello}",
        f"DTSTART;VALUE=DATE:{dia.strftime('%Y%m%d')}",
        f"DTEND;VALUE=DATE:{(dia + timedelta(days=1)).strftime('%Y%m%d')}",
        f"SUMMARY:{_ics_escape(resumen)}",
        f"DESCRIPTION:{_ics_escape(descripcion)}",
        "END:VEVENT",
    ]


def a_ics(resultado: Resultado) -> str:
    """Calendario con finales, arranques de preparación y parciales."""
    hoy = resultado.datos.calendario.hoy
    sello = datetime(hoy.year, hoy.month, hoy.day).strftime("%Y%m%dT%H%M%SZ")
    lineas = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//utn-boost//planificador-carrera//ES",
        "CALSCALE:GREGORIAN",
        f"X-WR-CALNAME:{_ics_escape('Plan de carrera (utn-boost)')}",
    ]
    for final in resultado.plan_finales.finales:
        base = f"utn-boost-{final.codigo.lower()}-{final.fecha.isoformat()}"
        lineas += _evento_dia(
            f"{base}-final",
            final.fecha,
            f"🎓 Final {final.codigo} — {final.nombre}",
            f"Ventana {final.ventana}. Score {final.score.total:g}. {final.score.explicacion()}",
            sello,
        )
        lineas += _evento_dia(
            f"{base}-prep",
            final.preparacion.inicio,
            f"📚 Arrancar {final.codigo} (final el {final.fecha})",
            (
                f"{final.preparacion.horas:g} h estimadas en ~{final.preparacion.dias_calendario} días "
                f"({final.preparacion.origen_horas})."
            ),
            sello,
        )
    for parcial in resultado.datos.calendario.parciales:
        lineas += _evento_dia(
            f"utn-boost-{parcial.codigo.lower()}-parcial{parcial.numero}-{parcial.fecha.isoformat()}",
            parcial.fecha,
            f"📝 {parcial.etiqueta} — {parcial.nombre}",
            "Parcial de cursada (calendario.json).",
            sello,
        )
    lineas.append("END:VCALENDAR")
    return "\r\n".join(lineas) + "\r\n"
