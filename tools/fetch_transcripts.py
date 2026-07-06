"""Baja las transcripciones que faltan del lote, para correr en una red NO bloqueada
por YouTube (IP residencial, p. ej. tu Mac).

IMPORTANTE: este script NO genera apuntes ni llama a ningún modelo. Solo descarga cada
transcripción y la guarda como JSON en <eval>/apuntes/transcripts/NN-<slug>.json. La generación
de los apuntes la sigue haciendo Claude a partir de esos JSON, así la calidad del
resultado es idéntica a la de los apuntes que ya salieron (01-08, 15).

Uso:
    python tools/fetch_transcripts.py     # baja los que faltan (saltea los ya bajados)
    python tools/fetch_transcripts.py --force   # rebaja aunque el JSON ya exista

Si tu 'python' no tiene las dependencias, usá el venv del repo:
    venv/bin/python tools/fetch_transcripts.py
"""

from __future__ import annotations

import argparse
import json
import sys
import time
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

# (NN, URL) de los videos del lote que quedaron pendientes por el bloqueo de IP.
REMAINING: list[tuple[str, str]] = [
    ("09", "https://youtu.be/tCim6SO5R3Q"),
    ("10", "https://youtu.be/Z7MavOmpW8s"),
    ("11", "https://youtu.be/A20l3JCSSAU"),
    ("12", "https://youtu.be/NL0A1Tyn2Nk"),
    ("13", "https://youtu.be/MswDmKXZpBc"),
    ("14", "https://youtu.be/djt3sX5V2lk"),
    ("15", "https://youtu.be/LLxa2v7Pjoo"),
    ("16", "https://youtu.be/EPpyWckw-uE"),
]

OUT_DIR = Path("materias/analisis-matematico-2/segundo-parcial/apuntes/transcripts")
PAUSE_SECONDS = 6.0  # pausa entre pedidos, para no gatillar el bloqueo de YouTube.
RETRIES = 3


def fetch_one(nn: str, url: str) -> tuple[Path, str]:
    """Descarga una transcripción y la guarda como JSON. Devuelve (ruta, título)."""
    video_id = extract_video_id(url)
    title = fetch_video_title(video_id)
    segments = fetch_transcript(video_id, tuple(DEFAULT_LANGUAGES))
    if not segments:
        raise RuntimeError("la transcripción vino vacía")

    # Mismo armado que dump_transcript.py: timestamps + plantilla de enlaces.
    transcript = render_transcript(segments, with_timestamps=True)
    contents = _build_contents(transcript, video_id, with_links=True)
    slug = slugify(title)

    data = {
        "nn": nn,
        "video_id": video_id,
        "title": title,
        "url": f"https://www.youtube.com/watch?v={video_id}",
        "slug": slug,
        "contents": contents,
    }
    path = OUT_DIR / f"{nn}-{slug}.json"
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return path, title


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Baja las transcripciones faltantes del lote (no genera apuntes)."
    )
    parser.add_argument(
        "--force", action="store_true", help="Rebajar aunque el JSON ya exista."
    )
    args = parser.parse_args(argv)

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    ok: list[str] = []
    failed: list[str] = []
    skipped: list[str] = []

    for i, (nn, url) in enumerate(REMAINING):
        existing = list(OUT_DIR.glob(f"{nn}-*.json"))
        if existing and not args.force:
            print(f"↷ {nn}: ya existe {existing[0].name}, salteo")
            skipped.append(nn)
            continue

        for attempt in range(1, RETRIES + 1):
            try:
                path, title = fetch_one(nn, url)
                print(f"✓ {nn}: {title} → {path}")
                ok.append(nn)
                break
            except Exception as exc:  # noqa: BLE001 - queremos reportar cualquier fallo.
                print(
                    f"  {nn} intento {attempt}/{RETRIES} falló: {exc}", file=sys.stderr
                )
                if attempt < RETRIES:
                    time.sleep(PAUSE_SECONDS * attempt)  # backoff creciente.
        else:
            failed.append(nn)

        # Pausa entre videos distintos (no después del último).
        if i < len(REMAINING) - 1:
            time.sleep(PAUSE_SECONDS)

    print(
        f"\nResumen: {len(ok)} ok, {len(skipped)} salteados, {len(failed)} fallidos."
    )
    if failed:
        print("Fallidos:", ", ".join(failed))
        print(
            "Si siguen fallando, probá desde otra red (datos del celular, etc.) o "
            "reintentá más tarde."
        )
        return 1

    print(
        f"\nListo: transcripciones en {OUT_DIR}/. "
        "Avisale a Claude para que genere los apuntes desde ahí."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
