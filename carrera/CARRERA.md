# Carrera — planificación de finales y cursada futura

Esta carpeta es la capa de **proyección de carrera** del sistema: no trackea el
presente (eso ya lo hace la web de la facu), sino que **simula hacia adelante**:
qué finales rendir y cuándo, con cuánta anticipación prepararlos, qué cursar en
los próximos cuatrimestres y cuándo da la graduación. Complementa a `materias/`:
acá se decide **QUÉ y CUÁNDO**; en cada `materias/<slug>/` se resuelve **CÓMO**
(apuntes, estrategia, plan de días).

## Cómo se usa

```
/carrera                 ← corrida completa: regenera plan-carrera.md + exports
/carrera escenario 3     ← ¿y si curso 3 materias por cuatrimestre?
/carrera objetivos       ← validar los targets de datos/objetivos.json
/carrera valida          ← chequear consistencia de los datos
```

O directo por CLI (mismo motor):

```bash
venv/bin/python -m tools.planificador.cli plan
venv/bin/python -m tools.planificador.cli tablero     # regenerar solo el tablero arrastrable
venv/bin/python -m tools.planificador.cli ranking -v
venv/bin/python -m tools.planificador.cli proyeccion --max 4
venv/bin/python -m tools.planificador.cli objetivos
venv/bin/python -m tools.planificador.cli json        # para integrar con otras apps
```

El circuito cómodo del día a día: abrir **`exports/tablero.html`**, arrastrar,
exportar `plan-manual.json` a `datos/` y correr `/carrera`.

## Archivos

```
carrera/
  CARRERA.md            ← este archivo (esquema de datos + reglas)
  plan-carrera.md       ← EL PLAN generado (verdad canónica legible, regenerable)
  datos/                ← LO QUE EDITÁS VOS
    estado.json         ← estado académico (se actualiza al aprobar/regularizar algo)
    correlativas.json   ← correlatividades del plan K08 (casi nunca cambia)
    calendario.json     ← fechas del cuatrimestre en curso (se recarga cada cuatri)
    objetivos.json      ← tus targets ("AM2 en sep", "recibirme en 2028")
    plan-manual.json    ← lo que FIJASTE en el tablero (lo exporta tablero.html)
    config.json         ← parámetros de reglas, con defaults documentados
  exports/              ← regenerables, no editar a mano
    tablero.html        ← EL TABLERO arrastrable: editor visual del plan
    plan-carrera.json   ← salida estructurada completa (para otras apps)
    plan-carrera.html   ← vista visual: Gantt + proyección + mapa de correlativas
    plan-carrera.ics    ← calendario (finales, arranques de preparación, parciales)
```

**Qué mantener a mano y cuándo:**

| Evento | Archivo a tocar |
|---|---|
| Aprobaste/regularizaste una materia | `datos/estado.json` (status, grade, year) |
| Desaprobaste un final | `datos/estado.json` (`intentosFinal` +1) o el tablero |
| Arranca un cuatrimestre nuevo | `datos/calendario.json` (ventanas de finales + parciales) |
| Te enteraste de una fecha de final/parcial | `datos/calendario.json` |
| Cambiaron tus metas | `datos/objetivos.json` |
| Decidiste QUÉ rendir/cursar y CUÁNDO | el tablero (`exports/tablero.html`) → exportar `plan-manual.json` |
| La facu confirma una regla (cupos, etc.) | `datos/config.json` |

Después de cualquier edición: `/carrera` y el plan entero se recalcula.

## El tablero (la forma cómoda de planificar)

`exports/tablero.html` es el plan **arrastrable**: la sugerencia del motor ya viene
puesta y vos la acomodás. Se abre en cualquier navegador, sin internet ni servidor.

- **Arrastrás** cursadas entre cuatrimestres y finales entre mesas (o al pool para
  sacarlos del plan). Todo el calendario real de mesas está a la vista, años hacia
  adelante (las de años sin confirmar se marcan `est.`; abril/octubre, `especial`).
- **Valida en vivo**: correlativas (con el motivo exacto y la fecha en que se
  destrabaría), cupo por cuatrimestre, anuales que arrancan en 1C, mesas antes del
  cierre de cursada, intentos agotados. Rojo = regla rota; amarillo = aviso.
- **✨ promoción**: marcás una cursada como "promociono por parciales" y su final
  desaparece del plan. **Intentos**: contador por final (a los 4, la materia pide
  recursada y el tablero te hace arrastrar su cursada de nuevo).
- **📌 fijar**: lo que arrastrás queda fijado; lo demás sigue siendo sugerencia
  recalculable. **Exportar plan** descarga `plan-manual.json` → lo guardás en
  `carrera/datos/` → `/carrera`, y el motor respeta lo tuyo, completa el resto y
  reporta cualquier pin que rompa una regla (lo ejecuta igual: mandás vos, pero
  queda señalado).
- Guarda un **borrador local** en el navegador mientras jugás; "↺ Sugerencia"
  vuelve al plan del motor.

## Esquema de datos (los 3 inputs)

### `estado.json`

```jsonc
{
  "plan": "K08 (Sistemas)",
  "career": "Ingeniería en Sistemas de Información",
  "summary": { ... },              // opcional; si está, el validador lo cruza contra subjects
  "subjects": [
    {
      "code": "AM2",               // identificador único (el que usan las correlativas)
      "name": "Análisis Matemático II",
      "level": 2,                  // nivel/año del plan de estudios
      "status": "regularizada",    // aprobada | regularizada | cursando | bloqueada
      "grade": null,               // nota si está aprobada
      "year": 2026,                // año de cursada (base del cálculo de vigencia)
      "elective": false,           // true si es electiva
      "electiveHours": 0,          // horas que aporta al requisito de electivas
      "duration": "cuatrimestral", // opcional: "anual" para PFinal (default cuatrimestral)
      "slug": "analisis-matematico-2", // opcional: carpeta en materias/ (enlaza las skills)
      "intentosFinal": 0,          // opcional: finales ya desaprobados de esta materia
      "promocionable": true,       // opcional: la cátedra ofrece promoción (solo informativo)
      "asumirPromocion": false,    // opcional: el plan asume que promocionás (sin final)
      "regularidadHasta": "2027-03-01" // opcional: solo se usa si vigencia modo "anios"
    }
  ]
}
```

### `correlativas.json`

```jsonc
[
  {
    "code": "AN",
    "requiresRegularized": ["AM2"],       // deben estar al menos regularizadas para CURSAR
    "requiresApproved": ["AM1", "AGA"]    // deben estar aprobadas para CURSAR
  }
]
// Las materias sin correlativas no necesitan entrada.
```

### `calendario.json`

```jsonc
{
  "today": "2026-08-11",            // fecha de referencia (la CLI permite --hoy para simular)
  "finalExamWindows": [             // ventanas de finales DECLARADAS (las que conocés)
    { "id": "sep", "from": "2026-09-22", "to": "2026-09-23",
      "calls": 1,                   // cantidad de llamados dentro de la ventana
      "candidateSubjects": ["AM2"] } // tu intención declarada (prioridad sobre lo sugerido)
  ],
  "midterms": [                     // parciales de lo que estás cursando
    { "code": "GG", "name": "Gestión Gerencial",
      "exams": [ { "n": 1, "date": "2026-09-28" }, { "n": 2, "date": "2026-11-16" } ] }
  ]
}
```

Para los años futuros donde todavía no hay fechas, el motor genera **ventanas
estimadas** con la plantilla `ventanas_tipicas` de `config.json`, que trae el
calendario académico real UTN (se repite todos los años):

| Mesa | Cuándo | Llamados | |
|---|---|---|---|
| feb-mar | 10/02 → 06/03 | 3 | |
| abril | 20/04 → 24/04 | 1 | **especial** (pocas materias aplican) |
| mayo | 19/05 → 20/05 | 1 | |
| jul-1 | 13/07 → 18/07 | 1 | |
| jul-2 | 27/07 → 01/08 | 1 | |
| sep | 22/09 → 23/09 | 1 | |
| oct | 26/10 → 30/10 | 1 | **especial** (pocas materias aplican) |
| dic | 01/12 → 22/12 | 3 | |

Se marcan `est.` en todas las salidas y NUNCA pisan una ventana declarada:
siempre arrancan después de la última que cargaste. A las **mesas especiales**
el motor no les asigna materias solo: entran únicamente las que declares como
candidatas o fijes en el tablero (configurable con `finales.usar_mesas_especiales`).

### `plan-manual.json` (lo exporta el tablero)

```jsonc
{
  "generado": "2026-08-11",
  "cursadas":  { "CD": "1C-2027" },       // materia → cuatrimestre fijado
  "finales":   { "AM2": "sep-2026" },     // materia → mesa fijada (id-año)
  "promociones": ["GG"],                  // se asume que promocionan (sin final)
  "intentosFinal": { "SySL": 2 },         // finales desaprobados (pisa estado.json)
  "maxMateriasPorCuatrimestre": 4         // opcional: tope elegido en el tablero
}
```

No hace falta escribirlo a mano: lo genera **Exportar plan** en `tablero.html`.
El motor respeta estos pins al recalcular; si alguno rompe una regla, lo ejecuta
igual y lo lista en "Decisiones del tablero que rompen reglas".

### `objetivos.json`

```jsonc
[
  { "id": "am2-septiembre", "tipo": "aprobar",   "materia": "AM2", "ventana": "sep" },
  { "id": "cursar-ia",      "tipo": "cursar",    "materia": "IA",  "cuatrimestre": "1C-2028" },
  { "id": "recibirme",      "tipo": "recibirme", "antesDe": "2028-12-31" }
]
```

Cada objetivo recibe un veredicto: ✅ alcanzable / 🟡 ajustado (se puede, con
condiciones explícitas) / ❌ inalcanzable (con qué haría falta cambiar).

## Reglas de negocio que aplica el motor

1. **Cursar** exige todas las `requiresRegularized` al menos regularizadas y
   todas las `requiresApproved` aprobadas.
2. **Rendir final** exige estar regularizada. Una materia `cursando` solo entra
   en ventanas posteriores al cierre de su cursada (asume que aprueba la
   cursada; desactivable con `finales.asumir_regulariza_cursando`).
3. **La regularidad NO vence** (regla confirmada del reglamento; modo
   `no_vence`). Lo que sí corre: **4 finales desaprobados → recursar la
   materia** (`intentos_final.maximo`). Los intentos usados se cargan por
   materia (`intentosFinal` o el tablero); con 3 usados el plan marca "último
   intento" y con 4 saca la materia de todas las mesas y la mete de nuevo en la
   proyección de cursada. La antigüedad de una regularidad vieja igual pesa en
   la prioridad (contenido olvidado). *(Si el reglamento cambiara o esto se usa
   en otra facultad, existe el modo `anios` con vencimiento parametrizable.)*
4. **Promoción:** algunas cátedras aprueban sin final con ~8 en ambos parciales
   (a lo sumo 1 recuperatorio). El motor NO adivina cuáles: marcá la materia
   (✨ en el tablero o `asumirPromocion` en estado.json) y el plan la aprueba al
   cierre de la cursada, sin final. Solo vale para materias cursando o por
   cursar: una ya regularizada rinde final sí o sí (salvo que la recurses).
5. **Duración:** todo es cuatrimestral salvo lo declarado `anual`
   (default: PFinal), que ocupa dos cuatrimestres y arranca en 1C.
6. **Dos cuatrimestres por año** (1C mar–jul, 2C ago–nov, configurable) y las
   **8 mesas anuales reales** de la plantilla (ver tabla de arriba), con
   abril/octubre como mesas especiales que no se auto-asignan.
7. **Electivas:** requisito acumulado por nivel — N3: 6 h, N4: 12 h, N5: 24 h
   (configurable en `electivas.horas_requeridas_por_nivel`).
8. **Pins del tablero:** lo fijado en `plan-manual.json` manda sobre lo
   sugerido. Un pin que rompe una regla se ejecuta igual pero queda reportado
   como violación (en el tablero, en plan-carrera.md y en el JSON).

## Parámetros y defaults (config.json)

| Sección | Parámetro | Default | Qué controla |
|---|---|---|---|
| `vigencia_regularidad` | `modo` | `no_vence` | Acá la regularidad no vence; `anios` activa vencimiento |
| | `anios` / `referencia_mes_dia` / `aviso_por_vencer_dias` | 5 / `12-31` / 365 | Solo en modo `anios` |
| `intentos_final` | `maximo` | 4 | Finales desaprobados antes de recursar |
| | `aviso_desde` | 2 | Desde cuántos usados empezar a avisar |
| `esfuerzo` | `horas_por_nivel` | 45/40/35/30/25 | Horas de preparación por nivel (1→5) |
| | `horas_por_materia` | `{}` | Override puntual por código |
| | `horas_por_dia` | 3 | Ritmo de estudio asumido |
| | `dias_utiles_por_semana` | 6 | Días de estudio por semana |
| | `dias_minimos_preparacion` | 5 | Piso de días aunque el esfuerzo sea bajo |
| `finales` | `dias_minimos_entre_finales` | 7 | Menos que esto = conflicto |
| | `bloqueo_parcial_dias_antes/despues` | 5 / 1 | Ventana protegida alrededor de un parcial |
| | `max_por_ventana` | null (= llamados) | Tope de finales por ventana |
| | `usar_mesas_especiales` | false | Si el motor puede sugerir en abril/octubre |
| `cursada` | `max_materias_por_cuatrimestre` | 5 | Cupo de la proyección |
| | `asumir_promocion` | false | Default global (mejor marcar materia por materia) |
| `electivas` | `horas_requeridas_por_nivel` | 6/12/24 | Requisito acumulado N3/N4/N5 |
| `scoring` | `pesos` | 0.25/0.35/0.25/0.15 | urgencia/impacto/proximidad/esfuerzo |
| | `horizonte_antiguedad_anios` | 6 | A cuántos años de cursada la urgencia por olvido es máxima |
| `horizonte` | `max_cuatrimestres` | 24 | Techo de la simulación |
| `objetivos` | `horas_por_dia_tope` | 8 | Más que esto = target inalcanzable |

## Qué NO hace (a propósito)

- No trackea asistencia, TPs ni el día a día de una cursada: eso es de cada
  materia (`materias/<slug>/registro.md`).
- No inventa fechas ni reglas: las mesas sin confirmar se marcan `est.` y no
  asume que una materia promociona salvo que la marques vos.
- No decide por vos: lo fijado en el tablero y los `candidateSubjects`
  declarados siempre tienen prioridad sobre lo sugerido por score — incluso si
  rompe una regla (se ejecuta y se señala, no se descarta en silencio).

## Motor

Vive en `tools/planificador/` (Python puro, sin dependencias externas, separado
de toda presentación). Tests: `venv/bin/python -m unittest discover -s
tools/planificador/tests -t .` — corren sobre una copia congelada de los datos,
así que editar `datos/` no los rompe.
