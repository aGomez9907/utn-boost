"""Export visual del plan de carrera: HTML autocontenido con Gantt + DAG.

Sin dependencias ni CDN: todo el SVG se calcula acá y el CSS va inline, así el
archivo se abre offline en cualquier navegador (y en el iPad). Respeta modo
claro/oscuro con `prefers-color-scheme`, igual que los exports de apuntes.
"""

from __future__ import annotations

import html
from datetime import date, timedelta

from .salidas import Resultado

# Paleta por estado (claro, oscuro se ajusta con CSS vars).
COLORES = {
    "aprobada": "var(--ok)",
    "regularizada": "var(--reg)",
    "cursando": "var(--cur)",
    "bloqueada": "var(--blo)",
}

CSS = """
:root {
  color-scheme: light dark;
  --fondo: #ffffff; --tinta: #1a1a1a; --suave: #667085; --linea: #e4e7ec;
  --tarjeta: #f8fafc; --ok: #12b76a; --reg: #2e90fa; --cur: #f79009; --blo: #98a2b3;
  --rojo: #f04438; --violeta: #7a5af8; --hoy: #f04438;
}
@media (prefers-color-scheme: dark) {
  :root {
    --fondo: #16181c; --tinta: #e6e6e6; --suave: #98a2b3; --linea: #30343c;
    --tarjeta: #1f2228; --ok: #32d583; --reg: #53b1fd; --cur: #fdb022; --blo: #667085;
    --rojo: #f97066; --violeta: #9b8afb; --hoy: #f97066;
  }
}
* { box-sizing: border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  margin: 0; padding: 2rem 1.25rem 4rem; background: var(--fondo); color: var(--tinta);
  line-height: 1.5; max-width: 1240px; margin-inline: auto;
}
h1 { font-size: 1.6rem; margin: 0 0 .2rem; }
h2 { font-size: 1.15rem; margin: 2.2rem 0 .8rem; border-bottom: 1px solid var(--linea); padding-bottom: .3rem; }
.sub { color: var(--suave); font-size: .9rem; margin-bottom: 1.4rem; }
.chips { display: flex; flex-wrap: wrap; gap: .5rem; margin: .8rem 0; }
.chip {
  border: 1px solid var(--linea); border-radius: 999px; padding: .25rem .7rem;
  font-size: .82rem; background: var(--tarjeta);
}
.chip b { font-weight: 600; }
.ok { border-color: var(--ok); } .warn { border-color: var(--cur); } .bad { border-color: var(--rojo); }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: .8rem; }
.card { background: var(--tarjeta); border: 1px solid var(--linea); border-radius: 10px; padding: .9rem 1rem; }
.card h3 { margin: 0 0 .4rem; font-size: .95rem; }
.card .big { font-size: 1.5rem; font-weight: 700; }
.card .nota { color: var(--suave); font-size: .8rem; }
svg text { fill: var(--tinta); }
svg .suave { fill: var(--suave); }
.scroll { overflow-x: auto; border: 1px solid var(--linea); border-radius: 10px; background: var(--tarjeta); padding: .6rem; }
.leyenda { display: flex; flex-wrap: wrap; gap: 1rem; font-size: .8rem; color: var(--suave); margin: .5rem 0 0; }
.leyenda span { display: inline-flex; align-items: center; gap: .35rem; }
.cuadrito { width: 12px; height: 12px; border-radius: 3px; display: inline-block; }
.semestres { display: flex; gap: .8rem; overflow-x: auto; padding-bottom: .5rem; }
.semestre { min-width: 210px; flex: 1; }
.semestre .titulo { font-weight: 700; margin-bottom: .5rem; }
.semestre .materia { border-left: 3px solid var(--reg); padding: .2rem .5rem; margin: .25rem 0; font-size: .85rem; background: var(--fondo); border-radius: 0 6px 6px 0; }
.semestre .materia.anual { border-left-color: var(--violeta); }
.semestre .final { font-size: .8rem; color: var(--suave); margin: .2rem 0 0 .2rem; }
.semestre .final b { color: var(--tinta); }
table { border-collapse: collapse; font-size: .88rem; }
th, td { border: 1px solid var(--linea); padding: .35rem .7rem; text-align: left; }
th { background: var(--tarjeta); }
footer { margin-top: 3rem; color: var(--suave); font-size: .8rem; border-top: 1px solid var(--linea); padding-top: 1rem; }
"""


def _esc(texto: str) -> str:
    return html.escape(str(texto), quote=True)


# --------------------------------------------------------------------------
# Gantt de finales + parciales
# --------------------------------------------------------------------------


def _gantt(resultado: Resultado) -> str:
    datos = resultado.datos
    hoy = datos.calendario.hoy
    finales = sorted(resultado.plan_finales.finales, key=lambda f: f.fecha)
    parciales = list(datos.calendario.parciales)
    if not finales and not parciales:
        return "<p>No hay finales ni parciales cargados en el calendario.</p>"

    fin_max = max(
        [f.fecha for f in finales] + [p.fecha for p in parciales] + [hoy + timedelta(days=30)]
    )
    inicio_min = min([f.preparacion.inicio for f in finales] + [hoy]) - timedelta(days=3)
    dias_totales = (fin_max - inicio_min).days + 8

    px_dia = max(5.0, min(9.0, 950 / dias_totales))
    gutter = 150
    ancho = gutter + int(dias_totales * px_dia) + 20
    fila_h = 34
    filas = len(finales) + (1 if parciales else 0)
    alto = 70 + filas * fila_h + 30

    def x(fecha: date) -> float:
        return gutter + (fecha - inicio_min).days * px_dia

    s: list[str] = [
        f'<svg viewBox="0 0 {ancho} {alto}" width="{ancho}" role="img" '
        f'aria-label="Cronograma de preparación y finales" xmlns="http://www.w3.org/2000/svg">'
    ]

    # Rejilla mensual.
    cursor = date(inicio_min.year, inicio_min.month, 1)
    while cursor <= fin_max:
        if cursor >= inicio_min:
            s.append(
                f'<line x1="{x(cursor):.1f}" y1="40" x2="{x(cursor):.1f}" y2="{alto - 25}" '
                'stroke="var(--linea)" stroke-width="1"/>'
            )
            s.append(
                f'<text x="{x(cursor) + 4:.1f}" y="34" font-size="11" class="suave">'
                f"{cursor.strftime('%m/%Y')}</text>"
            )
        cursor = date(cursor.year + (cursor.month == 12), cursor.month % 12 + 1, 1)

    # Línea de HOY.
    s.append(
        f'<line x1="{x(hoy):.1f}" y1="40" x2="{x(hoy):.1f}" y2="{alto - 25}" '
        'stroke="var(--hoy)" stroke-width="1.5" stroke-dasharray="4 3"/>'
        f'<text x="{x(hoy) + 4:.1f}" y="52" font-size="10" fill="var(--hoy)">hoy</text>'
    )

    y = 62
    # Fila de parciales.
    if parciales:
        s.append(f'<text x="8" y="{y + 16}" font-size="12" font-weight="600">Parciales</text>')
        for parcial in parciales:
            cx = x(parcial.fecha)
            s.append(
                f'<g><rect x="{cx - 5:.1f}" y="{y + 6}" width="10" height="14" rx="2" fill="var(--cur)"/>'
                f'<text x="{cx:.1f}" y="{y + 32}" font-size="9" text-anchor="middle" class="suave">'
                f"{_esc(parcial.etiqueta)}</text>"
                f"<title>{_esc(parcial.etiqueta)} — {parcial.fecha}</title></g>"
            )
        y += fila_h

    # Una fila por final: barra de preparación + rombo del examen.
    for final in finales:
        prep = final.preparacion
        en_riesgo = final.regularidad.situacion == "vencida" or (
            final.intentos is not None and final.intentos.situacion in ("ultima-chance", "agotado")
        )
        color = "var(--rojo)" if en_riesgo else "var(--reg)"
        s.append(f'<text x="8" y="{y + 16}" font-size="12" font-weight="600">{_esc(final.codigo)}</text>')
        s.append(
            f'<rect x="{x(prep.inicio):.1f}" y="{y + 5}" width="{max(3, (x(prep.fin) - x(prep.inicio))):.1f}" '
            f'height="14" rx="7" fill="{color}" opacity="0.35"/>'
        )
        cx = x(final.fecha)
        s.append(
            f'<g><path d="M {cx:.1f} {y + 2} l 8 10 l -8 10 l -8 -10 z" fill="{color}"/>'
            f"<title>Final {_esc(final.codigo)} — {final.fecha} ({_esc(final.ventana)}). "
            f"Preparación desde {prep.inicio} ({prep.horas:g} h).</title></g>"
        )
        s.append(
            f'<text x="{cx + 12:.1f}" y="{y + 16}" font-size="10" class="suave">{final.fecha.strftime("%d/%m")}</text>'
        )
        y += fila_h

    s.append("</svg>")
    return "".join(s)


# --------------------------------------------------------------------------
# Mapa de correlativas (DAG por capas)
# --------------------------------------------------------------------------


def _dag(resultado: Resultado) -> str:
    grafo = resultado.grafo
    datos = resultado.datos
    estado = datos.estado_inicial()
    niveles = grafo.niveles_topologicos()

    # Cuándo proyecta cursarse/rendirse cada pendiente.
    cursa_en: dict[str, str] = {}
    rinde_en: dict[str, str] = {}
    for periodo in resultado.proyeccion.periodos:
        for codigo in periodo.nuevas:
            cursa_en.setdefault(codigo, periodo.cuatrimestre.etiqueta)
        for final in periodo.finales:
            rinde_en.setdefault(final.codigo, final.fecha.strftime("%m/%Y"))

    capas: dict[int, list[str]] = {}
    for codigo, capa in niveles.items():
        capas.setdefault(capa, []).append(codigo)
    for lista in capas.values():
        lista.sort(key=lambda c: (datos.materia(c).nivel, c))

    caja_w, caja_h, paso_x, paso_y = 118, 44, 172, 62
    max_filas = max(len(v) for v in capas.values())
    ancho = 20 + len(capas) * paso_x
    alto = 40 + max_filas * paso_y

    pos: dict[str, tuple[float, float]] = {}
    for capa, lista in sorted(capas.items()):
        margen = (max_filas - len(lista)) * paso_y / 2
        for i, codigo in enumerate(lista):
            pos[codigo] = (14 + capa * paso_x, 20 + margen + i * paso_y)

    s: list[str] = [
        f'<svg viewBox="0 0 {ancho} {alto}" width="{ancho}" role="img" '
        f'aria-label="Mapa de correlatividades" xmlns="http://www.w3.org/2000/svg">'
    ]

    # Aristas primero (debajo de los nodos).
    for codigo in grafo.codigos():
        corr = grafo.correlativas.get(codigo)
        if corr is None:
            continue
        x2, y2 = pos[codigo]
        for req, estilo in [(r, "dash") for r in corr.requiere_regularizadas] + [
            (r, "solid") for r in corr.requiere_aprobadas
        ]:
            if req not in pos:
                continue
            x1, y1 = pos[req]
            ax, ay = x1 + caja_w, y1 + caja_h / 2
            bx, by = x2, y2 + caja_h / 2
            medio = (ax + bx) / 2
            dash = ' stroke-dasharray="4 3"' if estilo == "dash" else ""
            cumplida = (
                estado.al_menos(req, "aprobada")
                if estilo == "solid"
                else estado.al_menos(req, "regularizada")
            )
            opacidad = "0.55" if cumplida else "0.95"
            color = "var(--blo)" if cumplida else "var(--cur)"
            s.append(
                f'<path d="M {ax:.0f} {ay:.0f} C {medio:.0f} {ay:.0f} {medio:.0f} {by:.0f} {bx:.0f} {by:.0f}" '
                f'fill="none" stroke="{color}" stroke-width="1.3" opacity="{opacidad}"{dash}/>'
            )

    # Nodos.
    for codigo, (cx, cy) in pos.items():
        materia = datos.materia(codigo)
        color = COLORES[materia.estado]
        etiqueta2 = ""
        if materia.estado == "bloqueada" and codigo in cursa_en:
            etiqueta2 = f"cursaría {cursa_en[codigo]}"
        elif materia.estado in ("regularizada", "cursando") and codigo in rinde_en:
            etiqueta2 = f"final {rinde_en[codigo]}"
        elif materia.estado == "aprobada" and materia.nota:
            etiqueta2 = f"nota {materia.nota}"
        titulo = f"{materia.nombre} — {materia.estado}"
        if etiqueta2:
            titulo += f" · {etiqueta2}"
        s.append(
            f'<g><rect x="{cx:.0f}" y="{cy:.0f}" width="{caja_w}" height="{caja_h}" rx="8" '
            f'fill="{color}" opacity="0.16" stroke="{color}" stroke-width="1.6"/>'
            f'<text x="{cx + caja_w / 2:.0f}" y="{cy + 18:.0f}" font-size="11.5" font-weight="700" '
            f'text-anchor="middle">{_esc(codigo)}</text>'
            + (
                f'<text x="{cx + caja_w / 2:.0f}" y="{cy + 34:.0f}" font-size="9" text-anchor="middle" '
                f'class="suave">{_esc(etiqueta2)}</text>'
                if etiqueta2
                else ""
            )
            + f"<title>{_esc(titulo)}</title></g>"
        )

    s.append("</svg>")
    return "".join(s)


# --------------------------------------------------------------------------
# Proyección por cuatrimestre (tarjetas)
# --------------------------------------------------------------------------


def _semestres(resultado: Resultado) -> str:
    datos = resultado.datos
    tarjetas: list[str] = []
    for periodo in resultado.proyeccion.periodos:
        materias = []
        for codigo in periodo.cursa:
            clase = "materia anual" if datos.materia(codigo).es_anual else "materia"
            materias.append(f'<div class="{clase}">{_esc(codigo)} — {_esc(datos.materia(codigo).nombre)}</div>')
        finales = [
            f'<div class="final">🎓 <b>{_esc(f.codigo)}</b> {f.fecha.strftime("%d/%m/%Y")}'
            + (" <i>(est.)</i>" if f.ventana_estimada else "")
            + "</div>"
            for f in periodo.finales
        ]
        etiqueta = periodo.cuatrimestre.etiqueta
        if not periodo.inscripcion_abierta and not periodo.nuevas:
            etiqueta += " · en curso"
        tarjetas.append(
            '<div class="semestre card"><div class="titulo">'
            + _esc(etiqueta)
            + "</div>"
            + ("".join(materias) or '<div class="nota">— no cursa nada —</div>')
            + "".join(finales)
            + "</div>"
        )
    return '<div class="semestres">' + "".join(tarjetas) + "</div>"


# --------------------------------------------------------------------------
# Página completa
# --------------------------------------------------------------------------


def a_html(resultado: Resultado) -> str:
    datos = resultado.datos
    proy = resultado.proyeccion
    hoy = datos.calendario.hoy

    grad = proy.graduacion.strftime("%d/%m/%Y") if proy.graduacion else "no cierra en el horizonte"
    conflictos_alta = [c for c in resultado.plan_finales.conflictos if c.severidad == "alta"]

    objetivos_html = ""
    if resultado.veredictos:
        clases = {"alcanzable": "ok", "ajustado": "warn", "inalcanzable": "bad"}
        iconos = {"alcanzable": "✅", "ajustado": "🟡", "inalcanzable": "❌"}
        chips = "".join(
            f'<span class="chip {clases[v.resultado]}" title="{_esc(v.motivo)}">'
            f"{iconos[v.resultado]} <b>{_esc(v.objetivo.id)}</b></span>"
            for v in resultado.veredictos
        )
        objetivos_html = f"<h2>Objetivos</h2><div class='chips'>{chips}</div>"

    escenarios_filas = "".join(
        f"<tr><td>{e.max_materias}</td>"
        f"<td>{e.graduacion.strftime('%d/%m/%Y') if e.graduacion else 'no termina'}</td>"
        f"<td>{e.cuatrimestres}</td></tr>"
        for e in resultado.escenarios
    )

    conflictos_html = ""
    if resultado.plan_finales.conflictos:
        items = "".join(
            f"<li><b>{_esc(c.tipo)}</b> ({_esc(' + '.join(c.involucra))}): {_esc(c.mensaje)}</li>"
            for c in resultado.plan_finales.conflictos
        )
        conflictos_html = f"<h2>Conflictos</h2><ul>{items}</ul>"

    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Plan de carrera — {_esc(datos.plan)}</title>
<style>{CSS}</style>
</head>
<body>
<h1>Plan de carrera — {_esc(datos.carrera)}</h1>
<div class="sub">{_esc(datos.plan)} · generado el {hoy} · regenerable con <code>/carrera</code></div>

<div class="grid">
  <div class="card"><h3>🎓 Graduación estimada</h3><div class="big">{_esc(grad)}</div>
    <div class="nota">{proy.cuatrimestres_restantes} cuatrimestres · máx. {proy.max_materias} materias c/u</div></div>
  <div class="card"><h3>📝 Próximo final</h3><div class="big">{_esc(resultado.plan_finales.finales[0].codigo if resultado.plan_finales.finales else '—')}</div>
    <div class="nota">{_esc(resultado.plan_finales.finales[0].fecha.strftime('%d/%m/%Y') + ' · preparar desde ' + resultado.plan_finales.finales[0].preparacion.inicio.strftime('%d/%m') if resultado.plan_finales.finales else 'sin ventanas cargadas')}</div></div>
  <div class="card"><h3>⚠️ Conflictos altos</h3><div class="big">{len(conflictos_alta)}</div>
    <div class="nota">de {len(resultado.plan_finales.conflictos)} detectados</div></div>
  <div class="card"><h3>⛓️ Cadena crítica</h3><div class="big">{proy.piso_teorico} cuatris</div>
    <div class="nota">{_esc(' → '.join(proy.cadena_critica) or '—')}</div></div>
</div>

{objetivos_html}

<h2>Cronograma: preparación, finales y parciales</h2>
<div class="scroll">{_gantt(resultado)}</div>
<div class="leyenda">
  <span><span class="cuadrito" style="background:var(--reg);opacity:.4"></span> preparación</span>
  <span>◆ final</span>
  <span><span class="cuadrito" style="background:var(--cur)"></span> parcial</span>
  <span style="color:var(--rojo)">◆ en riesgo (último intento / regularidad vencida)</span>
  <span style="color:var(--hoy)">┆ hoy</span>
</div>

<p class="sub">¿Querés mover cosas a mano? Abrí <b><code>tablero.html</code></b> (misma carpeta):
es la versión arrastrable de este plan, con validación en vivo y export de <code>plan-manual.json</code>.</p>

<h2>Proyección cuatrimestre a cuatrimestre</h2>
{_semestres(resultado)}

<h2>Escenarios</h2>
<table><thead><tr><th>Materias/cuatri</th><th>Graduación</th><th>Cuatrimestres</th></tr></thead>
<tbody>{escenarios_filas}</tbody></table>

<h2>Mapa de correlatividades</h2>
<div class="scroll">{_dag(resultado)}</div>
<div class="leyenda">
  <span><span class="cuadrito" style="background:var(--ok)"></span> aprobada</span>
  <span><span class="cuadrito" style="background:var(--reg)"></span> regularizada</span>
  <span><span class="cuadrito" style="background:var(--cur)"></span> cursando</span>
  <span><span class="cuadrito" style="background:var(--blo)"></span> bloqueada</span>
  <span>— requiere aprobada · ┄ requiere regularizada · naranja = requisito pendiente</span>
</div>

{conflictos_html}

<footer>Generado el {hoy} por <code>tools/planificador</code> desde <code>carrera/datos/</code>.
Archivo regenerable: no editar a mano. La verdad canónica es <code>carrera/plan-carrera.md</code>.</footer>
</body>
</html>
"""
