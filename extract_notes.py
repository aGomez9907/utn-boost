"""Extrae apuntes universitarios de un video de YouTube usando Gemini.

Descarga la transcripción (incluso autogenerada), la procesa con Gemini y
guarda un apunte en Markdown listo para estudiar.

Uso:
    python extract_notes.py "https://www.youtube.com/watch?v=XXXX"
    python extract_notes.py "https://youtu.be/XXXX" --out-dir apuntes --lang es en
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import urllib.parse
import urllib.request
from dataclasses import dataclass
from json import loads as json_loads
from pathlib import Path

from google import genai
from google.genai import types
from youtube_transcript_api import (
    NoTranscriptFound,
    TranscriptsDisabled,
    YouTubeTranscriptApi,
)

try:
    from dotenv import load_dotenv
except ImportError:  # python-dotenv es opcional; sin él se usan env vars normales.

    def load_dotenv(*_args: object, **_kwargs: object) -> bool:
        return False

# --- Configuración -----------------------------------------------------------

MODEL: str = "gemini-2.5-pro"  # El modelo más capaz de Gemini para razonamiento.
# MODEL: str = "gemini-2.5-flash"

DEFAULT_LANGUAGES: tuple[str, ...] = ("es", "es-419", "en")

SYSTEM_INSTRUCTION: str = (
    "Sos un profesor experto en Análisis Matemático II. Analizá la siguiente "
    "transcripción cruda de una clase universitaria y extraé únicamente:\n\n"
    "- Definiciones teóricas clave (ej: campo conservativo, función potencial).\n"
    "- Teoremas principales, sus hipótesis y tesis (ej: Teorema de Green, "
    "Divergencia).\n"
    "- Fórmulas cerradas importantes.\n\n"
    "Reglas estrictas:\n"
    "- Ignorá por completo saludos, interrupciones, comentarios irrelevantes del "
    "profesor y el paso a paso algebraico o resoluciones numéricas de los "
    "ejercicios prácticos.\n"
    "- Basate únicamente en la transcripción. Si el audio está confuso o algo no se "
    "entiende, marcalo como `[poco claro en la transcripción]` en lugar de "
    "completarlo con tu propio conocimiento.\n"
    "- Estructurá la salida en Markdown utilizando títulos (H2, H3), viñetas y "
    "bloques de código LaTeX (encerrados entre $ o $$) para las fórmulas "
    "matemáticas, asegurando que sea un apunte directo y listo para estudiar."
)

# Addendum opcional: pide un índice navegable con enlaces al minuto del video.
INDEX_INSTRUCTION: str = (
    "\n\nLa transcripción incluye marcadores de tiempo con el formato "
    "[mm:ss|SEGUNDOSs]. Comenzá la salida con una sección \"## Índice\" que liste, "
    "en orden cronológico, los temas principales del apunte. Cada ítem debe ser un "
    "enlace de Markdown al momento del video donde empieza ese tema, con el formato "
    "\"- [mm:ss](ENLACE) — Tema\", usando la plantilla de enlace provista al inicio "
    "del contenido y reemplazando {SEGUNDOS} por el valor en segundos del marcador "
    "más cercano al inicio de ese tema. Después del índice, escribí el apunte "
    "completo y, en cada título de sección (H2/H3), agregá también su enlace al "
    "timestamp correspondiente. Regla estricta: NO inventes timestamps; usá "
    "únicamente los valores que aparecen en los marcadores de la transcripción."
)

# Prompt de la Pasada 2: extrae (no inventa) los ejercicios que resuelve el profe.
EXERCISES_INSTRUCTION: str = (
    "Sos un profesor experto en Análisis Matemático II. A partir de la siguiente "
    "transcripción cruda de una clase, identificá y extraé ÚNICAMENTE los ejercicios "
    "prácticos que el profesor resuelve durante la clase. Ignorá la teoría y los "
    "comentarios irrelevantes.\n\n"
    "Para cada ejercicio generá:\n"
    "- Un título de la forma \"## [mm:ss](ENLACE) — Ejercicio N: <tema>\", usando el "
    "marcador [mm:ss|SEGUNDOSs] más cercano al inicio del ejercicio y la plantilla de "
    "enlace provista al inicio del contenido (reemplazando {SEGUNDOS}).\n"
    "- El enunciado lo más completo posible, con LaTeX (entre $ o $$) para las "
    "fórmulas.\n"
    "- La resolución resumida en sus pasos clave (el método y las fórmulas, no cada "
    "cuenta numérica), dentro de un bloque colapsable para poder practicar antes de "
    "mirarla. Identificá cada paso con una etiqueta en negrita (\"**Paso 1:** ...\"), "
    "NO con listas numeradas de Markdown. Estructura exacta:\n"
    "<details><summary>Ver resolución</summary>\n\n"
    "**Paso 1:** explicación del paso.\n\n"
    "$$\nfórmula del paso\n$$\n\n"
    "**Paso 2:** ...\n\n"
    "</details>\n\n"
    "Reglas estrictas:\n"
    "- Formato de fórmulas (CRÍTICO para que rendericen): cada fórmula en bloque "
    "($$...$$) va en líneas propias, SIN ninguna sangría (pegada al margen "
    "izquierdo) y con una línea en blanco antes y después. NUNCA indentes una "
    "fórmula ni la metas dentro de una lista numerada o con viñetas, porque el visor "
    "la interpreta como bloque de código y no la renderiza.\n"
    "- Basate ÚNICAMENTE en la transcripción. NO inventes ejercicios, datos ni "
    "resultados, ni completes con tu propio conocimiento.\n"
    "- La transcripción viene del audio: cuando un paso clave estaba en el pizarrón y "
    "no se verbaliza (queda ambiguo, p. ej. \"y acá queda esto\"), marcalo como "
    "`[paso en el pizarrón, ver video]` en lugar de adivinarlo.\n"
    "- Si en la clase no se resuelve ningún ejercicio, respondé exactamente: "
    "\"No se identificaron ejercicios resueltos en esta clase.\""
)

# Prompt consolidado: teoría + ejercicios desplegables en una sola pasada/archivo.
CONSOLIDATED_INSTRUCTION: str = (
    "Sos un profesor experto en Análisis Matemático II. Analizá la siguiente "
    "transcripción cruda de una clase y generá un ÚNICO apunte de estudio en "
    "Markdown, con dos partes:\n\n"
    "PARTE 1 — TEORÍA (visible, sin colapsar). Extraé y desarrollá en el cuerpo del "
    "documento:\n"
    "- Definiciones teóricas clave (ej: campo conservativo, función potencial).\n"
    "- Teoremas principales, con sus hipótesis y tesis (ej: Teorema de Green, "
    "Divergencia).\n"
    "- Fórmulas cerradas importantes.\n"
    "Ignorá saludos, interrupciones, comentarios irrelevantes y el paso a paso "
    "numérico de los ejercicios dentro de esta parte teórica.\n\n"
    "PARTE 2 — EJERCICIOS. Bajo el título \"## Ejercicios\", extraé ÚNICAMENTE los "
    "ejercicios que el profesor resuelve en la clase. Cada ejercicio va dentro de un "
    "bloque colapsable, y su resolución dentro de OTRO bloque colapsable anidado. "
    "Usá esta estructura EXACTA, respetando las líneas en blanco:\n\n"
    "<details>\n"
    "<summary>📝 Ejercicio N — <a href=\"ENLACE\">mm:ss</a>: tema</summary>\n\n"
    "Enunciado del ejercicio, con sus fórmulas.\n\n"
    "<details>\n"
    "<summary>Ver resolución</summary>\n\n"
    "**Paso 1:** explicación del paso.\n\n"
    "$$\nfórmula del paso\n$$\n\n"
    "**Paso 2:** ...\n\n"
    "</details>\n\n"
    "</details>\n\n"
    "Reglas estrictas:\n"
    "- Basate ÚNICAMENTE en la transcripción. NO inventes teoría ni ejercicios. Si "
    "el audio está confuso, marcá `[poco claro en la transcripción]` en lugar de "
    "completarlo con tu propio conocimiento.\n"
    "- En los ejercicios, los pasos que quedaron escritos en el pizarrón y no se "
    "verbalizan (quedan ambiguos) marcalos `[paso en el pizarrón, ver video]`.\n"
    "- Formato de fórmulas (CRÍTICO para que rendericen): cada fórmula en bloque "
    "($$...$$) va en líneas propias, SIN ninguna sangría (pegada al margen "
    "izquierdo) y con una línea en blanco antes y después. NUNCA indentes una "
    "fórmula ni la metas dentro de una lista numerada o con viñetas.\n"
    "- Dentro de la línea <summary> el contenido es HTML: el enlace al timestamp DEBE "
    "ser una etiqueta HTML <a href=\"ENLACE\">mm:ss</a>, NUNCA un enlace Markdown "
    "[mm:ss](ENLACE) (en HTML no se renderiza y se ve el texto crudo).\n"
    "- Usá LaTeX (entre $ o $$) para toda la matemática y estructurá con títulos "
    "(H2, H3) y viñetas, para que sea un apunte directo y listo para estudiar."
)

# Cada cuántos segundos insertar un marcador de tiempo en la transcripción.
TIMESTAMP_INTERVAL_SECONDS: float = 30.0


@dataclass(frozen=True)
class Segment:
    """Un fragmento de transcripción con su marca de tiempo de inicio."""

    text: str
    start: float  # Segundos desde el comienzo del video.


@dataclass(frozen=True)
class VideoNotes:
    """Resultado del procesamiento de un video."""

    video_id: str
    title: str
    markdown: str  # Apunte de teoría.
    practice: str | None = None  # Ejercicios extraídos (opcional).


# --- Transcripción y metadatos ----------------------------------------------


def extract_video_id(url: str) -> str:
    """Obtiene el ID de 11 caracteres a partir de una URL de YouTube."""
    # Sin esquema (ej: "youtube.com/watch?v=..."), urlparse mete el host en el
    # path; anteponemos "https://" para que hostname/path queden bien.
    if "://" not in url and re.match(r"^(?:www\.)?(?:youtube\.com|youtu\.be)/", url):
        url = "https://" + url

    parsed = urllib.parse.urlparse(url)

    if parsed.hostname in {"youtu.be"}:
        candidate = parsed.path.lstrip("/")
    elif parsed.path == "/watch":
        candidate = urllib.parse.parse_qs(parsed.query).get("v", [""])[0]
    elif parsed.path.startswith(("/embed/", "/shorts/", "/live/")):
        candidate = parsed.path.split("/")[2]
    else:
        candidate = url  # Quizás ya nos pasaron el ID pelado.

    if re.fullmatch(r"[\w-]{11}", candidate):
        return candidate
    raise ValueError(f"No pude extraer un ID de video válido de: {url!r}")


def fetch_transcript(video_id: str, languages: tuple[str, ...]) -> list[Segment]:
    """Descarga la transcripción como una lista de segmentos con timestamps.

    Prioriza los idiomas indicados; si no encuentra ninguno, cae a la primera
    transcripción disponible (manual o autogenerada).
    """
    api = YouTubeTranscriptApi()

    try:
        fetched = api.fetch(video_id, languages=list(languages))
    except NoTranscriptFound:
        # Fallback: tomar cualquier transcripción listada (incl. autogenerada).
        transcript_list = api.list(video_id)
        transcript = next(iter(transcript_list))
        fetched = transcript.fetch()

    return [
        Segment(text=snippet.text.strip(), start=float(snippet.start))
        for snippet in fetched
        if snippet.text and snippet.text.strip()
    ]


def _format_hms(seconds: float) -> str:
    """Formatea segundos como mm:ss (o h:mm:ss para videos de más de una hora)."""
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def render_transcript(
    segments: list[Segment],
    *,
    with_timestamps: bool,
    interval: float = TIMESTAMP_INTERVAL_SECONDS,
) -> str:
    """Concatena los segmentos en un bloque de texto.

    Si ``with_timestamps`` es True, intercala marcadores ``[mm:ss|Ns]`` cada
    ``interval`` segundos para que el modelo pueda anclar el índice al video.
    """
    parts: list[str] = []
    next_marker = 0.0
    for segment in segments:
        if with_timestamps and segment.start >= next_marker:
            secs = int(segment.start)
            parts.append(f"[{_format_hms(segment.start)}|{secs}s]")
            next_marker = segment.start + interval
        parts.append(segment.text)

    return re.sub(r"[ \t]+", " ", " ".join(parts)).strip()


def fetch_video_title(video_id: str) -> str:
    """Obtiene el título del video vía el endpoint oembed de YouTube."""
    oembed = (
        "https://www.youtube.com/oembed?url="
        + urllib.parse.quote(f"https://www.youtube.com/watch?v={video_id}", safe="")
        + "&format=json"
    )
    try:
        with urllib.request.urlopen(oembed, timeout=15) as response:
            data = json_loads(response.read().decode("utf-8"))
        return str(data.get("title") or video_id)
    except Exception:  # noqa: BLE001 - el título es best-effort.
        return video_id


# --- Procesamiento con Gemini ------------------------------------------------


def generate_notes(
    contents: str, *, system_instruction: str, client: genai.Client
) -> str:
    """Envía la transcripción a Gemini y devuelve el apunte en Markdown."""
    response = client.models.generate_content(
        model=MODEL,
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.2,  # Bajo: queremos fidelidad, no creatividad.
        ),
    )
    if not response.text:
        raise RuntimeError("Gemini devolvió una respuesta vacía.")
    return response.text.strip()


def _build_contents(transcript: str, video_id: str, *, with_links: bool) -> str:
    """Antepone la plantilla de enlace a la transcripción si se usan timestamps."""
    if not with_links:
        return transcript
    link_template = f"https://www.youtube.com/watch?v={video_id}&t={{SEGUNDOS}}s"
    return (
        f"Plantilla de enlace para los timestamps: {link_template}\n\n"
        f"Transcripción:\n{transcript}"
    )


def process_video(
    url: str,
    languages: tuple[str, ...],
    *,
    with_index: bool = True,
    with_practice: bool = False,
    consolidated: bool = False,
) -> VideoNotes:
    """Orquesta la extracción completa para una URL.

    - ``consolidated``: una sola pasada que produce un único apunte con la teoría
      visible y los ejercicios (y sus resoluciones) en bloques desplegables.
    - Si no, hace una pasada de teoría y, con ``with_practice``, una segunda pasada
      que extrae los ejercicios en un archivo aparte.
    """
    video_id = extract_video_id(url)
    title = fetch_video_title(video_id)
    segments = fetch_transcript(video_id, languages)
    if not segments:
        raise RuntimeError("La transcripción está vacía.")

    # Los timestamps hacen falta para enlazar índice y ejercicios al video.
    need_timestamps = with_index or with_practice or consolidated
    transcript = render_transcript(segments, with_timestamps=need_timestamps)
    contents = _build_contents(transcript, video_id, with_links=need_timestamps)

    client = genai.Client(api_key=_require_api_key())
    index_addendum = INDEX_INSTRUCTION if with_index else ""

    if consolidated:
        markdown = generate_notes(
            contents,
            system_instruction=CONSOLIDATED_INSTRUCTION + index_addendum,
            client=client,
        )
        return VideoNotes(video_id=video_id, title=title, markdown=markdown)

    markdown = generate_notes(
        contents, system_instruction=SYSTEM_INSTRUCTION + index_addendum, client=client
    )

    practice: str | None = None
    if with_practice:
        print("→ Extrayendo ejercicios...", file=sys.stderr)
        practice = generate_notes(
            contents, system_instruction=EXERCISES_INSTRUCTION, client=client
        )

    return VideoNotes(
        video_id=video_id, title=title, markdown=markdown, practice=practice
    )


# --- Utilidades de salida ----------------------------------------------------


def _require_api_key() -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "Falta GEMINI_API_KEY. Pegá tu clave en el archivo .env "
            "(copiá .env.example a .env) o exportala como variable de entorno."
        )
    return api_key


def slugify(value: str, *, max_length: int = 80) -> str:
    """Convierte un título en un nombre de archivo seguro."""
    value = value.strip()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return (value[:max_length].rstrip("-") or "apunte").lower()


def _write_doc(
    *, title: str, video_id: str, body: str, path: Path
) -> Path:
    """Escribe un documento Markdown con encabezado de título y fuente."""
    header = (
        f"# {title}\n\n"
        f"> Fuente: https://www.youtube.com/watch?v={video_id}\n\n"
        "---\n\n"
    )
    path.write_text(header + body + "\n", encoding="utf-8")
    return path


def save_markdown(notes: VideoNotes, out_dir: Path) -> list[Path]:
    """Guarda el apunte (y la práctica si existe) y devuelve las rutas escritas."""
    out_dir.mkdir(parents=True, exist_ok=True)
    slug = slugify(notes.title)

    paths = [
        _write_doc(
            title=notes.title,
            video_id=notes.video_id,
            body=notes.markdown,
            path=out_dir / f"{slug}.md",
        )
    ]
    if notes.practice:
        paths.append(
            _write_doc(
                title=f"{notes.title} — Práctica",
                video_id=notes.video_id,
                body=notes.practice,
                path=out_dir / f"{slug}-practica.md",
            )
        )
    return paths


# --- CLI ---------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    load_dotenv()  # Lee GEMINI_API_KEY desde el archivo .env del proyecto.

    parser = argparse.ArgumentParser(
        description="Extrae apuntes de Análisis Matemático II desde un video de YouTube."
    )
    parser.add_argument("url", help="URL (o ID) del video de YouTube.")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("apuntes"),
        help="Directorio donde guardar el .md (por defecto: ./apuntes).",
    )
    parser.add_argument(
        "--lang",
        nargs="+",
        default=list(DEFAULT_LANGUAGES),
        metavar="CODE",
        help="Idiomas preferidos de la transcripción, en orden (ej: es en).",
    )
    parser.add_argument(
        "--no-index",
        action="store_true",
        help="No generar el índice con enlaces a los timestamps del video.",
    )
    parser.add_argument(
        "--practice",
        action="store_true",
        help="Generar además un .md aparte con los ejercicios que resuelve el profesor.",
    )
    parser.add_argument(
        "--consolidated",
        action="store_true",
        help="Un único .md (una sola pasada): teoría visible + ejercicios y "
        "resoluciones en bloques desplegables.",
    )
    args = parser.parse_args(argv)

    try:
        print("→ Descargando transcripción...", file=sys.stderr)
        print("→ Procesando con Gemini...", file=sys.stderr)
        notes = process_video(
            args.url,
            tuple(args.lang),
            with_index=not args.no_index,
            with_practice=args.practice and not args.consolidated,
            consolidated=args.consolidated,
        )
        paths = save_markdown(notes, args.out_dir)
    except (ValueError, RuntimeError, TranscriptsDisabled, NoTranscriptFound) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    for path in paths:
        print(f"✓ Guardado: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
