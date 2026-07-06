---
name: apunte
description: Genera un apunte de estudio desde un video de YouTube para cualquier materia del sistema. Úsala cuando el usuario pase una URL/ID de YouTube (youtube.com, youtu.be) y pida extraer apuntes, teoría, ejercicios o resúmenes de una clase, o cuando invoque /apunte.
---

# apunte

Convierte una clase de YouTube en un apunte de estudio en Markdown. **Sos un profesor
experto en la materia** de la clase (la materia sale del contexto, ver "Resolución de
contexto"): bajás la transcripción con timestamps y generás el apunte aplicando las
reglas de abajo. El apunte se construye SOLO con lo que dice la transcripción.

## Invocación y flags

Invocación: `/apunte <url> [flags]`. La `<url>` puede ser una URL completa o el ID pelado.

| Flag | Efecto | Default |
|---|---|---|
| `--consolidated` | Un solo .md: teoría visible + ejercicios en `<details>` anidados. | **activado** |
| `--theory-only` | Solo teoría (sin sección de ejercicios). | off |
| `--practice` | Dos archivos: teoría + `…-practica.md` con los ejercicios resueltos. | off |
| `--no-index` | No generar el `## Índice` con enlaces a timestamps. | índice activado |
| `--lang es en …` | Idiomas preferidos de la transcripción, en orden. | `es es-419 en` |
| `--out-dir <dir>` | Carpeta de salida del .md. | `materias/<materia>/<evaluacion>/apuntes/md/` |
| `--html` | Además exporta a `.html` con `tools/md_to_html.py`. | off |
| `--pdf` | Además exporta a `.pdf` (Chrome headless) con `tools/md_to_html.py --pdf`. | off |

Modos mutuamente excluyentes: `--consolidated` (default), `--theory-only`, `--practice`.
Si el usuario no aclara, usá **consolidado + índice**.

## Resolución de contexto (materia/evaluación)

El usuario puede dar la ruta `materias/<materia>/<evaluacion>` explícita. Si no la da,
aplicá la regla de "Resolución de contexto" de `CLAUDE.md`:

1. **Materia:** la única con `estado: cursando` en su `MATERIA.md`. Si hay varias, preguntar.
2. **Evaluación:** la próxima por fecha (según la tabla de evaluaciones de `MATERIA.md`).
3. Ante ambigüedad real, preguntar. Nunca adivinar en silencio.

Antes de generar, leé el `MATERIA.md` de la materia resuelta para conocer su contexto.

## Pasos

1. **Bajar la transcripción**:
   ```bash
   venv/bin/python tools/dump_transcript.py "<url>" [--lang es en]
   ```
   (fallback: `python tools/dump_transcript.py …` si el venv no está disponible).
   Guardá la salida JSON en
   `materias/<materia>/<evaluacion>/apuntes/transcripts/NN-<slug>.json`; si ese JSON
   ya existe, leelo de ahí en vez de volver a pegarle a YouTube (mismo cache que usa
   `/apuntes-batch` — evita el rate-limit al regenerar un apunte).
   Devuelve JSON con `video_id`, `title`, `url`, `suggested_path` y `contents`
   (la transcripción ya trae los marcadores `[mm:ss|SEGUNDOSs]` y, al inicio, la
   plantilla de enlace `https://www.youtube.com/watch?v=ID&t={SEGUNDOS}s`).
   - Si la transcripción está vacía o da error, avisale al usuario y pará.

2. **Leer `contents` completo** y generar el cuerpo del apunte aplicando la instrucción
   del modo elegido (ver "Prompts" abajo). Trabajá sobre TODO el contenido, no sobre una
   muestra.

3. **Escribir el/los archivo(s)** en la carpeta de salida (default
   `materias/<materia>/<evaluacion>/apuntes/md/`) con el nombre `NN-<slug>.md`, donde
   `<slug>` sale del `suggested_path` (slug del título) y `NN` es el **siguiente número
   libre de dos dígitos** en esa carpeta (los apuntes van SIEMPRE numerados en orden
   cronológico de las clases: si el último es `07-…`, el nuevo es `08-…`). Si el usuario
   indica otro `NN`, respetarlo. Cada archivo lleva este encabezado EXACTO antes del cuerpo:
   ```markdown
   # {title}

   > Fuente: {url}

   ---

   ```
   …y el cuerpo, terminado con un `\n` final. Para `--practice`, el segundo archivo es
   `NN-{slug}-practica.md` con título `# {title} — Práctica`.

4. **Exportar (opcional)** si pidieron `--html` o `--pdf`, a las carpetas hermanas
   `apuntes/html/` y `apuntes/pdf/`:
   ```bash
   venv/bin/python tools/md_to_html.py <ruta.md> --out-dir <…>/apuntes/html                # --html
   venv/bin/python tools/md_to_html.py <ruta.md> --pdf --no-html --out-dir <…>/apuntes/pdf  # --pdf
   ```
   (el `--no-html` es necesario: sin él, el export a PDF deja también un `.html`
   espurio dentro de `apuntes/pdf/`).

5. **Actualizar `MATERIA.md`:** si la tabla "Estado del material" de la materia cambió
   (p. ej. la cantidad de apuntes de la evaluación), actualizala.

6. Confirmá las rutas escritas (`✓ Guardado: …`).

## Prompts (reglas de generación)

Seguí estas reglas al pie de la letra para que el output sea consistente entre materias.

### Reglas comunes (todos los modos)
- **Basate ÚNICAMENTE en la transcripción.** NO inventes teoría, ejercicios, datos ni
  resultados, ni completes con tu propio conocimiento.
- Si el audio está confuso o algo no se entiende, marcalo `[poco claro en la transcripción]`.
- Ignorá saludos, interrupciones y comentarios irrelevantes del profesor.
- **Formato de fórmulas (CRÍTICO):** cada fórmula en bloque (`$$…$$`) va en líneas propias,
  SIN sangría (pegada al margen izquierdo) y con una línea en blanco antes y después. NUNCA
  indentes una fórmula ni la metas dentro de una lista numerada o con viñetas (el visor la
  toma como bloque de código y no la renderiza). Usá `$…$` para matemática inline.
- Estructurá con títulos (H2/H3) y viñetas; apunte directo y listo para estudiar.
- **Timestamps:** usá ÚNICAMENTE los valores que aparecen en los marcadores `[mm:ss|Ns]`.
  NO inventes timestamps. Para cada enlace usá la plantilla provista reemplazando `{SEGUNDOS}`
  por el valor `N` del marcador más cercano al inicio de ese tema.

### Índice (salvo `--no-index`)
Empezá la salida con una sección `## Índice` que liste, en orden cronológico, los temas
principales, cada uno como `- [mm:ss](ENLACE) — Tema`. Después del índice va el apunte, y en
cada título de sección (H2/H3) agregá también su enlace al timestamp:
`### Tema — [mm:ss](ENLACE)`.

### Modo CONSOLIDADO (default)
Un único apunte donde **teoría y ejercicios van intercalados en orden cronológico del
video** (sincronizados con la clase): cada ejercicio aparece JUSTO DESPUÉS de la sección de
teoría que el profesor termina de explicar antes de resolverlo, según su timestamp. NO los
agrupes todos al final ni uses encabezados `# PARTE 1 — TEORÍA` / `## Ejercicios`; el
documento es una sola línea temporal de secciones `##` (teoría) con bloques `<details>`
(ejercicios) insertados en el punto del video que les corresponde.

- **Innegociable:** los ejercicios y sus resoluciones SIEMPRE van en bloques `<details>`
  desplegables (colapsables), nunca como texto plano visible.
- **Teoría** (secciones `##`, visibles): definiciones teóricas clave, teoremas principales
  (con hipótesis y tesis) y fórmulas cerradas importantes. Los cálculos ilustrativos cortos
  (una o dos líneas) van en la teoría; los problemas completos que el profesor desarrolla van
  como ejercicios desplegables.
- **Ejercicios:** extraé ÚNICAMENTE los que el profesor resuelve. El `## Índice` lista TODOS
  los bloques (teoría y ejercicios) en orden cronológico; a los ítems de ejercicio antepo-
  neles `📝` para distinguirlos. Cada ejercicio en un `<details>`, y su resolución en OTRO
  `<details>` anidado. Estructura EXACTA (respetá las líneas en blanco):

```markdown
<details>
<summary>📝 Ejercicio N — <a href="ENLACE">mm:ss</a>: tema</summary>

Enunciado del ejercicio, con sus fórmulas.

<details>
<summary>Ver resolución</summary>

**Paso 1:** explicación del paso.

$$
fórmula del paso
$$

**Paso 2:** ...

</details>

</details>
```

- Dentro del `<summary>` el contenido es HTML: el enlace DEBE ser `<a href="ENLACE">mm:ss</a>`,
  NUNCA un enlace Markdown `[mm:ss](ENLACE)` (en HTML no renderiza).
- Identificá los pasos con `**Paso N:**` en negrita, NO con listas numeradas de Markdown.
- Pasos que quedaron en el pizarrón y no se verbalizan (ambiguos): marcalos
  `[paso en el pizarrón, ver video]`.
- Si no se resuelve ningún ejercicio, omití la sección o aclaralo.

### Modo THEORY-ONLY (`--theory-only`)
Solo la parte de teoría de arriba, con su índice. Sin sección de ejercicios.

### Modo PRACTICE (`--practice`)
Archivo 1 = teoría (igual que theory-only, con índice).
Archivo 2 (`…-practica.md`) = SOLO los ejercicios que el profesor resuelve. Para cada uno:
- Título `## [mm:ss](ENLACE) — Ejercicio N: <tema>`.
- Enunciado lo más completo posible, con LaTeX.
- Resolución resumida (método y fórmulas, no cada cuenta numérica) dentro de un
  `<details><summary>Ver resolución</summary>` con pasos `**Paso N:**`. Estructura:
  ```markdown
  <details><summary>Ver resolución</summary>

  **Paso 1:** explicación del paso.

  $$
  fórmula del paso
  $$

  **Paso 2:** ...

  </details>
  ```
- Pasos del pizarrón no verbalizados: `[paso en el pizarrón, ver video]`.
- Si no se resuelve ningún ejercicio, respondé exactamente:
  `No se identificaron ejercicios resueltos en esta clase.`

## Notas
- **Rate-limit de YouTube:** bajá las transcripciones de a una, con pausa. Para procesar
  varios videos en lote usá `/apuntes-batch`.
- No sos determinístico: el formato y la calidad son consistentes entre corridas, pero no
  carácter a carácter. Eso es esperable.
