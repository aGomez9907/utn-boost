"""Convierte apuntes .md a .html con LaTeX renderizado, sin dependencias.

Genera un HTML autocontenido que renderiza el Markdown (incluidos los bloques
<details>) y las fórmulas LaTeX ($...$ y $$...$$) en el navegador, usando
markdown-it + KaTeX desde CDN. No requiere pandoc ni paquetes de pip.

Uso:
    python md_to_html.py apuntes/clase.md
    python md_to_html.py apuntes                 # todos los .md de la carpeta
    python md_to_html.py apuntes/*.md --out-dir html

Nota: como el LaTeX se renderiza en el navegador, hace falta conexión a internet
la primera vez que se abre el .html (para bajar markdown-it y KaTeX del CDN).
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# Versiones fijadas del CDN para que el resultado sea reproducible.
KATEX_VERSION = "0.16.11"
MARKDOWN_IT_VERSION = "14.1.0"
TEXMATH_VERSION = "1.0.0"

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@{katex}/dist/katex.min.css">
<style>
:root {{ color-scheme: light dark; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  line-height: 1.65; max-width: 820px; margin: 2.5rem auto; padding: 0 1.25rem;
  color: #1a1a1a; background: #fff;
}}
@media (prefers-color-scheme: dark) {{
  body {{ color: #e6e6e6; background: #16181c; }}
  a {{ color: #6cb6ff; }}
  details {{ background: #1f2228; border-color: #30343c; }}
  summary {{ background: #232730; }}
  blockquote {{ color: #aab; border-color: #30343c; }}
  code {{ background: #232730; }}
  th {{ background: #232730; }}
  th, td {{ border-color: #30343c; }}
  tbody tr:nth-child(even) {{ background: #1c1f24; }}
}}
h1, h2, h3 {{ line-height: 1.25; margin-top: 1.8rem; }}
h1 {{ border-bottom: 2px solid currentColor; padding-bottom: .3rem; }}
h2 {{ border-bottom: 1px solid #ddd; padding-bottom: .25rem; }}
a {{ color: #0969da; text-decoration: none; }}
a:hover {{ text-decoration: underline; }}
blockquote {{ margin: 1rem 0; padding: .2rem 1rem; border-left: 4px solid #ddd; color: #555; }}
code {{ background: #f3f4f6; padding: .12em .35em; border-radius: 4px; font-size: .9em; }}
details {{
  border: 1px solid #e1e4e8; border-radius: 8px; padding: 0 1rem; margin: .8rem 0;
  background: #fafbfc;
}}
details[open] {{ padding-bottom: .6rem; }}
summary {{
  cursor: pointer; font-weight: 600; padding: .7rem 1rem; margin: 0 -1rem;
  background: #f1f3f5; border-radius: 8px; user-select: none;
}}
details details {{ margin-left: .2rem; }}
.katex-display {{ overflow-x: auto; overflow-y: hidden; padding: .3rem 0; }}
.katex-error {{ color: #d1242f; }}
table {{ border-collapse: collapse; margin: 1rem 0; }}
th, td {{ border: 1px solid #c9ccd1; padding: .35rem .65rem; text-align: left; vertical-align: top; }}
th {{ background: #f1f3f5; }}
tbody tr:nth-child(even) {{ background: #f8f9fa; }}
@media print {{
  body {{ margin: 1.2cm; max-width: none; color: #000; background: #fff; }}
  summary {{ background: none; margin: 0; padding: .2rem 0; }}
  details {{ border-color: #ccc; background: #fff; padding: 0; }}
  a {{ color: #000; }}
  tr, blockquote, .katex-display {{ page-break-inside: avoid; }}
  thead {{ display: table-header-group; }}
  h1, h2, h3 {{ page-break-after: avoid; }}
  th, td {{ border-color: #999; }}
  th {{ background: #ececec; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  tbody tr:nth-child(even) {{ background: #f5f5f5; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
}}
</style>
</head>
<body>
<div id="content">Renderizando…</div>

<script type="text/markdown" id="md-source">
{markdown}
</script>

<script src="https://cdn.jsdelivr.net/npm/katex@{katex}/dist/katex.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it@{mdit}/dist/markdown-it.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/markdown-it-texmath@{texmath}/texmath.js"></script>
<script>
  const source = document.getElementById("md-source").textContent;
  const md = window.markdownit({{ html: true, linkify: true }})
    .use(window.texmath, {{
      engine: window.katex,
      delimiters: "dollars",
      katexOptions: {{ throwOnError: false }},
    }});
  document.getElementById("content").innerHTML = md.render(source);
</script>
</body>
</html>
"""


def extract_title(markdown: str, fallback: str) -> str:
    """Usa el primer encabezado H1 como título; si no hay, el nombre del archivo."""
    match = re.search(r"^#\s+(.+)$", markdown, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback


def build_html(md_path: Path, *, expand_details: bool = False) -> str:
    """Construye el HTML autocontenido de un .md.

    Con ``expand_details`` abre todos los bloques <details> (necesario para el
    PDF, donde no se pueden desplegar a mano).
    """
    markdown = md_path.read_text(encoding="utf-8")
    if expand_details:
        markdown = markdown.replace("<details>", "<details open>")
    # Evita que el contenido cierre el <script> que lo embebe.
    safe_markdown = markdown.replace("</script", "<\\/script")
    return HTML_TEMPLATE.format(
        title=extract_title(markdown, md_path.stem),
        markdown=safe_markdown,
        katex=KATEX_VERSION,
        mdit=MARKDOWN_IT_VERSION,
        texmath=TEXMATH_VERSION,
    )


def convert(md_path: Path, out_path: Path) -> None:
    """Convierte un .md en un .html autocontenido."""
    out_path.write_text(build_html(md_path), encoding="utf-8")


def find_chrome() -> str:
    """Ubica el binario de Chrome/Chromium para imprimir a PDF."""
    env = os.environ.get("CHROME_PATH")
    if env and Path(env).exists():
        return env
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for path in candidates:
        if Path(path).exists():
            return path
    found = shutil.which("google-chrome") or shutil.which("chromium")
    if found:
        return found
    raise RuntimeError(
        "No encontré Chrome/Chromium para generar el PDF. Instalá Chrome o seteá "
        "la variable de entorno CHROME_PATH con la ruta al binario."
    )


def convert_pdf(md_path: Path, out_path: Path) -> None:
    """Renderiza el .md a un PDF estático (math horneada) usando Chrome headless.

    El render ocurre en esta máquina, así que el PDF resultante se abre en
    cualquier lado (iPad, GoodNotes, WhatsApp) sin JS ni internet.
    """
    chrome = find_chrome()
    # HTML temporal con los <details> abiertos para que el PDF muestre todo.
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, encoding="utf-8"
    ) as tmp:
        tmp.write(build_html(md_path, expand_details=True))
        tmp_path = Path(tmp.name)
    try:
        subprocess.run(
            [
                chrome,
                "--headless=new",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--virtual-time-budget=15000",  # espera a que cargue KaTeX del CDN
                "--run-all-compositor-stages-before-draw",
                f"--print-to-pdf={out_path}",
                tmp_path.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
    finally:
        tmp_path.unlink(missing_ok=True)


def collect_md_files(inputs: list[Path]) -> list[Path]:
    """Resuelve archivos y directorios a una lista de .md."""
    files: list[Path] = []
    for item in inputs:
        if item.is_dir():
            files.extend(sorted(item.glob("*.md")))
        elif item.suffix.lower() == ".md":
            files.append(item)
        else:
            print(f"Aviso: ignoro {item} (no es .md)", file=sys.stderr)
    return files


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Convierte apuntes .md a .html con LaTeX renderizado."
    )
    parser.add_argument(
        "inputs",
        nargs="+",
        type=Path,
        help="Archivos .md o carpetas que los contengan.",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Carpeta de salida (por defecto: junto a cada .md).",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="Generar también un PDF estático (se abre en iPad/GoodNotes sin internet).",
    )
    parser.add_argument(
        "--no-html",
        action="store_true",
        help="No escribir el .html (solo tiene sentido con --pdf, p. ej. para volcar el "
        "PDF en su propia carpeta sin dejar un .html al lado).",
    )
    args = parser.parse_args(argv)

    if args.no_html and not args.pdf:
        print("Error: --no-html solo tiene sentido junto con --pdf.", file=sys.stderr)
        return 1

    md_files = collect_md_files(args.inputs)
    if not md_files:
        print("Error: no encontré archivos .md.", file=sys.stderr)
        return 1

    if args.out_dir:
        args.out_dir.mkdir(parents=True, exist_ok=True)

    for md_path in md_files:
        out_dir = args.out_dir or md_path.parent
        if not args.no_html:
            html_path = out_dir / f"{md_path.stem}.html"
            convert(md_path, html_path)
            print(f"✓ {md_path.name} → {html_path}")
        if args.pdf:
            pdf_path = out_dir / f"{md_path.stem}.pdf"
            try:
                convert_pdf(md_path, pdf_path)
            except (RuntimeError, subprocess.CalledProcessError) as exc:
                print(f"  PDF falló: {exc}", file=sys.stderr)
            else:
                print(f"✓ {md_path.name} → {pdf_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
