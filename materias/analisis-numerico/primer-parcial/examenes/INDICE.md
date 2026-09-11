# Índice de parciales — Primer Parcial · Análisis Numérico (UTN.BA)

> **Para qué sirve:** los parciales vienen como PDFs tipeados, escaneos y fotos de hojas
> resueltas a mano, y dos `.docx` con fórmulas incrustadas como objetos que no se pueden
> extraer. Este archivo es la **única representación textual** de todos: transcripción
> curada (matemática intacta) de cada hoja de examen, con **tags por tema**. Para cualquier
> análisis (frecuencias, brechas, simulacros) se grepea **este archivo**, nunca se re-leen
> los PDFs/fotos.
>
> **Cómo buscar** (desde `examenes/`):
> ```bash
> grep -n "#Estabilidad" INDICE.md          # todos los ítems de sistemas estables
> grep -n "#EcuacionDiferencia" INDICE.md   # ecuaciones en diferencias (Z)
> grep -B2 "#CompletarFuncion" INDICE.md    # Fourier "completar la función", con su hoja
> grep -n "^## " INDICE.md                  # listar las 16 hojas de examen
> grep -n "RECICLADO" INDICE.md             # problemas repetidos entre fechas
> ```
> **Mantenimiento:** al agregar un parcial nuevo, sumá su sección con los mismos tags y
> actualizá las tablas del final. Si viene con resolución en el mismo archivo va a
> `resueltos/`; si es copia de uno ya indexado, a `duplicados/`.

## Cómo está armado el dataset

- **Unidad de conteo = hoja de examen.** En cada fecha la cátedra toma **Tema 1 y Tema 2**
  (mismos tipos de ítem, datos distintos). Acá cada tema es una sección propia porque son
  problemas distintos para practicar: **16 hojas** de **11 instancias** (fechas o
  cuatrimestres). Los porcentajes de `estrategia.md` se calculan sobre las 16 hojas.
- **Dos formatos históricos del examen:**
  - **Viejo (2015 → 2024-2C):** 5 ejercicios de 2 puntos (o tabla de puntos fraccionados,
    "nota = X − 2"), con un ejercicio de **números complejos** y un ítem de **multiple
    choice justificado**.
  - **Vigente (2025-1C, curso K3052):** **4 ejercicios en orden fijo — Ej1 Fourier, Ej2
    Laplace, Ej3 Sistemas estables, Ej4 Transformada Z —**, cada ítem a/b/c vale 1 punto
    (10 ítems), se aprueba con 6, **sin ejercicio de complejos**. Es el formato que se asume
    para el 2026-10-06.
- **Nombres:** `AAAA-MM-DD_…` cuando la fecha exacta es visible; `AAAA-1C_…` / `AAAA-2C_…`
  cuando solo se conoce el cuatrimestre; `sin-fecha…` cuando no hay nada. Sufijo `-T1`/`-T2`
  = tema; `_resuelto` = hoja de alumno o de cátedra con la resolución en el mismo archivo;
  `_respuestas` = hoja de respuestas oficial separada.
- **Materia con nombres viejos:** "Matemática Superior" (plan 2008) y "Modelos Numéricos"
  (K3012, 2015) son la misma materia; el temario del 1P no cambió.

## Leyenda de tags

**Series de Fourier:** `#SerieTrigonometrica` `#SerieExponencial` `#CompletarFuncion`
`#SimetriaMediaOnda` `#ValorMedio` `#Espectro` `#SumaSerieNumerica` `#Fasores`

**Transformada de Laplace:** `#TransformadaLaplace` `#IntegralPorLaplace`
`#Antitransformada` `#Convolucion` `#EcuacionIntegral` `#SistemaEDO`

**Sistemas estables:** `#Estabilidad` `#PolosCeros` `#CorteEje` `#RespuestaTemporal`
`#TipoRespuesta` `#ModuloGrafico` `#FuncionTransferencia`

**Transformada Z:** `#TransformadaZ` `#ROC` `#AntitransformadaZ` `#EcuacionDiferencia`
`#SumaSeriePorZ` `#SecuenciaFinita`

**Números complejos:** `#Complejos` `#PotenciasRaices` `#LogaritmoComplejo`
`#ConjuntosComplejos`

**Forma de la consigna:** `#MultipleChoice` `#VoF` `#Demostracion`

> Convención: cada ejercicio es una línea `- **EjN)** enunciado … → #Tag #Tag`; los ítems
> a/b/c van dentro de la misma línea. `«≈»` marca un detalle aproximado (escaneo borroso o
> fórmula reconstruida desde la hoja de respuestas oficial). `[RECICLADO]` marca un ítem que
> ya apareció, casi textual, en otra hoja. `(MC)` = multiple choice con justificación; la
> opción marcada como correcta por el docente se anota entre corchetes cuando se ve.

---

## 2015-05-29 · Tema 1 · `resueltos/2015-05-29_Parcial-T1_resuelto.pdf` (escaneo, "Modelos Numéricos" K3012, resuelto por alumno, nota 10; 4 ejercicios, nota = ítems correctos − 2)

- **Ej1)** `f(x) = 4` si `0 < x < 2`, `k` si `−2 < x < 0`, `f(x) = f(x+4)`. a) Indicar, si es posible, un valor de `k` para que la serie trigonométrica de Fourier **no tenga términos con cosenos** y su **valor medio sea 3**; justificar. b) Con `k = −4`, desarrollar `f(x)` en serie exponencial de Fourier. → #CompletarFuncion #ValorMedio #SerieExponencial #SerieTrigonometrica **[RECICLADO]**
- **Ej2)** (MC, cuatro ítems): i) `∫₀^∞ tⁿ e^{−2t} dt` vale `(n+1)!/2^{n+1}` / `(n+1)!/2ⁿ` / `n!/2^{n+1}` / n.a. [c]. ii) La ecuación `zⁿ = 1` tiene dos raíces imaginarias puras siempre que `n` sea par / múltiplo de 4 / múltiplo de 8 / n.a. [b y c]. iii) El valor principal de `z = j^{2j}` es `e^π` / `e^{−π}` / `1` / `−1` [b]. iv) La amplitud de `f(t) = cos(4t + π/2) + 2cos(4t − π/2)` es `√5` / `3` / `1` / n.a. [c]. → #MultipleChoice #IntegralPorLaplace #PotenciasRaices #LogaritmoComplejo #Fasores
- **Ej3)** `G(s) = K(s² − 2s − 3) / ((s − 3)(s + 2)(s² + 4))`. a) Indicar si el sistema es estable y dibujar en forma aproximada la respuesta en frecuencia de `G(s)` (corte por el eje imaginario). b) Hallar `K ∈ ℝ` sabiendo que `|G(j)| = √(2/5)`. c) Con `K = 8`, hallar la respuesta `y(t)` a la entrada `f(t) = e^{−t}` (`t > 0`). → #Estabilidad #CorteEje #ModuloGrafico #RespuestaTemporal
- **Ej4)** Resolver por transformada Z: `x(n+1) + 3x(n) = 5·2ⁿ`, `x(0) = 2`. Verificar hallando `x(3)` con la ecuación en diferencias y con la solución. → #EcuacionDiferencia

## 2015-05-29 · Tema 2 · `resueltos/2015-05-29_Parcial-T2_resuelto.pdf` (foto, K3012, resuelto por alumno, nota 9)

- **Ej1)** `f(t) = 2t` si `0 < t < 2`, `k(t)` si `−2 < t < 0`, `f(t) = f(t+4)`. a) Hallar `k(t)` para que la serie trigonométrica de Fourier tenga términos con cosenos (solo). b) Desarrollar `f(t)` en serie exponencial de Fourier. → #CompletarFuncion #SerieExponencial #SerieTrigonometrica
- **Ej2)** (MC): i) El desarrollo en STF de `f(x) = cos³(x)` tiene solo dos términos y valor medio nulo / dos términos y valor medio no nulo / infinitos términos / un solo término [a]. ii) `L(aᵗ)` es `1/(s−a)` / `1/(s−eᵃ)` / `1/(s − ln a)` / n.a. [c]. iii) `∫₀^∞ (sen t / t) e^{−√3 t} dt` es `0` / `π/2` / `π/4` / `π/6` [d]. iv) El valor principal de `z = jʲ` es real positivo / real negativo / imaginario puro / n.a. [a]. → #MultipleChoice #SerieTrigonometrica #TransformadaLaplace #IntegralPorLaplace #LogaritmoComplejo
- **Ej3)** `G(s) = 25(s² − Ks + 12) / ((s² + 4s + 5)(s² − 3s))`. a) Hallar `K ∈ ℝ` sabiendo que el sistema es estable y graficar aproximadamente el corte de `|G(s)|` por el eje real. b) Respuesta del sistema a una entrada impulso unitario. → #Estabilidad #CorteEje #RespuestaTemporal
- **Ej4)** Resolver por transformada Z: `x(n+1) = 3x(n) + 2`, `x(0) = 2`. Verificar con `x(2)`. → #EcuacionDiferencia

## sin fecha (≈2015) · Tema 1 · `resueltos/sin-fecha-2_Parcial-T1_resuelto.pdf` (escaneo, "Matemática Superior", resuelto por alumna, nota 10; 5 ejercicios, "nota = X − 2") · ⚠ sin fecha visible; el archivo tiene fecha de modificación 2015-06-02, igual que las fotos del 2015-05-29, y el formato de 5 ejercicios con MC es el de esa época → probablemente 1er cuatrimestre 2015, otro curso

- **Ej1)** (MC, tres ítems): a) Si `f(t) = 2ᵗ e^{−4t}`, `L[f(t)]` es `1/ln(2s+4)` / `1/(s − ln2 + 4)` / `1/(s − ln2) · 1/(s+4)` / otra [b]. b) La superposición de dos ondas senoidales de igual frecuencia y distinta amplitud **puede** ser: de distinta frecuencia / de amplitud igual a la suma de ambas / una función no senoidal / n.a. [b]. c) Para que `G(s) = (s² − ks + 12) / ((s² + 8s + 25)(s − 2))` sea estable: `k = 0` / `k = 8` / cualquier `k` / no existe `k` [b]. → #MultipleChoice #TransformadaLaplace #Fasores #Estabilidad
- **Ej2)** Resolver por Laplace: `y(t) + 2∫₀ᵗ cos(t−u) y(u) du = e^{−t}`. → #EcuacionIntegral #Convolucion #Antitransformada
- **Ej3)** `f(x) = 4` si `0 ≤ x ≤ 2`, `k` si `−2 ≤ x ≤ 0`, `f(x) = f(x+4)`. Indicar, si es posible, un valor de `k` para que la STF no tenga términos con cosenos y su valor medio sea 3; justificar. Con `k = 0`, desarrollar `f(x)` en serie exponencial de Fourier. → #CompletarFuncion #ValorMedio #SerieExponencial **[RECICLADO]**
- **Ej4)** Hallar la antitransformada Z de `X(z) = z(2z + 3) / (z² − 7z + 6)`. → #AntitransformadaZ
- **Ej5)** Hallar los valores de `k` reales tales que el logaritmo natural del complejo `z = ((k+1) + 2kj)/5` sea imaginario puro. → #LogaritmoComplejo #Complejos

## sin fecha (≈2015) · Tema 2 · `resueltos/sin-fecha-2_Parcial-T2_resuelto.pdf` (escaneo, "Matemática Superior", resuelto por alumno, nota 6)

- **Ej1)** (MC): a) El logaritmo complejo de un número real negativo tiene siempre: la misma parte real / el mismo módulo / la misma parte imaginaria / n.a. [c, corregido a "la misma parte imaginaria `π + 2kπ`"]. b) Los valores de `k ∈ ℝ` para que `G(s) = (s³ − 3s² − 4s) / ((s − 4)(s − k)(s² + 8s + 17))` sea estable son: `∀k` / solo `k ≥ 0` / solo `k ≤ 0` / no existen / n.a. [c]. c) La señal `f(x) = x² sen(x)` en `[−1, 1)`, `f(x) = f(x+2)`, tiene los coeficientes de su SEF: todos reales / todos imaginarios puros / uno real y el resto imaginarios / solo los impares no nulos / n.a. [b]. → #MultipleChoice #LogaritmoComplejo #Estabilidad #SerieExponencial
- **Ej2)** Resolver por Laplace: `y(t) = e^{−t} + 2∫₀ᵗ y(u) cos(t−u) du`. → #EcuacionIntegral #Convolucion #Antitransformada
- **Ej3)** `f(x) = x + 1` en `(0, 1)`. a) Completar `f(x)` con período `T = 2` para que la STF sea solo de senos y desarrollarla. b) ¿La función completada tiene simetría de media onda? Justificar. → #CompletarFuncion #SerieTrigonometrica #SimetriaMediaOnda
- **Ej4)** Hallar la transformada Z de la secuencia finita del gráfico: `x(1) = 1, x(2) = 3, x(3) = 2, x(4) = 1` (cero en el resto). → #SecuenciaFinita #TransformadaZ **[RECICLADO]**
- **Ej5)** Hallar en forma analítica y gráfica `A = {z ∈ ℂ : |z|² + Re(z²) ≤ 16}`, `B = {z ∈ ℂ : z² + (3 + j)z − 10 + 5j = 0}` y `A ∩ B`. → #ConjuntosComplejos #PotenciasRaices

## sin fecha ("15/10", curso K3521) · Tema 1 · `resueltos/sin-fecha_Parcial-K3521-T1_resuelto.pdf` (foto, "Matemática Superior", resuelto por alumno, nota 9; 5 ejercicios con puntaje fraccionado) · ⚠ el Tema 2 lleva "15/10" escrito a mano; el curso K3521 es el mismo del 2022-10-11, pero es otro examen. Un martes 15/10 → 2019 o 2024; el formato viejo (MC + complejos, tabla de puntos 1/1/1,5…) apunta a **≈2019-10-15**

- **Ej1)** a) Hallar `n ∈ ℕ` tal que `(1 − 2j)ⁿ = 117 − 44j` (justificar cómo se halla). b) Resolver en ℂ: `z⁴ + 16 = 0 ∧ |z + 1 − j| ≤ 1`. → #PotenciasRaices #ConjuntosComplejos
- **Ej2)** (MC) `∫₀^∞ t cos(3t) e^{−5t} dt =` `4/289` / `5/34` / `5/1156` / `∞` / n.a. (justificar con Laplace) [a]. → #IntegralPorLaplace #MultipleChoice
- **Ej3)** `f(t) = |t|` si `−1 < t < 1`, `k` si `1 < |t| < 2`, `f(t) = f(t+4)`. a) Indicar `k ∈ ℝ` para que el valor medio de la señal sea 1; justificar. b) Para `k = 0`, desarrollar en STF. → #ValorMedio #SerieTrigonometrica #CompletarFuncion
- **Ej4)** `G(s) = (41(s³ + s²) + 87s + 87) / (s(s + 3)(s² + 10s + 29))`. a) Indicar si el sistema es estable; justificar. b) Graficar aproximadamente el corte de `|G(s)|` por el eje real. c) Hallar la respuesta del sistema a la entrada impulso `δ(t)`. → #Estabilidad #PolosCeros #CorteEje #RespuestaTemporal
- **Ej5)** Transformada Z de `x(n) = (−3)ⁿ` si `n` es par, `5·2ⁿ` si `n` es impar, indicando la región de convergencia. → #TransformadaZ #ROC **[RECICLADO]**

## sin fecha ("15/10", curso K3521) · Tema 2 · `resueltos/sin-fecha_Parcial-K3521-T2_resuelto.pdf` (foto, resuelto por alumno, nota 6)

- **Ej1)** a) Hallar `n ∈ ℕ` tal que `(1 + 2j)ⁿ = 41 − 38j`. b) Resolver en ℂ: `z² = 2·z̄`. → #PotenciasRaices #Complejos
- **Ej2)** (MC) `∫₀^∞ (e^{−5t} − e^{−10t}) / t dt =` `ln 2` / `ln 5` / `∞` / n.a. (justificar con Laplace) [a]. → #IntegralPorLaplace #MultipleChoice **[RECICLADO]**
- **Ej3)** `f(x) = 3x` en `(0, 2)`. a) Completar la función para que la STF sea de cosenos y desarrollar; usar el resultado para hallar los `Cₙ` de la SEF sin resolver la integral. b) ¿La función definida en a) tiene simetría de media onda? Justificar. → #CompletarFuncion #SerieTrigonometrica #SerieExponencial #SimetriaMediaOnda
- **Ej4)** `G(s) = 10(s² − 4s + k) / (s³ + 5s² + 4s − 10)`. a) Hallar `K` para que `G(s)` sea estable. b) Respuesta temporal a una entrada escalón unitario `E(t)`. c) Indicar el tipo de respuesta (oscilatoria o no, amortiguada o no) y el valor estable. → #Estabilidad #RespuestaTemporal #TipoRespuesta **[RECICLADO]**
- **Ej5)** Resolver por transformada Z: `x(n+1) − 4x(n) = 4(1 − n)·2ⁿ`, `x(0) = 3`. → #EcuacionDiferencia **[RECICLADO]**

## 2022-10-11 · `resueltos/2022-10-11_Parcial_resuelto.pdf` (enunciados tipeados + resolución de cátedra fechada 2022-10-14, curso K3521; 5 ejercicios)

- **Ej1)** `f(t) = t + 2` si `t ∈ (0, 2)`, `f(t) = f(t+4)`. 1) Completar la función en todo el eje real para que su STF sea solo de cosenos y desarrollarla. 2) Con ese desarrollo hallar los `Cₙ` de la SEF. 3) Con el resultado anterior hallar el valor al que converge `Σ_{k=0}^∞ 1/(2k+1)²`. → #CompletarFuncion #SerieTrigonometrica #SerieExponencial #SumaSerieNumerica **[RECICLADO]**
- **Ej2)** Resolver por Laplace la ecuación integral `y(t) − ∫₀ᵗ y(u) sen(t−u) du = t⁴`. → #EcuacionIntegral #Convolucion #Antitransformada **[RECICLADO]**
- **Ej3)** Dados `A = {z ∈ ℂ : z³ + (2 − 2j)z² + z(3 + 2j) = 0}`, `B = {valor principal de ln(z) : z = j^{1−3j}}`, `C = {z ∈ ℂ : |(z + 3 − 2j)/(1 + 3j)| > 1}`, hallar los elementos de `A`, `B`, `C` y `(A ∪ B) ∩ C`. → #ConjuntosComplejos #PotenciasRaices #LogaritmoComplejo
- **Ej4)** Resolver por transformada Z: `2x(n+2) − x(n+1) = 3x(n) − 1`, `x(0) = 0`, `x(1) = 1`. → #EcuacionDiferencia **[RECICLADO]**
- **Ej5)** `G(s) = 17(s² + s − k) / ((s − 2)(s² + 8s + 17))`. a) Hallar `k` para que sea estable. Sabiendo que la entrada `f(t)` es un escalón unitario: b) dibujar un corte por el eje real de `Y(s)`; c) hallar la respuesta temporal `y(t)`. → #Estabilidad #CorteEje #RespuestaTemporal

## 2024-1C · Tema 1 · `resueltos/2024-1C_Parcial-T1_resuelto.pdf` (enunciados tipeados + resolución de cátedra fechada 2024-05-20; 5 ejercicios) · fecha exacta del examen no visible (≈ mediados de mayo de 2024)

- **Ej1)** `f(t) = t + 2` si `t ∈ (0, 2)`, `f(t) = f(t+4)`. a) Completar en todo el eje real para que su STF sea solo de cosenos y desarrollarla. b) Usando la función del ítem a), completar analítica y gráficamente en el intervalo `(−8, 8)` para que tenga simetría de media onda. c) Con el resultado de a), hallar el valor al que converge `Σ_{k=0}^∞ 1/(2k+1)²`. → #CompletarFuncion #SerieTrigonometrica #SimetriaMediaOnda #SumaSerieNumerica **[RECICLADO]**
- **Ej2)** Resolver por Laplace: `y(t) − ∫₀ᵗ y(u) sen(t−u) du = t⁴`. → #EcuacionIntegral #Convolucion #Antitransformada **[RECICLADO]**
- **Ej3)** `A = {z ∈ ℂ : |z|² + 6z̄ = −6·Im(z)·j}`, `B = {z ∈ ℂ : z³ + 2z² − 6z + 4z²j = 0}`. a) Dibujar ambos conjuntos en un mismo gráfico. b) Hallar `A ∩ B`. → #ConjuntosComplejos #PotenciasRaices
- **Ej4)** Resolver por transformada Z: `2x(n+2) − x(n+1) = 3x(n) − 1`, `x(0) = 0`, `x(1) = 1`. → #EcuacionDiferencia **[RECICLADO]**
- **Ej5)** `G(s) = k(s² − s − 2) / ((s − 2)(s² + 10s + 26))`. a) Hallar la constelación de polos y ceros de `G(s)`. b) Hallar `k` para que `G(0) = 2`. c) Sabiendo que la entrada `f(t)` es un escalón unitario `E(t)`, dibujar un corte por el eje real de `Y(s)`. d) Hallar la respuesta temporal `y(t)` y clasificarla (oscilatoria o exponencial, amortiguada o creciente); hallar, si existe, el valor estable. → #PolosCeros #Estabilidad #CorteEje #RespuestaTemporal #TipoRespuesta

## 2024-1C · Tema 2 · `resueltos/2024-1C_Parcial-T2_resuelto.pdf` (enunciados tipeados + resolución de cátedra fechada 2024-05-20)

- **Ej1)** `f(t) = t²`, `t ∈ (0, 2)`. a) Completar la función para que la STF sea solo de cosenos y desarrollarla. b) Con el resultado de a) hallar el valor al que converge `Σ_{n=1}^∞ (−1)ⁿ/n²`. c) Dada `f(t) = t²` en `(0, 2)`, completarla analítica y gráficamente para que sea impar y tenga simetría de media onda. → #CompletarFuncion #SerieTrigonometrica #SumaSerieNumerica #SimetriaMediaOnda
- **Ej2)** Resolver por Laplace: `y(t) − 2∫₀ᵗ y(u) cos(t−u) du = 1`. → #EcuacionIntegral #Convolucion #Antitransformada **[RECICLADO]**
- **Ej3)** `A = {z ∈ ℂ : |z|² + 4z̄ = 33/4 − 4·Im(z)·j}`, `B = {z ∈ ℂ : raíz de índice (11/z) de (√3/2 − j/2) = √2/2 + (√2/2)j}` (usar siempre valor principal). a) Dibujar ambos conjuntos en un mismo gráfico. b) Hallar `A ∩ B`. → #ConjuntosComplejos #LogaritmoComplejo
- **Ej4)** `G(s) = 5(s² − ks − 2) / ((s² + s − 6)(s² + 2s + 2))`. a) Hallar `k` para que el sistema sea estable. b) Con ese `k`, respuesta temporal a una entrada `f(t) = δ(t)`. c) Decir si es verdadera o falsa: `|G(2 + j)| = 5√5/39` (usar el método gráfico). → #Estabilidad #RespuestaTemporal #ModuloGrafico #VoF **[RECICLADO]**
- **Ej5)** Resolver la ecuación en diferencias `x(n+2) − 4x(n) = 3ⁿ`, `x(0) = 1`, `x(1) = 2`. → #EcuacionDiferencia

## 2024-2C · Tema 1 · `2024-2C_Parcial.docx` (tipeado, curso K3573; 5 ejercicios de 2 puntos; respuestas oficiales en `resueltos/2024-2C_Parcial_respuestas.docx`) · ⚠ varias fórmulas están incrustadas como objetos MathType que no se pudieron renderizar; los enunciados marcados «≈» se reconstruyeron desde la hoja de respuestas oficial

- **Ej1)** Dado `z = [√2, 7π/4]¹⁰ / [2, π/6]⁵` «≈». a) Hallar `z` en forma polar y binómica e indicar en qué cuadrante está. b) Hallar el valor principal de `ln(z)`. → #PotenciasRaices #LogaritmoComplejo
- **Ej2)** Completar gráfica y analíticamente `f(t)` para que los coeficientes `Cₙ` de su SEF sean imaginarios puros, con `f(t) = t` en `0 < t < π` «≈» y `f(t) = f(t + 2π)`. Hallar la STF y la SEF. → #CompletarFuncion #SerieTrigonometrica #SerieExponencial
- **Ej3)** a) Resolver una ecuación integro-diferencial [enunciado no extraíble del .docx; la respuesta oficial es `Y(s) = (s−2)(s+1)/(s(s−1)²)`, `y(t) = −2 − 2te^t + 3e^t`]. b) Resolver `∫₀^∞ sen(t)/t dt`. → #EcuacionIntegral #IntegralPorLaplace #Antitransformada
- **Ej4)** `G(s) = 10(s² − 4s + k) / (s³ + 5s² + 4s − 10)` «≈» (la respuesta oficial es `k = 3` y `G(s) = 10(s−3)/(s² + 6s + 10)`). a) Hallar `K` para que sea estable. b) Con ese `k`, respuesta temporal a una entrada escalón `E(t)`. c) Indicar el tipo de respuesta (no si es estable, sino el tipo). → #Estabilidad #RespuestaTemporal #TipoRespuesta **[RECICLADO]**
- **Ej5)** a) Transformada Z y región de convergencia de `x(n) = 3^{−n}` si `n` es par, `5·2ⁿ` si `n` es impar «≈» (reconstruida de `X(z) = 9z²/(9z²−1) + 10z/(z²−4)`, ROC `|z| > 2`). b) Resolver `Σ_{n=0}^∞ n·2^{−n}` (respuesta: 2). → #TransformadaZ #ROC #SumaSeriePorZ **[RECICLADO]**

## 2024-2C · Tema 2 · `2024-2C_Parcial.docx` (tipeado, K3573)

- **Ej1)** Indicar el conjunto solución de `A = {z ∈ ℂ : z² − (3 + j)z + 4 + 3j = 0 ∧ |z − 1| < 2}` «≈» (respuesta: raíces `2 − j` y `1 + 2j`; solo `2 − j` cumple). → #ConjuntosComplejos #PotenciasRaices
- **Ej2)** `f(x) = 4` si `0 < x < 2`, `k` si `−2 < x < 0`, `f(x) = f(x+4)` «≈». a) Indicar, si es posible, un valor de `k` para que los `Cₙ` de la SEF sean todos imaginarios puros excepto `C₀`, que debe valer 3; justificar. b) Con `k = −4`, desarrollar `f(x)` en SEF y STF. → #CompletarFuncion #ValorMedio #SerieExponencial #SerieTrigonometrica **[RECICLADO]**
- **Ej3)** a) Resolver la ecuación integro-diferencial `y'(t) − 2y(t) = 2 − [término no extraíble ≈ 2∫₀ᵗ u·eᵘ du]`, `y(0) = 0` (respuesta oficial `Y(s) = 2/(s−1)²`, `y(t) = 2te^t`). b) Resolver `∫_{−∞}^{∞} sen(t)/t dt`. → #EcuacionIntegral #IntegralPorLaplace #Antitransformada
- **Ej4)** `G(s) = 5(s² − ks − 2) / ((s² + s − 6)(s² + 2s + 2))`. a) Hallar `k`, si existe, para que el sistema sea estable. b) Con ese `k`, respuesta temporal a una entrada `f(t) = e^{−t}` «≈» (reconstruida de `Y(s) = 5/((s²+2s+2)(s+3))`). c) Hallar el corte por el eje real de `|Y(s)|`. → #Estabilidad #RespuestaTemporal #CorteEje **[RECICLADO]**
- **Ej5)** a) Transformada Z y región de convergencia de `x(n) = (−2)ⁿ` si `n` es par, `4ⁿ` si `n` es impar. b) Resolver `Σ_{n=0}^∞ n²·4^{−n}` (respuesta: `20/27`). → #TransformadaZ #ROC #SumaSeriePorZ **[RECICLADO]**

## 2024-2C · 1er recuperatorio (≈ diciembre 2024) · `2024-2C_Recuperatorio.docx` (tipeado, K3573; 5 ejercicios de 2 puntos; respuestas en `resueltos/2024-2C_Recuperatorio_respuestas.docx`)

- **Ej1)** ¿Cuántos elementos contiene `A = {z ∈ ℂ : |z|² − Re(z²) ≤ 200 ∧ z = ln(4 − 4j)}`? (respuesta: 3). → #LogaritmoComplejo #ConjuntosComplejos
- **Ej2)** Hallar la SEF de `f(t) = 1` en `(−π/5, π/5)` y `0` en `(−π, −π/5) ∪ (π/5, π)`. Dibujar el espectro de `Cₙ`. → #SerieExponencial #Espectro
- **Ej3)** a) Transformada de Laplace de `y(t) = cos³(t)`, `t > 0`. b) Antitransformar `Y(s) = 1/(s² + 1)²`. → #TransformadaLaplace #Antitransformada #Convolucion **[RECICLADO]**
- **Ej4)** `G(s) = 34(s³ − 3s² − as) / ((s − 5)(s + b)(s² + 8s + 17))`. a) Indicar todos los valores de `a, b ∈ ℝ` para los que el sistema es estable; justificar. b) Con el `a` hallado y `b = 0`, respuesta temporal al escalón `E(t)`. → #Estabilidad #RespuestaTemporal
- **Ej5)** Resolver por transformada Z `x(n+1) = 2x(n) + 3n − 1`, `x(0) = 0`. Comprobar hallando `x(2)` con la solución y con la ecuación en diferencias. → #EcuacionDiferencia

## 2025-02-13 · 2do recuperatorio del 1P (del 2C 2024) · `resueltos/2025-02-13_Recuperatorio_resuelto.pdf` (fotos, "Matemática Superior", docente L. Garofalo, resuelto por alumna, nota 3; 5 ejercicios)

- **Ej1)** a) Hallar los `z` complejos que verifican `z² + z^{−2} = 1`. b) Dada una ecuación polinómica de grado 5 con todos sus coeficientes reales, ¿todas sus raíces son complejas? Verdadero o falso, justificar. → #PotenciasRaices #Complejos #VoF
- **Ej2)** a) `f(x) = x` en `[0, 2]`, `f(x) = f(x+4)`. Completar en forma gráfica y analítica para que: 1) tenga simetría de media onda; 2) la SEF tenga todos los coeficientes reales. b) Señal `f(t) = 4` si `0 < t < 2`, `3` si `2 < t < 4`, `2` si `4 < t < 6`, `f(t) = f(t+6)`: I) hallar el valor medio; ¿tiene SMO? Si no, justificar. II) ¿Qué coeficientes tiene el desarrollo en STF? → #CompletarFuncion #SimetriaMediaOnda #SerieExponencial #ValorMedio #SerieTrigonometrica
- **Ej3)** Resolver por Laplace el sistema `x'(t) = 2x(t) − 3y(t)`, `−2y'(t) = −2y(t) + 4x(t)`, con `x(0) = 8`, `y(0) = 3`. → #SistemaEDO #Antitransformada
- **Ej4)** `G(s) = 20(s² − ks + 4) / ((s³ + 7s² + 19s + 13)(s − 4))` es la transferencia de un sistema estable. Hallar la respuesta a la entrada `e(t) = eᵗ(1 + 2t)`. → #Estabilidad #RespuestaTemporal
- **Ej5)** Resolver por transformada Z: `x(n) = 4ⁿ` si `n` es par, `3^{−n}` si `n` es impar. Determinar el radio de convergencia. → #TransformadaZ #ROC **[RECICLADO]**

## 2025-1C · Tema 1 · `2025-1C_Parcial.pdf` (tipeado, curso K3052; **formato vigente: 4 ejercicios, ítems de 1 punto**; respuestas oficiales en `resueltos/2025-1C_Parcial_respuestas.pdf`, cuya hoja OneNote está fechada **2025-05-02**, probable fecha del examen) · el enunciado no trae fecha

- **Ej1)** `f(t) = π − t` si `0 < t < π`. a) Completar en todo el eje real para que la SEF tenga solamente coeficientes reales; desarrollar la STF. b) Justificar: la STF de `f(x) = 2sen(x)cos(x)` es: la misma función / una serie con infinitos términos no nulos en senos / un solo término no nulo / infinitos términos en cosenos. c) `f(t) = t` si `0 < t < 1`: completar en forma gráfica y analítica para que la SEF tenga coeficientes imaginarios puros y además `f(t)` tenga simetría de media onda. → #CompletarFuncion #SerieTrigonometrica #SerieExponencial #SimetriaMediaOnda #MultipleChoice
- **Ej2)** a) Resolver con Laplace: `∫₀^∞ t·e^{−5t}·cos(t) dt`. b) Antitransformar `Y(s) = 1/(s² + 1)²`. c) Demostrar que `L(2ᵗ) = 1/(s − ln 2)`. → #IntegralPorLaplace #Antitransformada #Convolucion #Demostracion **[RECICLADO]**
- **Ej3)** Ecuación diferencial `f(t) − K·y(t) − B·y'(t) = M·y''(t)` del sistema mecánico de traslación (masa `M = 1`, amortiguador `B = 2`, resorte `K = 2`). a) Hallar la función de transferencia `G(s)` sabiendo que `y(0) = 0` y parte del reposo. b) Hallar la respuesta del sistema si la entrada es `f(t) = −e^{−t}`. → #FuncionTransferencia #RespuestaTemporal
- **Ej4)** a) Transformada Z y región de convergencia de `x(n) = (−2)ⁿ` si `n` es par, `4^{−n}` si `n` es impar. b) Resolver mediante Z: `Σ_{n=0}^∞ (3ⁿ/n!)·2^{−n}`. → #TransformadaZ #ROC #SumaSeriePorZ **[RECICLADO]**

## 2025-1C · Tema 2 · `2025-1C_Parcial.pdf` (tipeado, K3052)

- **Ej1)** `f(t) = −π − t` si `−π < t < 0`. a) Completar en todo el eje real para que la SEF tenga solamente coeficientes imaginarios puros; desarrollar la STF. b) (mismo ítem que T1: STF de `2sen(x)cos(x)`). c) `f(t) = t` si `0 < t < 1`: completar para que la SEF tenga coeficientes reales y además simetría de media onda. → #CompletarFuncion #SerieTrigonometrica #SerieExponencial #SimetriaMediaOnda #MultipleChoice
- **Ej2)** a) Transformada de Laplace de `sen³(t)`, `t > 0`. b) Antitransformar utilizando convolución: `Y(s) = s²/(s² + 1)²`. → #TransformadaLaplace #Antitransformada #Convolucion **[RECICLADO]**
- **Ej3)** `G(s) = 10(s² − 4s + k) / (s³ + 5s² + 4s − 10)`. a) Hallar `K` para que sea estable. b) Con ese `k`, respuesta temporal a una entrada escalón unitario `E(t)`. c) Indicar el tipo de respuesta (no confundir con estabilidad) y el valor estable. → #Estabilidad #RespuestaTemporal #TipoRespuesta **[RECICLADO]**
- **Ej4)** a) Resolver mediante Z: `Σ_{n=0}^∞ cos(πn)·3^{−n}`. b) Resolver la ecuación en diferencias `x(n+1) − 4x(n) = 4(1 − n)·2ⁿ`, `x(0) = 3`; verificar con `x(2)`. → #SumaSeriePorZ #EcuacionDiferencia **[RECICLADO]**

## 2025-1C · 1er recuperatorio · `2025-1C_Recuperatorio.pdf` (tipeado, K3052, formato de 4 ejercicios; respuestas en `resueltos/2025-1C_Recuperatorio_respuestas.pdf`, hoja OneNote fechada **2025-06-23**, probable fecha del examen)

- **Ej1)** `f(x) = 2x` en `(0, 2)`. a) Completar para que la STF sea de senos y desarrollar. b) Con ese resultado calcular los `Cₙ` de la SEF. c) Graficar el espectro de amplitudes (`|Cₙ|` vs. `ω₀·n`). → #CompletarFuncion #SerieTrigonometrica #SerieExponencial #Espectro
- **Ej2)** a) Calcular `∫₀^∞ (e^{−5t} − e^{−10t}) / t dt`. b) Resolver `L[∫₀ᵗ u·cos(u)·e^{t−u} du]`. → #IntegralPorLaplace #Convolucion #TransformadaLaplace **[RECICLADO]**
- **Ej3)** `G(s) = 2(s² + 2s − 3) / ((s − 1)(s + 2)(s² + 8s + 17))`. a) Indicar los polos y ceros de `G(s)` y si representa un sistema estable o no. b) Graficar un corte por el eje real de `|G(s)|`. c) Hallar la respuesta `y(t)` sabiendo que la entrada es `f(t) = e^{−3t}`. → #PolosCeros #Estabilidad #CorteEje #RespuestaTemporal
- **Ej4)** a) Verdadero o falso (justificar): la región de convergencia de la transformada Z de `x(n) = (−2)ⁿ` si `n` es par, `4^{−n}` si `n` es impar, es `|z| > 2`. b) Dada la secuencia finita del gráfico (`x(1) = 1, x(2) = 3, x(3) = 2, x(4) = 1`), hallar su transformada Z. → #ROC #VoF #SecuenciaFinita #TransformadaZ **[RECICLADO]**

---

## Índice inverso: tema → hojas (para búsqueda rápida)

Nombres cortos: `2015-T1/T2`, `sf2-T1/T2` (sin-fecha-2, ≈2015), `sfK-T1/T2` (sin-fecha K3521, ≈2019), `2022`, `2024-1C-T1/T2`, `2024-2C-T1/T2`, `2024-2C-rec`, `2025-02-13`, `2025-1C-T1/T2`, `2025-1C-rec`. Total: **16 hojas**.

| Tag | Aparece en | Hojas |
|---|---|---|
| `#CompletarFuncion` | 2015-T1, 2015-T2, sf2-T1, sf2-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2025-02-13, 2025-1C-T1, 2025-1C-T2, 2025-1C-rec | 15/16 |
| `#SerieTrigonometrica` | 2015-T1, 2015-T2, sf2-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2025-02-13, 2025-1C-T1, 2025-1C-T2, 2025-1C-rec (+ 2015-T2 y 2025-1C como MC) | 14/16 |
| `#SerieExponencial` | 2015-T1, 2015-T2, sf2-T1, sf2-T2, sfK-T2, 2022, 2024-2C-T1, 2024-2C-T2, 2024-2C-rec, 2025-02-13, 2025-1C-T1, 2025-1C-T2, 2025-1C-rec | 13/16 |
| `#Estabilidad` | 2015-T1, 2015-T2, sf2-T1, sf2-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2024-2C-rec, 2025-02-13, 2025-1C-T2, 2025-1C-rec | 15/16 |
| `#RespuestaTemporal` | 2015-T1, 2015-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2024-2C-rec, 2025-02-13, 2025-1C-T1, 2025-1C-T2, 2025-1C-rec | 14/16 |
| `#Antitransformada` | sf2-T1, sf2-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2024-2C-rec, 2025-02-13, 2025-1C-T1, 2025-1C-T2 (y, en la práctica, en toda respuesta temporal) | 11/16 |
| `#TransformadaZ` / `#ROC` | sf2-T2, sfK-T1, 2024-2C-T1, 2024-2C-T2, 2025-02-13, 2025-1C-T1, 2025-1C-rec | 7/16 |
| `#EcuacionDiferencia` | 2015-T1, 2015-T2, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-rec, 2025-1C-T2 | 8/16 |
| `#IntegralPorLaplace` | 2015-T1, 2015-T2, sfK-T1, sfK-T2, 2024-2C-T1, 2024-2C-T2, 2025-1C-T1, 2025-1C-rec | 8/16 |
| `#EcuacionIntegral` | sf2-T1, sf2-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2 | 7/16 |
| `#Convolucion` | sf2-T1, sf2-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-rec, 2025-1C-T1, 2025-1C-T2, 2025-1C-rec | 9/16 |
| `#CorteEje` | 2015-T1, 2015-T2, sfK-T1, 2022, 2024-1C-T1, 2024-2C-T2, 2025-1C-rec | 7/16 |
| `#TipoRespuesta` | sfK-T2, 2024-1C-T1, 2024-2C-T1, 2025-1C-T2 | 4/16 |
| `#PolosCeros` | sfK-T1, 2024-1C-T1, 2025-1C-rec | 3/16 |
| `#ModuloGrafico` | 2015-T1, 2024-1C-T2 | 2/16 |
| `#FuncionTransferencia` | 2025-1C-T1 | 1/16 |
| `#SistemaEDO` | 2025-02-13 | 1/16 |
| `#TransformadaLaplace` (calcular una transformada / propiedad) | 2015-T2, sf2-T1, 2024-2C-rec, 2025-1C-T2, 2025-1C-rec | 5/16 |
| `#SimetriaMediaOnda` | sf2-T2, sfK-T2, 2024-1C-T1, 2024-1C-T2, 2025-02-13, 2025-1C-T1, 2025-1C-T2 | 7/16 |
| `#ValorMedio` | 2015-T1, sf2-T1, sfK-T1, 2024-2C-T2, 2025-02-13 | 5/16 |
| `#SumaSerieNumerica` | 2022, 2024-1C-T1, 2024-1C-T2 | 3/16 |
| `#SumaSeriePorZ` | 2024-2C-T1, 2024-2C-T2, 2025-1C-T1, 2025-1C-T2 | 4/16 |
| `#SecuenciaFinita` | sf2-T2, 2025-1C-rec | 2/16 |
| `#AntitransformadaZ` (suelta) | sf2-T1 | 1/16 |
| `#Espectro` | 2024-2C-rec, 2025-1C-rec | 2/16 |
| `#Fasores` | 2015-T1, sf2-T1 | 2/16 |
| `#Complejos` (cualquier tag de complejos) | 2015-T1, 2015-T2, sf2-T1, sf2-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T1, 2024-2C-T2, 2024-2C-rec, 2025-02-13 — **0 en las 3 hojas de 2025-1C** | 13/16 |
| `#ConjuntosComplejos` | sf2-T2, sfK-T1, 2022, 2024-1C-T1, 2024-1C-T2, 2024-2C-T2, 2024-2C-rec | 7/16 |
| `#PotenciasRaices` | 2015-T1, sf2-T2, sfK-T1, sfK-T2, 2022, 2024-1C-T1, 2024-2C-T1, 2024-2C-T2, 2025-02-13 | 9/16 |
| `#LogaritmoComplejo` | 2015-T1, 2015-T2, sf2-T1, sf2-T2, 2022, 2024-1C-T2, 2024-2C-T1, 2024-2C-rec | 8/16 |
| `#MultipleChoice` | 2015-T1, 2015-T2, sf2-T1, sf2-T2, sfK-T1, sfK-T2, 2025-1C-T1, 2025-1C-T2 (solo el ítem 1b) | 8/16 |
| `#VoF` | 2024-1C-T2, 2025-02-13, 2025-1C-rec | 3/16 |
| `#Demostracion` | 2025-1C-T1 (demostrar `L(2ᵗ)`) | 1/16 |

## Problemas reciclados (idénticos o casi entre hojas)

- **`G(s) = 10(s² − 4s + k) / (s³ + 5s² + 4s − 10)`** → K estable (`k = 3`, cancela `(s − 1)`), respuesta al escalón, tipo de respuesta y valor estable: **sfK-T2 Ej4, 2024-2C-T1 Ej4 «≈», 2025-1C-T2 Ej3**. **(3 veces, textual)** Respuesta oficial: `y(t) = −3 + 3cos(t)e^{−3t} + 19sen(t)e^{−3t}`, oscilatoria amortiguada, valor estable `−3`.
- **`f(x) = 4` en `(0,2)`, `k` en `(−2,0)`, período 4 → `k` para que no haya cosenos (impar desplazada) y valor medio 3 (`k = 2`); con `k = −4` (o `k = 0`) desarrollar la SEF** → **2015-T1 Ej1, sf2-T1 Ej3, 2024-2C-T2 Ej2 «≈»**. **(3 veces)** Variante lineal: `f(t) = 2t` / `k(t)` (2015-T2 Ej1); variante `|t|`/`k` con valor medio 1 (sfK-T1 Ej3).
- **`f(t) = t + 2` en `(0,2)`, período 4 → completar solo cosenos, `Cₙ`, y usar la serie para sumar `Σ 1/(2k+1)² = π²/8`** → **2022 Ej1, 2024-1C-T1 Ej1** (esta última suma el ítem de SMO en `(−8,8)`). Variante `t²` con `Σ(−1)ⁿ/n² = −π²/12` (2024-1C-T2 Ej1).
- **Ecuación integral con convolución `y(t) − ∫₀ᵗ y(u) sen(t−u) du = t⁴`** → **2022 Ej2, 2024-1C-T1 Ej2** (textual). Familia con coseno: `y(t) − 2∫y(u)cos(t−u)du = 1` (2024-1C-T2 Ej2), `y(t) + 2∫cos(t−u)y(u)du = e^{−t}` (sf2-T1 Ej2), `y(t) = e^{−t} + 2∫y(u)cos(t−u)du` (sf2-T2 Ej2). **(5 hojas, misma receta)**
- **Ecuación en diferencias `2x(n+2) − x(n+1) = 3x(n) − 1`, `x(0)=0, x(1)=1`** → **2022 Ej4, 2024-1C-T1 Ej4** (textual; respuesta `x(n) = ½ − ½(−1)ⁿ`).
- **`x(n+1) − 4x(n) = 4(1 − n)·2ⁿ`, `x(0) = 3`** → **sfK-T2 Ej5, 2025-1C-T2 Ej4b** (textual; respuesta oficial `x(n) = 2n·2ⁿ + 3·4ⁿ`).
- **Sucesión definida por paridad de `n` → `X(z)` y ROC** (`(−3)ⁿ`/`5·2ⁿ` en sfK-T1; `3^{−n}`/`5·2ⁿ` «≈» y `(−2)ⁿ`/`4ⁿ` en 2024-2C; `(−2)ⁿ`/`4^{−n}` en 2025-1C-T1 y, como V/F, en 2025-1C-rec; `4ⁿ`/`3^{−n}` en 2025-02-13) → **6 hojas**. Es EL ítem de Z del formato vigente.
- **`∫₀^∞ (e^{−5t} − e^{−10t})/t dt = ln 2`** → **sfK-T2 Ej2, 2025-1C-rec Ej2a** (textual). Familia "integral impropia por Laplace": `∫ t cos(3t) e^{−5t}` (sfK-T1), `∫ t e^{−5t} cos(t)` (2025-1C-T1), `∫ tⁿ e^{−2t}` (2015-T1), `∫ sen(t)/t` (2024-2C-T1/T2, 2015-T2 con `e^{−√3 t}`).
- **Antitransformar `1/(s² + 1)²` (polo doble complejo / convolución)** → **2024-2C-rec Ej3b, 2025-1C-T1 Ej2b** (textual); variante `s²/(s²+1)²` por convolución (2025-1C-T2 Ej2b).
- **Secuencia finita del gráfico `x = (0, 1, 3, 2, 1)` → `X(z) = z^{−1} + 3z^{−2} + 2z^{−3} + z^{−4}`** → **sf2-T2 Ej4, 2025-1C-rec Ej4b** (mismo gráfico).
- **`G(s)` con factor `(s² + 8s + 17)` y un polo inestable a cancelar con el numerador** → sf2-T2 Ej1b, 2022 Ej5 (`17(s²+s−k)/((s−2)(s²+8s+17))`), 2024-2C-rec Ej4 (`34(s³−3s²−as)/((s−5)(s+b)(s²+8s+17))`), 2025-1C-rec Ej3 (`2(s²+2s−3)/((s−1)(s+2)(s²+8s+17))`). **(4 hojas, misma receta: elegir K para que el numerador se anule en el polo positivo)**
- **`G(s) = 5(s² − ks − 2) / ((s² + s − 6)(s² + 2s + 2))`** → **2024-1C-T2 Ej4, 2024-2C-T2 Ej4** (textual, `k = 1`).
- **`(s² − ks + 12)` como numerador con `k` a elegir** → sf2-T1 Ej1c (`/((s²+8s+25)(s−2))`, `k = 8`), 2015-T2 Ej3 (`25(s²−Ks+12)/((s²+4s+5)(s²−3s))`, `K = 7`).
- **`cos³(t)` / `sen³(t)` / `2sen(x)cos(x)`: reducir con identidades antes de transformar o desarrollar** → 2015-T2 Ej2i (STF de `cos³`), 2024-2C-rec Ej3a (`L(cos³ t)`), 2025-1C-T2 Ej2a (`L(sen³ t)`), 2025-1C Ej1b (STF de `2sen x cos x`).
- **Sumas numéricas vía Z evaluando `X(z)` en un punto** (`Σ n·2^{−n} = 2`, `Σ n²·4^{−n} = 20/27`, `Σ cos(πn)3^{−n} = 3/4`, `Σ (3ⁿ/n!)2^{−n} = e^{3/2}`) → 2024-2C-T1/T2 Ej5b, 2025-1C-T1 Ej4b, 2025-1C-T2 Ej4a. **(4 hojas, formato vigente)**
- **Completar `f(t) = t` (o `2x`, `x+1`, `3x`) en medio período para senos / cosenos / SMO / coeficientes reales o imaginarios** → sf2-T2 Ej3, sfK-T2 Ej3, 2025-02-13 Ej2a, 2025-1C-T1 Ej1c, 2025-1C-T2 Ej1c, 2025-1C-rec Ej1. **(6 hojas; el ítem c) del Ej1 vigente)**

## Equivalencias (mismo archivo o mismo examen, no practicar dos veces)

- `duplicados/2025-1C_Recuperatorio_respuestas_copia.pdf` ≡ `resueltos/2025-1C_Recuperatorio_respuestas.pdf` (idénticos byte a byte).
- `2024-2C_Parcial.docx` contiene Tema 1 y Tema 2 en el mismo archivo; `2025-1C_Parcial.pdf` ídem. Cada tema se cuenta como hoja aparte.
- `2024-1C_Parcial-T1/T2_resuelto.pdf` son las dos hojas de una misma fecha (mismo tipo de ítems).
- No hay dos hojas idénticas en el dataset; el reciclaje es a nivel de ejercicio (ver arriba).

## Fuera de dataset

- **`segundo-parcial/examenes/2025-1C_Parcial.pdf`, `2025-1C_Parcial_respuestas.pdf`, `2025-1C_Recuperatorio.pdf`, `2025-1C_Recuperatorio_respuestas.pdf`** — venían mezclados en esta carpeta pero son del **2do parcial** (raíces, sistemas lineales, interpolación y ajuste, integración, EDO). Movidos el 2026-09-10 a `../../segundo-parcial/examenes/`, sin indexar todavía.
- Los PDFs de la raíz de la materia (cronograma, links de clases virtuales, consigna del TP, hoja de fórmulas manuscrita, fracciones simples) se movieron a `fuentes/`.
- `resueltos/RESOLUCIONES-2025.md` — transcripción de los métodos y resultados de las respuestas oficiales 2025-1C (parcial + recuperatorio), para estudiar cómo resuelve la cátedra sin abrir los PDFs.

---

*Índice generado el 2026-09-10 a partir de la lectura (con visión) de 26 archivos originales: 7 PDFs escaneados, 16 fotos JPG/JPEG (unidas en 3 PDFs), 4 `.docx` (texto y ecuaciones OMML extraídos; los objetos MathType quedaron sin renderizar y se reconstruyeron «≈» desde las respuestas oficiales) y 4 PDFs tipeados. Los enunciados de fotos/escaneos pueden tener detalles menores aproximados.*
