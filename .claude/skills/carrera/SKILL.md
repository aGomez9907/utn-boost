---
name: carrera
description: Planificador de carrera (finales + cursada futura). Corre el motor de tools/planificador sobre carrera/datos/ y regenera plan-carrera.md + exports (tablero arrastrable, JSON, HTML con Gantt, .ics). Usala cuando el usuario pregunte qué finales rendir y cuándo, cuánto falta para recibirse, qué puede cursar el cuatrimestre que viene, si le da para un objetivo ("¿llego a rendir X?", "¿me recibo en 2028?"), cuando quiera acomodar el plan a mano (tablero), cuando desapruebe un final o confirme una promoción, cuando actualice carrera/datos/ o traiga un plan-manual.json exportado del tablero, o cuando invoque /carrera.
---

# carrera

Corre el **planificador de carrera**: la capa que decide **QUÉ final rendir y
CUÁNDO, qué cursar en los próximos cuatrimestres y cuándo da la graduación**.
Es el complemento "macro" del sistema: las skills por materia (`/estrategia`,
`/plan`, `/apunte`…) resuelven el CÓMO de cada examen; esta resuelve el mapa
grande. Leé `carrera/CARRERA.md` antes de operar si no lo tenés fresco.

## Entrada / argumentos

Invocación: `/carrera [subcomando] [texto libre]`

| Argumento | Efecto |
|---|---|
| *(nada)* | Corrida completa: regenerar plan + exports (incluido el tablero) y resumir. |
| `tablero` | Regenerar solo `exports/tablero.html` y ofrecérselo al usuario. |
| `escenario N` | Proyección con N materias por cuatrimestre (`--max N`). |
| `objetivos` | Solo validar los targets de `carrera/datos/objetivos.json`. |
| `valida` | Solo chequear consistencia de los datos. |
| texto libre | Novedades del usuario ("aprobé AM2 con un 8", "me bocharon en SySL", "GG la promociono", "el final de F2 pasó al 28/10"): PRIMERO actualizá el JSON que corresponda, DESPUÉS regenerá. |

## Requisitos previos

- `carrera/datos/` con `estado.json`, `correlativas.json` y `calendario.json`.
  Si falta alguno → pará y pedilo (el esquema está en `carrera/CARRERA.md`).
- El motor corre con `venv/bin/python` (fallback `python3`). No necesita
  paquetes externos.

## Pasos

1. **Interpretar la novedad (si hay texto libre).** Mapear lo que cuenta el
   usuario al archivo correcto de `carrera/datos/` y editarlo:
   - aprobó/regularizó algo → `estado.json` (status, grade, year del hecho);
   - **desaprobó un final** → `estado.json`: `intentosFinal` +1 en esa materia
     (regla: al 4º desaprobado se recursa; el motor avisa solo);
   - **promociona / se le cayó la promoción** → `estado.json`:
     `asumirPromocion` true/false en esa materia (o sacarla de `promociones`
     en `plan-manual.json` si vino del tablero);
   - fechas nuevas de finales/parciales → `calendario.json` (las mesas
     especiales de abril/octubre llevan `"special": true`);
   - metas → `objetivos.json`;
   - **trae un `plan-manual.json` exportado del tablero** → guardarlo tal cual
     en `carrera/datos/plan-manual.json` (pisar el anterior);
   - reglas confirmadas por la facu (cupos, cambios de reglamento)
     → `config.json`.
   Fechas SIEMPRE absolutas (AAAA-MM-DD). No inventar: si el usuario no da la
   fecha exacta, preguntar o dejar el dato como estaba. NUNCA marcar una
   materia como promocionable/promocionada porque sí: eso lo dice el usuario.

2. **Actualizar `today`.** Antes de correr, poné la fecha real (`date +%F`) en
   `calendario.json → today`. La simulación arranca de ahí.

3. **Correr el motor:**

   ```bash
   venv/bin/python -m tools.planificador.cli plan          # corrida completa
   venv/bin/python -m tools.planificador.cli tablero       # solo el tablero
   venv/bin/python -m tools.planificador.cli plan --max N  # escenario N
   venv/bin/python -m tools.planificador.cli objetivos     # solo targets
   venv/bin/python -m tools.planificador.cli validar       # solo consistencia
   ```

   `plan` regenera: `carrera/plan-carrera.md` (verdad canónica),
   `carrera/exports/tablero.html` (el editor arrastrable) y
   `carrera/exports/plan-carrera.{json,html,ics}`.

4. **Resumir al usuario** (leyendo `plan-carrera.md`, no inventando):
   - los próximos finales con su fecha de arranque de preparación, marcando qué
     es 📌 fijado por él, qué declarado y qué sugerido;
   - los conflictos de severidad alta (choques con parciales, arranques tardíos,
     último intento disponible) y qué sugiere el plan;
   - si hay **violaciones de pins** ("Decisiones del tablero que rompen
     reglas"), listarlas: el plan las respeta pero el usuario tiene que saberlo;
   - el veredicto de cada objetivo declarado, las promociones asumidas ✨;
   - la fecha estimada de graduación y el escenario elegido;
   - si el validador tiró avisos de datos, mencionarlos UNA vez con la
     corrección sugerida.

5. **Ofrecer el tablero cuando toque.** Si el usuario quiere decidir/mover cosas
   ("¿y si rindo X en diciembre?", "quiero acomodar el plan"), en vez de
   iterar JSONs a mano: mandale `carrera/exports/tablero.html` (SendUserFile,
   display render) y explicá el circuito en una línea — arrastrar → Exportar →
   guardar como `carrera/datos/plan-manual.json` → `/carrera`. El tablero ya
   trae la sugerencia del motor puesta.

6. **Tender el puente con las materias.** Si un final planificado tiene `slug`
   (carpeta en `materias/`), recordar el circuito: `/estrategia` → `/plan` en esa
   materia usando la fecha del final y el arranque de preparación como marco. Si
   no tiene carpeta y la preparación arranca dentro del mes, sugerir
   `/nueva-materia`. Ofrecer el `.ics` para importar al calendario si el usuario
   quiere las fechas en el teléfono.

## Reglas

- **El motor decide, la skill traduce.** No recalcules a mano nada que el motor
  ya calcula (scores, fechas, conflictos): corré el CLI y leé su salida. Si el
  resultado parece raro, revisá los datos de entrada, no "corrijas" el resumen.
- **Los generados se regeneran:** `plan-carrera.md` y `exports/` no se editan a
  mano. Los únicos archivos editables son los de `carrera/datos/`.
- **Supuestos visibles:** al resumir, si una fecha viene de ventana estimada
  (`est.`) o de la vigencia supuesta de regularidad, decilo igual que lo dice el
  plan. No presentar supuestos como hechos.
- **No tocar `materias/`** desde acá: esta skill no genera apuntes ni planes de
  días; para eso están las skills de cada materia.
- Español rioplatense (voseo), tono directo, igual que el resto del repo.

## Notas

- Tests del motor: `venv/bin/python -m unittest discover -s tools/planificador/tests -t .`
  (fixtures congeladas: editar `carrera/datos/` no los rompe). Correrlos si se
  tocó código en `tools/planificador/`.
- La CLI acepta `--hoy AAAA-MM-DD` para simular desde otra fecha y `--datos
  <carpeta>` para probar con otros datos sin tocar los reales.
