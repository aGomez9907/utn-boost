# Sistema de estudio universitario

Este repo es el **sistema de estudio multi-materia** de Lucho. Nació para Análisis
Matemático II (AM2) y está generalizado para cualquier materia de la facultad. El
objetivo siempre es el mismo: **preparar y aprobar parciales y finales** con el menor
desperdicio de tiempo posible.

## La metodología (el porqué de todo)

El sistema tiene 3 capas, en este orden:

1. **Ingesta** — convertir el material crudo (videos de YouTube, PDFs de cátedra,
   libros, fotos de apuntes) en **apuntes Markdown normalizados**: teoría visible,
   ejercicios resueltos en bloques `<details>` desplegables, todo en LaTeX, con
   índice navegable (timestamps para videos, páginas para documentos).
2. **Dataset de exámenes** — los exámenes reales (PDFs/fotos, muchas veces sin capa
   de texto) se transcriben UNA vez a un `INDICE.md` curado con tags por tema.
   Después todo análisis se hace grepeando el índice, **nunca re-leyendo las
   imágenes**.
3. **Estrategia** — cruzar la frecuencia histórica de temas (capa 2) contra la
   cobertura de los apuntes (capa 1) para decidir **qué dominar, qué leer por
   arriba y qué saltear**, armar el plan de días, el banco de problemas tipo y el
   checklist teórico. De acá salen también los simulacros, las flashcards y el plan
   recalculable.

**Regla de oro:** la estrategia se construye con evidencia (frecuencias reales de
los exámenes), no con intuición. Y los apuntes se construyen SOLO con lo que dice la
fuente (transcripción/PDF), sin inventar contenido.

## Estructura de directorios

```
CLAUDE.md                  ← este archivo
README.md                  ← walkthrough para el usuario (humanos)
tools/                     ← scripts Python compartidos (ver "Herramientas")
plantillas/                ← plantillas para materias/evaluaciones nuevas
venv/                      ← entorno Python (usar venv/bin/python)
materias/
  <slug-materia>/          ← p. ej. analisis-matematico-2/
    MATERIA.md             ← config de la materia: evaluaciones, fechas, estructura
    │                        del examen, fuentes, leyenda de tags. LEERLO PRIMERO.
    fuentes/               ← material crudo: PDFs de cátedra, libros, fotos
    <slug-evaluacion>/     ← p. ej. segundo-parcial/, final/
      apuntes/
        md/                ← apuntes fuente (NN-slug.md) — la verdad canónica
        html/              ← export con KaTeX (regenerable)
        pdf/               ← export para iPad/compartir (regenerable)
        transcripts/       ← JSON de transcripciones cacheadas
      examenes/            ← exámenes reales (AAAA-MM-DD_Parcial.pdf|png|jpg)
        INDICE.md          ← transcripción curada + tags (capa 2)
      simulacros/          ← exámenes simulados generados
      estrategia.md        ← análisis frecuencias + brechas + banco + checklist
      que-saltear.md       ← poda sección por sección de cada apunte
      plan.md              ← plan de días recalculable
      registro.md          ← registro de práctica y errores
      flashcards.md        ← mazo de repaso teórico (+ flashcards-anki.tsv)
```

## Skills disponibles

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

## Resolución de contexto (materia/evaluación)

Todas las skills aceptan la ruta `materias/<materia>/<evaluacion>` explícita, pero si
el usuario no la da:

1. Materia: la única con `estado: cursando` en su `MATERIA.md`. Si hay varias, preguntar.
2. Evaluación: la próxima por fecha (según la tabla de evaluaciones de `MATERIA.md`).
3. Ante ambigüedad real, preguntar. Nunca adivinar en silencio.

## Convenciones (obligatorias)

- **Idioma:** todo en español rioplatense (voseo), igual que el material existente.
- **Apuntes:** archivo `NN-slug.md` (NN = orden cronológico de la clase). Encabezado
  exacto: `# {título}` + `> Fuente: {url|archivo}` + `---`. Teoría en secciones `##`
  visibles; CADA ejercicio en `<details>` con su resolución en otro `<details>`
  anidado; pasos como `**Paso N:**`; fórmulas en bloque `$$…$$` en líneas propias,
  SIN sangría, con línea en blanco antes y después (si se indentan no renderizan);
  dentro de `<summary>` los enlaces van en HTML (`<a href>`), nunca Markdown.
- **No inventar:** los apuntes salen ÚNICAMENTE de la fuente. Timestamps solo de los
  marcadores reales `[mm:ss|Ns]`. Lo confuso se marca `[poco claro en la
  transcripción]`; lo que quedó en el pizarrón, `[paso en el pizarrón, ver video]`.
- **Exámenes:** archivos `AAAA-MM-DD_Parcial.<ext>` (o `sin-fecha_...` si no se sabe).
  El `INDICE.md` es la única representación textual: cada problema es una línea
  `- **Pn)** enunciado → #Tag #Tag`, teóricos `**T1)/T2)**`, tags en `#CamelCase`
  según la leyenda de `MATERIA.md`. Mantiene índice inverso tema→fechas, problemas
  reciclados y equivalencias entre exámenes (mismo examen ≠ practicar dos veces).
- **No re-leer exámenes:** para análisis usar SIEMPRE `INDICE.md` (grep). Las
  imágenes/PDFs de `examenes/` solo se leen con visión al indexarlos por primera vez.
- **Fechas:** siempre absolutas (AAAA-MM-DD). Los documentos generados llevan al pie
  la fecha de generación y sus fuentes.
- **Prioridades:** la escala compartida es 🔴 dominar / 🟠 alta / 🟡 media / ⚪ baja-
  descartable (estrategia) y 🗑️ saltear / 📖 por arriba / ✅ núcleo (poda).

## Herramientas técnicas (`tools/`)

- `dump_transcript.py <url>` — baja la transcripción de YouTube con marcadores
  `[mm:ss|Ns]` y devuelve JSON (`video_id`, `title`, `url`, `suggested_path`,
  `contents`). Correr con `venv/bin/python`.
- `md_to_html.py <ruta.md>` — export a HTML con KaTeX; `--pdf` genera PDF con Chrome
  headless (para iPad los `<details>` salen expandidos). `--out-dir` para elegir carpeta.
- `fetch_transcripts.py` — descarga masiva de transcripciones desde IP residencial
  cuando YouTube bloquea (editar su lista `REMAINING`).
- `extract_notes.py` — LEGACY: el pipeline original con Gemini. Ya no se usa (Claude
  genera los apuntes), pero conserva los prompts originales de referencia.
- **Rate-limit de YouTube:** bajar transcripciones de a una, con pausa. Si aparece
  `IpBlocked`/`RequestBlocked` en IP de nube, usar `fetch_transcripts.py` en la Mac.

## Reglas para Claude en este repo

1. Antes de trabajar sobre una materia, leer su `MATERIA.md` y, si existe, la
   `estrategia.md` de la evaluación activa.
2. No gastar contexto leyendo PDFs/JPGs de `examenes/` salvo indexación explícita.
3. Los archivos generados (estrategia, plan, simulacros…) se REGENERAN: no editar a
   mano salvo pedido puntual; regenerar con la skill correspondiente.
4. Ante un examen nuevo que el usuario traiga: primero `/indexar-examenes`, después
   regenerar estrategia/plan si cambia el patrón.
5. Commitear con mensajes en español describiendo el material agregado.
