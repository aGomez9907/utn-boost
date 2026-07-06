"""Vuelca la transcripción lista para procesar, SIN llamar a Gemini.

Reusa la maquinaria de extract_notes.py (descarga de transcripción, timestamps,
plantilla de enlaces) y emite un JSON con todo lo que el modelo necesita para
generar el apunte. La idea es que el procesamiento (el rol de Gemini) lo haga
Claude, leyendo este volcado y escribiendo el .md con el mismo formato.

Uso:
    python dump_transcript.py "https://youtu.be/XXXX"
    python dump_transcript.py "https://youtu.be/XXXX" --lang es en
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from extract_notes import (
    DEFAULT_LANGUAGES,
    _build_contents,
    extract_video_id,
    fetch_transcript,
    fetch_video_title,
    render_transcript,
    slugify,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Vuelca la transcripción (con timestamps) lista para procesar a mano."
    )
    parser.add_argument("url", help="URL (o ID) del video de YouTube.")
    parser.add_argument(
        "--lang",
        nargs="+",
        default=list(DEFAULT_LANGUAGES),
        metavar="CODE",
        help="Idiomas preferidos de la transcripción, en orden (ej: es en).",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("apuntes"),
        help="Directorio sugerido para el .md (solo informativo).",
    )
    args = parser.parse_args(argv)

    video_id = extract_video_id(args.url)
    title = fetch_video_title(video_id)
    segments = fetch_transcript(video_id, tuple(args.lang))
    if not segments:
        print("Error: la transcripción está vacía.", file=sys.stderr)
        return 1

    # Mismo armado que process_video con timestamps + plantilla de enlaces.
    transcript = render_transcript(segments, with_timestamps=True)
    contents = _build_contents(transcript, video_id, with_links=True)

    slug = slugify(title)
    out = {
        "video_id": video_id,
        "title": title,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "suggested_path": str(args.out_dir / f"{slug}.md"),
        "contents": contents,
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
