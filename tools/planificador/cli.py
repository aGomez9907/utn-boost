"""CLI del planificador de carrera.

Uso (desde la raíz del repo):

    venv/bin/python -m tools.planificador.cli plan            # corrida completa → md + json + ics
    venv/bin/python -m tools.planificador.cli plan --max 4    # escenario con otro tope
    venv/bin/python -m tools.planificador.cli finales         # solo plan de finales (texto)
    venv/bin/python -m tools.planificador.cli ranking         # solo prioridades (texto)
    venv/bin/python -m tools.planificador.cli proyeccion      # solo cursada futura (texto)
    venv/bin/python -m tools.planificador.cli objetivos       # solo targets (texto)
    venv/bin/python -m tools.planificador.cli validar         # chequear los datos
    venv/bin/python -m tools.planificador.cli json            # JSON completo a stdout

Los datos se leen de carrera/datos/ (o --datos <carpeta>). Los archivos se
escriben en carrera/ (plan-carrera.md) y carrera/exports/ (json + ics).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import correr
from .grafo import validar as validar_datos
from .modelo import ErrorDeDatos, cargar
from .salidas import Resultado, a_ics, a_json, a_markdown
from .tablero import a_tablero_html
from .visual import a_html

RAIZ = Path(__file__).resolve().parents[2]
DATOS_DEFAULT = RAIZ / "carrera" / "datos"
SALIDA_MD = RAIZ / "carrera" / "plan-carrera.md"
SALIDA_EXPORTS = RAIZ / "carrera" / "exports"


def _cargar(args: argparse.Namespace):
    datos = cargar(Path(args.datos))
    if args.hoy:
        from datetime import date

        datos = datos.con_hoy(date.fromisoformat(args.hoy))
    if args.max:
        datos = datos.con_config(
            datos.config.con(cursada={"max_materias_por_cuatrimestre": int(args.max)})
        )
    return datos


def cmd_validar(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    validacion = validar_datos(datos)
    for problema in validacion.errores:
        print(f"🔴 {problema.codigo}: {problema.mensaje}")
    for problema in validacion.avisos:
        print(f"🟠 {problema.codigo}: {problema.mensaje}")
    if validacion.ok and not validacion.avisos:
        print("✅ Datos consistentes.")
    return 0 if validacion.ok else 1


def cmd_plan(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos, max_materias=int(args.max) if args.max else None)

    SALIDA_EXPORTS.mkdir(parents=True, exist_ok=True)
    SALIDA_MD.write_text(a_markdown(resultado), encoding="utf-8")
    ruta_json = SALIDA_EXPORTS / "plan-carrera.json"
    ruta_json.write_text(
        json.dumps(a_json(resultado), ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    ruta_ics = SALIDA_EXPORTS / "plan-carrera.ics"
    ruta_ics.write_text(a_ics(resultado), encoding="utf-8")
    ruta_html = SALIDA_EXPORTS / "plan-carrera.html"
    ruta_html.write_text(a_html(resultado), encoding="utf-8")
    ruta_tablero = SALIDA_EXPORTS / "tablero.html"
    ruta_tablero.write_text(a_tablero_html(resultado), encoding="utf-8")

    print(f"✓ {SALIDA_MD.relative_to(RAIZ)}")
    print(f"✓ {ruta_json.relative_to(RAIZ)}")
    print(f"✓ {ruta_ics.relative_to(RAIZ)}")
    print(f"✓ {ruta_html.relative_to(RAIZ)}")
    print(f"✓ {ruta_tablero.relative_to(RAIZ)} (arrastrable)")
    _imprimir_resumen(resultado)
    return 0


def _imprimir_resumen(resultado: Resultado) -> None:
    print()
    print("— Resumen —")
    marcas = {"fijado": "📌", "declarado": "🎯", "sugerido": "💡"}
    for final in resultado.plan_finales.finales:
        print(
            f"{marcas.get(final.origen, '💡')} {final.fecha} {final.codigo} ({final.ventana}) "
            f"— preparar desde {final.preparacion.inicio}"
        )
    promovidas = sorted(
        m.codigo for m in resultado.datos.materias if resultado.datos.promocion_asumida(m.codigo)
    )
    if promovidas:
        print(f"✨ Promocionan sin final (asumido): {', '.join(promovidas)}")
    if resultado.proyeccion.graduacion:
        print(
            f"🎓 Graduación estimada: {resultado.proyeccion.graduacion} "
            f"({resultado.proyeccion.cuatrimestres_restantes} cuatrimestres)"
        )
    alta = [c for c in resultado.plan_finales.conflictos if c.severidad == "alta"]
    if alta:
        print(f"⚠️ {len(alta)} conflicto(s) de severidad alta — ver plan-carrera.md")
    violaciones = resultado.plan_finales.violaciones + resultado.proyeccion.violaciones
    if violaciones:
        print(f"🔴 {len(violaciones)} pin(s) del tablero rompen reglas — ver plan-carrera.md")


def cmd_finales(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos)
    for final in resultado.plan_finales.finales:
        prep = final.preparacion
        print(
            f"{final.fecha}  {final.codigo:8s} {final.ventana:14s} llamada {final.llamado} "
            f"[{final.origen}] preparar desde {prep.inicio} ({prep.horas:g} h)"
        )
    for conflicto in resultado.plan_finales.conflictos:
        print(f"  ⚠ [{conflicto.severidad}] {conflicto.mensaje}")
    return 0


def cmd_ranking(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos)
    for i, score in enumerate(resultado.ranking, 1):
        print(f"{i}. {score.codigo:8s} {score.explicacion()}")
        if args.verbose:
            for comp in score.componentes:
                print(f"     · {comp.nombre}: {comp.crudo}")
    return 0


def cmd_proyeccion(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos, max_materias=int(args.max) if args.max else None)
    proy = resultado.proyeccion
    for periodo in proy.periodos:
        finales_txt = ", ".join(f"{f.codigo}({f.fecha})" for f in periodo.finales) or "—"
        print(f"{periodo.cuatrimestre.etiqueta:8s} cursa: {', '.join(periodo.cursa) or '—'}")
        print(f"{'':8s} finales: {finales_txt}")
    if proy.graduacion:
        print(f"\n🎓 Graduación estimada: {proy.graduacion} ({proy.cuatrimestres_restantes} cuatrimestres)")
    else:
        print(f"\n⚠ No se completa la carrera en el horizonte; quedan: {', '.join(proy.pendientes)}")
    print("\nEscenarios:")
    for escenario in resultado.escenarios:
        grad = escenario.graduacion or "no termina"
        print(f"  {escenario.max_materias} materias/cuatri → {grad} ({escenario.cuatrimestres} cuatris)")
    return 0


def cmd_objetivos(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos)
    if not resultado.veredictos:
        print("No hay objetivos en carrera/datos/objetivos.json.")
        return 0
    iconos = {"alcanzable": "✅", "ajustado": "🟡", "inalcanzable": "❌"}
    for veredicto in resultado.veredictos:
        print(f"{iconos[veredicto.resultado]} {veredicto.objetivo.id}: {veredicto.motivo}")
        for paso in veredicto.que_haria_falta:
            print(f"   → {paso}")
    return 0


def cmd_json(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos)
    print(json.dumps(a_json(resultado), ensure_ascii=False, indent=2))
    return 0


def cmd_tablero(args: argparse.Namespace) -> int:
    datos = _cargar(args)
    resultado = correr(datos)
    SALIDA_EXPORTS.mkdir(parents=True, exist_ok=True)
    ruta = SALIDA_EXPORTS / "tablero.html"
    ruta.write_text(a_tablero_html(resultado), encoding="utf-8")
    print(f"✓ {ruta.relative_to(RAIZ)}")
    print("Abrilo en el navegador, acomodá el plan y exportá plan-manual.json a carrera/datos/.")
    return 0


def main(argv: list[str] | None = None) -> int:
    comunes = argparse.ArgumentParser(add_help=False)
    comunes.add_argument("--datos", default=str(DATOS_DEFAULT), help="Carpeta con los JSON de entrada.")
    comunes.add_argument("--hoy", default=None, help="Pisar la fecha de hoy (AAAA-MM-DD), para simular.")
    comunes.add_argument("--max", default=None, help="Tope de materias por cuatrimestre para la proyección.")

    parser = argparse.ArgumentParser(
        prog="planificador", description="Planificador de carrera (finales + cursada futura)."
    )
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("validar", parents=[comunes], help="Chequear consistencia de los datos.").set_defaults(fn=cmd_validar)
    sub.add_parser("plan", parents=[comunes], help="Corrida completa: escribe md + json + html + ics.").set_defaults(fn=cmd_plan)
    sub.add_parser("finales", parents=[comunes], help="Plan de finales por ventana (texto).").set_defaults(fn=cmd_finales)
    ranking_parser = sub.add_parser("ranking", parents=[comunes], help="Prioridades con desglose (texto).")
    ranking_parser.add_argument("-v", "--verbose", action="store_true")
    ranking_parser.set_defaults(fn=cmd_ranking)
    sub.add_parser("proyeccion", parents=[comunes], help="Cursada futura y graduación (texto).").set_defaults(fn=cmd_proyeccion)
    sub.add_parser("objetivos", parents=[comunes], help="Validar los targets declarados.").set_defaults(fn=cmd_objetivos)
    sub.add_parser("json", parents=[comunes], help="JSON completo a stdout.").set_defaults(fn=cmd_json)
    sub.add_parser("tablero", parents=[comunes], help="Regenerar solo el tablero arrastrable (exports/tablero.html).").set_defaults(fn=cmd_tablero)

    args = parser.parse_args(argv)
    try:
        return args.fn(args)
    except ErrorDeDatos as exc:
        print(f"Error de datos: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
