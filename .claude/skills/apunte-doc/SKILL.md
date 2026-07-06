---
name: apunte-doc
description: Genera apuntes de estudio en Markdown desde material que NO es video, PDFs de cátedra (diapositivas, guías), capítulos de libros y fotos de apuntes propios o del pizarrón. Usala cuando el usuario pase rutas a PDFs o imágenes (típicamente en materias/<materia>/fuentes/) y pida convertirlos en apuntes, teoría o ejercicios con el formato del sistema, o cuando invoque /apunte-doc.
---

# apunte-doc

Convierte un documento (PDF, diapositivas, capítulo de libro, fotos de apuntes) en un
apunte de estudio en Markdown con el MISMO formato que los apuntes generados desde video
(`/apunte`): teoría visible en secciones `##`, ejercicios resueltos en `<details>`
anidados, todo en LaTeX. La única diferencia: **no hay timestamps** — el índice y los
títulos referencian páginas `[p. N]` (o número de diapositiva / número de foto).

## Entrada / argumentos

Invocación: `/apunte-doc <ruta(s)> [flags]`. Las rutas suelen estar en
`materias/<materia>/fuentes/`. Puede ser un PDF, varios PDFs o una serie de imágenes.

| Flag | Efecto | Default |
|---|---|---|
| `--paginas A-B` | Procesar solo ese rango de páginas del PDF. **OBLIGATORIO para libros largos: procesar por capítulo.** | documento completo |
| `--consolidated` | Un solo .md: teoría visible + ejercicios en `<details>` anidados, en el orden del documento. | **activado** |
| `--theory-only` | Solo teoría (sin sección de ejercicios). | off |
| `--no-index` | No generar el `## Índice`. | índice activado |
| `--out-dir <dir>` | Carpeta de salida. | `materias/<materia>/<evaluacion>/apuntes/md/` |
| `--html` | Además exporta a `.html` con `tools/md_to_html.py`. | off |
| `--pdf` | Además exporta a `.pdf` (Chrome headless) con `tools/md_to_html.py --pdf`. | off |

Modos mutuamente excluyentes: `--consolidated` (default) y `--theory-only`. Si el
usuario no aclara, usá **consolidado + índice**.

**Resolución de materia/evaluación:** si el usuario no da la ruta
`materias/<materia>/<evaluacion>` explícita, aplicá la regla de "Resolución de
contexto" de `CLAUDE.md`: materia = la única con `estado: cursando` en su `MATERIA.md`
(si hay varias, preguntar); evaluación = la próxima por fecha según la tabla de
`MATERIA.md`; ante ambigüedad real, preguntar — nunca adivinar en silencio. Antes de
generar, leé el `MATERIA.md` de la materia.

## Pasos

1. **Leer la fuente.**
   - **PDFs:** leelos con la tool `Read` usando el parámetro `pages` — máximo 20
     páginas por request. Para documentos más largos, troceá en tandas consecutivas
     (`pages: "1-20"`, luego `"21-40"`, etc.) hasta cubrir el rango pedido. Si el
     usuario no pasó `--paginas` y el PDF supera ~40 páginas (un libro), NO lo proceses
     entero: preguntá qué capítulo/rango quiere, o proponé la división por capítulos
     según el índice del libro.
   - **Imágenes (fotos de apuntes/pizarrón):** leé cada foto con `Read` (visión) en el
     orden dado. Transcribí el contenido manuscrito a Markdown+LaTeX de forma FIEL: no
     corrijas ni completes las cuentas; donde no se lea, marcá `[ilegible]`.
   - Si un archivo no existe o no se puede leer, avisale al usuario y pará.

2. **Generar el cuerpo del apunte** aplicando las reglas de la sección "Reglas de
   generación". Trabajá sobre TODO el material leído, no sobre una muestra.

3. **Escribir el archivo** en `materias/<materia>/<evaluacion>/apuntes/md/` (o en
   `--out-dir`) como `NN-<slug>.md`, donde `NN` es el siguiente número libre en esa
   carpeta (orden cronológico/temático del material) y `<slug>` sale del título del
   apunte. Encabezado EXACTO antes del cuerpo:

   ```markdown
   # {título}

   > Fuente: {archivo}, págs. X–Y

   ---

   ```

   Para fotos: `> Fuente: {carpeta o archivos}, fotos 1–N`. Para diapositivas, usá
   "diaps. X–Y". El cuerpo termina con un `\n` final.

4. **Exportar (opcional)** si pidieron `--html` o `--pdf`:
   ```bash
   venv/bin/python tools/md_to_html.py <ruta.md> --out-dir <eval>/apuntes/html            # --html
   venv/bin/python tools/md_to_html.py <ruta.md> --pdf --no-html --out-dir <eval>/apuntes/pdf  # --pdf
   ```
   (fallback: `python tools/md_to_html.py …` si el venv no está). El `--out-dir` es
   obligatorio: sin él el script escribe en la carpeta del `.md` (o sea dentro de
   `apuntes/md/`), y sin `--no-html` el export a PDF deja también un `.html` espurio.

5. Confirmá las rutas escritas (`✓ Guardado: …`) y actualizá la tabla **"Estado del
   material"** de `MATERIA.md` con la cantidad nueva de apuntes.

## Reglas de generación

El apunte final debe ser **indistinguible** de uno hecho desde video, salvo las
referencias a páginas en lugar de timestamps.

### Comunes (todos los modos)
- **Basate ÚNICAMENTE en el documento.** NO inventes teoría, ejercicios, datos ni
  resultados, ni completes con tu propio conocimiento. Si algo está cortado o no se
  entiende (escaneo malo, manuscrito), marcalo `[ilegible]`.
- **Formato de fórmulas (CRÍTICO):** cada fórmula en bloque (`$$…$$`) va en líneas
  propias, SIN sangría (pegada al margen izquierdo) y con una línea en blanco antes y
  después. NUNCA indentes una fórmula ni la metas dentro de una lista (el visor la toma
  como bloque de código y no la renderiza). Usá `$…$` para matemática inline.
- Estructurá con títulos (H2/H3) y viñetas; apunte directo y listo para estudiar.
  Ignorá carátulas, encabezados repetidos de página y contenido administrativo.
- **Referencias de página:** usá ÚNICAMENTE los números de página reales del documento
  (o número de diapositiva / de foto). Formato `[p. N]` (o `[diap. N]`, `[foto N]`).

### Índice (salvo `--no-index`)
Empezá la salida con `## Índice` listando los temas principales en el orden del
documento, cada uno como `- [p. N] — Tema`. Después del índice va el apunte, y cada
título de sección lleva también su referencia: `## Tema — [p. N]`.

### Modo CONSOLIDADO (default)
Un único apunte donde **teoría y ejercicios van intercalados en el orden del
documento**: cada ejercicio aparece justo después de la teoría que le corresponde. NO
los agrupes todos al final; el documento es una sola secuencia de secciones `##`
(teoría) con bloques `<details>` (ejercicios) insertados donde aparecen en la fuente.

- **Teoría** (secciones `##`, visibles): definiciones clave, teoremas (con hipótesis y
  tesis) y fórmulas cerradas importantes. Cálculos ilustrativos cortos van en la
  teoría; los problemas desarrollados van como ejercicios desplegables.
- **Ejercicios resueltos en la fuente:** cada uno en un `<details>`, con su resolución
  en OTRO `<details>` anidado. En el `## Índice` listá TODOS los bloques (teoría y
  ejercicios) en orden; a los ejercicios anteponeles `📝`. Estructura EXACTA (respetá
  las líneas en blanco):

```markdown
<details>
<summary>📝 Ejercicio N — [p. 15]: tema</summary>

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

- Dentro del `<summary>` el contenido es HTML plano: si alguna vez necesitás un enlace
  ahí, va como `<a href>`, NUNCA como enlace Markdown (no renderiza).
- Pasos identificados con `**Paso N:**` en negrita, NO con listas numeradas.
- **Ejercicios SIN resolver en la fuente** (típico de guías de práctica): van igual en
  su `<details>` con el enunciado completo, pero SIN el `<details>` de resolución;
  cerrá con la línea `*(sin resolución en la fuente)*`. NO los resuelvas vos.
- Si el documento no trae ejercicios, omití los bloques o aclaralo.

### Modo THEORY-ONLY (`--theory-only`)
Solo la teoría de arriba, con su índice. Sin ejercicios.

## Varios capítulos / varios archivos

- Generá **un apunte por unidad temática** (un capítulo, una guía, un mazo de
  diapositivas, una tanda de fotos de la misma clase), no un archivo gigante.
- Si hay **más de 2 unidades**, despachá un subagente por unidad (mismo patrón que
  `/apuntes-batch`): cada subagente recibe un prompt AUTOCONTENIDO con (a) la
  instrucción de leer esta skill (`.claude/skills/apunte-doc/SKILL.md`) y seguirla,
  (b) la ruta del archivo y el rango de páginas de su unidad, (c) la ruta de salida
  exacta `materias/<materia>/<evaluacion>/apuntes/md/NN-<slug>.md` (asigná vos los NN
  de antemano para que no colisionen) y (d) los flags pedidos. Al final, verificá que
  todos los archivos existan y reportá la lista.

## Notas
- Esta skill es la contraparte documental de `/apunte` (video). Si cambian las reglas
  de formato allá, actualizá esta skill para que sigan siendo indistinguibles.
- No leas PDFs/fotos de `examenes/` con esta skill: eso es trabajo de
  `/indexar-examenes` (regla de CLAUDE.md).
- Los apuntes en `md/` son la verdad canónica; `html/` y `pdf/` son regenerables.
