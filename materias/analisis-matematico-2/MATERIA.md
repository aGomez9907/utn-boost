# Análisis Matemático II (AM2)

- **Slug:** `analisis-matematico-2`
- **Estado:** cursando
- **Año/cuatrimestre:** 2026 · 1er cuatrimestre
- **Carrera/facultad:** _(completar)_

## Evaluaciones

| Evaluación | Carpeta | Fecha | Estado |
|---|---|---|---|
| Primer parcial | `primer-parcial/` | _(ya rendido)_ | rendido |
| Segundo parcial | `segundo-parcial/` | 2026-07-08 | rendido |
| Recuperatorio 1er parcial | `primer-parcial/` | 2026-07-17 | rendido |
| Recuperatorio 2do parcial | `segundo-parcial/` | 2026-07-17 | rendido |
| Recuperatorio 2do parcial (2ª instancia) | `segundo-parcial/` | **2026-07-31** | **próximo** |
| Final | `final/` | **2026-09-29** _(movido del 22)_ | **próximo** |

> Los recuperatorios se preparan en la **carpeta de su parcial** (mismo temario, mismos
> apuntes y mismo dataset de exámenes). El próximo (2026-07-31) es **solo del segundo
> parcial**, con dedicación exclusiva: el final de Física II del 29/7 no se rinde.

## Estructura del examen

- **Segundo parcial:** 4 problemas prácticos (P1–P4) + 2 teóricos (T1, T2), 2 horas.
  Patrón por posición (estable 2014–2025): P1 integral múltiple (volumen/masa/
  baricentro/área), P2 circulación/trabajo o conservativo+potencial, P3 flujo
  (directo o Gauss), P4 EDO 2° orden o segundo flujo/volumen, T1/T2 demostraciones
  (conservativo, cambio de variables, Green, divergencia, superposición de EDO).
- **Primer parcial:** 4 problemas prácticos (P1–P4) + 2 teóricos (T1, T2), estructura
  estable 2017–2026. El orden por posición NO es tan rígido como en el 2P, pero el
  patrón temático sí: casi siempre **trayectorias ortogonales (EDO 1er orden)** en P1 o
  P4, **derivada direccional** combinada con regla de la cadena + función implícita en
  1–2 problemas, **curva intersección de superficies** (recta tangente / plano normal) y
  **extremos por Hessiano**; rotan aproximación lineal, plano tangente a superficie y
  Taylor de grado 2. Teóricos: definir + demostrar/calcular (los más reciclados:
  derivadas direccionales de una función partida por definición, continuidad de función
  partida, regla de la cadena, y "derivada direccional máxima = ‖∇f‖").
- **Recuperatorios 2026-07-17 (rendidos):** se rindieron los dos el mismo día
  ("parcial integrador"). _El enunciado no está en el dataset: si aparece,
  indexarlo con `/indexar-examenes` — es la mejor pista para la 2ª instancia._
- **Recuperatorio 2ª instancia (2026-07-31):** solo temario del **2º parcial**; se
  asume la estructura estándar del 2P (4 prácticos + 2 teóricos, 2 h).
- **Final:** 4 problemas prácticos (P1–P4) + 2 teóricos (T1, T2), 2 horas. Estructura
  constante en los 24 finales del dataset (2024-03 → 2026-07). **Condición de aprobación
  (6 puntos): tres ejercicios correctamente resueltos, uno de T1 o T2 y dos de P1–P4.**
  A diferencia de los parciales, el orden por posición NO es rígido: el mismo tema cae en
  cualquier P según la fecha. El final **integra 1P y 2P**: casi la mitad de los ítems son
  de varias variables (implícita, plano tangente, gradiente, extremos, direccional). Temas
  con presencia dominante: flujo (96%), circulación/trabajo (92%), EDO (92%) y enunciado de
  los teoremas integrales (83%). Nunca cayeron baricentro, longitud de curva, momento de
  inercia ni superposición. Detalle en `final/estrategia.md`.

## Temario por evaluación

- **Final:** unión del temario de ambos parciales. En la práctica el dataset muestra
  dos bloques: **cálculo vectorial** (flujo directo y por Gauss, circulación por Green y
  por Stokes, conservativos y función potencial, líneas de campo y equipotenciales,
  integrales dobles/triples, área e integral de superficie, cambio de variables) y
  **varias variables + EDO** (derivación implícita, plano tangente y recta normal,
  gradiente y derivada direccional, regla de la cadena, extremos y Hessiano, Taylor y
  aproximación lineal, curva en el espacio y punto regular, diferenciabilidad y
  continuidad de funciones partidas, EDO de 1er y 2º orden, trayectorias ortogonales).
- **Segundo parcial:** integrales dobles y triples (volumen, masa, baricentro,
  cambio de variables/Jacobiano, cilíndricas y esféricas), curvas (longitud, trabajo,
  circulación), Green, campos conservativos y función potencial, superficies (área,
  masa de chapa, flujo), divergencia/Gauss, rotor/Stokes, EDO de 1er y 2° orden,
  superposición.
- **Primer parcial:** ecuaciones diferenciales ordinarias de 1er orden (lineal, variables
  separables, PVI) y trayectorias ortogonales; funciones de varias variables: dominio,
  límites y continuidad, derivadas parciales, diferenciabilidad y aproximación lineal,
  derivada direccional y gradiente, regla de la cadena (composición) y derivación
  implícita, plano tangente y recta normal a superficies (incluida paramétrica), recta
  tangente / plano normal a curvas en el espacio, polinomio de Taylor de grado 2,
  extremos locales libres (Hessiano) y extremos sobre una región. **Ojo: el 1P de esta
  cátedra SÍ incluye EDO**, no es solo varias variables.

## Fuentes

- **Videos:** clases grabadas en YouTube _(canal del profesor; completar nombre/playlist)_.
  Transcripciones cacheadas en `<eval>/apuntes/transcripts/`.
- **Exámenes reales:** 24 archivos del segundo parcial (2014–2026, incluido el
  tomado el 2026-07-08) en `segundo-parcial/examenes/`. Primer parcial: **16 exámenes
  reales de contenido distinto** (+ 2 simulacros de cátedra, 2017–2026) indexados en
  `primer-parcial/examenes/INDICE.md`, con `resueltos/` (11 resoluciones de cátedra +
  compilación) y `duplicados/` aparte. **Final: 24 exámenes distintos** (2024-03-05 →
  2026-07-28) indexados en `final/examenes/INDICE.md`, con `resueltos/` (12 resoluciones
  + respuestas oficiales del 2024-07-23) y `duplicados/` aparte. 20 de los PDFs tienen
  capa de texto; sólo 4 son escaneos que requirieron visión.

## Leyenda de tags (para `examenes/INDICE.md`)

Compartidos entre parciales: `#EDO` `#Demostracion`

**Segundo parcial** (cálculo vectorial e integrales): `#Volumen` `#MasaCuerpo`
`#Baricentro` `#AreaRegion` `#AreaSuperficie` `#LongitudCurva` `#Circulacion`
`#Trabajo` `#Green` `#Conservativo` `#FuncionPotencial` `#Flujo` `#Divergencia`
`#Rotor` `#Stokes` `#Superposicion` `#CambioVariables` `#MomentoInercia`

**Primer parcial** (funciones de varias variables + EDO): `#TrayectoriasOrtogonales`
`#Limite` `#Continuidad` `#DerivadasParciales` `#Diferenciabilidad`
`#AproximacionLineal` `#DerivadaDireccional` `#Gradiente` `#ReglaCadena`
`#DerivacionImplicita` `#PlanoTangente` `#SuperficieParametrizada` `#CurvaEspacio`
`#Taylor` `#Extremos`

**Final** (usa la unión de ambas listas, más): `#MasaChapa` (integral de superficie
escalar) `#LineasCampo` (líneas de campo / equipotenciales) `#PuntoRegular`
`#EDOPrimerOrden` `#EDOSegundoOrden`, y dos tags de **forma de consigna**, no de tema:
`#VoF` (verdadero-o-falso justificando) y `#PlantearIntegral` (plantear los límites sin
calcular).

## Estado del material

| Evaluación | Apuntes | INDICE | Estrategia | Poda | Plan | Registro | Flashcards | Machete | Simulacros |
|---|---|---|---|---|---|---|---|---|---|
| Segundo parcial (+recu) | ✅ 19 | ✅ 17 exámenes distintos | ✅ | ✅ | ✅ (recu 2ª inst. 2026-07-31) | ✅ (vacío, listo para usar) | ✅ 61 cartas | ✅ | ✅ 1 |
| Primer parcial (+recu) | — | ✅ 16 reales + 2 sim. | ✅ | — | _(viejo, del 17/7)_ | — | — | ✅ | — |
| **Final (2026-09-29)** | — (usa los del 2P + ambos machetes) | ✅ **24 finales** + 12 resueltos | ✅ | — | ✅ (recalculado 2026-09-20) | ✅ | ✅ 26 cartas | ✅ unificado 1P+2P | — |
