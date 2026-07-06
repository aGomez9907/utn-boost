---
name: apuntes-batch
description: Genera apuntes de una materia en masa a partir de VARIOS videos de YouTube (una lista de URLs/IDs). Un apunte por video, un subagente por video. Úsala cuando el usuario pase múltiples links de YouTube y pida procesarlos todos, generar apuntes masivamente, en lote o batch, o cuando invoque /apuntes-batch. Procesa cada video en su PROPIO contexto aislado (un subagente por video) para que la calidad sea la misma que hacerlos de a uno. Requiere subagentes.
---

# apuntes-batch

## Propósito

Procesa muchos videos de una (un apunte por video) **sin perder calidad**: cada video se
genera en un **subagente con contexto limpio**, dedicado solo a esa transcripción. Eso
evita que el contexto se llene y que los últimos apuntes salgan apurados. Las reglas de
generación de cada apunte NO viven acá: viven en la skill `apunte`
(`.claude/skills/apunte/SKILL.md`), que es la fuente de verdad. Esta skill solo orquesta.

## Entrada

1. Una **lista ordenada** de URLs (o IDs) de YouTube. **El orden importa**: el primer
   video es el `01`, el segundo el `02`, etc. Esa numeración va como prefijo en el
   nombre de archivo.
2. Opcionalmente, la ruta de destino `materias/<materia>/<evaluacion>`. Si el usuario no
   la da, aplicá la regla de **Resolución de contexto** de `CLAUDE.md`: materia = la
   única con `estado: cursando` en su `MATERIA.md`; evaluación = la próxima por fecha
   según la tabla de evaluaciones de `MATERIA.md`; ante ambigüedad real, **preguntá**,
   nunca adivines en silencio.

En lo que sigue, `<eval>` = `materias/<materia>/<evaluacion>` ya resuelta (p. ej.
`materias/analisis-matematico-2/segundo-parcial` — solo un ejemplo).

## Estructura de salida

Cada video produce 3 archivos, cada uno en su carpeta, con el mismo nombre `NN-slug`:

```
<eval>/apuntes/md/NN-slug.md
<eval>/apuntes/html/NN-slug.html
<eval>/apuntes/pdf/NN-slug.pdf
```

- `NN` = índice cronológico con dos dígitos (`01`, `02`, …, `10`, `11`, …) según el
  orden en que el usuario mandó los videos. Si la carpeta ya tiene apuntes numerados y
  el usuario está agregando videos, continuá la numeración existente (confirmá si hay dudas).
- `slug` = slug del título del video (el `suggested_path` que devuelve
  `tools/dump_transcript.py` ya lo trae calculado).
- Las transcripciones cacheadas van en `<eval>/apuntes/transcripts/NN-<slug>.json`.

## Orquestación (lo hace el agente principal)

1. Resolvé `<eval>` (ver "Entrada") y asegurate de que existan las carpetas:
   `mkdir -p <eval>/apuntes/md <eval>/apuntes/html <eval>/apuntes/pdf <eval>/apuntes/transcripts`.
2. Numerá los videos según el orden recibido (1-based, dos dígitos).
3. Si el lote es grande (>8 videos), primero aplicá el protocolo de **Rate-limit de
   YouTube** (abajo): bajá y cacheá todas las transcripciones antes de despachar nada.
4. **Despachá un subagente por video** (tipo `general-purpose`), en **tandas de 3 a 5 en
   paralelo** (no todos de golpe: más paralelismo no mejora la calidad y complica el
   control). Pasale a cada subagente un prompt autocontenido (ver plantilla abajo) con
   su `NN`, su URL y la ruta `<eval>` ya resuelta.
5. Cuando termina cada tanda, juntá los resultados y seguí con la siguiente.
6. Al final, mostrá un **resumen** en tabla: `NN`, título, ruta del `.md`, nº de
   ejercicios, y cualquier problema (transcripción vacía/desactivada, PDF falló, "sin
   ejercicios", etc.) para que el usuario revise solo lo dudoso. Actualizá también la
   tabla **"Estado del material"** de `MATERIA.md` con la cantidad nueva de apuntes.

## Plantilla del prompt para cada subagente

> Sos un generador de apuntes universitarios. Procesá UN solo video y generá su apunte
> siguiendo al pie de la letra las reglas de `.claude/skills/apunte/SKILL.md`
> (LEELA primero; es la fuente de verdad del formato), en modo **consolidado con teoría
> y ejercicios intercalados en orden cronológico del video**. Los ejercicios y sus
> resoluciones SIEMPRE en bloques `<details>` desplegables anidados.
>
> Video: `<URL_O_ID>`  ·  Número de orden: `<NN>`  ·  Destino: `<eval>/apuntes/`
>
> Pasos:
> 1. Conseguí la transcripción. Si existe `<eval>/apuntes/transcripts/<NN>-*.json`,
>    leé ese JSON y NO le pegues a YouTube. Si no existe, bajala con
>    `venv/bin/python tools/dump_transcript.py "<URL_O_ID>"` (fallback:
>    `python tools/dump_transcript.py …`) y guardá el JSON en
>    `<eval>/apuntes/transcripts/<NN>-<slug>.json`. Si la transcripción está vacía o da
>    error, NO inventes nada: reportá el fallo y terminá.
> 2. Del JSON tomá `video_id`, `title`, `url`, `contents` y el `slug` (el
>    `suggested_path` del JSON ya trae el slug del título).
> 3. Generá el apunte con el encabezado exacto (`# {title}` + `> Fuente: {url}` + `---`)
>    y el cuerpo cronológico (índice + secciones `##` de teoría con los `<details>` de
>    ejercicios insertados en su timestamp). Usá únicamente timestamps reales de los
>    marcadores `[mm:ss|Ns]`. Marcá `[poco claro en la transcripción]` y `[paso en el
>    pizarrón, ver video]` cuando corresponda.
> 4. Escribí el `.md` en `<eval>/apuntes/md/<NN>-<slug>.md`.
> 5. Exportá:
>    - HTML: `venv/bin/python tools/md_to_html.py <eval>/apuntes/md/<NN>-<slug>.md --out-dir <eval>/apuntes/html`
>    - PDF:  `venv/bin/python tools/md_to_html.py <eval>/apuntes/md/<NN>-<slug>.md --pdf --no-html --out-dir <eval>/apuntes/pdf`
> 6. Devolvé UNA línea de resumen: `NN | título | <eval>/apuntes/md/<NN>-<slug>.md |
>    N ejercicios | <ok / problema>`.

(Reemplazá `<URL_O_ID>`, `<NN>`, `<slug>` y `<eval>` por los valores concretos: el prompt
que reciba el subagente no debe tener placeholders sin resolver.)

## Rate-limit de YouTube (IMPORTANTE)

Bajar muchas transcripciones en paralelo/seguidas hace que YouTube **bloquee el IP**
(`IpBlocked` / `RequestBlocked`), y ahí fallan todos los pedidos por un rato. Para lotes
grandes (>8 videos), en vez de que cada subagente baje su transcripción en paralelo:

1. El agente principal baja las transcripciones **de a una, secuencialmente y con pausa**
   (unos segundos entre cada una) con `tools/dump_transcript.py`, y cachea cada JSON en
   `<eval>/apuntes/transcripts/NN-<slug>.json`.
2. Recién después despacha los subagentes de generación, que leen el JSON cacheado (sin
   volver a pegarle a YouTube). Así la parte rate-limiteada queda centralizada y
   controlada.

Si aparece `IpBlocked` / `RequestBlocked` y el entorno corre en un IP de nube (el error
lo dice), el cooldown NO alcanza: hay que bajar las transcripciones desde una **red
residencial**. Para eso está `tools/fetch_transcripts.py`: editás su lista `REMAINING`
con los `(NN, URL)` que faltan y su `OUT_DIR` con `<eval>/apuntes/transcripts`, el
usuario lo corre en su máquina (`venv/bin/python tools/fetch_transcripts.py`; baja de a
uno, con pausa, saltea los ya bajados) y deja los JSON en
`<eval>/apuntes/transcripts/NN-<slug>.json`. Después generás los apuntes leyendo esos
JSON (campo `contents`), SIN volver a pegarle a YouTube — la calidad queda idéntica.

## Notas

- La calidad por apunte es equivalente a hacerlos de a uno, porque cada subagente
  arranca con contexto limpio dedicado a un único video.
- Reglas de generación (formato, LaTeX, `<details>`, encabezado): viven en la skill
  `apunte` (fuente de verdad). Si `apunte` cambia, esta skill no necesita cambios.
- Nada acá es específico de una materia: la misma orquestación sirve para cualquier
  `materias/<materia>/<evaluacion>`.
- `tools/dump_transcript.py` acepta URLs sin esquema, con `www`, `youtu.be` o el ID pelado.
- Si un PDF falla (falta Chrome/`CHROME_PATH`), el `.md` y el `.html` igual quedan;
  anotalo en el resumen y seguí.
- Los JSON de `transcripts/` se conservan después del lote: son el cache para regenerar
  apuntes sin volver a tocar YouTube.
