---
name: apuntes-batch
description: Genera apuntes de Análisis Matemático II en masa, a partir de VARIOS videos de YouTube (una lista de URLs/IDs). Un apunte por video. Úsala cuando el usuario pase múltiples links de YouTube y pida procesarlos todos / generar apuntes masivamente / en lote / batch, o cuando invoque /apuntes-batch. Procesa cada video en su PROPIO contexto aislado (un subagente por video) para que la calidad sea la misma que hacerlos de a uno. Requiere subagentes.
---

# apuntes-batch

Procesa muchos videos de una (un apunte por video) **sin perder calidad**: cada video se
genera en un **subagente con contexto limpio**, dedicado solo a esa transcripción. Eso
evita que el contexto se llene y que los últimos apuntes salgan apurados. La generación de
cada apunte sigue exactamente las reglas de la skill `apunte-am2` (modo consolidado con
teoría y ejercicios **intercalados en orden cronológico del video**).

## Entrada

Una **lista ordenada** de URLs (o IDs) de YouTube. **El orden importa**: el primer video es
el `01`, el segundo el `02`, etc. Esa numeración va como prefijo en el nombre de archivo.

## Estructura de salida

Cada apunte produce 3 archivos, cada uno en su carpeta, con el mismo nombre `NN-slug`:

```
apuntes/md/NN-slug.md
apuntes/html/NN-slug.html
apuntes/pdf/NN-slug.pdf
```

- `NN` = índice cronológico con dos dígitos (`01`, `02`, …, `10`, `11`, …) según el orden
  en que el usuario mandó los videos.
- `slug` = slug del título del video (la misma función `slugify` de `extract_notes.py`).

## Orquestación (lo hace el agente principal)

1. Asegurate de que existan las carpetas: `mkdir -p apuntes/md apuntes/html apuntes/pdf`.
2. Numerá los videos según el orden recibido (1-based, dos dígitos).
3. **Despachá un subagente por video** (tipo `general-purpose`), en **tandas de 3 a 5 en
   paralelo** (no todos de golpe: más paralelismo no mejora la calidad y complica el
   control). Pasale a cada subagente un prompt autocontenido (ver plantilla abajo) con su
   `NN` y su URL.
4. Cuando termina cada tanda, juntá los resultados y seguí con la siguiente.
5. Al final, mostrá un **resumen** en tabla: `NN`, título, ruta del `.md`, nº de ejercicios,
   y cualquier problema (transcripción vacía/desactivada, PDF falló, "sin ejercicios", etc.)
   para que el usuario revise solo lo dudoso.

## Plantilla del prompt para cada subagente

> Sos un generador de apuntes de Análisis Matemático II. Procesá UN solo video y generá su
> apunte siguiendo al pie de la letra las reglas de `.claude/skills/apunte-am2/SKILL.md`
> (LEELA primero), en modo **consolidado con teoría y ejercicios intercalados en orden
> cronológico del video**. Los ejercicios y sus resoluciones SIEMPRE en bloques `<details>`
> desplegables anidados.
>
> Video: `<URL_O_ID>`  ·  Número de orden: `<NN>`
>
> Pasos:
> 1. Bajá la transcripción: `venv/bin/python dump_transcript.py "<URL_O_ID>"`. Si falla por
>    deps probá `python dump_transcript.py …`. Si la transcripción está vacía o da error,
>    NO inventes nada: reportá el fallo y terminá.
> 2. Del JSON tomá `video_id`, `title`, `url`, `contents` y el `slug` (derivá el slug del
>    título igual que `slugify`; el `suggested_path` del JSON ya trae el slug).
> 3. Generá el apunte con el encabezado exacto (`# {title}` + `> Fuente: {url}` + `---`) y el
>    cuerpo cronológico (índice + secciones `##` de teoría con los `<details>` de ejercicios
>    insertados en su timestamp). Usá únicamente timestamps reales de los marcadores
>    `[mm:ss|Ns]`. Marcá `[poco claro en la transcripción]` y `[paso en el pizarrón, ver
>    video]` cuando corresponda.
> 4. Escribí el `.md` en `apuntes/md/<NN>-<slug>.md`.
> 5. Exportá:
>    - HTML: `venv/bin/python md_to_html.py apuntes/md/<NN>-<slug>.md --out-dir apuntes/html`
>    - PDF:  `venv/bin/python md_to_html.py apuntes/md/<NN>-<slug>.md --pdf --no-html --out-dir apuntes/pdf`
> 6. Devolvé UNA línea de resumen: `NN | título | apuntes/md/<NN>-<slug>.md | N ejercicios |
>    <ok / problema>`.

## Rate-limit de YouTube (IMPORTANTE)
Bajar muchas transcripciones en paralelo/seguidas hace que YouTube **bloquee el IP**
(`IpBlocked` / `RequestBlocked`), y ahí fallan todos los pedidos por un rato. Para lotes
grandes (>8 videos), en vez de que cada subagente baje su transcripción en paralelo:
1. El agente principal baja las transcripciones **de a una, secuencialmente y con pausa**
   (unos segundos entre cada una), y cachea cada JSON de `dump_transcript.py` en el
   scratchpad.
2. Recién después despacha los subagentes de generación, que leen el JSON cacheado (sin
   volver a pegarle a YouTube). Así la parte rate-limiteada queda centralizada y controlada.
Si aparece `IpBlocked` / `RequestBlocked` y el entorno corre en un IP de nube (el error lo
dice), el cooldown NO alcanza: hay que bajar las transcripciones desde una red residencial.
Para eso está `fetch_transcripts.py`: editás su lista `REMAINING` con los `(NN, URL)` que
faltan, el usuario lo corre en su máquina (baja de a uno, con pausa) y deja los JSON en
`apuntes/transcripts/NN-<slug>.json`. Después generás los apuntes leyendo esos JSON (campo
`contents`), SIN volver a pegarle a YouTube — la calidad queda idéntica.

## Notas
- La calidad por apunte es equivalente a hacerlos de a uno, porque cada subagente arranca
  con contexto limpio dedicado a un único video.
- Reglas de generación: viven en `apunte-am2` (fuente de verdad). Esta skill solo orquesta.
- `dump_transcript.py` y `extract_video_id` ya aceptan URLs sin esquema, con `www`,
  `youtu.be` o el ID pelado.
- Si un PDF falla (falta Chrome/`CHROME_PATH`), el `.md` y el `.html` igual quedan; anotalo
  en el resumen y seguí.
