# Índice de parciales — Primer Parcial AM2

> **Para qué sirve:** los parciales son PDFs tipeados, capturas y fotos. Varios **no tienen capa de texto**, así que no se pueden `grep`ear directamente. Este archivo es la transcripción curada (matemática intacta) de cada examen, con **tags por tema**, para poder buscar y analizar frecuencias sin re-leer las imágenes.
>
> **Cómo buscar** (desde esta carpeta, `examenes/`):
> ```bash
> grep -n "#TrayectoriasOrtogonales" INDICE.md   # todas las trayectorias ortogonales
> grep -n "#DerivadaDireccional" INDICE.md        # todo lo de derivada direccional
> grep -B1 "#Taylor" INDICE.md                     # Taylor, con la línea de fecha arriba
> grep -n "^## " INDICE.md                         # listar todos los exámenes por fecha
> ```
> **Mantenimiento:** cuando agregues un parcial nuevo, sumá su sección acá con los mismos tags (y actualizá la tabla tag→fechas del final). Corré `/indexar-examenes` sobre la imagen y pegá el resultado con este formato.

## Leyenda de tags

**Ecuaciones diferenciales** (cae en casi todos, P1 o P4): `#EDO` `#TrayectoriasOrtogonales`
**Continuidad / diferenciabilidad:** `#Limite` `#Continuidad` `#DerivadasParciales` `#Diferenciabilidad` `#AproximacionLineal`
**Derivada direccional y gradiente:** `#DerivadaDireccional` `#Gradiente`
**Composición / implícita:** `#ReglaCadena` `#DerivacionImplicita`
**Geometría (superficies y curvas):** `#PlanoTangente` `#SuperficieParametrizada` `#CurvaEspacio`
**Aproximación polinómica y extremos:** `#Taylor` `#Extremos`
**Teóricos:** `#Demostracion`

> Convención: cada problema es una línea `- **Pn)** enunciado … → #Tag #Tag`. Los teóricos son `**T1)** / **T2)**`. El tag principal va primero. Los enunciados de exámenes escaneados/foto pueden tener detalles menores aproximados (marcados con «≈»).
>
> Notas de alcance de algunos tags:
> - `#CurvaEspacio` = recta tangente / plano normal a una curva en ℝ³ (dada como intersección de dos superficies o paramétrica `λ(t)`), e intersección curva–superficie.
> - `#PlanoTangente` = plano tangente **y recta normal a una superficie** (explícita, implícita o parametrizada).
> - `#AproximacionLineal` = calcular un valor aproximado vía diferencial (casi siempre con `z` en forma implícita).
> - `#TrayectoriasOrtogonales` siempre va con `#EDO` (es una aplicación de EDO de 1er orden).

---

## 2017-05-05  ·  `2017-05-05_Parcial.PNG` (captura)

- **P1)** Calcular la solución particular de la ecuación diferencial `cos(x)·y' + sin(x)·y = 1` tal que `y(0) = 2`. → #EDO
- **P2)** Hallar las ecuaciones de las rectas normales a la superficie `2x² + 3y² − z² = 5` en `(1, 2, z₀)`. → #PlanoTangente #Gradiente
- **P3)** Siendo `z = u + v·e^(u−v)` tal que `2y − u·x − ln(u) = 0` y `v² = y`, hallar la derivada direccional **mínima** de `z = h(x,y)` en `(2,1)`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x³y²(1 − x − y)` para `(x,y) ≠ (0,0)`. → #Extremos
- **T1)** Definir derivada direccional de una función escalar de dos variables. Calcular las derivadas direccionales de `f(x,y) = {2x²/(x²+2y²) si (x,y)≠(0,0); 0 si (x,y)=(0,0)}` en `(0,0)`. → #Demostracion #DerivadaDireccional #Continuidad
- **T2)** Demostrar que toda función escalar de dos variables diferenciable en un punto es continua en dicho punto. Estudiar la continuidad de la función anterior en ℝ². → #Demostracion #Diferenciabilidad #Continuidad
→ estructura: 4 prácticos + 2 teóricos

## 2017-09-29  ·  `2017-09-29_Parcial.PNG` (captura)

- **P1)** Hallar la solución particular de `y' − y/x − x² = 0` sujeta a `y(1) = 2`. → #EDO
- **P2)** Hallar el punto de intersección del plano `z = 0` con la recta normal a la superficie parametrizada `σ(u,v) = (u·v, u+v, u−v)` en el punto `(x₀, 3, −1)`. → #PlanoTangente #SuperficieParametrizada
- **P3)** Para `x = 1.98`, `y = 1.01` calcular mediante una aproximación lineal el valor de `z`, siendo `e^(xz−2) + yz − 2 = 0`. → #AproximacionLineal #DerivacionImplicita
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x² + xy + 2y² − x − 2y + 1`. → #Extremos
- **T1)** Definir continuidad de una función escalar de ℝ². Estudiar la continuidad de `f(x,y) = {x³/(x²+y) si x²+y≠0; 0 si x²+y=0}` en `(0,0)`. → #Demostracion #Continuidad
- **T2)** Demostrar que la derivada direccional máxima de `f ∈ C¹` es igual a `‖∇f‖`. Indicar las direcciones de derivada direccional nula de `f(x,y) = x³·y + x·y³` en `(1,2)`. → #Demostracion #DerivadaDireccional #Gradiente
→ estructura: 4 prácticos + 2 teóricos

## 2018-07-12  ·  `2018-07-12_Parcial.pdf` (pdf)  ·  ≡ `duplicados/2018-07-12_captura.PNG`

- **P1)** Hallar la familia de curvas ortogonales a `y = C·e^(2x)`. De la familia hallada, indicar la curva que pasa por `(1,1)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Hallar la ecuación de la recta tangente y el plano normal a la curva intersección de `z = x² − y²` y `z = x + y` en `(2,1,3)`. → #CurvaEspacio
- **P3)** Calcular la derivada direccional máxima de `h = g ∘ f⃗` en `(1,1)`, con `g(u,v)` definida por `z − u² + v² + ln(v+z) = 0` y `f⃗(x,y) = (xy², y − x²)`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x − y² − x³ + 2xy`. → #Extremos
- **T1)** Definir derivada parcial de una función escalar de ℝ². Calcular (si existen) las derivadas parciales de `f(x,y) = {x²/y si y≠0; 0 si y=0}` en `(0,0)`. → #Demostracion #DerivadasParciales
- **T2)** Siendo `yₚ` solución particular de `x²y'' − 2y = f(x)` con `y(2)=3`, verificar que `y = x·yₚ` es solución particular de `x·y'' − 2y' = f(x)` que pasa por `(2, y₀)`. → #Demostracion #EDO
→ estructura: 4 prácticos + 2 teóricos

## 2018-10-05  ·  `2018-10-05_Parcial.pdf` (pdf)

- **P1)** Hallar la familia de curvas ortogonales a `y = C·e^(−x)`. Indicar la curva que pasa por `(1,1)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Hallar la ecuación del plano normal a la curva intersección de `y = 2x² + 2z²` y `y = 1 + x² + z²` en `(0,2,1)`. → #CurvaEspacio
- **P3)** Calcular la derivada direccional máxima de `h = g ∘ f⃗` en `(1,1)`, con `g(u,v)` definida por `z − u² + v² + ln(v+z) = 0` y `f⃗(x,y) = (xy², y − x²)`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P4)** Analizar la existencia de extremos **absolutos** de `f(x,y) = x² + y² − 2x` en la región `x² + y² ≤ 4`. → #Extremos #ExtremosLigados
- **T1)** Definir solución general de una EDO. Verificar si `y = C·x·eˣ` es solución de `y'' − 2y' + y = 0` y, en caso afirmativo, si es la solución general. → #Demostracion #EDO
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {x³/y si y≠0; 0 si y=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2019-05-22  ·  `2019-05-22_Parcial.pdf` (pdf)

- **P1)** Indicar la dirección de la derivada direccional máxima de `h = g ∘ f⃗` en `(1,1)`, con `f⃗(x,y) = (y − x², xy²)` y `g(u,v)` definida por `z + u² − v² + ln(u+z) = 0`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P2)** a) Hallar el plano normal a la curva intersección de `z = √(25 − y²)` y `x² + y² = 25` en `(3,4,3)`. b) Determinar el plano que contiene la curva. → #CurvaEspacio
- **P3)** Analizar la existencia de extremos locales de `f(x,y) = y² − xy − x² + x³`. → #Extremos
- **P4)** Hallar la familia de curvas ortogonales a `y = C/x`. Indicar la curva que pasa por `(1,1)`. → #TrayectoriasOrtogonales #EDO
- **T1)** Definir solución general y particular de una EDO de orden `n`. Resolver `y' − y/x − x² = 0`. → #Demostracion #EDO
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {y²/x si x≠0; 0 si x=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2019-08-15  ·  `2019-08-15_Parcial.pdf` (pdf)  ·  ≡ `2022-07-22_Parcial.pdf`, `duplicados/2019-08-15_captura.PNG`

- **P1)** Hallar la familia de curvas ortogonales a `x·y² = C`. Indicar la curva que pasa por `(1,2)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Indicar la dirección de la derivada direccional **nula** de `h = g ∘ f⃗` en `(1,1)`, con `f⃗(x,y) = (xy², y − x²)` y `g(u,v)` definida por `z − u² + v² + ln(v+z) = 0`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P3)** a) Hallar el plano normal a la curva intersección de `x = √(25 − y²)` y `y² + z² = 25` en `(3,4,3)`. b) Determinar el plano que contiene la curva. → #CurvaEspacio
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x² − xy − y² + y`. → #Extremos
- **T1)** Definir solución general y particular de una EDO de orden `n`. Resolver `x·y' − y − x³ = 0`. → #Demostracion #EDO
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {y/x si x≠0; 0 si x=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2019-10-11  ·  `2019-10-11_Parcial.pdf` (pdf)  ·  ≡ `2022-10-05_Parcial-simulacro.pdf`

- **P1)** Hallar la solución de `cos(x)·y' + sin(x)·y = 1` tal que `y = 2` cuando `x = 0`. → #EDO
- **P2)** Hallar la intersección de la recta normal a la superficie `(x,y,z) = (uv, u+v, u²/v)` en `(3,4,9)` con el plano `x + y = 19`. → #PlanoTangente #SuperficieParametrizada
- **P3)** Hallar la derivada direccional máxima de `h = f ∘ g⃗` en `(1,1)`, con `g⃗(u,v) = (u+v, u−v)` y `f(x,y)` definida por `z + x² − y² + ln(z+x−y) = 3`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P4)** Siendo `f ∈ C²` con polinomio de Taylor de grado 2 en `(0,1)` igual a `p(x,y) = 5 + x² + x(y−1) + 4(y−1)²`, hallar la ecuación del plano tangente a la gráfica de `f` en `(0,1,f(0,1))` y analizar si `f` tiene extremo local en `(0,1)`. → #Taylor #PlanoTangente #Extremos
- **T1)** Definir continuidad de una función escalar de `n` variables. Determinar si `f(x,y) = {y/(x−y) si x≠y; 0 si x=y}` es continua en `(0,0)`. → #Demostracion #Continuidad
- **T2)** Definir máximo local de una función escalar de `n` variables. Determinar si `f(x,y) = x² + xy − y² + y + 1` tiene extremos locales y clasificarlos. → #Demostracion #Extremos
→ estructura: 4 prácticos + 2 teóricos

## 2022-05-20  ·  `2022-05-20_Parcial.pdf` (pdf)

> «≈ el encabezado dice "Mayo 5 de 2022"; se conserva la fecha del nombre de archivo (2022-05-20). Verificar cuál es la correcta si aparece otra copia.

- **P1)** Siendo `f ∈ C¹`, `f'(Ā,(0.6;0.8)) = 3` y `f'(Ā,(0.8;0.6)) = 11`, calcular `f'(Ā,(−0.8;0.6))`. → #DerivadaDireccional #Gradiente
- **P2)** Calcular mediante una aproximación lineal el valor de `z` para `(x,y) = (1.03; 1.98)`, siendo `xz + e^(yz−2) − 2 = 0`. → #AproximacionLineal #DerivacionImplicita
- **P3)** Siendo `f ∈ C¹`, `∇f(2,1,3) = (3,7,1)` y `g(x,y) = (xy−y, xy−3, xy−1)`, calcular la derivada direccional máxima de `h(x,y) = f(g(x,y))` en `(2,2)` e indicar la dirección. → #ReglaCadena #DerivadaDireccional #Gradiente
- **P4)** La superficie `Σ` queda definida por `xz + y + ln(x²+y+z−5) − 3 = 0` en un entorno de `Ā = (2,1,z₀)`. Siendo `π₀` el plano tangente a `Σ` en `Ā`, indicar la intersección de `π₀` con el eje `X`. → #PlanoTangente #DerivacionImplicita
- **T1)** Definir mínimo local de una función escalar de `n` variables. Demostrar que `f(x,y) = −1 + x⁶ + y⁴` tiene un mínimo local en el origen. → #Demostracion #Extremos
- **T2)** Calcular `m` de modo que `y(x) = e^(m·x)` sea solución de `y'' + p·y' + q·y = 0`. Expresar `m` en función de `p, q` y usarlo para resolver `y'' − y' − 2y = 0`. → #Demostracion #EDO
→ estructura: 4 prácticos + 2 teóricos

## 2022-06-01  ·  `2022-06-01_Parcial.pdf` (pdf)

- **P1)** Siendo `f ∈ C¹`, `f'(Ā,(−0.6;0.8)) = −2` y `f'(Ā,(0.8;0.6)) = 1`, hallar `f'(Ā,(0.3;−0.4))` e indicar las direcciones en que la derivada direccional es nula en `Ā`. → #DerivadaDireccional #Gradiente
- **P2)** Siendo `g(x,y) = (xy+1, xy−x, xy−1)`, `∇f(7,3,5) = (3,−2,1)` y `f ∈ C¹`, calcular la derivada direccional máxima de `h(x,y) = f(g(x,y))` en `(3,2)` e indicar la dirección. → #ReglaCadena #DerivadaDireccional #Gradiente
- **P3)** Hallar la recta normal a la superficie `Σ`: `x + yz + ln(x+y²−z−3) − 3 = 0` en `Ā = (1,2,z₀)`. Hallar su intersección con el plano `XZ`. → #PlanoTangente #DerivacionImplicita
- **P4)** Hallar la solución de `x·(dy/dx) − 4y = x⁶eˣ` con `y(1) = 1`. → #EDO
- **T1)** Definir continuidad de una función escalar de `n` variables. Determinar si `f(x,y) = {y/(x−y) si x≠y; 0 si x=y}` es continua en `(0,0)`. → #Demostracion #Continuidad
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {y²/x si x≠0; 0 si x=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2022-07-22  ·  `2022-07-22_Parcial.pdf` (pdf)  ·  **≡ 2019-08-15 (mismo examen reutilizado — ver esa sección)**

## 2022-08-11  ·  `2022-08-11_Parcial.pdf` (pdf)  ·  ≡ `duplicados/2022-08-11_foto.jpg`; resuelto por Lucho (nota 7) en `resueltos/AMII 1P 2022-08-11 resuelto-lucho.pdf`

- **P1)** Siendo `z = h(x,y)` tal que `z = u·x·v²`, `u = x√y` y `2v + e^(y−2x) − y/x = 1`, calcular mediante aproximación lineal `h(1.01, 3.98)`. → #AproximacionLineal #ReglaCadena #DerivacionImplicita
- **P2)** Dada `z = f(x,y)` definida implícitamente por `xz + yz + ln(xy + z − 5) − 12 = 0`, calcular la derivada direccional máxima de `f` en `Ā = (1,2)` e indicar la dirección. → #DerivadaDireccional #DerivacionImplicita #Gradiente
- **P3)** Hallar los puntos de intersección de la curva `λ⃗(t) = (t+2, 2t+5, t+1)` con la superficie `x² + (y−3)² − z² = 1`. En ellos, indicar la(s) recta(s) tangente(s) a la curva. → #CurvaEspacio
- **P4)** Hallar la familia de curvas ortogonales a las rectas `y = k·x`. Determinar la curva que contiene a `(3,4)`. → #TrayectoriasOrtogonales #EDO
- **T1)** Enunciar el teorema de la regla de la cadena para funciones vectoriales. Dada `h(x,y) = f(g(x,y))`, calcular `∇h(1,2)` sabiendo que `Df(u,v) = (u·v², u²·v)` es la matriz jacobiana de `f` y `g(x,y) = (2x + y², y·x²)`. → #Demostracion #ReglaCadena #Gradiente
- **T2)** Definir mínimo local de una función escalar de 2 variables. Dada `f(x,y) = x⁴ + x²y⁴ + 3`, analizar si `f(0,0)` es extremo local y clasificarlo. → #Demostracion #Extremos
→ estructura: 4 prácticos + 2 teóricos

## 2022-10-05  ·  `2022-10-05_Parcial-simulacro.pdf` (pdf, simulacro de cátedra)  ·  **≡ 2019-10-11 (mismo examen — ver esa sección)**

## 2022-10-12  ·  `2022-10-12_Parcial.pdf` (pdf)

- **P1)** Hallar la familia de curvas ortogonales a las rectas `y = k·x`. Determinar la curva que contiene a `(3,−4)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Siendo `z = h(x,y)` tal que `z = u·x·v²`, `u = x√y` y `2v + e^(y−2x) − y/x = 1`, calcular mediante aproximación lineal `h(0.99, 4.02)`. → #AproximacionLineal #ReglaCadena #DerivacionImplicita
- **P3)** Dada `z = f(x,y)` definida implícitamente por `xz + yz + ln(xy + z − 5) − 12 = 0`, calcular la derivada direccional **mínima** de `f` en `Ā = (1,2)` e indicar la dirección. → #DerivadaDireccional #DerivacionImplicita #Gradiente
- **P4)** Hallar los puntos de intersección de la curva `λ⃗(t) = (t+2, 2t+5, t+1)` con la superficie `x² + (y−3)² − z² = 1`. En ellos, indicar el plano normal a la curva. → #CurvaEspacio
- **T1)** Enunciar el teorema de la regla de la cadena para funciones vectoriales. Dada `h(x,y) = f(g(x,y))`, calcular `∇h(1,2)` con `g(x,y) = (2x + y², y·x²)` y `Df(u,v) = (u·v², u²·v)`. → #Demostracion #ReglaCadena #Gradiente
- **T2)** Definir mínimo y máximo local de una función escalar de `n` variables. Dada `f(x,y) = x⁴ + x²y⁴ + 3`, analizar si `f(0,0)` es extremo local y clasificarlo. → #Demostracion #Extremos
→ estructura: 4 prácticos + 2 teóricos

## 2022-12-01  ·  `2022-12-01_Parcial.pdf` (pdf)

- **P1)** Siendo `h(x,y) = f(g(x,y))` con `∇f(2,7) = (3,5)`, jacobiana `Dg(x,y) = [[2xy, x²],[y/x, ln(x)]]` y `g(1,2) = (2,7)`, calcular la derivada direccional máxima de `h` en `(1,2)` e indicar la dirección. → #DerivadaDireccional #ReglaCadena #Gradiente
- **P2)** Sea `f ∈ C³` con polinomio de Taylor de 2º orden en `(2,2)` igual a `p(u,v) = 14 + v² − 2uv − u²`. Si `h(x,y) = f(x²−2y, y²+xy−1)`, estimar `h(1.98, 1.02)` con una aproximación lineal. → #Taylor #AproximacionLineal #ReglaCadena
- **P3)** Hallar la intersección de la recta tangente a la curva `z = 9 − x²`, `z = y` en `(2,5,5)` con el plano `XZ`. → #CurvaEspacio
- **P4)** Hallar la familia de curvas ortogonales a `y = k/x`. Determinar la curva que contiene a `(3,4)`. → #TrayectoriasOrtogonales #EDO
- **T1)** Dado `g(x,y) = {x²/(x²+y⁴) si (x,y)≠(0,0); 0 si (x,y)=(0,0)}`, indicar si son V o F (justificar): a) es discontinuo en `(0,0)`; b) no admite derivada en ninguna dirección en `(0,0)`. → #Demostracion #Continuidad #DerivadaDireccional #Limite
- **T2)** Definir conjunto de nivel de un campo escalar. Analizar si el conjunto de nivel 2 de `f(x,y,z) = 1 + e^(z−xy−1)` admite algún punto donde el plano tangente sea paralelo al plano `XY`. → #Demostracion #PlanoTangente #Gradiente
→ estructura: 4 prácticos + 2 teóricos

## 2022-12-16  ·  `2022-12-16_Parcial.pdf` (pdf)

- **P1)** Dada la familia `y = Cx`, hallar la curva de la familia ortogonal que pasa por `(4,−3)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Dada `z = f(x,y)` definida implícitamente por `x·ln(z + x − 2) + y·e^(yz−6) − 3 = 0`, calcular aproximadamente `f(0.99, 3.02)` mediante una aproximación lineal. → #AproximacionLineal #DerivacionImplicita
- **P3)** Dada `h(x,y) = f(g(x,y))` con `∇f(u,v) = (2uv, u² + 3v²)`, calcular `∇h(a,b)` sabiendo que `g(a,b) = (2,1)`, `g'ₓ(a,b) = (3,5)` y `g'_y(a,b) = (1,4)`. → #ReglaCadena #Gradiente
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x²y − x² + y²/2 − 5y + 1` en su dominio natural (clasificarlos y calcularlos). → #Extremos
- **T1)** Calcular `m` de modo que `y(x) = e^(m·x)` sea solución de `y'' + p·y' + q·y = 0`. Expresar `m` en función de `p, q` y usarlo para resolver `y'' − y' − 2y = 0`. → #Demostracion #EDO
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {y²/x si x≠0; 0 si x=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2023-05-31  ·  `2023-05-31_Parcial.pdf` (pdf)

- **P1)** Siendo `h(x,y) = f(g(x,y))` con `∇f(2,1) = (3,5)`, jacobiana `Dg(x,y) = [[2xy, x²],[2x+2y, 2x−2y]]` y `g(1,2) = (2,1)`, calcular la derivada direccional máxima de `h` en `(1,2)` e indicar la dirección. → #DerivadaDireccional #ReglaCadena #Gradiente
- **P2)** Sea `f ∈ C³` con polinomio de Taylor de 2º orden en `(2,3)` igual a `p(u,v) = 9 + v² − 2uv − u²`. Si `h(x,y) = f(x²−2y, xy+1)`, estimar `h(2.01, 0.98)` con una aproximación lineal. → #Taylor #AproximacionLineal #ReglaCadena
- **P3)** Hallar la intersección del plano normal a la curva `z = 5 − x²`, `z = y` en `(2,1,1)` con el eje `X`. → #CurvaEspacio
- **P4)** Hallar la familia de curvas ortogonales a `y = k·x³`. Indicar las curvas de ambas familias que pasan por `(1,1)`; determinar la que contiene a `(3,4)`. → #TrayectoriasOrtogonales #EDO
- **T1)** Dado `g(x,y) = {y²/(x⁴+y²) si (x,y)≠(0,0); 0 si (x,y)=(0,0)}`, indicar si son V o F (justificar): a) es discontinuo en `(0,0)`; b) no admite derivada en ninguna dirección en `(0,0)`. → #Demostracion #Continuidad #DerivadaDireccional #Limite
- **T2)** Siendo `f ∈ C¹` con `f'((1,1),(1,3)) = 17` y `lím_{t→0} [f(1+t,1) − f(1,1)]/t = 5`, calcular `f'_y(1,1)`. → #DerivadaDireccional #DerivadasParciales #Gradiente
→ estructura: 4 prácticos + 2 teóricos

## 2023-07-28  ·  `2023-07-28_Parcial.pdf` (pdf)

- **P1)** Hallar la familia de curvas ortogonales a `x·y² = k`. Indicar la curva que pasa por `(1,3)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Indicar la dirección de la derivada direccional **mínima** de `h = g ∘ f⃗` en `(1,1)`, con `f⃗(x,y) = (y − x², xy²)` y `g(u,v)` definida por `z + u² − v² + ln(u+z) = 0`. → #DerivadaDireccional #ReglaCadena #DerivacionImplicita #Gradiente
- **P3)** Hallar la recta tangente a la curva intersección de `y = √(25 − x²)` y `x² + z² = 25` en `(4,3,3)`. Determinar el plano que contiene la curva. → #CurvaEspacio
- **P4)** Analizar la existencia de extremos locales de `f(x,y) = x² − y² − xy + y + 1`. → #Extremos
- **T1)** Definir solución general y particular de una EDO de orden `n`. Resolver `cos(x)·y' + sin(x)·y − 1 = 0`. → #Demostracion #EDO
- **T2)** Definir derivada direccional de una función escalar de ℝ². Calcular (si existen) las derivadas direccionales de `f(x,y) = {y/x² si x≠0; 0 si x=0}` en `(0,0)`. → #Demostracion #DerivadaDireccional
→ estructura: 4 prácticos + 2 teóricos

## 2024-05-17  ·  `2024-05-17_Parcial-simulacro.pdf` (pdf, simulacro de cátedra)

- **P1)** Hallar la familia de curvas ortogonales a `y = k·x³`. Indicar las curvas de ambas familias que pasan por `(3,4)`. → #TrayectoriasOrtogonales #EDO
- **P2)** Hallar los puntos de intersección de la curva `y = x ∧ x² + z = 3` con el paraboloide `z − x² − y² = 0`. Determinar el ángulo entre la recta tangente a la curva y la recta normal al paraboloide en dichos puntos. → #CurvaEspacio #PlanoTangente
- **P3)** Siendo `f ∈ C³` con polinomio de Taylor de 2º grado en `(0,1)` igual a `p(x,y) = 5 + x² + x(y−1) + 4(y−1)²`, hallar el plano tangente a la gráfica de `f` en `(0,1,f(0,1))` y analizar si `f` alcanza un extremo en `(0,1)`. → #Taylor #PlanoTangente #Extremos
- **P4)** Siendo `z = eˣ·cos(y)` con `x³ + eˣ − t² − t − 1 = 0` y `y·t² + y²·t + y − t + 1 = 0`, calcular `dz/dt` en `t = 0`. → #ReglaCadena #DerivacionImplicita
- **T1)** Dado `g(x,y) = {y²/(x⁴+y²) si (x,y)≠(0,0); 0 si (x,y)=(0,0)}`, indicar si son V o F (justificar): a) es discontinuo en `(0,0)`; b) no admite derivada en ninguna dirección en `(0,0)`. → #Demostracion #Continuidad #DerivadaDireccional
- **T2)** Siendo `f ∈ C¹` con `f'((1,1),(1,3)) = 17` y `lím_{t→0} [f(1+t,1) − f(1,1)]/t = 5`, calcular `f'_y(1,1)`. → #DerivadaDireccional #DerivadasParciales #Gradiente
→ estructura: 4 prácticos + 2 teóricos  ·  ⚠ rotulado "PRIMER PARCIAL (simulacro)"; ensamblado con problemas reciclados (P3 = Taylor de 2019-10-11; T1/T2 = teóricos de 2023-05-31).

## 2026-05-22  ·  `2026-05-22_Parcial.pdf` (pdf)  ·  **[el más reciente — mejor referencia para el recuperatorio]**

- **P1)** Hallar el plano normal a la curva intersección de `x + 1 = (z − 4)²` e `y = 3` en `(3,3,6)`. → #CurvaEspacio
- **P2)** Calcular mediante una aproximación lineal el valor de `z` para `(x,y) = (1.01; 1.98)`, siendo `xz + e^(yz−2) − 2 = 0`. → #AproximacionLineal #DerivacionImplicita
- **P3)** Siendo `f ∈ C¹`, `∇f(2,1,3) = (3,2,−1)` y `g(x,y) = (xy − y, xy − 3, xy − 1)`, calcular la derivada direccional máxima de `h(x,y) = f(g(x,y))` en `(2,2)` e indicar la dirección. → #ReglaCadena #DerivadaDireccional #Gradiente
- **P4)** Siendo `z = f(x,y)` definida implícitamente por `y + xz + z + ln(z − xy) = 10`, hallar la recta normal a la gráfica de `f` en `(2,1,f(2,1))`. Analizar si esa recta interseca la superficie `x = 7 − y²` y, en caso afirmativo, indicar los puntos. → #DerivacionImplicita #PlanoTangente
- **T1)** Definir mínimo y máximo local de una función escalar de `n` variables. Analizar la existencia de extremos locales de `f(x,y) = −3 + 2x² − 4y⁴` en su dominio. → #Demostracion #Extremos
- **T2)** Definir superficie parametrizada y punto regular. Siendo `σ(u,v) = (u+v, u−v, u²−v²)` la parametrización de `S`, analizar si `(3,2,1)` es un punto regular de `S`. → #Demostracion #SuperficieParametrizada
→ estructura: 4 prácticos + 2 teóricos  ·  (en la hoja el teórico va rotulado T2 y luego T1; se respeta el contenido)

---

## Índice inverso: tema → fechas (para búsqueda rápida)

> Frecuencias sobre **16 exámenes reales de contenido distinto** (N = 16), más 2 simulacros de cátedra (2024-05-17 único; 2022-10-05 ≡ 2019-10-11). Se descuentan las 2 equivalencias (2022-07-22≡2019-08-15, 2022-10-05≡2019-10-11). Los simulacros se marcan `(sim)` y no cuentan en los porcentajes.

| Tag | Aparece en | Frecuencia |
|---|---|---|
| `#TrayectoriasOrtogonales` / `#EDO` (juntas) | 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-08-11, 2022-10-12, 2022-12-01, 2022-12-16, 2023-05-31, 2023-07-28, 2024-05-17 (sim) | ~11/15 · **casi fijo (P1 o P4)** |
| `#EDO` (sola: 1er orden, PVI o `y=e^{mx}`) | 2017-05-05, 2017-09-29, 2018-07-12 (T), 2018-10-05 (T), 2019-05-22 (T), 2019-08-15 (T), 2019-10-11, 2022-05-20 (T), 2022-06-01, 2022-12-16 (T), 2023-07-28 (T) | práctico o teórico en casi todos |
| `#DerivadaDireccional` | 2017-05-05, 2017-09-29, 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-05-20, 2022-06-01, 2022-08-11, 2022-10-12, 2022-12-01, 2022-12-16, 2023-05-31, 2023-07-28, 2026-05-22 | **15/15 · universal** |
| `#Gradiente` | prácticamente todos los de derivada direccional | ~14/15 |
| `#ReglaCadena` | 2017-05-05, 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2019-10-11, 2022-05-20, 2022-06-01, 2022-08-11, 2022-10-12, 2022-12-01, 2022-12-16, 2023-05-31, 2023-07-28, 2024-05-17 (sim), 2026-05-22 | **~14/15** |
| `#DerivacionImplicita` | 2017-05-05, 2017-09-29, 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-05-20, 2022-08-11, 2022-10-12, 2022-12-16, 2023-07-28, 2024-05-17 (sim), 2026-05-22 | **~12/15** |
| `#Extremos` | 2017-05-05, 2017-09-29, 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2019-10-11, 2022-05-20 (T), 2022-08-11 (T), 2022-10-12 (T), 2022-12-16, 2023-07-28, 2026-05-22 (T) | **~13/15** |
| `#CurvaEspacio` | 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-08-11, 2022-10-12, 2022-12-01, 2023-05-31, 2023-07-28, 2024-05-17 (sim), 2026-05-22 | **~10/15** |
| `#AproximacionLineal` | 2017-09-29, 2022-05-20, 2022-08-11, 2022-10-12, 2022-12-01, 2022-12-16, 2023-05-31, 2026-05-22 | ~8/15 (fuerte en 2022+) |
| `#PlanoTangente` (superficie/recta normal) | 2017-05-05, 2017-09-29, 2019-10-11, 2022-05-20, 2022-06-01, 2022-12-01 (T), 2024-05-17 (sim), 2026-05-22 | ~7/15 |
| `#Continuidad` | 2017-05-05 (T), 2017-09-29 (T), 2019-10-11 (T), 2022-06-01 (T), 2022-12-01 (T), 2023-05-31 (T), 2024-05-17 (sim, T) | teórico frecuente |
| `#Taylor` | 2019-10-11, 2022-12-01, 2023-05-31, 2024-05-17 (sim) | ~4/15 |
| `#SuperficieParametrizada` | 2017-09-29, 2019-10-11, 2026-05-22 (T) | ~3/15 |
| `#DerivadasParciales` | 2018-07-12 (T), 2023-05-31 (T) | teórico ocasional |
| `#Limite` | 2022-12-01 (T), 2023-05-31 (T) | dentro de teóricos V/F |

## Problemas reciclados (idénticos o casi entre fechas — oro para practicar)

- **Trayectorias ortogonales + curva por un punto** → 2018-07-12 (`y=Ce^{2x}`), 2018-10-05 (`y=Ce^{−x}`), 2019-05-22 (`y=C/x`), 2019-08-15 (`xy²=C`), 2022-08-11 (`y=kx`), 2022-10-12 (`y=kx`), 2022-12-01 (`y=k/x`), 2022-12-16 (`y=Cx`), 2023-05-31 (`y=kx³`), 2023-07-28 (`xy²=k`), 2024-05-17 (`y=kx³`). **(el problema más reciclado del 1P — cae casi siempre en P1 o P4)**
- **`h = g∘f` con `g` implícita → derivada direccional máx/mín/nula** (familia `f⃗=(xy²,y−x²)`, `g: z−u²+v²+ln(v+z)=0`) → 2018-07-12 (máx), 2018-10-05 (máx), 2019-05-22 (máx, variante), 2019-08-15 (nula), 2023-07-28 (mín, variante). **(≥5 veces)**
- **Aproximación lineal con `z` implícita** → dos sub-familias: `xz+e^{yz−2}−2=0` (2022-05-20, 2026-05-22, y el análogo `e^{xz−2}+yz−2=0` de 2017-09-29) y `z=u·x·v²`, `u=x√y`, `2v+e^{y−2x}−y/x=1` (2022-08-11 con `h(1.01,3.98)`, 2022-10-12 con `h(0.99,4.02)`). **(≥6 veces)**
- **`h=f(g)` con `∇f` o jacobiana dados → derivada direccional máxima** → 2022-05-20, 2022-06-01, 2022-12-01, 2022-12-16, 2023-05-31, 2026-05-22. **(patrón moderno 2022+, 6 veces)**
- **Curva intersección de dos superficies (o `λ(t)`) → recta tangente / plano normal** → 2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-08-11, 2022-10-12, 2022-12-01, 2023-05-31, 2023-07-28, 2026-05-22. El caso `x=√(25−y²) ∧ y²+z²=25 en (3,4,3)` se repite exacto en 2019-08-15 y 2023-07-28 (variante). **(≥10 veces)**
- **Taylor grado 2 → plano tangente + extremo**, mismo `p(x,y)=5+x²+x(y−1)+4(y−1)²` → 2019-10-11, 2022-10-05 (sim), 2024-05-17 (sim). Variante Taylor + aproximación vía composición → 2022-12-01 (`p=14+v²−2uv−u²`), 2023-05-31 (`p=9+v²−2uv−u²`).
- **Extremos locales libres por Hessiano** (polinomio cuadrático/cúbico) → 2017-05-05, 2017-09-29, 2018-07-12, 2019-05-22, 2019-08-15, 2022-12-16, 2023-07-28, y como teórico en 2019-10-11, 2022-05-20, 2022-08-11, 2022-10-12. **(casi universal)**

### Teóricos reciclados
- **Derivadas direccionales por definición de función partida en `(0,0)`** (`y²/x`, `y/x`, `y/x²`, `x³/y`, `x²/y`) → 2018-07-12 (T1, `x²/y` parciales), 2018-10-05 (`x³/y`), 2019-05-22 (`y²/x`), 2019-08-15 (`y/x`), 2022-06-01 (`y²/x`), 2022-12-16 (`y²/x`), 2023-07-28 (`y/x²`). **(el teórico más reciclado)**
- **Continuidad de función partida en `(0,0)`** (`y/(x−y)`, `x³/(x²+y)`) → 2017-09-29, 2019-10-11, 2022-06-01, 2022-10-05 (sim).
- **V/F: campo partido discontinuo / no admite derivada direccional** (`x²/(x²+y⁴)`, `y²/(x⁴+y²)`) → 2022-12-01, 2023-05-31, 2024-05-17 (sim).
- **Enunciar regla de la cadena + calcular `∇h` con jacobiana `Df=(uv²,u²v)`, `g=(2x+y²,yx²)`** → 2022-08-11, 2022-10-12.
- **`m` tal que `y=e^{mx}` es solución de `y''+py'+qy=0`; aplicar a `y''−y'−2y=0`** → 2022-05-20, 2022-12-16.
- **`f'((1,1),(1,3))=17` y `lím[...]=5` → `f'_y(1,1)`** → 2023-05-31, 2024-05-17 (sim).
- **Definir solución general/particular de EDO + resolver** (`x·y'−y−x³=0`, `y'−y/x−x²=0`, `cos x·y'+sin x·y=1`) → 2019-05-22, 2019-08-15, 2022-07-22 (≡), 2023-07-28.

## Equivalencias (mismo examen, no practicar dos veces)

- `2022-07-22` **≡** `2019-08-15` (mismo examen reutilizado; además `duplicados/2019-08-15_captura.PNG` es una captura del mismo).
- `2022-10-05` (simulacro) **≡** `2019-10-11` (mismo examen).
- `2018-07-12_Parcial.pdf` y `duplicados/2018-07-12_captura.PNG` son el mismo examen (PDF tipeado + captura).
- `2022-08-11_Parcial.pdf`, `duplicados/2022-08-11_foto.jpg` y `resueltos/AMII 1P 2022-08-11 resuelto-lucho.pdf` son el mismo examen (enunciado + foto + resolución manuscrita de Lucho, nota 7).

## Fuera de dataset

- **`_fuera-dataset_2doParcial-2017-07-06.PNG`** — es un **SEGUNDO parcial** (rótulo "SEGUNDO PARCIAL", 2017-07-06) que estaba mal archivado entre los del primero. No se computa en las frecuencias del 1P. Si querés, se puede indexar en `../../segundo-parcial/examenes/` con `/indexar-examenes` (temas: EDO 1er orden, plano tangente a superficie paramétrica, aproximación lineal, extremos, continuidad — de arrastre del 1P).
- **`resueltos/`** — 11 exámenes resueltos por la cátedra + `Parciales varios.pdf` (compilación) + la resolución de Lucho del 2022-08-11. Son **soluciones**, no enunciados nuevos: no se indexan como exámenes; sirven de clave de respuestas para el banco de la estrategia.

---

*Índice generado el 2026-07-10 a partir de la lectura con visión (5 subagentes en paralelo) de 24 archivos de `examenes/`: 16 exámenes reales de contenido distinto + 2 simulacros de cátedra (uno ≡ a un real), 4 duplicados/equivalencias y 1 segundo parcial mal archivado. Los enunciados de exámenes escaneados/foto pueden tener detalles menores aproximados («≈»). Cobertura temporal: 2017–2026.*
