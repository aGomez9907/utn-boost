---
name: estrategia
description: Genera o actualiza estrategia.md de una evaluación cruzando el patrón histórico de exámenes (examenes/INDICE.md) contra la cobertura de los apuntes (apuntes/md/). Produce frecuencia por tema con prioridades, brechas críticas, plan inicial de días, banco de problemas tipo y checklist teórico. Usala cuando el usuario pida armar/actualizar la estrategia de estudio, saber qué temas caen más, qué le falta cubrir o cómo llegar al examen, o cuando invoque /estrategia.
---

# estrategia

La skill MÁS IMPORTANTE del sistema: convierte evidencia (frecuencias reales de los
exámenes) + cobertura de apuntes en un plan de ataque. **Regla de oro:** todo sale de
datos del repo, nunca de intuición sobre "qué suele tomar la cátedra".

**Modelo de referencia (calidad esperada):**
`materias/analisis-matematico-2/segundo-parcial/estrategia.md`. Leelo antes de generar
tu primera estrategia: el output debe tener ESA estructura y ese nivel de concreción
(fechas exactas, números de apunte, porcentajes sobre exámenes distintos).

## Invocación

`/estrategia [materias/<materia>/<evaluacion>] [notas del usuario]`

| Argumento | Efecto |
|---|---|
| ruta `materias/<m>/<e>` | Evaluación objetivo explícita. |
| texto libre | Punto de partida del usuario ("vengo por el video X", "ya domino flujo"). Se registra en el encabezado y ajusta el plan. |

Si no dan la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`: materia = la
única con `estado: cursando` en su `MATERIA.md` (si hay varias, preguntar); evaluación =
la próxima por fecha según la tabla de `MATERIA.md`. Ante ambigüedad real, preguntar —
nunca adivinar en silencio.

## Paso 0 — Levantar contexto

Con `<base> = materias/<materia>/<evaluacion>`:

1. `MATERIA.md` — fecha del examen, estructura (cuántos problemas/teóricos, duración),
   leyenda de tags.
2. `<base>/examenes/INDICE.md` — **obligatorio**. Si no existe, **parar** y pedir que
   corra `/indexar-examenes` primero. No leer los PDFs/imágenes de `examenes/` jamás:
   el INDICE es la única representación textual válida.
3. Títulos y secciones de los apuntes: listar `<base>/apuntes/md/*.md` y correr
   `grep -H "^## " <base>/apuntes/md/*.md` (más el `# ` de cada uno). No hace falta
   leer los apuntes enteros: con títulos + secciones alcanza para mapear cobertura;
   leé por dentro solo lo que necesites verificar (paso 4).
4. Si existen: `<base>/que-saltear.md` (poda ya decidida) y `<base>/registro.md`
   (errores del usuario — ver "Ponderación por errores").
5. Días restantes hasta el examen (fecha de `MATERIA.md` vs. hoy) y el punto de
   partida declarado por el usuario.

## Paso 1 — Deduplicar exámenes

Usá la sección de equivalencias del INDICE: el mismo examen en dos formatos o
reeditado cuenta como **UNO**. Definí `N = cantidad de exámenes DISTINTOS`. **Todo
porcentaje del documento se calcula sobre N**, nunca sobre la cantidad de archivos.
Dejá el detalle en el Anexo A del output.

## Paso 2 — Frecuencia por tema

Para cada tag de la leyenda, contá en cuántos de los N exámenes distintos aparece
(grep sobre el INDICE, descontando duplicados). Tabla ordenada de mayor a menor:
`# | Tema | Aparece en X de N | % | Prioridad`, con esta escala fija:

| Prioridad | Umbral |
|---|---|
| 🔴 MÁXIMA | ≥ 85 % |
| 🟠 ALTA | 50–84 % |
| 🟡 MEDIA | 25–49 % |
| ⚪ BAJA | < 25 % |
| ⚪ DESCARTABLE | 0 % |

Cerrá con una **"Lectura del patrón"**: cuál es el núcleo duro (los 🔴 que juntos
cubren la mayoría de los puntos), cuál es el "tema rey" (el de mayor frecuencia,
el que no se puede fallar) y cuáles son los "comodines" (temas que rotan en una
misma posición).

## Paso 3 — Estructura por posición

Tabla `Posición | Qué cae casi siempre` para P1, P2, … y T1/T2 (o la estructura que
defina `MATERIA.md`), deducida de las posiciones reales en el INDICE.

## Paso 4 — Contraste con apuntes

1. **Brechas críticas 🔴:** temas frecuentes SIN apunte o con cobertura débil.
   Verificá con grep de keywords del tema sobre `<base>/apuntes/md/` (ej.: si el tema
   es EDO de 2° orden, grepeá `y''`, "superposición", "ecuación característica").
   0 apariciones en tema 🟠/🔴 = brecha grave; cuantificá el costo ("~1 punto por
   examen sin preparar") y decí de dónde sacarlo. Si una brecha ya se cerró con
   apuntes nuevos, marcala **✅ RESUELTA (fecha)** indicando qué apunte la cubre.
2. **Sobrecarga innecesaria 🟡:** apuntes cuyo tema casi no cae. Tabla
   `Apunte | Frecuencia | Recomendación` + la traducción práctica (a qué tema
   transferir esas horas).
3. **Mapa tema → apunte → frecuencia → qué hacer:** tabla completa que conecta cada
   tema del examen con sus archivos `NN-slug.md` y la acción (Dominar / Dominar +
   demostración / Saber fórmula y un ejemplo / Repaso / Mínimo).

## Paso 5 — Problemas reciclados

Extraé del INDICE los problemas que aparecen casi idénticos en varios exámenes, con
sus **fechas exactas** (`AAAA-MM-DD`). Son el mayor ROI de práctica: destacalos como
tal ("si dominás este, tenés un Pn casi asegurado").

## Paso 6 — Plan inicial de días

Tabla `Día | Foco | Entregable del día` desde hoy hasta el examen. Reglas:

- Núcleo duro (🔴) primero; comodines y teoría después; simulacros cronometrados en
  los últimos días; **día previo liviano** (repaso de fórmulas, nada nuevo).
- Cada entregable referencia **problemas de fechas concretas** del banco (paso 7).
- Ajustar al punto de partida declarado y a los errores de `registro.md`.
- Aclarar en el documento que este es el plan **inicial**: el plan vivo lo recalcula
  `/plan` en `plan.md`.

## Paso 7 — Banco de problemas tipo

Lista tema → fechas exactas donde practicarlo (`AAAA-MM-DD`, tal como se llaman los
archivos de `examenes/`). **Reservá 1–2 exámenes completos "a ciegas"** para simulacro
real de los últimos días: elegí los que combinan varios temas y tienen ítems poco
reciclados, marcalos explícitamente ("dejalos sin mirar") y aclarar que `/simulacro`
no debe quemarlos.

## Paso 8 — Checklist teórico

Checkboxes `- [ ]` con TODO lo que los exámenes piden "enunciar y demostrar",
indicando en cursiva el apunte donde está cada demostración (o marcando que falta /
está solo como "idea de demostración"). Encabezado tipo: "tenés que poder ESCRIBIRLO,
no solo reconocerlo".

## Salida

Escribir `<base>/estrategia.md` con EXACTAMENTE esta estructura (la del modelo):

1. `# Estrategia <evaluación> — <materia>` + encabezado en blockquote: fecha del
   examen y días restantes, punto de partida declarado, fuentes analizadas (N
   exámenes sobre M archivos + cantidad de apuntes).
2. `## 0. Cómo leer este documento` — mini-índice + **"Diagnóstico en una línea"**
   (qué está bien cubierto, cuál es LA brecha, cuál es la sobrecarga).
3. `## 1. Estructura del examen` (paso 3).
4. `## 2. Patrón real: frecuencia por tema` (paso 2, con lectura del patrón y
   problemas reciclados del paso 5).
5. `## 3. Contraste con tus apuntes` (paso 4: 3.1 brechas, 3.2 sobrecarga, 3.3 mapa).
6. `## 4. Plan de X días` (paso 6).
7. `## 5. Banco de "problemas tipo"` (paso 7, con los simulacros a ciegas marcados).
8. `## 6. Checklist teórico` (paso 8).
9. `## Anexo A — Equivalencias entre exámenes` y, si aplica, `## Anexo B` con
   archivos fuera del dataset (qué son y por qué no cuentan).
10. Pie en cursiva: fecha de generación (AAAA-MM-DD) + fuentes (`examenes/INDICE.md`
    y `apuntes/md/` de la evaluación).

## Regeneración (si estrategia.md ya existe)

**NO reescribir de cero.** Leer el existente y:

1. Agregar un bloque `> **Actualización AAAA-MM-DD:** …` arriba (después del
   diagnóstico, encima de las actualizaciones previas) explicando qué cambió: exámenes
   nuevos y si **refuerzan o cambian** el patrón, apuntes nuevos, brechas cerradas,
   formatos nuevos de problemas.
2. Actualizar las tablas y números afectados (N, frecuencias, prioridades, mapa,
   banco, checklist) y marcar brechas resueltas con ✅.
3. Recalcular el plan de días solo si cambió el panorama o quedan menos días.
4. Conservar anexos y actualizaciones anteriores.

## Ponderación por errores

Si `registro.md` tiene errores registrados: **tema frecuente + errores recientes =
la prioridad sube** (un 🟠 con errores repetidos se trata como 🔴 en el plan y se
menciona en el diagnóstico). Los temas con 0 errores y ya practicados bajan de
posición en el plan, no de prioridad en la tabla (la tabla refleja evidencia del
examen, el plan refleja al usuario).

## Reglas

- Español rioplatense (voseo), tono directo, concreto: fechas exactas, números de
  apunte, porcentajes — nada de "repasá un poco de todo".
- Nunca leer PDFs/imágenes de `examenes/`; el análisis es 100 % sobre `INDICE.md`.
- Sin INDICE no hay estrategia: parar y pedir `/indexar-examenes`.
- **Sin apuntes SÍ hay estrategia:** si `<base>/apuntes/md/` está vacía o no existe,
  avisar y generar igual — el paso 4 lista TODOS los temas 🔴/🟠 como brechas
  críticas, y el mapa tema→apunte y el checklist marcan "(sin apunte)".
- Si el documento modelo de referencia diverge de lo que esta skill especifica
  (umbrales de prioridad, títulos de sección), **manda la skill**: el modelo es
  referencia del nivel de detalle y concreción, no de estructura literal.
- No inventar frecuencias ni temas: cada número tiene que poder rehacerse grepeando
  el INDICE.
- Scripts (si hicieran falta): `venv/bin/python tools/<script>.py`, con fallback
  `python tools/<script>.py`.
- Después de generar, sugerir el siguiente paso del flujo: `/que-saltear` y `/plan`.
