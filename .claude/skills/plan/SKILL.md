---
name: plan
description: Recalcula plan.md, el plan de estudio día-por-día VIVO de una evaluación. Cruza los días restantes hasta el examen (fecha de MATERIA.md vs. hoy) con las prioridades y el banco de problemas de estrategia.md, el avance y los errores de registro.md, la poda de que-saltear.md y la disponibilidad que declare el usuario. Usala cuando el usuario pida armar o rehacer el plan de días, cuando diga que se atrasó / que hoy no puede / que ya vio tal tema, después de registrar errores o regenerar la estrategia, o cuando invoque /plan.
---

# plan

Genera o regenera `materias/<materia>/<evaluacion>/plan.md`: el plan día-por-día
**vivo** hasta el examen. La `estrategia.md` trae un plan inicial **congelado** (foto
del día que se generó); este archivo es el que se recalcula cada vez que cambia el
panorama: pasaron días, hubo errores en la práctica, se indexó un examen nuevo, el
usuario avisa que no puede estudiar tal día o que ya cubrió algo.

Es una **vista derivada y regenerable**: se reescribe entera en cada corrida, no se
edita a mano.

## Entrada / argumentos

Invocación: `/plan [materias/<materia>/<evaluacion>] [texto libre]`

| Argumento | Efecto | Default |
|---|---|---|
| `materias/<m>/<e>` | Ruta explícita de la evaluación a planificar. | resolución de contexto |
| texto libre | Restricciones y novedades del usuario: disponibilidad horaria ("solo 2 h por día", "el sábado no puedo"), avance no registrado ("ya vi Green", "hoy no toco nada"). Se respetan en el armado y quedan citadas en el pie. | ninguno |

Si el usuario no da la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`:

1. Materia: la única con `estado: cursando` en su `MATERIA.md`. Si hay varias, preguntá.
2. Evaluación: la próxima por fecha según la tabla de evaluaciones de `MATERIA.md`.
3. Ante ambigüedad real, preguntá. Nunca adivines en silencio.

## Requisitos previos (bloqueantes)

- `materias/<m>/MATERIA.md` con la **fecha del examen** de la evaluación. Sin fecha
  no hay días que repartir: pará y pedila.
- `materias/<m>/<e>/estrategia.md` — prioridades 🔴🟠🟡⚪, banco de problemas tipo,
  checklist teórico y exámenes reservados a ciegas. Si falta → **pará** y pedile al
  usuario correr `/estrategia` primero.

Opcionales (usarlos si existen): `<base>/registro.md`, `<base>/que-saltear.md`,
`<base>/plan.md` anterior (para el diff "Qué cambió").

## Pasos

Con `<base> = materias/<materia>/<evaluacion>`:

1. **Fecha de hoy y días restantes.** Corré `date +%F` (no asumas la fecha del
   contexto). Días restantes = fecha del examen (`MATERIA.md`) menos hoy. Si el
   usuario declaró días bloqueados u horas por día, descontalos: lo que cuenta son
   los **días útiles**. Casos borde:
   - **El examen es HOY** → plan de un solo día: repaso liviano de fórmulas y del
     checklist teórico, nada nuevo. Sin tabla de días.
   - **La fecha ya pasó** → parar y avisar: la tabla de evaluaciones de `MATERIA.md`
     quedó vieja; pedir actualizarla (o confirmar qué evaluación se está preparando)
     antes de planificar.

2. **Leer los insumos:**
   - `estrategia.md` completa: prioridades por tema, banco de problemas tipo (tema →
     fechas exactas de exámenes), checklist teórico, y **qué exámenes quedaron
     reservados "a ciegas"** para simulacro (no asignar sus problemas a días de
     práctica común: los quemarías).
   - `registro.md` (si existe): qué temas ya se practicaron y con qué resultado,
     errores recurrentes. Convención: lo que tenga ❌ o 🟡 está flojo; lo ✅
     está cubierto.
   - `que-saltear.md` (si existe): lo 🗑️ no entra al plan; lo 📖 entra como lectura
     liviana adosada a un día afín, nunca como foco de un día.
   - `plan.md` anterior (si existe): guardá su tabla para el diff del paso 6.

3. **Inventario de pendientes.** Armá la lista de temas a cubrir, ordenada así:
   1. Temas 🔴 con ❌/🟡 en el registro o sin practicar (el núcleo duro flojo).
   2. Temas 🟠 en la misma condición.
   3. Repaso corto de lo que ya salió ✅ (mantener, no re-estudiar).
   4. Temas 🟡 de la estrategia.
   5. Temas ⚪ — SOLO si sobra tiempo; si no entran, ni aparecen.

   Regla clave: **lo que falló se reprograma antes que el material nuevo.** Un 🟠
   con errores repetidos se trata como 🔴 (misma ponderación que usa `/estrategia`).

4. **Chequeo de factibilidad (antes de armar nada).** Contá los temas 🔴 pendientes
   del inventario contra los días útiles disponibles (descontando los 1–2 días
   finales de simulacro + repaso y el día previo liviano). Si quedan **menos días
   útiles que temas 🔴 pendientes**, NO armes un plan imposible que meta tres temas
   nuevos por día: decilo sin vueltas al principio del documento (sección
   `## ⚠️ No entra todo`) y proponé el **triaje**: qué 🔴 sacrificar o reducir a
   "fórmula + un ejemplo" y por qué (menor frecuencia dentro de los 🔴, menos puntos
   por examen, tema comodín que rota), qué 🟠/🟡 caen directamente, y qué implica en
   puntos esperados. El plan resultante refleja el triaje elegido, no la lista completa.

5. **Armar el plan día por día.** Tabla con **fechas reales** (una fila por día
   calendario hasta el examen, incluyendo los bloqueados marcados como tales):

   - **Núcleo duro primero y con más días:** los 🔴 flojos al principio, con más de
     un día si el registro muestra errores recurrentes en ellos.
   - **Cada día de práctica cierra con problemas REALES concretos** del banco de la
     estrategia: citá la fecha exacta del examen de donde sale cada uno (p. ej.
     "P3 del 2023-07-15 y P2 del 2024-02-10" — ejemplo). Nada de "hacé ejercicios
     del tema": el entregable tiene que ser verificable.
   - **Últimos 1–2 días:** simulacro cronometrado — el/los exámenes reservados a
     ciegas en la estrategia, o uno generado con `/simulacro` si no queda ninguno
     sin quemar — más repaso del checklist teórico **escribiendo de memoria** los
     enunciados y demostraciones (no releyéndolos).
   - **Día previo al examen:** repaso liviano (fórmulas, errores anotados en el
     registro), NADA nuevo.
   - Los temas ⚪ entran solo en días con hueco real, nunca desplazando un 🔴/🟠.

6. **Diff contra el plan anterior.** Si había `plan.md`, armá la sección "Qué cambió
   respecto del plan anterior": temas que se movieron/agregaron/cayeron y **por qué**
   (días perdidos, errores nuevos en el registro, examen nuevo indexado, pedido del
   usuario). Si es el primer plan, omitila.

7. **Escribir `<base>/plan.md`** (sobreescribir entero) con la estructura de abajo y
   confirmá la ruta. Si detectaste triaje (paso 4), repetí el resumen del triaje en
   tu respuesta al usuario, no solo en el archivo.

## Estructura del documento generado

```markdown
# Plan de estudio — <Evaluación> <Materia>

> Examen: **AAAA-MM-DD** · Hoy: AAAA-MM-DD · **N días restantes** (M útiles).
> Restricciones declaradas: <las del usuario, o "ninguna">.

## ⚠️ No entra todo            ← SOLO si aplica (paso 4)
<diagnóstico sin vueltas + triaje propuesto con su porqué>

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| Lun AAAA-MM-DD | 🔴 <Tema> (falló el AAAA-MM-DD según registro) | <ejercicio(s) con fecha de examen exacta> resueltos sin mirar apunte |
| ... | ... | ... |
| <anteúltimo> | Simulacro cronometrado: examen AAAA-MM-DD (reservado a ciegas) | Examen completo en <duración de MATERIA.md>, corregido y registrado |
| <día previo> | Repaso liviano: fórmulas + errores del registro | Checklist teórico escrito de memoria; NADA nuevo |

## Qué cambió respecto del plan anterior   ← solo si había plan.md
- <cambio> — <motivo>.

---

*Generado el AAAA-MM-DD con: MATERIA.md (fecha del examen), estrategia.md
(prioridades y banco), registro.md (<estado o "sin registro aún">),
que-saltear.md (<sí/no>), input del usuario (<resumen o "ninguno">).*
```

## Reglas

- **Fechas reales siempre:** cada fila del plan lleva su fecha absoluta
  (AAAA-MM-DD); la fecha de hoy sale de `date +%F`, nunca de memoria.
- **Evidencia, no intuición:** los problemas asignados salen del banco de
  `estrategia.md` con sus fechas exactas; no inventes ejercicios ni frecuencias.
  No re-leas los PDFs/imágenes de `examenes/` — si necesitás detalle, `INDICE.md`.
- **No quemar los simulacros:** los exámenes marcados "a ciegas" en la estrategia
  quedan intactos hasta el día de simulacro.
- **Plan honesto:** ante falta de días, triaje explícito (paso 4); jamás un plan
  decorativo que nadie puede cumplir.
- **Regenerable:** se reescribe entero en cada corrida. Si la estrategia se
  regeneró o hay exámenes nuevos indexados, este archivo queda viejo: recalcular.
- Scripts (si hicieran falta): `venv/bin/python tools/<script>.py`, con fallback
  `python tools/<script>.py`.
- Español rioplatense (voseo), tono directo, igual que el resto del repo.

## Notas

- El "plan de X días" dentro de `estrategia.md` es la foto **inicial**; no lo
  edites desde acá. La versión viva es siempre `plan.md`.
- Después de generar, sugerí el circuito de mantenimiento: estudiar + `/registrar`
  cada sesión, `/simulacro` en los días marcados, y volver a `/plan` cuando algo
  cambie el panorama.
