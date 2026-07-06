---
name: registrar
description: Anota una sesión de práctica en el registro.md de una evaluación y mantiene su tablero (veces practicado por tema, último resultado, tendencia y errores recurrentes). Usala cuando el usuario cuente qué practicó, cómo le fue con un problema/apunte/simulacro, qué errores cometió, o pida anotar/loguear una sesión de estudio, o cuando invoque /registrar.
---

# registrar

Convierte la descripción libre de una sesión de práctica ("hice el P3 del 2022-07-15,
salió pero dudé la orientación; el T1 de Green no me salió") en entradas estructuradas
de `registro.md`, y mantiene actualizado el **tablero** que `/plan` y `/estrategia`
leen para reponderar prioridades: lo que falla sube, lo que sale bien baja.

## Invocación

`/registrar [materias/<materia>/<evaluacion>] <descripción libre de la sesión>`

| Argumento | Efecto |
|---|---|
| ruta `materias/<m>/<e>` | Evaluación objetivo explícita. |
| descripción libre | Qué practicó, cómo salió, errores, tiempo. Puede traer VARIAS actividades. |

Si no dan la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`: materia = la
única con `estado: cursando` en su `MATERIA.md` (si hay varias, preguntar); evaluación =
la próxima por fecha según la tabla de `MATERIA.md`. Ante ambigüedad real, preguntar —
nunca adivinar en silencio.

## Archivos que toca

- **Escribe:** `materias/<m>/<e>/registro.md` (única salida).
- **Lee:** `examenes/INDICE.md` (para mapear problemas reales a tags), `plan.md` y
  `estrategia.md` de la evaluación si existen (para el cierre inteligente). NUNCA
  leer los PDFs/imágenes de `examenes/`.

## Pasos

### 1. Resolver contexto y abrir el registro

Resolvé materia/evaluación (arriba). Si `registro.md` no existe, crealo desde
`plantillas/registro.md`; si la plantilla tampoco existe, usá este esqueleto
(ajustando el título a la evaluación):

```markdown
# Registro de práctica y errores — <Evaluación> <Materia>

> Acá se anota **cada sesión de práctica** (con `/registrar` o a mano con este mismo
> formato). `/plan` y `/estrategia` leen este archivo para reponderar prioridades:
> lo que falla sube, lo que sale bien baja.

## Tablero (lo mantiene `/registrar`)

| Tema | Practicado | Último resultado | Tendencia |
|---|---|---|---|
| _(sin entradas todavía)_ | | | |

**Errores recurrentes detectados:** _(ninguno registrado aún)_

---

## Sesiones

<!-- Formato de cada entrada (una por sesión de práctica):

## AAAA-MM-DD — <qué se practicó>

- **Material:** P3 de 2022-07-15 / apunte 15 / simulacro 01…
- **Temas:** #Tag #Tag
- **Resultado:** ✅ bien | 🟡 con ayuda / dudas | ❌ mal
- **Errores puntuales:** (ej.: olvidé indicar la orientación; no supe arrancar la
  demostración)
- **Tiempo:** 25 min
- **Nota:** libre.
-->
```

### 2. Parsear la descripción a entradas estructuradas

El formato exacto está comentado al final de la sección `## Sesiones` de `registro.md`
(mantené ese comentario intacto). Cada entrada:

```markdown
## AAAA-MM-DD — <qué se practicó>

- **Material:** P3 de 2022-07-15 / apunte 15 / simulacro 01…
- **Temas:** #Tag #Tag  (los de la leyenda de MATERIA.md; ej. de AM2: #Flujo #Divergencia)
- **Resultado:** ✅ bien | 🟡 con ayuda / dudas | ❌ mal
- **Errores puntuales:** …
- **Tiempo:** 25 min
- **Nota:** libre.
```

Reglas de parseo:

- **Fecha:** hoy (AAAA-MM-DD), salvo que el usuario diga otra ("ayer hice…").
- **Material:** la referencia EXACTA — `Pn de AAAA-MM-DD` para problemas de exámenes
  reales, `Tn de AAAA-MM-DD` para teóricos, `apunte NN`, `simulacro NN`, `flashcards`.
  Si la referencia es ambigua ("el de flujo del 2022" y hay dos parciales de 2022),
  grepear `INDICE.md` y preguntar cuál era.
- **Temas:** tags `#CamelCase` de la leyenda de `INDICE.md`/`MATERIA.md`. Si el
  material es un problema real, sacá los tags grepeando su línea en `INDICE.md`
  (p. ej. `grep "P3" INDICE.md` bajo la sección de esa fecha) — no adivines. Si es
  apunte/simulacro/teoría suelta, asigná los tags de la leyenda que correspondan.
- **Resultado:** ✅ salió solo y bien · 🟡 salió con ayuda, dudas o errores menores
  ("salió pero dudé la orientación" → 🟡) · ❌ no salió ("no me salió", "no supe
  arrancar" → ❌).
- **Errores puntuales:** frases cortas y concretas del error conceptual (sirven para
  detectar recurrencias). Omitir la línea si no hubo.
- **Tiempo / Nota:** solo si el usuario los dice; omitir las líneas si no.
- **Varias actividades:** si comparten fecha y contexto, UNA entrada con varios ítems
  de Material/Resultado (un sub-bullet por actividad); si son sesiones claramente
  distintas (mañana/tarde, materiales inconexos), entradas separadas.

### 3. Insertar la entrada

Al **principio** de `## Sesiones` (la más reciente arriba), antes de las entradas
existentes y del comentario de formato si no hay ninguna.

### 4. Actualizar el tablero

Recalculalo COMPLETO releyendo todas las sesiones (no solo la nueva):

- **Fila por tema** (tag): ordenadas de peor a mejor (❌ y ↘️ arriba).
  - **Practicado:** cantidad de veces que el tag aparece en sesiones (p. ej. `4×`).
  - **Último resultado:** el emoji de la sesión más reciente con ese tag.
  - **Tendencia:** comparando las últimas 2–3 entradas del tema en orden cronológico:
    ↗️ mejorando (❌→🟡, 🟡→✅, ❌→✅) · → estable (mismo resultado, o una sola
    entrada) · ↘️ empeorando (✅→🟡, 🟡→❌, ✅→❌).
- **Errores recurrentes detectados:** todo error conceptual que aparezca en **≥2**
  sesiones (aunque con palabras distintas: "olvidé la orientación" y "dudé la normal"
  son el mismo error). Formato: `- <error> (2×: AAAA-MM-DD, AAAA-MM-DD) — #Tag`.
  Si no hay, dejar `_(ninguno registrado aún)_`.

### 5. Cierre inteligente

Después de escribir, mirá el contexto y cerrá con lo que aplique:

- Si registró ❌ (o ↘️) en un tema marcado 🔴 en `estrategia.md` → sugerí correr
  `/plan` para recalcular el plan con esa señal.
- Si `plan.md` existe y con esta sesión quedó completo todo lo planificado para hoy →
  decilo explícitamente ("completaste lo del día").
- Si detectaste un error recurrente NUEVO (recién llegó a 2×) → mencionalo.
- Si no aplica nada, un resumen de una línea de lo registrado alcanza.

## Salida

- `registro.md` actualizado: entrada(s) nueva(s) arriba de `## Sesiones` + tablero y
  errores recurrentes recalculados.
- En el chat: confirmación breve (qué se registró, con qué resultado) + el cierre
  inteligente del paso 5. No pegar el archivo entero.

## Reglas

- Español rioplatense (voseo), fechas siempre absolutas (AAAA-MM-DD).
- No inventar: registrá SOLO lo que el usuario contó. Si falta el resultado de alguna
  actividad ("hice el P2" sin decir cómo salió), preguntá antes de asignar emoji.
- Tags SIEMPRE de la leyenda existente; no crear tags nuevos sin avisar.
- No tocar nada fuera de `registro.md`; si hay que replanificar, eso es de `/plan`.
- Conservar el comentario `<!-- Formato de cada entrada … -->` dentro del archivo:
  es la referencia para anotar a mano.
- Scripts (si hicieran falta): `venv/bin/python tools/<script>.py`, con fallback
  `python tools/<script>.py`. Esta skill normalmente no necesita ninguno.
