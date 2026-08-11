# Plan de carrera — Ingeniería en Sistemas de Información

> Plan K08 (Sistemas) · Generado el **2026-08-11** · Motor `tools/planificador` v2.0.
> Documento REGENERABLE: se rehace con `/carrera` (no editar a mano).

## ⚠️ Datos: cosas a revisar

- 🟠 CdD: figura como aprobada pero falta regularizar Sim; falta aprobar BD (equivalencia, excepción o dato viejo: revisá)
- 🟠 electivas: las horas de electivas mezclan escalas (40.0, 3.0): parecen totales vs. semanales. Unificá el criterio o el acumulado no significa nada

## Hoy

- **Cursando:** AN, GG
- **Con final pendiente (regularizadas):** AM2, AdC, BD, F2, SSOO, SySL
- **Se podría anotar ya (cumple correlativas):** —

## Regularidades e intentos de final

La regularidad **no vence** en este reglamento. Lo que sí corre: cada final desaprobado suma un intento y al 4º hay que **recursar**; y cuanto más vieja la cursada, más olvidado el contenido.

| Materia | Cursada en | Hace | Intentos de final | Situación |
|---|---|---|---|---|
| AdC | 2020 | ~6 años | 0 de 4 | 🟠 contenido de hace 6 años: refrescar antes de rendir |
| AM2 | 2026 | ~0 años | 0 de 4 | 🟢 |
| SySL | 2021 | ~5 años | 0 de 4 | 🟠 contenido de hace 5 años: refrescar antes de rendir |
| F2 | 2025 | ~1 años | 0 de 4 | 🟢 |
| SSOO | 2022 | ~4 años | 0 de 4 | 🟠 contenido de hace 4 años: refrescar antes de rendir |
| BD | 2023 | ~3 años | 0 de 4 | 🟢 |

## Plan de finales

| Ventana | Fecha | Materia | Prepará desde | Carga | Score | Origen |
|---|---|---|---|---|---|---|
| sep 2026 | **2026-09-22** | AM2 — Análisis Matemático II | 2026-09-05 | 40 h (~17 días) | 56.3 | declarado |
| oct 2026 (esp.) | **2026-10-26** | F2 — Física II | 2026-10-09 | 40 h (~17 días) | 35.2 | declarado |
| dic 2026 | **2026-12-01** | AdC — Arquitectura de Computadoras | 2026-11-13 | 45 h (~18 días) | 72.9 | declarado |
| dic 2026 | **2026-12-11** | SySL — Sintaxis y Semántica de Lenguajes | 2026-11-24 | 40 h (~17 días) | 77.4 | sugerido |
| dic 2026 | **2026-12-22** | AN — Análisis Numérico | 2026-12-08 | 35 h (~14 días) | 60 | sugerido |

- Sin ventana asignada todavía: BD, GG, SSOO (cargá más ventanas en `calendario.json` o entran en la proyección).

### Conflictos detectados

- 🟠 **preparacion-solapada** (AdC + SySL): la preparación de AdC y la de SySL se pisan 8 días: necesitarías ~6 h/día en ese tramo.
  - Sugerencia: empezá AdC antes o corré SySL de ventana.
- 🟠 **preparacion-solapada** (SySL + AN): la preparación de SySL y la de AN se pisan 4 días: necesitarías ~6 h/día en ese tramo.
  - Sugerencia: empezá SySL antes o corré AN de ventana.
- 🔴 **choque-con-parcial** (AdC + GG): preparar AdC (desde 2026-11-13) cae encima del GG P2 del 2026-11-16: 5 días compartidos.
  - Sugerencia: adelantá el arranque de AdC o rendilo en el llamado siguiente.
- 🔴 **choque-con-parcial** (AdC + AN): preparar AdC (desde 2026-11-13) cae encima del AN P2 del 2026-11-24: 7 días compartidos.
  - Sugerencia: adelantá el arranque de AdC o rendilo en el llamado siguiente.
- 🔴 **choque-con-parcial** (SySL + AN): preparar SySL (desde 2026-11-24) cae encima del AN P2 del 2026-11-24: 2 días compartidos.
  - Sugerencia: adelantá el arranque de SySL o rendilo en el llamado siguiente.

## Qué preparar primero (ranking explicado)

| # | Materia | Score | Urgencia | Impacto | Proximidad | Esfuerzo |
|---|---|---|---|---|---|---|
| 1 | **SySL** | **75.5** | 20.8 | 33.1 | 16.6 | 5 |
| 2 | **AdC** | **71.4** | 25 | 25.3 | 17.3 | 3.8 |
| 3 | **AM2** | **56.3** | 0 | 29.2 | 22.1 | 5 |
| 4 | **AN** | **52.4** | 5 | 25.3 | 15.9 | 6.2 |
| 5 | **F2** | **34.8** | 4.2 | 5.8 | 19.8 | 5 |
| 6 | **SSOO** | **33.4** | 16.7 | 11.7 | 0 | 5 |
| 7 | **BD** | **28.4** | 12.5 | 9.7 | 0 | 6.2 |
| 8 | **GG** | **13.7** | 5 | 0 | 0 | 8.7 |

<details><summary>Desglose completo de cada score</summary>

**SySL** → 75.5/100

- urgencia (peso 0.25): regularizada hace ~5 años (2021): contenido a refrescar → aporta 20.8
- impacto (peso 0.35): 2 inmediatas, 3 directas, 5 aguas abajo → IyCS, SI → aporta 33.1
- proximidad (peso 0.25): final el 2026-12-11 (en 122 días) → aporta 16.6
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**AdC** → 71.4/100

- urgencia (peso 0.25): regularizada hace ~6 años (2020): contenido a refrescar → aporta 25
- impacto (peso 0.35): 1 inmediatas, 2 directas, 6 aguas abajo → CD → aporta 25.3
- proximidad (peso 0.25): final el 2026-12-01 (en 112 días) → aporta 17.3
- esfuerzo (peso 0.15): 45 h estimadas (default por nivel 1 (config.json)) → aporta 3.8

**AM2** → 56.3/100

- urgencia (peso 0.25): regularizada hace ~0 años (2026): contenido a refrescar → aporta 0
- impacto (peso 0.35): 1 inmediatas, 3 directas, 6 aguas abajo → Sim → aporta 29.2
- proximidad (peso 0.25): final el 2026-09-22 (en 42 días) → aporta 22.1
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**AN** → 52.4/100

- urgencia (peso 0.25): cursando: sin apuro propio todavía → aporta 5
- impacto (peso 0.35): 1 inmediatas, 3 directas, 4 aguas abajo → IO → aporta 25.3
- proximidad (peso 0.25): final el 2026-12-22 (en 133 días) → aporta 15.9
- esfuerzo (peso 0.15): 35 h estimadas (default por nivel 3 (config.json)) → aporta 6.2

**F2** → 34.8/100

- urgencia (peso 0.25): regularizada hace ~1 años (2025): contenido a refrescar → aporta 4.2
- impacto (peso 0.35): 0 inmediatas, 1 directas, 1 aguas abajo → aporta 5.8
- proximidad (peso 0.25): final el 2026-10-26 (en 76 días) → aporta 19.8
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**SSOO** → 33.4/100

- urgencia (peso 0.25): regularizada hace ~4 años (2022): contenido a refrescar → aporta 16.7
- impacto (peso 0.35): 0 inmediatas, 1 directas, 4 aguas abajo → aporta 11.7
- proximidad (peso 0.25): sin ventana asignada → aporta 0
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**BD** → 28.4/100

- urgencia (peso 0.25): regularizada hace ~3 años (2023): contenido a refrescar → aporta 12.5
- impacto (peso 0.35): 0 inmediatas, 1 directas, 3 aguas abajo → aporta 9.7
- proximidad (peso 0.25): sin ventana asignada → aporta 0
- esfuerzo (peso 0.15): 35 h estimadas (default por nivel 3 (config.json)) → aporta 6.2

**GG** → 13.7/100

- urgencia (peso 0.25): cursando: sin apuro propio todavía → aporta 5
- impacto (peso 0.35): 0 inmediatas, 0 directas, 0 aguas abajo → aporta 0
- proximidad (peso 0.25): sin ventana asignada → aporta 0
- esfuerzo (peso 0.15): 25 h estimadas (default por nivel 5 (config.json)) → aporta 8.7

</details>

## Proyección de cursada (cuatrimestre por cuatrimestre)

**Fecha estimada de graduación: 2028-12-01** (5 cuatrimestres, máx. 5 materias c/u).

Piso teórico por correlativas: **3 cuatrimestres** (cadena crítica: CD → RD → PFinal).

| Cuatrimestre | Cursa | Cierra cursada | Finales |
|---|---|---|---|
| **2C 2026 *(en curso)*** | AN, GG | AN, GG | AM2 (2026-09-22)<br>F2 (2026-10-26)<br>AdC (2026-12-01)<br>SySL (2026-12-11)<br>SSOO (2026-12-22)<br>AN (2027-02-10, est.)<br>BD (2027-02-22, est.)<br>GG (2027-03-06, est.) |
| **1C 2027** | CD, IO, IyCS, SI, Sim | CD, IO, IyCS, SI, Sim | CD (2027-07-27, est.) |
| **2C 2027** | IA, RD, SG, TpA | IA, RD, SG, TpA | IyCS (2027-09-22, est.)<br>RD (2027-12-01, est.)<br>IO (2027-12-11, est.)<br>Sim (2027-12-22, est.)<br>IA (2028-02-10, est.)<br>SG (2028-02-22, est.)<br>TpA (2028-03-06, est.) |
| **1C 2028** | PFinal, PPS, SSI | PPS, SSI | SI (2028-05-19, est.)<br>PPS (2028-07-27, est.) |
| **2C 2028** | PFinal | PFinal | SSI (2028-09-22, est.)<br>PFinal (2028-12-01, est.) |

Supuestos de la simulación: máximo 5 materias por cuatrimestre; se aprueba la cursada de todo lo que se cursa; se aprueba cada final en el primer intento; no hay inscripción a materias nuevas en un cuatrimestre ya empezado; las anuales arrancan en 1C.

### Escenarios (¿y si curso más/menos por cuatrimestre?)

| Materias/cuatrimestre | Graduación | Cuatrimestres |
|---|---|---|
| 3 | 2029-07-27 | 6 |
| 4 | 2028-12-11 | 5 |
| 5 | 2028-12-01 | 5 |

## Objetivos declarados

- ✅ **am2-septiembre** (alcanzable): AM2 puede rendir el 2026-09-22 arrancando la preparación el 2026-09-05 (40 h a 3 h/día).
- ✅ **f2-octubre** (alcanzable): F2 puede rendir el 2026-10-26 arrancando la preparación el 2026-10-09 (40 h a 3 h/día).
- ✅ **adc-diciembre** (alcanzable): AdC puede rendir el 2026-12-01 arrancando la preparación el 2026-11-13 (45 h a 3 h/día).
- 🟡 **recibirme-2028** (ajustado): la proyección con 5 materias/cuatrimestre termina el 2028-12-01 (30 días antes del límite).
  - → no hay margen para recursar ni desaprobar finales.
- ✅ **cursar-ia-1c2028** (alcanzable): la proyección ya la ubica en 2C 2027 (pedido: 1C 2028).

## Electivas

Acumuladas: **46 h** aprobadas — ELEC_QA, ELEC_UX, ELEC_TH.

| Nivel | Requeridas | Acumuladas | Falta |
|---|---|---|---|
| 3 | 6 h | 46 h | ✅ |
| 4 | 12 h | 46 h | ✅ |
| 5 | 24 h | 46 h | ✅ |

⚠️ las horas cargadas mezclan escalas (ELEC_QA=40, ELEC_UX=3, ELEC_TH=3): parecen horas totales vs. horas semanales. Unificá el criterio en estado.json antes de confiar en el acumulado.

## Siguiente paso en el sistema de estudio

- **AM2** vive en `materias/analisis-matematico-2/`: usá `/estrategia` y `/plan` ahí para bajar este objetivo (final el 2026-09-22, arrancar el 2026-09-05) a un plan de días concreto.
- **F2** vive en `materias/fisica-2/`: usá `/estrategia` y `/plan` ahí para bajar este objetivo (final el 2026-10-26, arrancar el 2026-10-09) a un plan de días concreto.
- Sin carpeta de materia todavía: AdC, SySL, AN → `/nueva-materia` cuando arranque la preparación.

## Ajustar el plan a mano

Abrí **`carrera/exports/tablero.html`**: arrastrás cursadas a cuatrimestres y finales a mesas, marcás promociones ✨ y anotás intentos, con validación en vivo. Al exportar te da `plan-manual.json`; guardalo en `carrera/datos/` y volvé a correr `/carrera` para que este plan respete lo que fijaste.

---

*Generado el 2026-08-11 desde `carrera/datos/` (estado.json, correlativas.json, calendario.json, config.json, objetivos.json). Regenerar con `/carrera`.*
