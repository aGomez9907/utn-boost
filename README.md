# Sistema de estudio universitario

Sistema **multi-materia** para preparar y aprobar **parciales y finales** con el menor
desperdicio de tiempo posible. Nació como un pipeline de apuntes para Análisis
Matemático II (AM2) y hoy está generalizado: cada materia vive en su carpeta, con sus
apuntes, sus exámenes reales indexados y su estrategia de estudio. Claude Code es el
motor: casi todo se opera con skills (`/apunte`, `/estrategia`, `/plan`, etc.).

## La metodología en 3 capas

**1. Ingesta.** Todo el material crudo (videos de YouTube, PDFs de cátedra, libros,
fotos de apuntes o del pizarrón) se convierte en **apuntes Markdown normalizados**:
teoría visible, ejercicios resueltos en bloques `<details>` desplegables, fórmulas en
LaTeX e índice navegable (timestamps para videos, páginas para documentos). ¿Por qué?
Porque estudiar de un formato único y grepeable es mucho más rápido que saltar entre
videos de 2 horas, diapositivas y fotos sueltas — y los apuntes salen SOLO de la
fuente, sin contenido inventado.

**2. Dataset de exámenes.** Los exámenes reales (PDFs y fotos, muchas veces sin capa
de texto) se transcriben **una sola vez** a un `INDICE.md` curado, con cada problema
taggeado por tema. Después, todo análisis se hace grepeando ese índice, nunca
re-leyendo las imágenes. ¿Por qué? Porque leer imágenes con visión es caro y lento;
transcribir una vez y consultar texto plano infinitas veces convierte los exámenes en
un dataset consultable.

**3. Estrategia.** Se cruza la frecuencia histórica de temas (capa 2) contra la
cobertura de los apuntes (capa 1) para decidir **qué dominar, qué leer por arriba y
qué saltear**, armar el plan de días, el banco de problemas tipo y el checklist
teórico. De acá salen también los simulacros, las flashcards y el plan recalculable.
¿Por qué? Porque la regla de oro del sistema es que la estrategia se construye con
**evidencia** (frecuencias reales de los exámenes), no con intuición.

## Estructura de carpetas

```
CLAUDE.md                  ← instrucciones para Claude (metodología + convenciones)
README.md                  ← este archivo
tools/                     ← scripts Python compartidos
plantillas/                ← plantillas para materias/evaluaciones nuevas
venv/                      ← entorno Python (usar venv/bin/python)
materias/
  <slug-materia>/          ← p. ej. analisis-matematico-2/
    MATERIA.md             ← config: evaluaciones, fechas, estructura del examen, tags
    fuentes/               ← material crudo: PDFs de cátedra, libros, fotos
    <slug-evaluacion>/     ← p. ej. segundo-parcial/, final/
      apuntes/md|html|pdf/ ← apuntes fuente (.md canónico) + exports regenerables
      apuntes/transcripts/ ← JSON de transcripciones cacheadas
      examenes/            ← exámenes reales + INDICE.md (transcripción curada + tags)
      simulacros/          ← exámenes simulados generados
      estrategia.md        ← frecuencias + brechas + banco + checklist
      que-saltear.md       ← poda sección por sección de cada apunte
      plan.md              ← plan de días recalculable
      registro.md          ← registro de práctica y errores
      flashcards.md        ← mazo de repaso teórico (+ flashcards-anki.tsv)
```

El detalle fino (convenciones de nombres, formato de apuntes e índice) está en
`CLAUDE.md`.

## Skills

| Skill | Qué hace |
|---|---|
| `/nueva-materia` | Scaffolding de una materia nueva (carpetas + MATERIA.md desde plantilla). |
| `/apunte` | Video de YouTube → apunte md (+html/pdf). |
| `/apuntes-batch` | Muchos videos → un apunte por video, un subagente por video. |
| `/apunte-doc` | PDF / diapositivas / capítulo de libro / fotos → apunte md. |
| `/indexar-examenes` | Exámenes nuevos (PDF/foto) → entradas en `examenes/INDICE.md` con tags. |
| `/estrategia` | Genera/actualiza `estrategia.md` (frecuencias, brechas, banco, checklist). |
| `/que-saltear` | Genera/actualiza `que-saltear.md` (poda 🗑️/📖/✅ por apunte). |
| `/plan` | Recalcula `plan.md` según días restantes, avance y registro de errores. |
| `/simulacro` | Genera un examen simulado nuevo respetando estructura y frecuencias. |
| `/flashcards` | Genera `flashcards.md` + `flashcards-anki.tsv` desde el checklist teórico. |
| `/registrar` | Anota una sesión de práctica/errores en `registro.md` y actualiza su tablero. |

**Flujo típico de una evaluación nueva:** `/apuntes-batch` (o `/apunte-doc`) →
`/indexar-examenes` → `/estrategia` → `/que-saltear` → `/plan` → estudiar +
`/registrar` → `/flashcards` para la teoría → `/simulacro` en los últimos días →
`/plan` de nuevo cuando cambia el panorama.

## Quickstart

Abrí Claude Code en la raíz del repo y:

1. **Materia nueva:** `/nueva-materia` — crea las carpetas y el `MATERIA.md` desde la
   plantilla. Completá fechas de evaluaciones y fuentes.
2. **Generar apuntes:** `/apunte <url-de-youtube>` para un video, `/apuntes-batch`
   para una lista, `/apunte-doc` para PDFs, diapositivas o fotos (dejalos antes en
   `materias/<materia>/fuentes/`).
3. **Indexar exámenes:** tirá los parciales/finales reales en la carpeta `examenes/`
   de la evaluación y corré `/indexar-examenes`.
4. **Estrategia y estudio:** `/estrategia` → `/que-saltear` → `/plan`. Cuando quieras
   repasar teoría, `/flashcards`; en los últimos días, `/simulacro`.
5. **Registrar práctica:** después de cada sesión de ejercicios, `/registrar` con lo
   que hiciste y en qué te equivocaste — el `/plan` siguiente lo tiene en cuenta.

Si no aclarás materia/evaluación, las skills resuelven solas: la materia con estado
`cursando` y la evaluación más próxima por fecha (y preguntan si hay ambigüedad).

## Instalación técnica

El venv solo hace falta para los scripts de `tools/` (transcripciones y exports):

```bash
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Export a HTML/PDF (`tools/md_to_html.py`)

Convierte los apuntes `.md` a `.html` con las fórmulas LaTeX renderizadas
(markdown-it + KaTeX desde CDN; hace falta internet la primera vez que abrís el
`.html`). Renderiza bien los `<details>` anidados.

```bash
venv/bin/python tools/md_to_html.py materias/<materia>/<evaluacion>/apuntes/md/01-clase.md
```

**PDF para iPad / GoodNotes / compartir (`--pdf`):** el `.html` no sirve en el iPad
(WhatsApp/Files lo previsualizan sin ejecutar JS y se queda en "Renderizando…"). El
flag `--pdf` renderiza con Chrome headless local y deja la math horneada, así el PDF
se abre en cualquier lado sin JS ni internet. Caveats: necesita Chrome instalado (o
la variable `CHROME_PATH`), y los `<details>` salen **expandidos** (en un PDF no se
pueden desplegar) — para el modo "tapá la respuesta", usá el `.html` en la compu.

```bash
venv/bin/python tools/md_to_html.py materias/.../apuntes/md/01-clase.md --pdf
```

### Rate-limit de YouTube

Bajar transcripciones **de a una, con pausa**. Si aparece `IpBlocked` /
`RequestBlocked` (típico en IPs de nube), usar `tools/fetch_transcripts.py` desde una
IP residencial (editar su lista `REMAINING`).

### API key de Gemini (LEGACY)

El `.env` con `GEMINI_API_KEY` solo hace falta para `tools/extract_notes.py`, el
pipeline original que procesaba las transcripciones con Gemini. **Ya no se usa**:
Claude genera los apuntes directamente vía las skills. El script queda como
referencia de los prompts originales; no configures la key salvo que quieras
revivirlo.

## Versionado

El repo está bajo git y **todo el material se versiona**: apuntes, índices de
exámenes, estrategias, planes y registros. Los archivos generados (estrategia, plan,
simulacros…) se regeneran con su skill, no se editan a mano; el historial de git es
el respaldo si algo se pisa.
