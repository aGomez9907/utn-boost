# Análisis Numérico (AN)

- **Slug:** `analisis-numerico`
- **Estado:** cursando
- **Año/cuatrimestre:** 2026 · 2do cuatrimestre (clases los martes; profesor del repaso: Ing. Juan Paoli)
- **Carrera/facultad:** Ingeniería en Sistemas de Información · UTN.BA (plan K08, nivel 3; la materia es la ex "Matemática Superior", los exámenes viejos llevan ese nombre o "Modelos Numéricos")

## Evaluaciones

| Evaluación | Carpeta | Fecha | Estado |
|---|---|---|---|
| Primer parcial | `primer-parcial/` | **2026-10-06** | **próximo** |
| Segundo parcial | `segundo-parcial/` | 2026-11-24 | pendiente |
| 1er recuperatorio (1P y 2P) | carpeta del parcial | _(a definir, semana de finales de diciembre 2026)_ | pendiente |
| 2do recuperatorio (1P y 2P) | carpeta del parcial | _(a definir, finales de febrero 2027)_ | pendiente |
| Final | `final/` | _(a definir)_ | pendiente |

> Fechas del cronograma oficial 2026-2C (`fuentes/cronograma-2026-2C.pdf`): repaso del
> 1P el 2026-09-29, **1er parcial 2026-10-06**, 2do parcial 2026-11-24. Los recuperatorios
> se preparan en la carpeta de su parcial. Se aprueba con **6 puntos**; se **promociona con
> 8 en cada parcial** y 8 en el TP grupal (mínimos cuadrados, `fuentes/TP-minimos-cuadrados-consigna.pdf`).
> Ojo: `analisis-matematico-2` también figura `cursando` (final el 2026-09-22): las skills
> van a preguntar qué materia usar cuando no se dé la ruta explícita.

## Estructura del examen

- **Primer parcial (formato vigente, K3052 2025):** 4 ejercicios, uno por tema, en este
  orden fijo: **Ej1 Series de Fourier · Ej2 Transformada de Laplace · Ej3 Sistemas
  estables · Ej4 Transformada Z**. Cada ejercicio tiene 2–3 ítems (a/b/c) de **1 punto
  cada uno** (10 ítems en total); se aprueba con 6. Dos temas (Tema 1 / Tema 2) con los
  mismos tipos de ítem y datos distintos. Sin ejercicio de números complejos como tal
  (en 2024-2C todavía había un Ej1 de complejos y 5 ejercicios de 2 puntos; el cronograma
  2026 solo tiene un "repaso rápido de complejos", así que se asume el formato 2025).
  Los parciales viejos (2015–2022) tenían 5 ejercicios con un ítem de multiple choice
  justificado y un ejercicio de complejos; su contenido de Fourier/Laplace/sistemas/Z
  sigue siendo el mismo. Detalle por posición en `primer-parcial/estrategia.md`.
- **Segundo parcial (2025):** 5 ejercicios de 2 puntos: Ej1 Raíces · Ej2 Sistemas de
  ecuaciones lineales (Jacobi/Gauss-Seidel) · Ej3 Interpolación y ajuste · Ej4
  Integración numérica · Ej5 Ecuaciones diferenciales (Euler, Lipschitz). _(sin indexar
  todavía: 4 archivos en `segundo-parcial/examenes/`)_
- **Final:** _(completar cuando haya finales)_

## Temario por evaluación

- **Primer parcial:** repaso de números complejos (forma polar, potencias y raíces,
  logaritmo complejo, valor principal, conjuntos en el plano); **series de Fourier**
  trigonométrica y exponencial (coeficientes, valor medio, paridad, simetría de media
  onda, completar una función definida en medio período para forzar paridad/SMO/
  coeficientes reales o imaginarios, espectro de amplitudes y de fase, uso de la serie
  para sumar series numéricas); **transformada de Laplace** (definición, tablas,
  propiedades de traslación, multiplicación y división por t, derivadas, convolución,
  teoremas del valor inicial/final, antitransformada por fracciones simples, evaluación
  de integrales impropias, ecuaciones integrales/integro-diferenciales, sistemas de EDO);
  **sistemas estables** (función de transferencia, polos y ceros, estabilidad y elección
  de K, corte de |G(s)| por el eje real/imaginario, respuesta temporal al impulso/escalón/
  entrada dada, tipo de respuesta y valor estable, método gráfico del módulo);
  **transformada Z** (definición, serie geométrica y región de convergencia, sucesiones
  definidas por paridad de n, propiedades de desplazamiento y multiplicación por n,
  antitransformada, ecuaciones en diferencias con verificación, sumas de series
  numéricas vía Z, secuencias finitas).
- **Segundo parcial:** raíces de ecuaciones no lineales (bisección, punto fijo,
  Newton-Raphson, cotas de error e iteraciones), sistemas de ecuaciones lineales
  (convergencia de Jacobi y Gauss-Seidel), interpolación polinómica (existencia y grado)
  y ajuste por mínimos cuadrados (recta, exponencial, potencial), diferenciación e
  integración numérica (trapecios, elección de h por cota de error), ecuaciones
  diferenciales (constante de Lipschitz, Euler).

## Fuentes

- **Videos:** clases virtuales grabadas de la cátedra (Aula Virtual UTN; el índice de
  links con teórica/práctica/OneNote por tema está en `fuentes/clases-virtuales-links.pdf`,
  los links no son públicos). Transcripciones cacheadas en `<eval>/apuntes/transcripts/`.
- **Documentos:** `fuentes/formulas-y-metodos-manuscrito.pdf` (hoja de fórmulas propia,
  6 páginas: Fourier, Laplace, sistemas estables, Z, fracciones simples; base del
  machete), `fuentes/metodo-fracciones-simples.pdf` (apunte de cátedra),
  `fuentes/cronograma-2026-2C.pdf`, `fuentes/TP-minimos-cuadrados-consigna.pdf`.
- **Exámenes reales:** primer parcial: **16 hojas de examen distintas (11 instancias,
  2015 → 2025)** en `primer-parcial/examenes/`, indexadas en `INDICE.md`. 4 archivos son
  enunciados puros (2024-2C y 2025-1C, parcial + 1er recuperatorio), 14 están en
  `resueltos/` (8 resueltos a mano por alumnos con corrección del docente, 3 resueltos por
  la cátedra, 4 hojas de respuestas oficiales). Segundo parcial: 4 archivos de 2025-1C
  (parcial + recuperatorio, con respuestas) en `segundo-parcial/examenes/`, sin indexar.

## Leyenda de tags (para `examenes/INDICE.md`)

**Series de Fourier:** `#SerieTrigonometrica` `#SerieExponencial` `#CompletarFuncion`
(extender la función dada en medio período para forzar paridad / SMO / coeficientes
reales o imaginarios / valor medio) `#SimetriaMediaOnda` `#ValorMedio` `#Espectro`
`#SumaSerieNumerica` (usar la serie para sumar una serie numérica) `#Fasores`

**Transformada de Laplace:** `#TransformadaLaplace` (calcular una transformada o usar una
propiedad) `#IntegralPorLaplace` (evaluar `∫₀^∞` con la definición o con `L{f/t}`)
`#Antitransformada` `#Convolucion` `#EcuacionIntegral` (ecuaciones integrales e
integro-diferenciales) `#SistemaEDO`

**Sistemas estables:** `#Estabilidad` (hallar K o decidir si es estable) `#PolosCeros`
`#CorteEje` (corte de `|G(s)|` o `|Y(s)|` por el eje real o imaginario)
`#RespuestaTemporal` (respuesta al impulso / escalón / entrada dada) `#TipoRespuesta`
(oscilatoria, amortiguada, valor estable) `#ModuloGrafico` (`|G(a+bj)|` por vectores)
`#FuncionTransferencia` (obtener `G(s)` desde la ecuación diferencial)

**Transformada Z:** `#TransformadaZ` `#ROC` (región de convergencia) `#AntitransformadaZ`
`#EcuacionDiferencia` `#SumaSeriePorZ` `#SecuenciaFinita`

**Números complejos:** `#Complejos` `#PotenciasRaices` `#LogaritmoComplejo`
`#ConjuntosComplejos`

**Forma de la consigna (no tema):** `#MultipleChoice` `#VoF` `#Demostracion`

## Estado del material

| Evaluación | Apuntes | INDICE | Estrategia | Poda | Plan | Registro | Flashcards | Machete | Simulacros |
|---|---|---|---|---|---|---|---|---|---|
| **Primer parcial (2026-10-06)** | — (sin apuntes; hoja de fórmulas en `fuentes/`) | ✅ 16 hojas / 11 instancias + 14 resueltos | ✅ | — (no hay apuntes que podar) | ✅ | ✅ (vacío) | — | — | — |
| Segundo parcial (2026-11-24) | — | pendiente (4 archivos sin indexar) | — | — | — | ✅ (vacío) | — | — | — |
