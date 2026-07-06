---
name: apunte-am2
description: Genera apuntes de Análisis Matemático II desde un video de YouTube. Úsala cuando el usuario pase una URL/ID de YouTube (youtube.com, youtu.be) y pida extraer apuntes, teoría, ejercicios o resúmenes de una clase, o cuando invoque /apunte-am2. Claude hace el rol del modelo (reemplaza la llamada a Gemini): baja la transcripción con dump_transcript.py y produce el .md con teoría + ejercicios desplegables en LaTeX, listo para estudiar.
---

# apunte-am2

Convierte una clase de YouTube en un apunte de estudio en Markdown. **Vos (Claude) hacés
el trabajo que antes hacía la API de Gemini**: bajás la transcripción con timestamps y
generás el apunte aplicando las reglas de abajo. El output debe tener el mismo formato y
calidad que producía `extract_notes.py` (ver ejemplos en `apuntes/flujo.md` y
`apuntes/integrales-dobles-iii.md`).

## Flags / argumentos

Invocación: `/apunte-am2 <url> [flags]`. La `<url>` puede ser una URL completa o el ID pelado.

| Flag | Efecto | Default |
|---|---|---|
| `--consolidated` | Un solo .md: teoría visible + ejercicios en `<details>` anidados. | **activado** |
| `--theory-only` | Solo teoría (sin sección de ejercicios). Equivale al script sin flags. | off |
| `--practice` | Dos archivos: teoría + `…-practica.md` con los ejercicios resueltos. | off |
| `--no-index` | No generar el `## Índice` con enlaces a timestamps. | índice activado |
| `--lang es en …` | Idiomas preferidos de la transcripción, en orden. | `es es-419 en` |
| `--out-dir <dir>` | Carpeta de salida. | `apuntes` |
| `--html` | Además exporta a `.html` con `md_to_html.py`. | off |
| `--pdf` | Además exporta a `.pdf` (Chrome headless) con `md_to_html.py --pdf`. | off |

Modos mutuamente excluyentes: `--consolidated` (default), `--theory-only`, `--practice`.
Si el usuario no aclara, usá **consolidado + índice**.

## Pasos

1. **Bajar la transcripción** (no llames a Gemini; reusá el helper):
   ```bash
   python dump_transcript.py "<url>" [--lang es en] [--out-dir apuntes]
   ```
   Devuelve JSON con `video_id`, `title`, `url`, `suggested_path` y `contents`
   (la transcripción ya trae los marcadores `[mm:ss|SEGUNDOSs]` y, al inicio, la
   plantilla de enlace `https://www.youtube.com/watch?v=ID&t={SEGUNDOS}s`).
   - Si falla por falta de deps, usá el venv del repo: `venv/bin/python dump_transcript.py …`.
   - Si la transcripción está vacía o da error, avisale al usuario y pará.

2. **Leer `contents` completo** y generar el cuerpo del apunte aplicando la instrucción
   del modo elegido (ver "Prompts" abajo). Trabajá sobre TODO el contenido, no sobre una
   muestra.

3. **Escribir el/los archivo(s)** en `out-dir` (default `apuntes/`), con el nombre
   `suggested_path` (slug del título). Cada archivo lleva este encabezado EXACTO antes del
   cuerpo (es lo que generaba `_write_doc`):
   ```markdown
   # {title}

   > Fuente: {url}

   ---

   ```
   …y el cuerpo, terminado con un `\n` final. Para `--practice`, el segundo archivo es
   `{slug}-practica.md` con título `# {title} — Práctica`.

4. **Exportar (opcional)** si pidieron `--html` o `--pdf`:
   ```bash
   python md_to_html.py <ruta.md>          # --html
   python md_to_html.py <ruta.md> --pdf    # --pdf
   ```

5. Confirmá las rutas escritas (`✓ Guardado: …`).

## Prompts (reglas de generación)

Estos son los mismos system instructions de `extract_notes.py` (fuente de verdad). Seguilos
al pie de la letra para que el output sea consistente.

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
Solo la PARTE 1 (teoría) de arriba, con su índice. Sin sección de ejercicios.

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
- El prompt canónico vive en `extract_notes.py` (constantes `CONSOLIDATED_INSTRUCTION`,
  `SYSTEM_INSTRUCTION`, `EXERCISES_INSTRUCTION`, `INDEX_INSTRUCTION`). Si cambian ahí,
  actualizá esta skill.
- No sos determinístico: el formato y la calidad coinciden con Gemini, pero no carácter a
  carácter. Eso es esperable.
