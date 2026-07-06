---
name: indexar-examenes
description: Incorpora exámenes reales (PDF/foto/escaneo) al INDICE.md de la carpeta examenes/ de una evaluación. Úsala cuando el usuario traiga parciales o finales nuevos, pida transcribir/indexar/taggear exámenes, o aparezcan archivos en examenes/ que no estén en el índice, o cuando invoque /indexar-examenes. Es LA ÚNICA operación autorizada a leer con visión los archivos de examenes/; después de indexar, todo análisis se hace grepeando el INDICE.md.
---

# indexar-examenes

Transcribe exámenes reales (PDFs tipeados, escaneos, fotos) a un `INDICE.md` curado con
tags por tema — la **capa 2 (dataset de exámenes)** del sistema. La regla de oro del repo
es que las imágenes/PDFs de `examenes/` se leen con visión **UNA sola vez**: acá. Todo lo
demás (`/estrategia`, `/simulacro`, análisis de frecuencias) se hace grepeando el índice.

**Modelo GOLD del formato:**
`materias/analisis-matematico-2/segundo-parcial/examenes/INDICE.md`. Leélo antes de
escribir: tu salida debe calcar su estructura (es un ejemplo, no hardcodees su contenido).

## Entrada / argumentos

Invocación: `/indexar-examenes [materias/<materia>/<evaluacion>] [rutas de archivos…]`

| Argumento | Efecto | Default |
|---|---|---|
| `materias/<materia>/<evaluacion>` | Evaluación a indexar. | Resolución de contexto (abajo) |
| Rutas de archivos | Indexar SOLO esos archivos. | Autodetectar los no indexados |
| `--todo` | Re-verificar todos los archivos de `examenes/` contra el índice. | off |

**Resolución de contexto** (regla de `CLAUDE.md`): si el usuario no da la ruta,
la materia es la única con `estado: cursando` en su `MATERIA.md`; la evaluación es la
próxima por fecha según la tabla de evaluaciones de ese archivo. Ante ambigüedad real
(varias materias cursando, fechas empatadas), **preguntá; nunca adivines en silencio**.

## Pasos

### 1. Contexto
- Resolvé materia/evaluación y leé `materias/<materia>/MATERIA.md`: de ahí salen la
  **leyenda de tags** de la materia y la **estructura del examen** (cuántos prácticos,
  cuántos teóricos, cómo se numeran).
- Ubicá `materias/<materia>/<evaluacion>/examenes/` y su `INDICE.md`. Si el índice no
  existe todavía, seguí igual con los pasos 2–7 (transcribir, taggear, comparar) y al
  final escribí el archivo nuevo usando el paso 8 como especificación del formato.

### 2. Detectar qué hay que indexar
- Si el usuario pasó rutas, usá esas.
- Si no: listá `examenes/` (`ls`) y compará contra los nombres de archivo que ya figuran
  en las secciones `## ` del `INDICE.md`. Los archivos que no aparecen son los nuevos.
- Si no hay nada nuevo, avisá y terminá (no re-leas nada con visión "por las dudas").

### 3. Leer con visión y transcribir
Por cada examen nuevo, leé el archivo con la tool Read (visión). Es la única lectura
autorizada de estos archivos; hacela valer:
- Transcribí **cada ítem** del examen: prácticos como `- **Pn)** enunciado → #Tag #Tag`,
  teóricos como `- **T1)** / **T2)** …` (adaptá la numeración a la estructura que declare
  `MATERIA.md`).
- La matemática va **INTACTA**, en el mismo estilo del modelo: unicode/LaTeX inline con
  backticks (`x²+y² ≤ 4`, `y'' + 2y' = 4x`, `∬_D`, `∇φ`). No parafrasees fórmulas ni
  "simplifiques" dominios: el enunciado transcripto reemplaza a la imagen para siempre.
- Si el escaneo/foto deja algún detalle dudoso (un exponente borroso, un límite de
  integración ilegible), transcribí tu mejor lectura marcada con **«≈»** y no lo des por
  exacto. Lo verdaderamente ilegible: `[ilegible en el escaneo]`.
- Anotá entre paréntesis el formato en el encabezado de la sección: `(escaneo)`, `(foto)`,
  o nada si es PDF tipeado.

### 4. Renombrar el archivo
- Si la fecha es visible en el examen, renombralo a `AAAA-MM-DD_Parcial.<ext>` (o el
  nombre de evaluación que corresponda, p. ej. `_Final`): `git mv "<viejo>" "<nuevo>"`
  (fallback `mv` si la carpeta no está trackeada todavía).
- Si NO hay fecha visible: `sin-fecha_Parcial.<ext>` (numerá `sin-fecha-2_…` si ya hay
  uno) y anotá en el encabezado de su sección las **pistas de datación** que encuentres
  (problemas compartidos con exámenes fechados, estilo de tipeo, temas que recién
  aparecen en cierto período), con un `⚠`.

### 5. Taggear
- Usá **exclusivamente** los tags `#CamelCase` de la leyenda de `MATERIA.md`. Un ítem
  puede llevar varios tags; el tag principal va primero.
- Si un ítem no encaja en ningún tag existente, creá uno nuevo `#CamelCase` y agregalo en
  **los dos lugares**: la leyenda de `MATERIA.md` y la sección "Leyenda de tags" del
  `INDICE.md`. Avisale al usuario del tag nuevo (suele indicar un tema nuevo en juego).

### 6. Comparar contra lo ya indexado
Antes de agregar la sección, grepeá el índice existente buscando coincidencias:
- **Equivalencia** (mismo examen completo con otra fecha u otro formato de archivo):
  NO dupliques la sección. Anotá `≡` en el encabezado de la sección existente y sumá la
  línea a la sección **"Equivalencias"** del final (mismo examen ≠ practicar dos veces).
- **Problema reciclado** (mismo problema o casi, en fechas distintas): marcá el ítem con
  `**[RECICLADO]**` y actualizá la sección **"Problemas reciclados"** con todas las
  fechas donde aparece. Son oro para practicar: lo que se repite, se vuelve a tomar.
- **Fuera de dataset**: si el archivo NO pertenece a esta evaluación (p. ej. un primer
  parcial mezclado, una guía de TP), no lo indexes como examen; anotalo en la sección
  "Fuera de dataset" con qué es y qué se hizo con él.

### 7. Actualizar los metadatos del índice
- **Índice inverso tema → fechas**: sumá las fechas nuevas a cada tag tocado (en el
  modelo, las fechas recién agregadas van en **negrita**). Si un tag de la leyenda no
  aparece en ningún examen, dejalo con la nota "(no aparece en ningún parcial)".
- **Pie de fecha**: actualizá la línea final en cursiva con la fecha de hoy (absoluta,
  AAAA-MM-DD), qué se agregó y desde cuántos archivos, conservando el historial previo
  ("generado el X y ampliado el Y con …").

### 8. Si el `INDICE.md` no existe: crearlo desde cero
Con el formato exacto del modelo GOLD:
1. `# Índice de <evaluación> — <materia>` + blockquote con **"Para qué sirve"** (los
   exámenes no siempre tienen capa de texto; este archivo es la transcripción curada),
   ejemplos de **comandos `grep`** reales con tags de esta materia, y una nota de
   **mantenimiento**.
2. `## Leyenda de tags` (copiada de `MATERIA.md`) + blockquote con la convención de
   líneas `- **Pn)** … → #Tag` y la marca «≈» para escaneos.
3. `---` y una sección `## AAAA-MM-DD · \`archivo\` (formato)` por examen, en orden
   cronológico (los `sin-fecha` al final).
4. `---` y las secciones de cierre: `## Índice inverso: tema → fechas` (tabla),
   `## Problemas reciclados`, `## Equivalencias`, `## Fuera de dataset` (si aplica).
5. `---` y el pie en cursiva con fecha de generación y fuentes.

### 9. Cierre
- Confirmá: archivos indexados (con sus renombres), tags nuevos, reciclados y
  equivalencias detectadas.
- Si el patrón histórico cambió (tema que nunca se tomaba, formato nuevo de teórico,
  estructura distinta del examen), **sugerí regenerar `/estrategia`** (y en cascada
  `/plan`): el índice es la evidencia sobre la que se construye todo lo demás.

## Reglas

- **Español rioplatense** (voseo), como todo el repo.
- **Una sola lectura con visión** por archivo. Si el usuario después pide analizar
  frecuencias o buscar un problema, la respuesta sale del `INDICE.md`, no de re-abrir
  imágenes.
- **No inventar**: transcribís lo que se ve. Duda chica → «≈»; duda grande →
  `[ilegible en el escaneo]`. Nunca completes un enunciado "como suele venir".
- **Fechas absolutas** (AAAA-MM-DD) en nombres de archivo, encabezados y pie.
- No borres entradas existentes del índice: solo agregás, marcás equivalencias y
  actualizás metadatos.
- Si necesitás scripts del repo, corrélos con `venv/bin/python tools/<script>.py`
  (fallback `python tools/<script>.py`), aunque esta skill normalmente no los necesita.

## Notas

- El ejemplo de referencia (AM2, segundo parcial) muestra casos reales de todo lo de
  arriba: exámenes en doble formato (pdf + png), un examen `sin-fecha` datado por un
  problema compartido, un flujo reciclado 4 veces y un PDF fuera de dataset. Es SOLO un
  ejemplo: cada materia tiene su propia leyenda de tags y estructura en `MATERIA.md`.
- Después de indexar, commiteá con mensaje en español describiendo el material agregado
  (regla del repo), si el usuario ya venía commiteando.
