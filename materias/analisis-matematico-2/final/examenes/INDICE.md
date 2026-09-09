# Índice de finales — Análisis Matemático II (UTN.BA)

> **Para qué sirve:** este archivo es la **única representación textual** de los finales.
> 20 de los 24 PDFs tienen capa de texto, 4 son escaneos; en todos los casos la
> transcripción curada vive acá. Para cualquier análisis (frecuencias, brechas, armado
> de simulacros) se grepea **este archivo**, nunca se re-leen los PDFs/JPGs.
>
> **Cómo buscar** (desde `examenes/`):
> ```bash
> grep -n "#Flujo" INDICE.md              # todos los flujos
> grep -n "#Demostracion" INDICE.md       # todo lo que hay que saber demostrar
> grep -B4 "#TrayectoriasOrtogonales" INDICE.md
> grep -n "^## " INDICE.md                # listar los 24 finales por fecha
> grep -n "RECICLADO" INDICE.md           # problemas repetidos entre fechas
> ```
> **Mantenimiento:** al agregar un final nuevo, sumá su sección con los mismos tags y
> actualizá las tablas del final del archivo.

## Estructura del examen (constante 2024-03 → 2026-07)

- **6 ítems:** `T1`, `T2` (teóricos, casi siempre con dos incisos a/b) y `P1`–`P4` (prácticos).
- **Duración:** 2 horas.
- **Aprobación (6 puntos):** *tres ejercicios correctamente resueltos: **uno** de T1 o T2 y
  **dos** de P1–P4.* → Sólo hace falta **1 teórico + 2 prácticos**. Esto define la estrategia
  entera: no hay que saber todo, hay que tener 2 prácticos blindados y 1 teórico seguro.
- **A diferencia de los parciales, el orden por posición NO es rígido:** el mismo tema
  aparece en P1, P2, P3 o P4 según la fecha. Lo que sí es estable es el *menú temático*.
- **El final integra 1er y 2do parcial:** cae tanto derivada direccional / implícita /
  extremos / Taylor (temario 1P) como flujo / circulación / integrales múltiples (2P).

## Leyenda de tags

**Cálculo vectorial e integrales (temario 2P):** `#Volumen` `#MasaCuerpo` `#Baricentro`
`#AreaRegion` `#AreaSuperficie` `#MasaChapa` `#LongitudCurva` `#Circulacion` `#Trabajo`
`#Green` `#Conservativo` `#FuncionPotencial` `#LineasCampo` `#Flujo` `#Divergencia`
`#Rotor` `#Stokes` `#CambioVariables` `#Superposicion` `#MomentoInercia`

**Varias variables (temario 1P):** `#Limite` `#Continuidad` `#DerivadasParciales`
`#Diferenciabilidad` `#AproximacionLineal` `#DerivadaDireccional` `#Gradiente`
`#ReglaCadena` `#DerivacionImplicita` `#PlanoTangente` `#SuperficieParametrizada`
`#CurvaEspacio` `#PuntoRegular` `#Taylor` `#Extremos`

**Ecuaciones diferenciales:** `#EDO` `#EDOPrimerOrden` `#EDOSegundoOrden`
`#TrayectoriasOrtogonales`

**Transversales (forma de la consigna, no tema):** `#Demostracion` (enunciar/definir/
demostrar), `#VoF` (verdadero-o-falso justificando), `#PlantearIntegral` (plantear los
límites sin calcular).

> Convención: cada ítem es una línea `- **Pn)** enunciado … → #Tag #Tag`. Los enunciados de
> exámenes **escaneados** pueden tener detalles menores aproximados (marcados con «≈»).
> `[RECICLADO]` marca un ítem que ya apareció, casi textual, en otra fecha.

---

## 2024-03-05 · `resueltos/2024-03-05_resuelto.pdf` (escaneo, con resolución de A. Rojas Torres)

- **T1a)** V/F: la circulación de `f = (y² − g(y−x), y² + g(y−x))`, `g ∈ C¹`, por la frontera de `D: x ≥ y² , x ≤ 2 − y²` recorrida en sentido negativo, es `3√2`. → #Circulacion #Green #VoF
- **T1b)** V/F: `2z² + xyz − xy² − x³ = 0` define `z = f(x,y)` cerca de `(−12, 12√3, 24√3)`; con `Hf = ((√3/2, 0), (0, √3/2))`, `f` alcanza extremo local en `(x₀,y₀)`. → #DerivacionImplicita #Extremos #VoF
- **T2a)** Demostrar que si `φ: S ⊆ R³ → R` es `C¹(S)`, entonces `∫_C ∇φ·ds = φ(Q) − φ(P)`. → #Conservativo #Demostracion
- **T2b)** ¿Admite plano tangente en el origen `g(x,y) = xy/√(x²+y²)` (0 en el origen)? → #Diferenciabilidad #PlanoTangente
- **P1)** Área del trozo de superficie `z = √(x²+y²)` con `x² + y² ≤ 4y`. → #AreaSuperficie
- **P2)** Líneas de campo de `F(x,y) = (x − y, x + y)`; hallar la que pasa por `(1,−1)`. → #LineasCampo #EDOPrimerOrden
- **P3)** Plantear (sin calcular) el flujo de `∇φ`, `φ = 2x² − 4yz²`, por la frontera de `W: 2x + y ≤ 4 , x + z ≤ 2 , 1er octante`. → #Flujo #Divergencia #PlantearIntegral
- **P4)** Circulación de `F = (yz + g(x), xz + g(y), y² + g(z))` por la curva `y + x² + z² = 0 ∩ y = −1`. → #Circulacion #Stokes

## 2024-05-10 · `resueltos/2024-05-10_resuelto.pdf` (escaneo, 2 resoluciones disponibles)

- **T1)** Enunciar y **demostrar** la condición necesaria para que un campo vectorial sea conservativo. Proponer un ejemplo `f: R² → R²` con función potencial y calcular la circulación por la curva cerrada `C` graficada. → #Conservativo #FuncionPotencial #Demostracion
- **T2)** Definir superficie parametrizada y punto regular. Siendo `F(u,v) = (u − v, u + v, 2u² + 2v²)`, analizar si `(1,1,2)` es punto regular de `Σ`. → #SuperficieParametrizada #PuntoRegular
- **P1)** Circulación `∮ F·dr` con `F(x,y) = (x + 2y, g(y) − x)`, `g ∈ C¹`, siendo `C_F` la frontera de la región limitada por `y = 2x + 1` y la curva solución de `2xy dx − y dy = 0` con recta tangente `y = 2x` en `(1, y₀)`. → #Circulacion #Green #EDOPrimerOrden
- **P2)** `z = f(x,y)` definida por `xz + z + y + ln(z − xy) = 10`. Recta normal al gráfico en `(2, 1, f(2,1))`; ¿corta a `x + y² = 7`? → #DerivacionImplicita #PlanoTangente
- **P3)** Flujo de `f = (g(y,z), h(x,z), z)` por la superficie abierta `z = 1 + x² + y²`, `z ≤ 2`, normal con tercera componente positiva. → #Flujo
- **P4)** Plantear el volumen del cuerpo limitado por `z = 0`, `x ≤ y²` y el plano normal a `C` en `(3,3,6)`, con `C: y = 3 ∩ x + 1 = (z − 4)²`. → #Volumen #CurvaEspacio #PlantearIntegral

## 2024-07-23 · `resueltos/2024-07-23_respuestas-oficiales.pdf` (tipeado + respuestas oficiales de cátedra)

- **T1a)** V/F: el flujo de `F = (x+y, y+z, x+z)` por `S: x²+y²+z²−2z = 0` con `z ≥ 1`, normal de componente z positiva, vale `π/2`. → #Flujo #Divergencia #VoF
- **T1b)** V/F: el plano tangente a `z = f(x,y) + x²` en `(1,2,4)` es `z = 2x + 2` sabiendo que `f ∈ C²(R²)` admite máximo local 3 en `(1,2)`. → #PlanoTangente #Extremos #VoF
- **T2a)** Definir punto silla de un campo escalar `f: U ⊂ R² → R`. → #Extremos
- **T2b)** Mostrar que `f(x,y) = x² ln(y − 5)` admite punto silla en `(0,6)`. → #Extremos
- **P1)** `f(x,y) = x·sen(y)/y` si `y > 0`, `xy` si `y ≤ 0`. Para cada `v̌ ∈ R²` determinar la existencia de `f'((0,0), v̌)`. → #DerivadaDireccional #Continuidad
- **P2)** Plantear la integral triple (sin calcular) del volumen de `z ≤ 4 − x − y`, `2x + y ≥ 4`, 1er octante. → #Volumen #PlantearIntegral
- **P3)** `F = (yz + 2, g(x,y,z), z)`, `g ∈ C²(R³)`. Si la circulación de `F` por `r(t) = (cos t, sen t, sen t)`, `t ∈ [0,π]`, es 1, calcular el flujo de `rot F` por la porción del plano `y = z` en `x² + y² ≤ 1`, `y ≥ 0`, normal con componente z positiva. → #Stokes #Rotor #Flujo #Circulacion
- **P4)** Solución de `(2y − 4x²)dx + x dy = 0` que pasa por `(1,1)`. → #EDOPrimerOrden

## 2024-07-30 · `2024-07-30_Final.pdf` (escaneo, con resolución manuscrita en págs. 2-5)

- **T1a)** Para `f: U ⊆ Rⁿ → R`, definir máximo local y mínimo global. → #Extremos #Demostracion
- **T1b)** Puntos de máximo local y de silla de `f(x,y) = x² − cos(y)` en `D: π/2 < y < 3π/2`. → #Extremos
- **T2a)** Definir líneas de campo de un campo conservativo `F: A ⊆ R² → R²` e indicar su relación con las líneas equipotenciales. → #LineasCampo #Conservativo #Demostracion
- **T2b)** Determinar las líneas de campo de `F(x,y) = (−x, 2y − 4x²)`. → #LineasCampo #EDOPrimerOrden
- **P1)** Masa de una chapa con forma de la superficie `S: 4z² = x² + y²`, `0 ≤ z ≤ 1`, `0 ≤ x ≤ y`, densidad ∝ distancia al plano `xy`. → #MasaChapa #AreaSuperficie
- **P2)** Flujo saliente de `F = (3x + h'_x, −2y + h'_y, 2x² + h'_z)` por la frontera de `T: x²+y²+z² ≤ 9, z ≥ 0`, con `h` armónica (`∇²h = 0`). → #Flujo #Divergencia
- **P3)** `g(x,y,z) = (x+y+z−1, xy+z²−1)`, `h(u,v) = cos u + eᵛ`. Derivada direccional de `f = h ∘ g` en `(0,0,1)` según `(1,1,−1)`. → #DerivadaDireccional #ReglaCadena
- **P4)** Trabajo de `G = (y e^{xy} − z sen(xz), x e^{xy}, −x sen(xz))` sobre `X(t) = (cos t, sen t, t)`, `t ∈ [0,2π]`. → #Trabajo #Conservativo

## 2024-10-09 · `2024-10-09_Final.pdf`

- **T1a)** Definir punto regular de una curva en `R³`. → #CurvaEspacio #PuntoRegular #Demostracion
- **T1b)** ¿Es `P₀ = (4,−4,3)` punto regular de la curva imagen de `f(t) = (t³+3t², t²+4t, 3)`? → #CurvaEspacio #PuntoRegular
- **T2a)** V/F: si `f(x,y) = x²y³/(x²+y²)` (2 en el origen), no existe `lím_{(x,y)→(0,0)} f`. → #Limite #VoF
- **T2b)** V/F: para `V` en el 1er octante con `√(x²+y²) ≤ z`, `x²+y² ≤ 4`, `z ≤ 4`, la integral `∭_V x dxdydz` se calcula en cilíndricas como `∫₀^{π/2}∫₀²∫₀^r r² cos θ dz dr dθ`. → #CambioVariables #Volumen #VoF
- **P1)** `Π` = plano tangente a `x² + y³ + z³ − z = 2` en `(1,1,0)`. Flujo de `f = (y,0,0)` por la porción de `Π` con `4x² + y² ≤ 4`, `y ≥ 0`, normal de tercera componente positiva. → #PlanoTangente #Flujo
- **P2)** Flujo de `f = (xy², yz², zx²)` por la frontera de `1 ≤ x²+y²+z² ≤ 9`, `z ≥ 0`, normal exterior. → #Flujo #Divergencia
- **P3)** Direcciones de derivada direccional **nula** en `x₀ = (4,2)` de `g(x,y) = x·f(x,y)`, con `z = f(x,y)` definida por `xy + z e^{z−1} = 9` cerca de `(4,2,1)`. → #DerivadaDireccional #DerivacionImplicita #Gradiente
- **P4)** Solución de `y'' − y' − 2y = −2x − 1` cuya recta tangente en `(0, y₀)` es `y = 7x + 3`. → #EDOSegundoOrden

## 2024-12-03 · `2024-12-03_Final.pdf`

- **T1a)** Enunciar la **Regla de la Cadena** en forma matricial con hipótesis. → #ReglaCadena #Demostracion
- **T1b)** Sea `F(x,y,z) = φ(z/(xy))`, `φ ∈ C¹`, `xy ≠ 0`. **Demostrar** que `x F'_x + y F'_y + 2z F'_z = 0`. → #ReglaCadena #Demostracion
- **T2a)** **Deducir** una fórmula de área plana aplicando el teorema de Green, con hipótesis. → #Green #AreaRegion #Demostracion
- **T2b)** Con `Df = ((6xy+1, 3x²+3), (3x², 2y))`, circulación de `f` por la frontera del triángulo `(−1,0), (2,0), (0,3)` en sentido positivo. → #Circulacion #Green
- **P1)** Plantear la masa de `H₃: z ≤ 4 − x² − y²`, `y ≥ x`, `x² + y² ≥ 2`, 1er octante, densidad ∝ distancia al eje z. → #MasaCuerpo #PlantearIntegral
- **P2)** `S: 1 − x² − 3xz + y² − ln z = 2`. Puntos donde el plano tangente a `S` en `(0,1,z₀)` corta a `C: y = x² ∩ z = 1 − 3x`. → #PlanoTangente #DerivacionImplicita #CurvaEspacio
- **P3)** Flujo de `f = (y, cos z + x, z − 2xy)` por `z = 4 − x²` con `y ≥ x`, `4 − x ≥ y`, 1er octante, normal de tercera componente positiva. → #Flujo
- **P4)** Familias `y = k x⁴ ∧ φ(x) + b y² = C`: hallar `b` para que sean ortogonales, siendo `φ` la solución de `y'' − y' = 2 − 2x` por el origen con `y'(0) = 0`. → #TrayectoriasOrtogonales #EDOSegundoOrden

## 2024-12-10 · `2024-12-10_Final.pdf`

- **T1a)** V/F: `x = 0` es solución singular de `x y' = 4x²`. → #EDO #VoF
- **T1b)** V/F: `z = f(x,y)` definida por `zx + ln(z+y) = 0` verifica `z'_x = z(y+z) z'_y`. → #DerivacionImplicita #VoF
- **T2a)** Definir campo de gradiente. **Demostrar** la independencia de la trayectoria en las integrales de línea. → #Conservativo #Demostracion
- **T2b)** Comprobar que `∮_C (x f(x²+y²) i + y f(x²+y²) j)·dr = 0` para `C` plana cerrada suave orientada positivamente. → #Circulacion #Conservativo
- **P1)** Plantear el flujo saliente de `f ∈ C¹(R³)` por la frontera de `H: 0 ≤ z ≤ √(x²+y²)`, `x²+y² ≤ 4`, `x²+y²−2y ≤ 0`, `x ≥ 0`, `y ≥ 0`, con `Df` dada. → #Flujo #Divergencia #PlantearIntegral
- **P2)** `f ∈ C³`; `P(x,y) = 2 − x − 3y + 3x² + ½y²` es el Taylor de grado 2 en `(1,1)`. Hallar `a, b` de `g = f − 3ax + by` para que el plano tangente en `A = (1,1,g(1,1))` sea `20x − 10y + 2z = D`. → #Taylor #PlanoTangente
- **P3)** Trabajo de `f ∈ C¹` por `C: x + z = 3 ∩ x² + y² = 1`, sabiendo que `rot f = (z, y, x)`; indicar el sentido. → #Trabajo #Stokes #Rotor
- **P4)** Plantear el área de `z = y³` con `4 − x² ≥ y ∧ y ≥ y_p`, 1er octante, hallando antes `y_p` solución de `y'' − y = −3x`, `y(0)=0`, `y'(0)=3`. → #AreaSuperficie #EDOSegundoOrden #PlantearIntegral

## 2024-12-17 · `2024-12-17_Final.pdf`

- **T1a)** Definir mínimo absoluto de `f: D ⊆ R² → R` en `D`. → #Extremos #Demostracion
- **T1b)** **Demostrar** que `f(x,y) = (x−y)⁴ + (y−1)²` presenta mínimo absoluto en `(1,1)`. ¿Estricto o amplio? → #Extremos #Demostracion
- **T2a)** Enunciar el teorema de **cambio de variable** en integrales dobles, con hipótesis. → #CambioVariables #Demostracion
- **T2b)** Dada `∫₋₁⁰ dx ∫₋ₓ^{√(2−x²)} dy`: graficar la región, plantear en polares, calcular por el sistema más conveniente e interpretar geométricamente el resultado. → #CambioVariables #AreaRegion
- **P1)** `f(x,y) = (3 − g(x)y, g'(x) − 2 sen x)`: hallar `g ∈ C²(R)` para que el trabajo por toda curva simple cerrada suave sea nulo, con `f(0,1) = (3,0)`. → #Conservativo #Green #EDOSegundoOrden
- **P2)** Expresar como integral doble la integral curvilínea de `f = (g, ½y², x² − z³)`, `g'_y = z + 6x − y`, por `C: z = 8 − 6x ∩ z = 8 − x² − y²`. → #Circulacion #Stokes #PlantearIntegral
- **P3)** Direcciones de derivada direccional nula y máxima de `h = f ∘ g` en `(1,1)`, con `g(x,y) = (x²y, x − y²)` y `z = f(u,v)` definida por `z − u² + v² + ln(v+z) = 0`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P4)** Dos integrales múltiples **distintas** (proyectando sobre planos coordenados distintos) para el volumen de `H: z ≤ 9 − x²`, `x + y ≤ 5`, 1er octante. → #Volumen #PlantearIntegral

## 2025-02-11 · `2025-02-11_Final.pdf` (resolución en `resueltos/2025-02-11_resuelto.pdf`)

- **T1a)** Definir superficie parametrizada y punto regular de una superficie. → #SuperficieParametrizada #PuntoRegular #Demostracion
- **T1b)** `R₀` = recta normal en `A = (2,1,3)` a `S: X = (2u², v−u, v+u)`. ¿Corta al plano `x + y = z + 5`? Hallar el punto. → #SuperficieParametrizada #PlanoTangente
- **T2a)** Graficar el conjunto de integración de `∫₀^{π/4}(∫₀^{2senθ} ρ² senθ dρ)dθ`. → #CambioVariables
- **T2b)** Expresar esa integral en coordenadas cartesianas. → #CambioVariables
- **P1)** `T(x,y) = x²y + y² + x²`: analizar y clasificar extremos locales. → #Extremos
- **P2)** `f` solenoidal (div nula) con `f(x,y,0) = (x, y−2, y²)`: flujo por `Σ: z = √(4 − x² − y²)`; indicar el versor normal. → #Flujo #Divergencia
- **P3)** Curva ortogonal a la familia `xy = K` que pasa por `(5,3)`; parametrizarla para `x, y > 0`. → #TrayectoriasOrtogonales #EDOPrimerOrden
- **P4)** Masa de `z ≥ √(x²+y²)`, `x²+y² ≤ 4`, `z ≤ 4`, densidad ∝ distancia al plano `xy`. → #MasaCuerpo

## 2025-02-18 · `2025-02-18_Final.pdf` (resolución en `resueltos/2025-02-18_resuelto.pdf`)

- **T1a)** Enunciar el **teorema de la divergencia** con hipótesis. → #Divergencia #Demostracion
- **T1b)** Hallar `a ∈ R` tal que el flujo de `f = (2xy, z − y², 2az)` por la frontera de `V` sea `8·vol(V)`. → #Divergencia #Flujo
- **T2a)** Definir curva de nivel `L_C` de `f: R² → R`. ¿Cuándo se asegura que `∇f ⊥ L_C` en `(x₀,y₀)`? → #Gradiente #Demostracion
- **T2b)** Recta en `R²` perpendicular a la curva de nivel 1 de `z = f(x,y)` en `(0,0)`, con `f` definida por `z³ + y + e^{xz} − 2 = 0`. → #Gradiente #DerivacionImplicita
- **P1)** Plano normal `α₀` a `C` en `(1,0,1)`, con `C: z = φ(x) − y ∩ z = x + y` y `φ` solución de `y'' = 6x`, `y(0)=y'(0)=0`. → #CurvaEspacio #EDOSegundoOrden
- **P2)** `F = (2xy, x²+z², 2yz)`: trabajo desde `A=(2,4,4)` hasta `B=(0,0,0)` por `C: y = x² ∩ z = 2x`, **por dos procedimientos distintos**. → #Trabajo #Conservativo #FuncionPotencial
- **P3)** Área de `z² = x² + y²` con `z ≥ 0`, dentro de `x²+y²+z² = 8` y fuera de `x²+y²+z² = 2`. → #AreaSuperficie
- **P4)** Plantear la masa de `x²+z² ≤ 4`, `x+z ≥ 2`, `y ≤ 3`, 1er octante, densidad ∝ distancia al plano `yz`. → #MasaCuerpo #PlantearIntegral

## 2025-02-25 · `2025-02-25_Final.pdf`

- **T1a)** Enunciar el **teorema del rotor (Stokes)** con hipótesis. → #Stokes #Demostracion
- **T1b)** **Demostrar** que la circulación de `f = (2z, g(x,y,z), 2x)`, `g ∈ C¹(R³)`, sobre cualquier curva cerrada contenida en `y = k` es nula. → #Stokes #Circulacion #Demostracion
- **T2a)** Definir máximo relativo de `f: D ⊆ R² → R`. → #Extremos #Demostracion
- **T2b)** ¿Alcanza `f(x,y) = 9 − √(4x² + 2y⁴)` un extremo relativo en `(0,0)`? → #Extremos
- **P1)** Trabajo de `f = (H(x) + 6, x² + M(y))`, `H, M ∈ C¹(R)`, por la frontera de `D: (x−1)² + y² ≤ 1`, `x ≥ 1`; indicar la orientación. → #Trabajo #Green
- **P2)** `φ(x)` = trayectoria ortogonal a `Kx = e^{−2y}` en `(0,0)`. Recta tangente y plano normal en `(−1,0,−1)` a `C: y + z + xφ(x) = −2 ∩ z − 4y = −1`. → #TrayectoriasOrtogonales #CurvaEspacio
- **P3)** Hallar `g(x)` para que `∇F ≡ (0,1)` en todo `R²`, con `F(x,y) = g'(x) − g(x) + x² + y`, `g'(0) = −2`, `g(0) = 0`. → #Gradiente #EDOSegundoOrden
- **P4)** `S` = frontera de `y ≥ x² + z²` con `y ≤ 4`: flujo saliente de `f` conservativo con potencial `U = xy + z² + C`; indicar la orientación. → #Flujo #Divergencia #Conservativo

## 2025-05-20 · `2025-05-20_Final.pdf`

- **T1a)** Enunciar el **criterio del Hessiano** para clasificar puntos críticos de `f: R² → R`, `f ∈ C²`. → #Extremos #Demostracion
- **T1b)** Hallar `a` tal que `f(x,y) = (1+y²)(x³ − 2ax² + 10)` tenga plano tangente horizontal en `(2,0,f(2,0))`; clasificar el extremo. → #Extremos #PlanoTangente
- **T2a)** V/F: `(3,0,0)` es punto regular y simple de `C: (x,y,z) = (2t+1, t²−t, t²−1)`, `−4 < t < 4`. → #CurvaEspacio #PuntoRegular #VoF
- **T2b)** V/F: con `g > 0`, `g ∈ C¹`, la circulación de `f = (y g(x), y², z²)` por el borde de `S: x+y+z = 4` (1er octante) orientado `(4,0,0)→(0,0,4)→(0,4,0)` es positiva. → #Circulacion #Stokes #VoF
- **P1)** Recta normal a la superficie de nivel 2 de `h` en `x₀ = (1,3,4)`, con `h = f ∘ g`, `w = f(u,v)` definida por `2v + u e^{w−2} − w = −1` y `Dg(1,3,4) = ((2,2,4), (−1,2,0))`. → #Gradiente #ReglaCadena #DerivacionImplicita #PlanoTangente
- **P2)** Área de `D = {x² + 2y² ≤ 4, 0 ≤ 2y ≤ x}`. → #AreaRegion #CambioVariables
- **P3)** Flujo de `f = (x g(xz), y², 1 − z g(xz))`, `g ∈ C¹`, por `Σ: y = x² + z²`, `y ≤ 4`; indicar la orientación. → #Flujo
- **P4)** Solución de `y'' + y' − 2y = 9eˣ` con `y(0)=0`, `y'(0)=3`. → #EDOSegundoOrden

## 2025-07-15 · `2025-07-15_Final.pdf`

- **T1a)** V/F: la derivada direccional de `h(x,y) = f(xy, x−y)` en `(1,2)` hacia `(3,5)`, con `Df(u,v) = ((2u+v, u), (1,1))`, es `−11/5`. → #DerivadaDireccional #ReglaCadena #VoF
- **T1b)** V/F: `f(x,y) = (x²+y⁴)√(xy)` admite en `(0,0)` un mínimo global en `U`. → #Extremos #VoF
- **T2a)** Definir **función potencial** de un campo vectorial. → #FuncionPotencial #Demostracion
- **T2b)** Comprobar que `F(x,y) = (2x, 2y)/(x²+y²)` admite potencial `φ` en `R²∖{(0,0)}`; con `φ(1,0) = 3`, hallar la línea equipotencial por `(1,0)`. → #FuncionPotencial #LineasCampo
- **P1)** Circulación de `F ∈ C¹(R³)` por `γ: x+y+z = 2 ∩ x²+y² = y`, con `DF = ((y, x, −2), (2x, y³, 1), (x², 0, z²))`; indicar el sentido. → #Circulacion #Stokes
- **P2)** Ecuación cartesiana de la solución de `y'' − y = 4eˣ` que pasa por el origen con pendiente 2. → #EDOSegundoOrden
- **P3)** Volumen de `H: (x−1)² + y² ≤ z ≤ 5 − 2x`. → #Volumen
- **P4)** Flujo de `F = (−y, x, xz)` por la superficie abierta `x² + y² = 2x` con `z ≤ 4 − (x²+y²)`, 1er octante. → #Flujo

## 2025-07-29 · `2025-07-29_Final.pdf` (resolución en `resueltos/2025-07-29_resuelto.pdf`)

- **T1a)** V/F: si `z = h(x,y)` está definida por `xz + z + y + ln(z − xy) = 10` cerca de `(2,1,h(2,1))`, la recta normal al gráfico en ese punto es paralela a `r: −2x − y + 8 = 0 ∩ z = 3`. → #DerivacionImplicita #PlanoTangente #VoF
- **T1b)** V/F: si el Maclaurin de 2º grado de `f` es `T₂ = 3 + 2x² + y²`, entonces `(0,0)` es mínimo local de `f`. → #Taylor #Extremos #VoF
- **T2a)** Definir **derivada direccional** de un campo escalar en `X₀` según `ǔ`. → #DerivadaDireccional #Demostracion
- **T2b)** Existencia de las derivadas direccionales de `f(x,y) = y/√(x²+y²)` (0 en el origen) en `(0,0)`. ¿Es `f` continua allí? → #DerivadaDireccional #Continuidad
- **P1)** Circulación de `F` por `C: x²+y²+z² = 8 ∩ z = √(x²+y²)`, sabiendo `rot F = (α(x), β(y), 3z)`; indicar la orientación. → #Circulacion #Stokes #Rotor
- **P2)** `y = f(x)` solución particular de `y'' + 4y = 8` con recta tangente `y = 6x + 2` en `(0,y₀)`: valores máximo y mínimo de `f` en `[0,π]`. → #EDOSegundoOrden #Extremos
- **P3)** Área del trozo de `z = √(x²+y²)` con `x² + 4y² ≤ 4`. → #AreaSuperficie
- **P4)** Flujo de `f = (x³+y³, x³+z³, x³+y³)` por `S` = frontera de `H: 3 ≤ z ≤ 7 − x² − y²`, normal saliente. → #Flujo #Divergencia

## 2025-09-25 · `2025-09-25_Final.pdf`

- **T1a)** **Demostrar** la independencia de la trayectoria para integrales de línea. → #Conservativo #Demostracion
- **T1b)** `f(x,y) = (4xy² + 1, 4x²y)`: circulación por `γ(t) = (t sen t, t cos t)`, `t ∈ [0,π]`, con su parametrización natural. → #Circulacion #Conservativo #FuncionPotencial
- **T2a)** Enunciar el teorema de **cambio de variables** en integrales dobles. → #CambioVariables #Demostracion
- **T2b)** Con `φ(u,v) = (u+2v, 2u+v)`, calcular `Área(D*)` sabiendo `Área(D) = 12`. → #CambioVariables **[RECICLADO — idéntico al T1 del 2º parcial 2016-07-06, con 12 en vez de 6]**
- **P1)** `f(x,y,z) = 3x² − 5y + 2z`: derivada direccional `f'(X₀, ǔ)` con `ǔ` orientado hacia el origen y normal a `x²+y²+z² = 6` en `X₀ = (2,1,1)`. → #DerivadaDireccional #Gradiente
- **P2)** Flujo de `F = (x + sen(yz), y + sen(xz), 3z + 2)` por `S: z = 9 − x² − y²`, `z ≥ 0`, orientada con `z⁺`. → #Flujo
- **P3)** Aproximar `f(1.98, 2.01)` con Taylor de 2º grado si `f(2,2) = 5` es extremo local y `D(∇f)(2,2) = ((3,1),(1,2))`. → #Taylor #AproximacionLineal
- **P4)** Circulación de `f = (x²+z², x², 3yz)` por `C: x²+y² = 9 ∩ x+z = 3`; indicar gráficamente la orientación. → #Circulacion #Stokes

## 2025-12-02 · `2025-12-02_Final.pdf`

- **T1a)** **Demostrar** que si `f: R² → R²` es continuo y conservativo con potencial `φ` y `C` es abierta regular a trozos de `x₁` a `x₂`, entonces `∫_C f·ds = φ(x₂) − φ(x₁)`. → #Conservativo #Demostracion
- **T1b)** Circulación de `f = (2x e^{xy} + x²y e^{xy}, x³e^{xy} + 3y²)` por la curva abierta de `(1,0)` a `(0,2)`. → #Circulacion #Conservativo
- **T2a)** Definir campo escalar **continuo** en un punto para `f: R² → R`. → #Continuidad #Demostracion
- **T2b)** ¿Se puede extender `f(x,y) = (x−π/2)²cos x / ((x−π/2)² + y⁴)` en `(π/2, 0)` de modo que resulte continua en `R²`? → #Continuidad #Limite
- **P1)** Área de la superficie `z = x + y` limitada lateralmente por `x² + y²/4 = 1`, 1er octante. → #AreaSuperficie
- **P2)** Circulación de `f` por `C: x+y+z = 2 ∩ x²+y² = y`, con `Df = ((y,x,−2),(z,0,x),(y,x,0))`; indicar el sentido. → #Circulacion #Stokes **[RECICLADO — misma curva y consigna que 2025-07-15 P1, cambia una fila del jacobiano]**
- **P3)** `f(x,y) = x²y + y² + 2y`: todos los `(x₀,y₀)` con plano tangente paralelo a `2y − z/2 = 8`. → #PlanoTangente
- **P4)** Flujo de `f = (xy, x, xz)` por la superficie abierta `x² + y² = 2x` con `z ≤ 4 − x² − y²`, 1er octante. → #Flujo **[RECICLADO — mismo cilindro y región que 2025-07-15 P4]**

## 2025-12-09 · `2025-12-09_Final.pdf`

- **T1a)** **Demostrar** que si `F(γ(u))` es constante, la dirección de crecimiento más rápido de `F` es ortogonal a la tangente a la curva. → #Gradiente #ReglaCadena #Demostracion
- **T1b)** Comprobarlo para `F = 3x²y − 3yz`, `γ(u) = (u, −u², u²)` en `(2,−4,4)`. → #Gradiente #ReglaCadena
- **T2a)** Definir **función potencial** para `f: R² → R²`. → #FuncionPotencial #Demostracion
- **T2b)** Sabiendo que `f = (−y/(x²+y²), x/(x²+y²))` admite potencial `∅` en `A: y > 0` con `∅(1,1) = π/4`, determinar la línea equipotencial por `(1,1)`. → #FuncionPotencial #LineasCampo
- **P1)** `β₀` = plano tangente a `xyz + ln(xyz) − z = 0` en `(1,1,1)`. Flujo de `f = (−xy+z, xy/2, xy−2z+4)` por la porción de `β₀` en el 1er octante; indicar la orientación. → #PlanoTangente #Flujo #DerivacionImplicita
- **P2)** Flujo de `f = (3x + yz, xy e^{−xz}, e^{−xz})` por `z = 1 − x²/4 − y²` sobre el plano `xy`, normal hacia `z⁺`. → #Flujo
- **P3)** Circulación de `f = (−3y + x e^{−2x}, y e^{−3y+1} − 3x + x²)` por la frontera de `D: x²+y² ≤ 2x`, `y ≥ x−1`, en sentido **negativo**. → #Circulacion #Green
- **P4)** `lím_{x→+∞} y_G` siendo `y_G` la solución general de `y'' + 2y' + y = 2e^{−x}`. → #EDOSegundoOrden

## 2025-12-16 · `2025-12-16_Final.pdf`

- **T1a)** V/F: el volumen de `V: x²+y²+z² ≤ 12`, `x²+y² ≤ z` es `∫₀^{2π}∫₀^{√12}∫_{r²}^{√(12−r²)} r dz dr dθ`. → #Volumen #CambioVariables #VoF
- **T1b)** V/F: la circulación de `f = (cos(x²) + y², sen(y²) + 2xy)` por cualquier circunferencia de radio `r` es nula. → #Circulacion #Green #Conservativo #VoF
- **T2a)** Definir campo escalar **diferenciable** en un punto para `f: A ⊆ R² → R`. → #Diferenciabilidad #Demostracion
- **T2b)** ¿Admite plano tangente en el origen el gráfico de `f(x,y) = xy²/(x²+y²)` (0 en el origen)? → #Diferenciabilidad #PlanoTangente
- **P1)** Masa de `W: z ≤ 4 + x² + y²`, `2x² + 2y² ≤ z`, densidad ∝ distancia al eje z. → #MasaCuerpo
- **P2)** Circulación de `f = (2xy, yz, xz + 5y)` por `γ: x+y+z = 5 ∩ x²/4 + y² = 2y`; indicar la orientación. → #Circulacion #Stokes
- **P3)** `f = ∇φ` con `φ = x²y + y²z`: flujo por la superficie abierta `x = 4 − y² − z²`, `x ≥ 0`; indicar la orientación. → #Flujo #Conservativo
- **P4)** `y_p` solución de `dy/dx = (2sec²(2x) − y)/x`, `y(π) = 0`. Mostrar que `lím_{x→0} y_P` es el extremo relativo (global) de `g(x,y) = x²y² + 2`. → #EDOPrimerOrden #Extremos

## 2026-02-10 · `2026-02-10_Final.pdf` (resoluciones en `resueltos/2026-02-10_resuelto-sylvina.pdf` y `.../2026-02-10_resuelto-fotos/`)

- **T1a)** Enunciar el **teorema de Gauss** con hipótesis. ¿Es aplicable en forma directa para el flujo de `f = (xy, x², z−3)` por `x² − 2x + y² = 0`, `−1 ≤ z ≤ 1`? → #Divergencia #Flujo #Demostracion
- **T1b)** ¿Es nulo el flujo de `f = (2x, z²+y, z−8)` por una esfera de radio 2? → #Divergencia #Flujo
- **T2a)** Dos ejemplos de campos que permitan calcular área por circulación; qué teorema y cómo se construyen. → #Green #AreaRegion #Demostracion
- **T2b)** V/F: la circulación de `f = (y, −x)` por la semicircunferencia de radio 3, `y ≥ 0`, es `24π`. → #Circulacion #VoF
- **P1)** `y_p` solución de `y' = 2x` con `y(1) = 4`. Con `∇F(1,0) = (1,−1)`, `F(1,0) = 0.5` y `G = y_p − 4F`, calcular `G(1.01, 2.02)` por aproximación lineal. → #AproximacionLineal #EDOPrimerOrden
- **P2)** Flujo de `F = (x, y, x + 2y + xz)` por `S: y = x²` con `0 ≤ z ≤ 9 − x²`, normal de segunda componente negativa. → #Flujo
- **P3)** `Df = ((g(xy,y), h(x,y)), (3x, x))`. Si la integral de línea de `f` de `(2,0)` a `(−2,0)` por el eje `x` vale `−1/3`, calcularla entre los mismos puntos por `y = 4 − x²` con la misma orientación. → #Circulacion #Green
- **P4)** `w = u² ln(2x−1)` con `u = f(x,y)` definida por `uy + e^{u−x} = 2`: plano tangente a `w = h(x,y)` en `(1,1,w₀)`. → #ReglaCadena #DerivacionImplicita #PlanoTangente

## 2026-02-24 · `2026-02-24_Final.pdf` ⚠ el encabezado trae `17/02/2026` **y** `24/02/2026`

- **T1a)** V/F, demostrando o con contraejemplo: «Todo campo escalar diferenciable en un punto es derivable en dicho punto». → #Diferenciabilidad #DerivadasParciales #VoF #Demostracion
- **T1b)** V/F: `x y' − y = x³` tiene por solución particular `y = x² + 3x` que pasa por `(1,3)`. → #EDOPrimerOrden #VoF
- **T2a)** Enunciar el **teorema de Gauss** con todas sus hipótesis y dar un ejemplo donde se note su practicidad. → #Divergencia #Demostracion
- **T2b)** Inventar un campo `f(x,y,z)` tal que el flujo por cualquier superficie cerrada sea `3·vol` del cuerpo encerrado; justificar. → #Divergencia #Flujo
- **P1)** Parametrizar `x² + (y−1)² = 9` y obtener la recta tangente en `(−3,1)`, justificando. → #CurvaEspacio #PuntoRegular
- **P2)** `f(x,y) = (y h(x), h'(x) + 2h(x))` con `f(0,1) = (2,2)`: determinar `h(x)` por Green para que la circulación en sentido positivo por la frontera de `D` sea `4·área(D)`. → #Green #Circulacion #EDOPrimerOrden
- **P3)** Integral de línea de `F = (yz, zx, xy + 2z)` de `P₀ = (0,2,z₀)` a `P₁ = (1,1,z₁)` por `z = x − y ∩ y = 2 − x²`. → #Trabajo #Circulacion #Conservativo
- **P4)** `f(x,y) = x + y g(x,y)`, `g` diferenciable, `g(1,−2) = 0`, `∇g(1,−2) = (2,5)`: recta normal a la curva de nivel 1 de `f` por `(1,−2)`. → #Gradiente

## 2026-03-03 · `2026-03-03_Final.pdf`

- **T1a)** Enunciar el **teorema de Green** con hipótesis y **deducir** de él una fórmula de área plana. → #Green #AreaRegion #Demostracion
- **T1b)** Circulación de `F` por la frontera de `y ≥ x² − 2x`, `y ≤ 2x`, con `DF = ((5y, 5x), (2x, 4y))`; indicar la orientación. → #Circulacion #Green
- **T2a)** Explicar el cambio de cartesianas a **polares** y calcular el jacobiano. → #CambioVariables #Demostracion
- **T2b)** Plantear `∬_D √(x²+y²) dxdy` en cartesianas y en polares, con `D: x²+y² ≤ 4 ∧ y ≥ x`. → #CambioVariables #PlantearIntegral
- **P1)** **Dos integrales distintas** para la masa de `z ≤ 4 − x²`, `x + y ≤ 4`, `y ≥ −2`, `z ≥ 0`, densidad ∝ distancia al plano `xy`. → #MasaCuerpo #PlantearIntegral
- **P2)** `z = f(x,y)` definida por `xz + z + y + ln(z − xy) = 10` en un disco centrado en `(2,1)`: (a) fórmula de aproximación lineal; (b) recta normal en `(2,1,f(2,1))` y si corta a `x + y² = 7`. → #AproximacionLineal #DerivacionImplicita #PlanoTangente **[RECICLADO — misma ecuación implícita que 2024-05-10 P2 y 2025-07-29 T1a]**
- **P3)** Familias `y = k x³` y `x² + a y² = C`: hallar `a` para que sean ortogonales. → #TrayectoriasOrtogonales
- **P4)** Flujo de `f = (7x + yz, ln x² − h(x,z), −3z)`, `h ∈ C¹`, por `z = 5 − 4x² − 4y²` con `z ≥ 1`; indicar la orientación. → #Flujo

## 2026-05-19 · `2026-05-19_Final.pdf` (resolución en `resueltos/2026-05-19_resuelto-sylvina.pdf`)

- **T1a)** Enunciar el **teorema de Green**. → #Green #Demostracion
- **T1b)** Circulación de `f = (P,Q) ∈ C¹` por la semicircunferencia `x²+y² = 4`, `y ≥ 0`, de `(2,0)` a `(−2,0)`, sabiendo `Q'_x − P'_y = 3` y `f(x,0) = (x², 6x)`. → #Green #Circulacion
- **T2a)** V/F: el plano tangente a `S: x³z + xy − xz² = −3` en `(1,−1,2)` y la recta tangente a `C: (t², 2t+1, 2t²)` en ese punto son perpendiculares. → #PlanoTangente #CurvaEspacio #VoF
- **T2b)** V/F: la familia `xy = k` es ortogonal a `x² + y² = R²`. → #TrayectoriasOrtogonales #VoF
- **P1)** Circulación de `g = (yz + sen(x²), 2xz² + cos(y²), sen(z²))` por `z = √(x²+y²) ∩ z = 6 − x² − y²`; indicar la orientación. → #Circulacion #Stokes
- **P2)** `∬_S y dσ` con `S` = porción de `z = √(x²+y²)` que verifica `x² + (y−2)² ≤ 4`. → #MasaChapa #AreaSuperficie
- **P3)** Flujo de `f = (y²+z², x²+z², z²)` por la frontera de `V: x²+y²+z² ≤ 9`, `x ≥ 0`, `z ≥ 0`; indicar la orientación. → #Flujo #Divergencia
- **P4)** Extremos relativos y absolutos de `f(x,y) = y` en `D: x² + y² ≤ 4`. → #Extremos

## 2026-07-14 · `2026-07-14_Final.pdf`

- **T1a)** Enunciar el **teorema de Stokes** (o del rotor). → #Stokes #Demostracion
- **T1b)** Circulación de `f` por `C: x²+y² = 4 ∩ z = y+3`, con `Df = ((P'_x, 1, 1), (3, Q'_y, z), (2, 0, R'_z))`; indicar la orientación. → #Circulacion #Stokes
- **T2a)** V/F: `f(x,y) = xy + x³ + y²` no tiene máximos locales. → #Extremos #VoF
- **T2b)** V/F: `∫₀^{2π}∫₀³∫_r^{√(9−r²)} r dz dr dθ` calcula el volumen de `V: x²+y²+z² ≤ 9`, `z ≥ √(x²+y²)`. → #Volumen #CambioVariables #VoF
- **P1)** Todos los puntos `X₀` de `S: 2x² + 2y² + z² = 10` donde el plano tangente es paralelo a `4x + 4y + 2z = 25`. → #PlanoTangente #Gradiente
- **P2)** Flujo saliente de `f = (x + y⁹, z¹⁰ − y, x⁵ + 2z)` por la frontera de la parte de `V: x²+y² ≤ z ≤ 5` contenida en el 1er octante. → #Flujo #Divergencia
- **P3)** `h ∈ C¹`, `f = (x² − y², h(y))`: circulación por `C: y = 4x − x²`, `y ≥ 0`, de `(4,0)` a `(0,0)`. → #Circulacion #Green
- **P4)** Hallar `g` tal que `f = (y² + 4y g(x), 2xy − 4x² + g'(x))` sea conservativo y `f(0,1) = (13,4)`. → #Conservativo #FuncionPotencial #EDOPrimerOrden

## 2026-07-28 · `2026-07-28_Final.pdf` ← **el más reciente**

- **T1a)** **Demostrar** que si `f: R² → R` es diferenciable en `X₀`, entonces `f'(X₀, ǔ) = ∇f(X₀)·ǔ` para todo versor `ǔ`. → #DerivadaDireccional #Gradiente #Demostracion
- **T1b)** V/F: `f(x,y) = 2x²y/(x²+y²)` (0 en el origen) es diferenciable en `(0,0)`. → #Diferenciabilidad #VoF
- **T2a)** Enunciar el **teorema del rotacional o de Stokes**. → #Stokes #Demostracion
- **T2b)** V/F: la circulación de `f = (x², 1, z)` por el triángulo `A=(0,0,0)`, `B=(1,1,0)`, `C=(0,0,1)` recorrido `A→B→C→A` es nula. → #Circulacion #Stokes #Conservativo #VoF
- **P1)** Flujo saliente de `f = (x³ + yz², 4y + e^{2xz}, z³ + x e^y)` por la frontera de `Ω: x²+z² ≤ 4`, `0 ≤ y ≤ 2`. → #Flujo #Divergencia
- **P2)** Circulación de `f = (e^{x²} − y, x⁴/4 + e^y)` por la frontera de `D: 9x² + y² ≤ 9`, `x ≥ 0`, `y ≥ 0`, en sentido antihorario. → #Circulacion #Green
- **P3)** Solución general de `y'' − 4y' + 4y = 25 sen(x)`. → #EDOSegundoOrden
- **P4)** Dirección y sentido de **máximo decrecimiento** de `z = g(x,y)` en `(0,0)` si `−2x² + 2y³ + z³ − xy − 2y = 1` define `g` cerca de `(0,0,z₀)`. → #Gradiente #DerivacionImplicita

---

## Índice inverso: tema → fechas

| Tag | # ítems | Fechas |
|---|---|---|
| `#Flujo` | **26** | 2024-03-05 P3 · 2024-05-10 P3 · 2024-07-23 T1a,P3 · 2024-07-30 P2 · 2024-10-09 P1,P2 · 2024-12-03 P3 · 2024-12-10 P1 · 2025-02-11 P2 · 2025-02-18 T1b · 2025-02-25 P4 · 2025-05-20 P3 · 2025-07-15 P4 · 2025-07-29 P4 · 2025-09-25 P2 · 2025-12-02 P4 · 2025-12-09 P1,P2 · 2025-12-16 P3 · 2026-02-10 T1a,T1b,P2 · 2026-02-24 T2b · 2026-03-03 P4 · 2026-05-19 P3 · 2026-07-14 P2 · 2026-07-28 P1 |
| `#Circulacion` | **26** | 2024-03-05 T1a,P4 · 2024-07-23 P3 · 2024-12-03 T2b · 2024-12-10 T2b · 2024-12-17 P2 · 2025-02-25 T1b · 2025-05-20 T2b · 2025-07-15 P1 · 2025-07-29 P1 · 2025-09-25 T1b,P4 · 2025-12-02 T1b,P2 · 2025-12-09 P3 · 2025-12-16 T1b,P2 · 2026-02-10 T2b,P3 · 2026-02-24 P2,P3 · 2026-03-03 T1b · 2026-05-19 T1b,P1 · 2026-07-14 T1b,P3 · 2026-07-28 T2b,P2 |
| `#Demostracion` | **25** | en **los 24 exámenes** (T1 o T2 siempre pide enunciar/definir/demostrar) |
| `#Stokes` | **15** | 2024-03-05 P4 · 2024-07-23 P3 · 2024-12-10 P3 · 2024-12-17 P2 · 2025-02-25 T1a,T1b · 2025-05-20 T2b · 2025-07-15 P1 · 2025-07-29 P1 · 2025-09-25 P4 · 2025-12-02 P2 · 2025-12-16 P2 · 2026-05-19 P1 · 2026-07-14 T1a,T1b · 2026-07-28 T2a,T2b |
| `#Divergencia` | **15** | 2024-03-05 P3 · 2024-07-23 T1a · 2024-07-30 P2 · 2024-10-09 P2 · 2024-12-10 P1 · 2025-02-11 P2 · 2025-02-18 T1a,T1b · 2025-02-25 P4 · 2025-07-29 P4 · 2026-02-10 T1a,T1b · 2026-02-24 T2a,T2b · 2026-05-19 P3 · 2026-07-14 P2 · 2026-07-28 P1 |
| `#Green` | **15** | 2024-03-05 T1a · 2024-05-10 P1 · 2024-12-03 T2a,T2b · 2024-12-17 P1 · 2025-02-25 P1 · 2025-09-25 T1b · 2025-12-09 P3 · 2025-12-16 T1b · 2026-02-10 T2a,P3 · 2026-02-24 P2 · 2026-03-03 T1a,T1b · 2026-05-19 T1a,T1b · 2026-07-14 P3 · 2026-07-28 P2 |
| `#Extremos` | **15** | 2024-03-05 T1b · 2024-07-23 T1b,T2a,T2b · 2024-07-30 T1a,T1b · 2024-12-17 T1a,T1b · 2025-02-11 P1 · 2025-02-25 T2a,T2b · 2025-05-20 T1a,T1b · 2025-07-15 T1b · 2025-07-29 T1b,P2 · 2025-12-16 P4 · 2026-05-19 P4 · 2026-07-14 T2a |
| `#EDOSegundoOrden` | **13** | 2024-10-09 P4 · 2024-12-03 P4 · 2024-12-10 P4 · 2024-12-17 P1 · 2025-02-18 P1 · 2025-02-25 P3 · 2025-05-20 P4 · 2025-07-15 P2 · 2025-07-29 P2 · 2025-12-09 P4 · 2026-07-28 P3 |
| `#PlanoTangente` | **13** | 2024-03-05 T2b · 2024-05-10 P2 · 2024-07-23 T1b · 2024-10-09 P1 · 2024-12-03 P2 · 2024-12-10 P2 · 2025-02-11 T1b · 2025-05-20 T1b,P1 · 2025-07-29 T1a · 2025-12-02 P3 · 2025-12-09 P1 · 2025-12-16 T2b · 2026-02-10 P4 · 2026-03-03 P2 · 2026-05-19 T2a · 2026-07-14 P1 |
| `#DerivacionImplicita` | **13** | 2024-03-05 T1b · 2024-05-10 P2 · 2024-10-09 P3 · 2024-12-03 P2 · 2024-12-10 T1b · 2024-12-17 P3 · 2025-02-18 T2b · 2025-05-20 P1 · 2025-07-29 T1a · 2025-12-09 P1 · 2026-02-10 P4 · 2026-03-03 P2 · 2026-07-28 P4 |
| `#Conservativo` | **13** | 2024-03-05 T2a · 2024-05-10 T1 · 2024-07-30 T2a,P4 · 2024-12-10 T2a,T2b · 2024-12-17 P1 · 2025-02-18 P2 · 2025-02-25 P4 · 2025-09-25 T1a,T1b · 2025-12-02 T1a,T1b · 2025-12-16 T1b,P3 · 2026-02-24 P3 · 2026-07-14 P4 · 2026-07-28 T2b |
| `#VoF` | **13 exámenes** | 2024-03-05 · 2024-07-23 · 2024-10-09 · 2024-12-10 · 2025-05-20 · 2025-07-15 · 2025-07-29 · 2025-12-16 · 2026-02-10 · 2026-02-24 · 2026-05-19 · 2026-07-14 · 2026-07-28 |
| `#Gradiente` | **12** | 2024-10-09 P3 · 2024-12-17 P3 · 2025-02-18 T2a,T2b · 2025-02-25 P3 · 2025-05-20 P1 · 2025-09-25 P1 · 2025-12-09 T1a,T1b · 2026-02-24 P4 · 2026-07-14 P1 · 2026-07-28 T1a,P4 |
| `#DerivadaDireccional` | **10** | 2024-07-23 P1 · 2024-07-30 P3 · 2024-10-09 P3 · 2024-12-17 P3 · 2025-07-15 T1a · 2025-07-29 T2a,T2b · 2025-09-25 P1 · 2026-07-28 T1a |
| `#CambioVariables` | **11** | 2024-10-09 T2b · 2024-12-17 T2a,T2b · 2025-02-11 T2a,T2b · 2025-05-20 P2 · 2025-09-25 T2a,T2b · 2025-12-16 T1a · 2026-03-03 T2a,T2b · 2026-07-14 T2b |
| `#EDOPrimerOrden` | **10** | 2024-03-05 P2 · 2024-05-10 P1 · 2024-07-23 P4 · 2024-07-30 T2b · 2025-02-11 P3 · 2025-12-16 P4 · 2026-02-10 P1 · 2026-02-24 T1b,P2 · 2026-07-14 P4 |
| `#AreaSuperficie` | **9** | 2024-03-05 P1 · 2024-07-30 P1 · 2024-12-10 P4 · 2025-02-18 P3 · 2025-07-29 P3 · 2025-12-02 P1 · 2026-05-19 P2 |
| `#PlantearIntegral` | **12** | 2024-03-05 P3 · 2024-05-10 P4 · 2024-07-23 P2 · 2024-12-03 P1 · 2024-12-10 P1,P4 · 2024-12-17 P2,P4 · 2025-02-18 P4 · 2026-03-03 T2b,P1 |
| `#MasaCuerpo` | **7** | 2024-12-03 P1 · 2025-02-11 P4 · 2025-02-18 P4 · 2025-12-16 P1 · 2026-03-03 P1 |
| `#FuncionPotencial` | **8** | 2024-05-10 T1 · 2025-02-18 P2 · 2025-07-15 T2a,T2b · 2025-09-25 T1b · 2025-12-09 T2a,T2b · 2026-07-14 P4 |
| `#CurvaEspacio` | **8** | 2024-05-10 P4 · 2024-10-09 T1a,T1b · 2024-12-03 P2 · 2025-02-18 P1 · 2025-02-25 P2 · 2025-05-20 T2a · 2026-02-24 P1 · 2026-05-19 T2a |
| `#Volumen` | **7** | 2024-05-10 P4 · 2024-07-23 P2 · 2024-10-09 T2b · 2024-12-17 P4 · 2025-07-15 P3 · 2025-12-16 T1a · 2026-07-14 T2b |
| `#TrayectoriasOrtogonales` | **7** | 2024-12-03 P4 · 2025-02-11 P3 · 2025-02-25 P2 · 2026-03-03 P3 · 2026-05-19 T2b |
| `#ReglaCadena` | **7** | 2024-07-30 P3 · 2024-12-03 T1a,T1b · 2024-12-17 P3 · 2025-05-20 P1 · 2025-07-15 T1a · 2025-12-09 T1a,T1b · 2026-02-10 P4 |
| `#PuntoRegular` | **6** | 2024-05-10 T2 · 2024-10-09 T1a,T1b · 2025-02-11 T1a · 2025-05-20 T2a · 2026-02-24 P1 |
| `#Diferenciabilidad` | **5** | 2024-03-05 T2b · 2025-12-16 T2a,T2b · 2026-02-24 T1a · 2026-07-28 T1b |
| `#Trabajo` | **5** | 2024-07-30 P4 · 2024-12-10 P3 · 2025-02-18 P2 · 2025-02-25 P1 · 2026-02-24 P3 |
| `#AreaRegion` | **5** | 2024-12-03 T2a · 2024-12-17 T2b · 2025-05-20 P2 · 2026-02-10 T2a · 2026-03-03 T1a |
| `#Taylor` | **4** | 2024-12-10 P2 · 2025-07-29 T1b · 2025-09-25 P3 |
| `#LineasCampo` | **5** | 2024-03-05 P2 · 2024-07-30 T2a,T2b · 2025-07-15 T2b · 2025-12-09 T2b |
| `#Continuidad` | **4** | 2024-07-23 P1 · 2025-07-29 T2b · 2025-12-02 T2a,T2b |
| `#AproximacionLineal` | **3** | 2025-09-25 P3 · 2026-02-10 P1 · 2026-03-03 P2 |
| `#Rotor` | **3** | 2024-07-23 P3 · 2024-12-10 P3 · 2025-07-29 P1 |
| `#MasaChapa` | **2** | 2024-07-30 P1 · 2026-05-19 P2 |
| `#Limite` | **2** | 2024-10-09 T2a · 2025-12-02 T2b |
| `#SuperficieParametrizada` | **2** | 2024-05-10 T2 · 2025-02-11 T1a,T1b |
| `#Baricentro` `#LongitudCurva` `#MomentoInercia` `#Superposicion` | **0** | **nunca cayeron en un final** (sí en parciales) |

## Qué se pide demostrar / enunciar (banco teórico real)

Ordenado por frecuencia. **Sólo hace falta acertar UNO de T1/T2**, así que basta con
dominar los 6-8 primeros de esta lista.

| Teórico | Veces | Fechas |
|---|---|---|
| **Green:** enunciar + deducir fórmula de área plana | 5 | 2024-12-03 T2a · 2026-02-10 T2a · 2026-03-03 T1a · 2026-05-19 T1a |
| **Stokes:** enunciar el teorema del rotor | 5 | 2025-02-25 T1a · 2026-07-14 T1a · 2026-07-28 T2a · (+2 como hipótesis en V/F) |
| **Gauss/divergencia:** enunciar con hipótesis | 4 | 2025-02-18 T1a · 2026-02-10 T1a · 2026-02-24 T2a |
| **Conservativo:** independencia de la trayectoria / `∫∇φ·ds = φ(Q) − φ(P)` | 5 | 2024-03-05 T2a · 2024-12-10 T2a · 2025-09-25 T1a · 2025-12-02 T1a |
| **Cambio de variables** en integrales dobles: enunciar / polares + jacobiano | 4 | 2024-12-17 T2a · 2025-09-25 T2a · 2026-03-03 T2a |
| **Conservativo:** condición necesaria + demostración | 2 | 2024-05-10 T1 · (recurrente en parciales) |
| **Derivada direccional:** definir; demostrar `f'(X₀,ǔ) = ∇f·ǔ` | 3 | 2025-07-29 T2a · 2026-07-28 T1a |
| **Función potencial:** definir | 2 | 2025-07-15 T2a · 2025-12-09 T2a |
| **Extremos:** definir máx/mín local/absoluto/silla; criterio del Hessiano | 5 | 2024-07-23 T2a · 2024-07-30 T1a · 2024-12-17 T1a · 2025-02-25 T2a · 2025-05-20 T1a |
| **Punto regular** de curva / de superficie parametrizada; superficie parametrizada | 4 | 2024-05-10 T2 · 2024-10-09 T1a · 2025-02-11 T1a |
| **Gradiente ⊥ curva/superficie de nivel** (demostración) | 2 | 2025-02-18 T2a · 2025-12-09 T1a |
| **Regla de la cadena** en forma matricial | 1 | 2024-12-03 T1a |
| **Diferenciabilidad / continuidad:** definir | 3 | 2025-12-02 T2a · 2025-12-16 T2a · 2026-02-24 T1a |
| **Líneas de campo** y equipotenciales: definir y relacionar | 1 | 2024-07-30 T2a |

## Problemas reciclados y equivalencias

Practicar uno sirve por todos los de su grupo:

- **Circulación por `x+y+z = 2 ∩ x²+y² = y` con `Df` dada:** `2025-07-15 P1` ≡ `2025-12-02 P2` (cambia una fila del jacobiano).
- **Flujo por el cilindro `x²+y² = 2x` con `z ≤ 4 − x² − y²`, 1er octante:** `2025-07-15 P4` ≡ `2025-12-02 P4` (cambia el campo).
- **Implícita `xz + z + y + ln(z − xy) = 10` cerca de `(2,1)`:** `2024-05-10 P2` ≡ `2026-03-03 P2` ≡ `2025-07-29 T1a`. **Cayó 3 veces en 2 años** — es el ejercicio más reciclado del dataset.
- **`Área(D*)` con `φ(u,v) = (u+2v, 2u+v)`:** `2025-09-25 T2b` ≡ 2º parcial `2016-07-06 T1` (área 12 vs 6).
- **Plano tangente + flujo por esa porción de plano:** `2024-10-09 P1` ≈ `2025-12-09 P1`.
- **Flujo por paraboloide abierto orientado `z⁺`:** `2025-09-25 P2` ≈ `2025-12-09 P2` ≈ `2026-03-03 P4`.
- **Función partida `xy²/(x²+y²)`-tipo: ¿diferenciable / admite plano tangente en el origen?:** `2024-03-05 T2b` ≡ `2025-12-16 T2b` ≡ `2026-07-28 T1b`.
- **Trayectorias ortogonales entre dos familias con parámetro a determinar:** `2024-12-03 P4` ≈ `2026-03-03 P3`.
- **Derivada direccional nula / máxima de una composición con implícita:** `2024-10-09 P3` ≈ `2024-12-17 P3` ≈ `2026-07-28 P4`.

## Archivos

- **24 finales distintos** entre 2024-03-05 y 2026-07-28.
- 21 en `examenes/` como `AAAA-MM-DD_Final.pdf`; **3 sólo existen dentro de `resueltos/`**
  (2024-03-05, 2024-05-10, 2024-07-23).
- `resueltos/` — 12 resoluciones (cátedra, Alexander Rojas Torres, Sylvina) + las respuestas
  oficiales del 2024-07-23 + 7 fotos del 2026-02-10.
- `duplicados/` — copias con otro nombre o formato del mismo examen (no se indexan aparte).

---

_Índice generado el 2026-09-09 a partir de la capa de texto de 20 PDFs y la lectura con visión de 4 escaneos._
