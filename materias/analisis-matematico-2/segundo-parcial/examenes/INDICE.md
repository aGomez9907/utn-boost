# Índice de parciales — Segundo Parcial AM2

> **Para qué sirve:** los parciales son PDFs tipeados, PDFs escaneados y fotos (JPG/PNG). La mitad **no tiene capa de texto**, así que no se pueden `grep`ear directamente. Este archivo es la transcripción curada (matemática intacta) de cada examen, con **tags por tema**, para poder buscar sin re-leer las imágenes.
>
> **Cómo buscar** (desde esta carpeta, `examenes/`):
> ```bash
> grep -n "#EDO" INDICE.md              # todos los ítems de ecuaciones diferenciales
> grep -n "#Flujo" INDICE.md            # todos los flujos
> grep -B1 "#Conservativo" INDICE.md    # conservativos, con la línea de fecha arriba
> grep -n "^## " INDICE.md              # listar todos los exámenes por fecha
> ```
> **Mantenimiento:** cuando agregues un parcial nuevo, sumá su sección acá con los mismos tags (y actualizá la tabla tag→fechas del final). Si querés, corré la skill de lectura sobre la imagen y pegá el resultado con este formato.

## Leyenda de tags

`#Volumen` `#MasaCuerpo` `#Baricentro` `#AreaRegion` `#AreaSuperficie` `#LongitudCurva` `#Circulacion` `#Trabajo` `#Green` `#Conservativo` `#FuncionPotencial` `#Flujo` `#Divergencia` `#Rotor` `#Stokes` `#EDO` `#Superposicion` `#CambioVariables` `#MomentoInercia` `#Demostracion`

> Convención: cada problema es una línea `- **Pn)** enunciado … → #Tag #Tag`. Los teóricos son `**T1)** / **T2)**`. Los enunciados de exámenes **escaneados** pueden tener detalles menores aproximados (marcados con «≈»).

---

## 2014-11-28  ·  `2014-11-28_Parcial.pdf` (escaneo)

- **P1)** Volumen del cuerpo ≈ `√(x²+y²) ≤ z ≤ 8 − √(x²+y²)`. → #Volumen
- **P2)** Integral del campo `f(x,y) = (x², −9y)` desde `A=(2,1)` hasta `B=(1,2)` a lo largo de la curva `xy = 2`. → #Trabajo #Circulacion
- **P3)** Superficie `Σ` dada implícitamente; calcular el área del trozo de `Σ` tangente ≈ (región `x²+y² ≤ 2`). → #AreaSuperficie
- **P4)** Campo `f ∈ C¹`; calcular el flujo de `f` a través de la superficie **abierta** `z = 4 − x² − y²`, `z ≥ 0`, indicando orientación. → #Flujo
- **T1)** Enunciar el Teorema de Green. Calcular la circulación de `f = (2xy·e^{x²}, x²e^{x²}+e^{y})` a lo largo de la frontera de `x²+y² ≤ 9`, `x ≥ 0`. → #Green #Circulacion
- **T2)** Enunciar y **demostrar** la condición necesaria para que `f = (f₁,f₂)` admita función potencial. → #FuncionPotencial #Demostracion

## 2015-11-25  ·  `2015-11-25_Parcial.pdf` (escaneo)

- **P1)** Verificar si `f(x,y) = (2x+y²+1, 2xy)` admite función potencial; en caso afirmativo calcular el potencial `φ` con `φ(0,0)=2`. → #Conservativo #FuncionPotencial
- **P2)** Calcular el área de la superficie `z = x²+y²` con `|x| ≤ 1`, `|y| ≤ 1`. → #AreaSuperficie
- **P3)** Calcular el flujo de `f = (6x−yz, xz, xy)` a través de la frontera de la región `x+y+z ≤ 2`, `y ≤ x`, 1er octante. → #Flujo #Divergencia
- **P4)** EDO `y'' + y' − 2y = cos x`, con `y(0)=0`, `y'(0)=1`. → #EDO
- **T1)** Enunciar la condición necesaria para la existencia de función potencial. Demostrarla. → #FuncionPotencial #Demostracion
- **T2)** Demostrar que si `y₁`, `y₂` son solución de la homogénea entonces `y = A·y₁ + B·y₂` es solución general. → #Superposicion #EDO #Demostracion

## 2016-07-06  ·  `2016-07-06_Parcial.png` (foto)  ·  ≡ `2022-07-22_Parcial.pdf`

- **P1)** Volumen de la región `2x²+2y²+z² ≤ 3`, `z ≥ √(x²+y²)`, `x ≤ y`. → #Volumen
- **P2)** Circulación de `f = (yz, 2xz, xy)` a lo largo de la curva intersección de `z = x²+4y²` con `z = 8−x²−4y²` (indicar orientación). → #Circulacion
- **P3)** Flujo de `f = (y², z²+x², x²)` a través de la superficie `y = x` tal que `x²+y²+2z² ≤ 2`. → #Flujo **[RECICLADO]**
- **P4)** EDO `y'' + 4y' = 8`. → #EDO
- **T1)** Cambio de variables `(x,y) = (u+2v, 2u+v)`; calcular área(D\*) sabiendo que área(D) = 6. → #CambioVariables
- **T2)** Enunciar la condición necesaria para la existencia de función potencial; indicar hipótesis; demostrarla. → #FuncionPotencial #Demostracion

## 2016-11-25  ·  `2016-11-25_Parcial.pdf` / `.png`  ·  (reutilizado como el 2023-07-13)

- **P1)** Volumen de `z + x² ≤ 6`, `y ≤ x`, `x ≤ z`, `x ≥ 0`, `y ≥ 0`. → #Volumen
- **P2)** Circulación de `f = (xy, y², xz)` a lo largo de la curva intersección de `z = x+y` con `x = y²`, desde `(0,0,0)` hasta `(4,2,6)`. → #Circulacion
- **P3)** Demostrar que `f = (2x, 2y)` es conservativo; calcular su función potencial `φ` con `φ(0,0)=1`. → #Conservativo #FuncionPotencial
- **P4)** EDO `y'' + 2y' = 4x`. → #EDO
- **T1)** Condición necesaria para la existencia de función potencial; indicar hipótesis; demostrar. → #FuncionPotencial #Demostracion
- **T2)** Enunciar el Teorema de la Divergencia. Sabiendo que para `f = (x, 2y, x−z)` el flujo por `∂S` es saliente e igual a `18π`, calcular el volumen del cuerpo `S`. → #Divergencia #Flujo

## 2017-07-05  ·  `2017-07-05_Parcial.pdf` / `.png`

- **P1)** Hallar las coordenadas del **baricentro** de `x²/4 + y² ≤ 1` con `y ≥ 0`. → #Baricentro #AreaRegion
- **P2)** Volumen de `(x−1)² + (y−1)² ≤ 1`, `z ≤ xy`, `z ≥ 0`. → #Volumen
- **P3)** Longitud de la curva `λ(t) = (2cos t, 2sin t, 2t)` entre `(2,0,0)` y `(−2,0,2π)`. → #LongitudCurva
- **P4)** Flujo de `f = (y², z²+x², x²)` a través de la superficie `y = x` tal que `x²+y²+2z² ≤ 2`. → #Flujo **[RECICLADO]**
- **T1)** Enunciar y demostrar la condición necesaria para la existencia de función potencial en `ℝ²`. → #FuncionPotencial #Demostracion
- **T2)** Demostrar que si `y₁` es solución de `y''+py'+qy = f₁(x)` e `y₂` de `= f₂(x)`, entonces `y₁+y₂` es solución de `= f₁(x)+f₂(x)`. → #Superposicion #EDO #Demostracion

## 2017-11-16  ·  `2017-11-16_Parcial.pdf` / `.png` (escaneo)

- **P1)** Masa del cuerpo `x²+y²+z² ≤ 18`, `z ≥ √(x²+y²)`, con densidad proporcional a la distancia al plano `xy`. → #MasaCuerpo
- **P2)** Circulación de `f = (x²+φ(y−x), x²−φ(y−x))` con `φ ∈ C¹`, a lo largo de la frontera de `D = {x² ≤ y ≤ x}`. → #Circulacion #Green
- **P3)** Flujo de `f = (y², z²+x², x²)` a través de la superficie `y = x` tal que `x²+y²+2z² ≤ 2`. → #Flujo **[RECICLADO]**
- **P4)** Flujo de `f = (y, x, 2z)` a través de la superficie `Σ` frontera del cuerpo `z ≤ 9−x²`, `x ≤ y ≤ 3`, 1er octante (indicar orientación). → #Flujo
- **T1)** Condición necesaria para función potencial; verificar si `f = (2xy, y²)` la admite. → #FuncionPotencial #Demostracion
- **T2)** Demostrar que `y₁ − y₂` es solución de `= f₁(x) − f₂(x)`. → #Superposicion #EDO #Demostracion

## 2019-11-21  ·  `2019-11-21_Parcial.pdf` / `.png`

- **P1)** EDO `y'' − 6y' + 9y = 2x`, con `y(0)=1`, `y'(0)=0`. → #EDO
- **P2)** Área del trozo de cono `z = √(x²+y²)` por debajo del plano `z = 2`. → #AreaSuperficie
- **P3)** Trabajo de `f = (z, y, x)` a lo largo de la curva intersección de `x²+y² = 4` y `z = x`, entre `(2,0,2)` y `(−2,0,−2)`. → #Trabajo #Circulacion
- **P4)** Volumen limitado por los planos `z=y`, `z=2−y`, `y=x+2`, `y=2−x` y el plano `xy`. → #Volumen
- **T1)** Condición suficiente para que `f = (f₁,f₂)` sea conservativo; verificar `f = (2xy+1, x²+2y)`; calcular su potencial sabiendo que vale 5 en `(1,2)`. → #Conservativo #FuncionPotencial
- **T2)** Enunciar el Teorema de Green. Calcular la circulación de `f = (xy²/2, 3x²y/2)` a lo largo de la frontera de `x² ≤ y ≤ x` (indicar sentido). → #Green #Circulacion

## 2022-07-15  ·  `2022-07-15_Parcial.pdf`  ·  ≡ `2022-11-17_Parcial.pdf`

- **P1)** Volumen de `x²+y² ≤ 4`, `z ≥ x+y`, `z ≤ 2x+y+3`. → #Volumen
- **P2)** Verificar que `f = (6xy+2y²+2, 3x²+4xy−2)` es conservativo; calcular su potencial sabiendo que vale 11 en `(1,2)`; evaluar el potencial en `(1,0)`. → #Conservativo #FuncionPotencial
- **P3)** Flujo de `f = (y²+z², y², x²+y²)` a través de la frontera del cuerpo `x/2 + y + z/3 ≤ 1` en el 1er octante. → #Flujo #Divergencia
- **P4)** EDO `y'' − 2y' + 5y = 2x`; calcular `y(0)`. → #EDO
- **T1)** Enunciar el Teorema de Green. Calcular la circulación de `f = (xy²/2, 3x²y/2)` a lo largo de la frontera de `x² ≤ y ≤ x`. → #Green #Circulacion
- **T2)** Demostrar que si `yₚ` es solución de `y''+p(x)y'+q(x)y = g(x)` entonces `k·yₚ` es solución de `= k·g(x)`. → #Superposicion #EDO #Demostracion

## 2022-11-24  ·  `2022-11-24_Parcial.pdf` (T1) / `.jpg` (T2)

- **P1)** Volumen de `x²−2x+y² ≤ 0`, `z ≤ 2+x`, `x+z ≥ 2`. → #Volumen
- **P2)** Verificar que `f = (4xy−2, 2x²−2y)` es conservativo; calcular su potencial sabiendo que vale 0 en `(1,1)`. → #Conservativo #FuncionPotencial
- **P3)** Flujo de `f = (y², z²+x², x²)` a través de la superficie `y = x` tal que `x²+y²+2z² ≤ 2`. → #Flujo **[RECICLADO]**
- **P4)** EDO `y'' − 4y' + 13y = 26`, con `y(0)=1`, `y'(0)=1`. → #EDO
- **T1)** Demostrar que si `f: ℝ²→ℝ²` es conservativo (`f = ∇φ`) entonces `∫_{A→B} f·dλ = φ(B) − φ(A)`. → #FuncionPotencial #Demostracion
- **T2)** Demostrar que `y₁ − y₂` es solución de `= f₁(x) − f₂(x)`. → #Superposicion #EDO #Demostracion

## 2022-12-02  ·  `2022-12-02_Parcial.pdf`

- **P1)** Masa del cuerpo `x²+y² ≤ 4`, `x−3 ≤ z ≤ 2+x`, con densidad proporcional a la distancia al eje `Z`. → #MasaCuerpo
- **P2)** Circulación de `f = (xy, −y², z²)` a lo largo de la curva intersección de `z = 9−x²`, `z = y`, desde `A=(3,0,0)` hasta `B=(0,9,9)`, `x,y,z ∈ ℝ₀⁺`. → #Circulacion
- **P3)** Flujo de `f = (x−yz, y+xz, z+2xy)` a través de la superficie `x²+y² = 2` tal que `x²+y²+z² ≤ 4` (indicar orientación). → #Flujo
- **P4)** `f = (x+g'(x), y·g'(x), −2z·g(x))` con `f ∈ C¹` y `f(0,0,1) = (2,0,0)`; hallar `g(x)` para que el flujo por la frontera del cuerpo esférico de radio `r` sea igual al volumen. → #Flujo #Divergencia
- **T1)** Enunciar el teorema de cambio de variables en integrales dobles. `(x,y) = (v−2u, u+v)`; calcular área(D\*) sabiendo que área(D) = 9. → #CambioVariables
- **T2)** Definir función potencial. `f = (2xy + 2x·g'(x²), x²)` con `f ∈ C¹`; calcular la circulación desde `(−2,4)` hasta `(2,5)`. → #FuncionPotencial #Circulacion

## 2022-12-16  ·  `2022-12-16_Parcial.pdf`

- **P1)** Siendo `rot(f) = (x, x²−2x, −z)`, calcular la circulación de `f` a lo largo de la curva intersección de `z = 3−x²−y²`, `z = 2x²+2y²` (indicar orientación). → #Rotor #Stokes #Circulacion
- **P2)** `f = (12x+2yz, 6y+2xz, 2xy)` admite función potencial; determinar los valores de `a` para los cuales la integral de línea desde `(−a,a,1)` hasta `(1,a,a)` es nula. → #Conservativo #FuncionPotencial
- **P3)** Flujo de `f = (x, 2y, x−z)` a través de la superficie `Σ`: `y = 4−x²`, `z ≤ y`, 1er octante (indicar orientación). → #Flujo
- **P4)** Masa del cuerpo `H`: `x²+z² ≤ 32`, `z ≥ √(x²+2y²)`, 1er octante, con densidad `δ(x,y,z) = K·z`, `K` constante. → #MasaCuerpo
- **T1)** Enunciar y demostrar la condición necesaria para función potencial. Determinar si `f = (2xy + 2x·g'(x²), x²)` con `f ∈ C¹` la admite. → #FuncionPotencial #Demostracion
- **T2)** Enunciar el teorema de cambio de variables en integrales dobles. `(x,y) = (v−2u, u+v)`; calcular área(D\*) sabiendo que área(D) = 9. → #CambioVariables

## 2023-07-14  ·  `2023-07-14_Parcial.pdf`

- **P1)** Hallar `g` tal que `f = (x²−4y·g(x), g'(x)−x+y)` sea conservativo, con `f(0,1) = (0,7)`. → #Conservativo #FuncionPotencial
- **P2)** Área de la región `D` encerrada por la curva `λ(t) = (t−t², t−t⁴)`, `t ∈ [0,1]`. → #AreaRegion
- **P3)** Masa del cuerpo `x²+z² ≤ 4`, `x−3 ≤ z ≤ 2+x`, con densidad proporcional a la distancia al eje `Y`. → #MasaCuerpo
- **P4)** Flujo de `f = (x−yz, y+xz, z+2xy)` a través de la superficie `x²+y²+z² ≤ 4`. → #Flujo #Divergencia
- **T1)** V/F justificar: con `(x,y) = (2u+v, 3u+v)`, si `∬_{D*} (2u+2v)·du·dv = 2` entonces `∬_D x·dx·dy = −8`. → #CambioVariables
- **T2)** Definir función potencial. `f = (2xy + 2x·g'(x²), x²)`; calcular la circulación desde `(−2,4)` hasta `(2,5)`. → #FuncionPotencial #Circulacion

## 2023-07-28  ·  `2023-07-28_Parcial.pdf`

- **P1)** Volumen de `2x²+2y²+z² ≤ 3`, `z ≥ √(x²+y²)`, `x ≥ 0`. → #Volumen
- **P2)** Circulación de `f = (yz, 2xz, xy)` a lo largo de la curva intersección de `z = 4x²+y²` con `z = 8−4x²−y²` (indicar orientación). → #Circulacion
- **P3)** Flujo de `f = (x−y−z, y−x−z, g(x,y))` con `g ∈ C¹`, a través de la frontera del cuerpo `2x+3y+4z ≤ 12` en el 1er octante (indicar orientación). → #Flujo #Divergencia
- **P4)** EDO `y'' − 3y' = 2 − 6x`, con `y(0) = y'(0) = 3`. → #EDO
- **T1)** Enunciar el teorema de cambio de variables. `(x,y) = (u+3v, 2u+2v)`; calcular área(D\*) sabiendo que área(D) = 6. → #CambioVariables
- **T2)** Enunciar la condición necesaria para la existencia de función potencial; indicar hipótesis; demostrarla. → #FuncionPotencial #Demostracion

## 2024-07-12  ·  `2024-07-12_Parcial.jpeg` (foto)

- **P1)** Volumen de la región `z ≤ 1−x²−y²`, `−z/2 ≤ √(x²+y²)+1`. → #Volumen
- **P2)** Área de la superficie `z = 1−x²−y²` tal que `z ≥ 0`. → #AreaSuperficie
- **P3)** Flujo de `f = (x+e^{yz}, y+e^{xz}, z+e^{xy})` a través de la frontera del cuerpo `x+z ≤ 4`, `z ≥ x ≥ 0`, `0 ≤ y ≤ x` (indicar orientación). → #Flujo #Divergencia
- **P4)** EDO `y'' − 2y' + 5y = 10`, con `y(0)=1`, `y'(0)=1`. → #EDO
- **T1)** Enunciar el Teorema de Green. Calcular la circulación de `f = (xy²/2, 3x²y/2)` a lo largo de la frontera de `x² ≤ y ≤ x` (indicar sentido). → #Green #Circulacion
- **T2)** Enunciar el teorema de cambio de variables para integrales dobles. Dada `∫₀^{π/2} ∫₀^{2cos φ} ρ³ dρ dφ`, graficar la región de integración en el plano `xy` y expresar la integral en coordenadas cartesianas. → #CambioVariables

## 2025-07-18  ·  `2025-07-18_Parcial.jpeg` (foto)

- **P1)** `f(x,y,z) = (x+g'(x), y·g(x), y²−xz)` con `f(0,1,0) = (1,1,1)`; hallar `g(x)` tal que `f` resulte **solenoidal** (`div f = 0`). → #Divergencia
- **P2)** Volumen del cuerpo `x²+y² ≤ 2y`, `|z| ≤ 2y`. → #Volumen
- **P3)** Circulación de `f = (2x, x+z, 2y)` a lo largo de la curva intersección de `x²+y² = 16` y `x+z = 4`, orientada de modo que `(0,1,0)` sea tangente en `(4,0,0)`. → #Circulacion
- **P4)** `f ∈ C¹` con `div f = 2z`; sabiendo que el flujo de `f` a través del disco `z = 0`, `x²+y² ≤ 4` orientado hacia `Z⁺` es `7π`, calcular el flujo a través de la superficie abierta `z = 4−x²−y²`, `z ≥ 0`, orientada hacia `Z⁺`. → #Flujo #Divergencia
- **T1)** Enunciar el Teorema de Green. `f = (y+g(x), 2x+g(y))`; suponiendo que se puede aplicar, calcular la circulación a lo largo de la frontera de `D = {x²+y² ≤ 2y}` (indicar orientación). → #Green #Circulacion
- **T2)** Definir solución general y solución particular de una EDO de orden `n`. Hallar la solución particular de `y'' − y = 4`, con `y(0) = −3`, `y'(0) = −1`. → #EDO

## sin fecha  ·  `sin-fecha_Parcial.jpeg` (foto)  ·  ⚠ la hoja NO trae fecha; comparte la T2 (integral polar) con 2024-07-12 → probablemente período 2024–2025

- **P1)** Área de la región `D` encerrada por la curva `C`: `λ(t) = (t−t³, t−t⁴)`, `0 ≤ t ≤ 1`. → #AreaRegion
- **P2)** Circulación de `f: ℝ³→ℝ³` de clase `C¹` con `rot f = (−x², 3y−x, 4z²−3xy)`, a lo largo de la curva intersección de `z = 3(x²+y²)` y `z = 4−(x²+y²)` (indicar orientación). → #Rotor #Stokes #Circulacion
- **P3)** Flujo de `f = (g(y,z), h(x,z), z)` a través de la superficie **abierta** `S`: `z = 1+x²+y²`, `z ≤ 2`, con `g,h ∈ C¹` y `S` orientada con el versor normal de tercera componente positiva. → #Flujo
- **P4)** EDO `y'' − 6y' + 9y = 9x`; hallar la solución particular sabiendo que en `(0,2)` su recta tangente es `y = x+2`. → #EDO
- **T1)** Enunciar el Teorema de Green. Calcular la circulación de `f = (xy², 3x²y)` a lo largo de la frontera de `x² ≤ y ≤ x` (indicar sentido). → #Green #Circulacion
- **T2)** Enunciar el teorema de cambio de variables para integrales dobles. Dada `∫₀^{π/2} ∫₀^{2cos φ} ρ³ dρ dφ`, graficar la región de integración en el plano `xy` y expresar la integral en coordenadas cartesianas. → #CambioVariables

---

## Índice inverso: tema → fechas (para búsqueda rápida)

| Tag | Aparece en |
|---|---|
| `#Volumen` | 2014-11-28, 2016-07-06, 2016-11-25, 2017-07-05, 2019-11-21, 2022-07-15, 2022-11-24, 2023-07-28, **2024-07-12**, **2025-07-18** |
| `#MasaCuerpo` | 2017-11-16, 2022-12-02, 2022-12-16, 2023-07-14 |
| `#Baricentro` / `#AreaRegion` | 2017-07-05, 2023-07-14, **sin-fecha** |
| `#AreaSuperficie` | 2014-11-28, 2015-11-25, 2019-11-21, **2024-07-12** |
| `#LongitudCurva` | 2017-07-05 |
| `#Circulacion` / `#Trabajo` | 2014-11-28, 2016-07-06, 2016-11-25, 2017-11-16, 2019-11-21, 2022-12-02, 2022-12-16, 2023-07-28, **2025-07-18**, **sin-fecha** |
| `#Green` | 2014-11-28, 2017-11-16, 2019-11-21, 2022-07-15, **2024-07-12**, **2025-07-18**, **sin-fecha** |
| `#Conservativo` / `#FuncionPotencial` | 2015-11-25, 2016-11-25, 2017-11-16, 2019-11-21, 2022-07-15, 2022-11-24, 2022-12-02, 2022-12-16, 2023-07-14, + teoría en casi todos |
| `#Flujo` | 2014-11-28, 2015-11-25, 2016-07-06, 2016-11-25, 2017-07-05, 2017-11-16, 2022-07-15, 2022-11-24, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28, **2024-07-12**, **2025-07-18**, **sin-fecha** |
| `#Divergencia` | 2015-11-25, 2016-11-25, 2022-07-15, 2022-12-02, 2023-07-14, 2023-07-28, **2024-07-12**, **2025-07-18** |
| `#Rotor` / `#Stokes` | 2022-12-16, **sin-fecha** |
| `#EDO` | 2015-11-25, 2016-07-06, 2016-11-25, 2019-11-21, 2022-07-15, 2022-11-24, 2023-07-28, **2024-07-12**, **2025-07-18**, **sin-fecha** |
| `#Superposicion` | 2015-11-25, 2017-07-05, 2017-11-16, 2022-07-15, 2022-11-24 |
| `#CambioVariables` | 2016-07-06, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28, **2024-07-12**, **sin-fecha** |
| `#MomentoInercia` | (no aparece en ningún parcial — cubierto en apunte 03 pero no se toma) |

## Problemas reciclados (idénticos o casi entre fechas)

- **Flujo `f = (y², z²+x², x²)` sobre `y = x`, `x²+y²+2z² ≤ 2`** → 2016-07-06, 2017-07-05, 2017-11-16, 2022-11-24. **(4 veces)**
- **Circulación `f = (yz, 2xz, xy)`** sobre intersección de paraboloides → 2016-07-06, 2023-07-28.
- **Flujo `f = (x−yz, y+xz, z+2xy)`** sobre superficie esférica → 2022-12-02, 2023-07-14.
- **Volumen `2x²+2y²+z² ≤ 3`, `z ≥ √(x²+y²)`** → 2016-07-06, 2023-07-28.
- **Cambio de variables `(x,y)=(u+2v,2u+v)` / `(v−2u,u+v)` → área(D\*)** → 2016-07-06, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28.
- **Green con `f = (xy²/2, 3x²y/2)` sobre `x² ≤ y ≤ x`** → 2019-11-21, 2022-07-15, **2024-07-12**, **sin-fecha** (y variante `(xy², 3x²y)`). **(el T1 más reciclado — casi fijo)**
- **Potencial de `f = (2xy + 2x·g'(x²), x²)`** (teórico) → 2022-12-02, 2022-12-16, 2023-07-14.
- **T2 «integral polar `∫₀^{π/2}∫₀^{2cos φ} ρ³ dρ dφ` → graficar región + pasar a cartesianas»** → 2024-07-12, **sin-fecha**. (Formato nuevo de T2 de cambio de variables, 2024–2025.)
- **Flujo por superficie abierta `z = 4−x²−y²` combinando disco `z=0` (divergencia)** → 2014-11-28 (variante), **2025-07-18**.
- **Volumen de `x²+y² ≤ 2y`** (paraboloides/cilindro con simetría en `2y`) → **2025-07-18** (y `z ≤ 2y`).

## Equivalencias (mismo examen, no practicar dos veces)

- `2016-07-06` ≡ `2022-07-22`
- `2022-07-15` ≡ `2022-11-17`
- `2016-11-25` fue reutilizado como el `2023-07-13`.
- `2016-11-25`, `2017-07-05`, `2017-11-16`, `2019-11-21`, `2022-11-24` existen en doble formato (pdf + png/jpg).

## Fuera de dataset

- **`Parciales varios.pdf`** — NO es un segundo parcial: compilación de **primeros parciales** (2019/2020) + teoría de extremos (Hessiano). Se dejó sin renombrar. *(Reorganización 2026-07-05: movido a `../../primer-parcial/examenes/`.)*

---

*Índice generado el 2026-07-01 y ampliado el 2026-07-04 con 3 parciales nuevos (2024-07-12, 2025-07-18 y uno sin fecha), a partir de la lectura (con visión) de los 23 archivos. Los enunciados de exámenes escaneados/foto pueden tener detalles menores aproximados.*
