# Plan de carrera — Ingeniería en Sistemas de Información

> Plan K08 (Sistemas) · Generado el **2026-08-12** · Motor `tools/planificador` v2.0.
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

✨ **Promociones asumidas (sin final):** AN, GG — si alguna promoción se cae, sacale la marca y recalculá.

## Plan de finales

| Ventana | Fecha | Materia | Prepará desde | Carga | Score | Origen |
|---|---|---|---|---|---|---|
| sep 2026 | **2026-09-22** | AM2 — Análisis Matemático II | 2026-09-05 | 40 h (~17 días) | 56.4 | declarado |
| oct 2026 (esp.) | **2026-10-26** | F2 — Física II | 2026-10-09 | 40 h (~17 días) | 35.3 | declarado |
| dic 2026 | **2026-12-01** | AdC — Arquitectura de Computadoras | 2026-11-13 | 45 h (~18 días) | 73 | declarado |
| dic 2026 | **2026-12-11** | SSOO — Sistemas Operativos | 2026-11-24 | 40 h (~17 días) | 50.8 | sugerido |

- Sin ventana asignada todavía: BD, SySL (cargá más ventanas en `calendario.json` o entran en la proyección).

### Conflictos detectados

- 🟠 **preparacion-solapada** (AdC + SSOO): la preparación de AdC y la de SSOO se pisan 8 días: necesitarías ~6 h/día en ese tramo.
  - Sugerencia: empezá AdC antes o corré SSOO de ventana.
- 🔴 **choque-con-parcial** (AdC + GG): preparar AdC (desde 2026-11-13) cae encima del GG P2 del 2026-11-16: 5 días compartidos.
  - Sugerencia: adelantá el arranque de AdC o rendilo en el llamado siguiente.
- 🔴 **choque-con-parcial** (AdC + AN): preparar AdC (desde 2026-11-13) cae encima del AN P2 del 2026-11-24: 7 días compartidos.
  - Sugerencia: adelantá el arranque de AdC o rendilo en el llamado siguiente.
- 🔴 **choque-con-parcial** (SSOO + AN): preparar SSOO (desde 2026-11-24) cae encima del AN P2 del 2026-11-24: 2 días compartidos.
  - Sugerencia: adelantá el arranque de SSOO o rendilo en el llamado siguiente.

## Qué preparar primero (ranking explicado)

| # | Materia | Score | Urgencia | Impacto | Proximidad | Esfuerzo |
|---|---|---|---|---|---|---|
| 1 | **AdC** | **71.5** | 25 | 25.3 | 17.4 | 3.8 |
| 2 | **SySL** | **58.9** | 20.8 | 33.1 | 0 | 5 |
| 3 | **AM2** | **56.4** | 0 | 29.2 | 22.2 | 5 |
| 4 | **SSOO** | **50.1** | 16.7 | 11.7 | 16.7 | 5 |
| 5 | **F2** | **34.9** | 4.2 | 5.8 | 19.9 | 5 |
| 6 | **BD** | **28.4** | 12.5 | 9.7 | 0 | 6.2 |

<details><summary>Desglose completo de cada score</summary>

**AdC** → 71.5/100

- urgencia (peso 0.25): regularizada hace ~6 años (2020): contenido a refrescar → aporta 25
- impacto (peso 0.35): 1 inmediatas, 2 directas, 6 aguas abajo → CD → aporta 25.3
- proximidad (peso 0.25): final el 2026-12-01 (en 111 días) → aporta 17.4
- esfuerzo (peso 0.15): 45 h estimadas (default por nivel 1 (config.json)) → aporta 3.8

**SySL** → 58.9/100

- urgencia (peso 0.25): regularizada hace ~5 años (2021): contenido a refrescar → aporta 20.8
- impacto (peso 0.35): 2 inmediatas, 3 directas, 5 aguas abajo → IyCS, SI → aporta 33.1
- proximidad (peso 0.25): sin ventana asignada → aporta 0
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**AM2** → 56.4/100

- urgencia (peso 0.25): regularizada hace ~0 años (2026): contenido a refrescar → aporta 0
- impacto (peso 0.35): 1 inmediatas, 3 directas, 6 aguas abajo → Sim → aporta 29.2
- proximidad (peso 0.25): final el 2026-09-22 (en 41 días) → aporta 22.2
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**SSOO** → 50.1/100

- urgencia (peso 0.25): regularizada hace ~4 años (2022): contenido a refrescar → aporta 16.7
- impacto (peso 0.35): 0 inmediatas, 1 directas, 4 aguas abajo → aporta 11.7
- proximidad (peso 0.25): final el 2026-12-11 (en 121 días) → aporta 16.7
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**F2** → 34.9/100

- urgencia (peso 0.25): regularizada hace ~1 años (2025): contenido a refrescar → aporta 4.2
- impacto (peso 0.35): 0 inmediatas, 1 directas, 1 aguas abajo → aporta 5.8
- proximidad (peso 0.25): final el 2026-10-26 (en 75 días) → aporta 19.9
- esfuerzo (peso 0.15): 40 h estimadas (default por nivel 2 (config.json)) → aporta 5

**BD** → 28.4/100

- urgencia (peso 0.25): regularizada hace ~3 años (2023): contenido a refrescar → aporta 12.5
- impacto (peso 0.35): 0 inmediatas, 1 directas, 3 aguas abajo → aporta 9.7
- proximidad (peso 0.25): sin ventana asignada → aporta 0
- esfuerzo (peso 0.15): 35 h estimadas (default por nivel 3 (config.json)) → aporta 6.2

</details>

## Proyección de cursada (cuatrimestre por cuatrimestre)

**Fecha estimada de graduación: 2028-12-22** (5 cuatrimestres, máx. 5 materias c/u).

Piso teórico por correlativas: **3 cuatrimestres** (cadena crítica: CD → RD → PFinal).

| Cuatrimestre | Cursa | Cierra cursada | Finales |
|---|---|---|---|
| **2C 2026 *(en curso)*** | AN, GG | ✨AN, ✨GG | AM2 (2026-09-22)<br>F2 (2026-10-26)<br>AdC (2026-12-01)<br>SSOO (2026-12-11)<br>📌 BD (2027-02-10, est.)<br>📌 SySL (2027-02-22, est.) |
| **1C 2027** | CD, IO, IyCS, SI, TpA | CD, IO, IyCS, SI, TpA | CD (2027-07-27, est.) |
| **2C 2027** | RD, 📌 Sim | RD, Sim | IyCS (2027-09-22, est.)<br>RD (2027-12-01, est.)<br>IO (2027-12-11, est.)<br>Sim (2027-12-22, est.)<br>TpA (2028-02-10, est.)<br>SI (2028-02-22, est.) |
| **1C 2028** | 📌 IA, PFinal, PPS, SSI | IA, PPS, SSI | PPS (2028-07-27, est.) |
| **2C 2028** | PFinal, 📌 SG | PFinal, SG | SSI (2028-09-22, est.)<br>📌 IA (2028-12-01, est.)<br>📌 SG (2028-12-11, est.)<br>PFinal (2028-12-22, est.) |

Supuestos de la simulación: máximo 5 materias por cuatrimestre; se aprueba la cursada de todo lo que se cursa; se aprueba cada final en el primer intento; no hay inscripción a materias nuevas en un cuatrimestre ya empezado; las anuales arrancan en 1C; promocionan por parciales (sin final): AN, GG; se respetan 3 cursada(s) y 4 final(es) fijados en el tablero.

### Escenarios (¿y si curso más/menos por cuatrimestre?)

| Materias/cuatrimestre | Graduación | Cuatrimestres |
|---|---|---|
| 3 | 2029-07-27 | 6 |
| 4 | 2028-12-22 | 5 |
| 5 | 2028-12-22 | 5 |

## Objetivos declarados

- ✅ **am2-septiembre** (alcanzable): AM2 puede rendir el 2026-09-22 arrancando la preparación el 2026-09-05 (40 h a 3 h/día).
- ✅ **f2-octubre** (alcanzable): F2 puede rendir el 2026-10-26 arrancando la preparación el 2026-10-09 (40 h a 3 h/día).
- ✅ **adc-diciembre** (alcanzable): AdC puede rendir el 2026-12-01 arrancando la preparación el 2026-11-13 (45 h a 3 h/día).
- 🟡 **recibirme-2028** (ajustado): la proyección con 5 materias/cuatrimestre termina el 2028-12-22 (9 días antes del límite).
  - → no hay margen para recursar ni desaprobar finales.
- ✅ **cursar-ia-1c2028** (alcanzable): la proyección ya la ubica en 1C 2028 (pedido: 1C 2028).

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
- Sin carpeta de materia todavía: AdC, SSOO → `/nueva-materia` cuando arranque la preparación.

## Ajustar el plan a mano

Abrí **`carrera/exports/tablero.html`**: arrastrás cursadas a cuatrimestres y finales a mesas, marcás promociones ✨ y anotás intentos, con validación en vivo. Al exportar te da `plan-manual.json`; guardalo en `carrera/datos/` y volvé a correr `/carrera` para que este plan respete lo que fijaste.

---

*Generado el 2026-08-12 desde `carrera/datos/` (estado.json, correlativas.json, calendario.json, config.json, objetivos.json, plan-manual.json (pins del tablero)). Regenerar con `/carrera`.*
