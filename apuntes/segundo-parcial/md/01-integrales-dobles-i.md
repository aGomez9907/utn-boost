# Integrales dobles I

> Fuente: https://www.youtube.com/watch?v=Gz884lGtXrk

---

## Índice
- [00:32](https://www.youtube.com/watch?v=Gz884lGtXrk&t=32s) — Región de integración y definición de integral doble
- [04:10](https://www.youtube.com/watch?v=Gz884lGtXrk&t=250s) — 📝 Ejercicio 1: Integral doble de $6-x-y$ sobre un triángulo
- [14:09](https://www.youtube.com/watch?v=Gz884lGtXrk&t=849s) — Propiedad de linealidad
- [15:14](https://www.youtube.com/watch?v=Gz884lGtXrk&t=914s) — Área de una región como integral doble de la función unitaria
- [18:35](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1115s) — 📝 Ejercicio 2: Área de la región del Ejercicio 1
- [21:17](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1277s) — Valor medio de una función de dos variables
- [22:19](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1339s) — 📝 Ejercicio 3: Valor medio de $6-x-y$ en el triángulo
- [30:18](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1818s) — Interpretación geométrica: la integral doble como volumen
- [38:14](https://www.youtube.com/watch?v=Gz884lGtXrk&t=2294s) — 📝 Ejercicio 4: Volumen de la esfera de radio $R$
- [1:00:56](https://www.youtube.com/watch?v=Gz884lGtXrk&t=3656s) — Aditividad respecto de la región de integración
- [1:02:29](https://www.youtube.com/watch?v=Gz884lGtXrk&t=3749s) — 📝 Ejercicio 5: Integral de $x+y$ sobre una región partida en dos

---

## Región de integración y definición de integral doble [00:32](https://www.youtube.com/watch?v=Gz884lGtXrk&t=32s)

La integral doble es una **extensión** de la integral de funciones de una variable al caso de funciones de **dos variables**.

Se supone una función $f$ **continua** en un conjunto $D$ del plano (la **región de integración**) que tiene una forma particular: la coordenada $x$ de cada punto varía entre dos constantes $a$ y $b$, y la coordenada $y$ está limitada por debajo por la gráfica de una función $g(x)$ y por arriba por la gráfica de una función $h(x)$, siendo $g$ y $h$ **continuas**.

$$
D = \{(x,y) : a \le x \le b,\ g(x) \le y \le h(x)\}
$$

Gráficamente, los puntos de $D$ están limitados por la recta $x=a$ por la izquierda, la recta $x=b$ por la derecha, la gráfica de $g(x)$ por debajo y la gráfica de $h(x)$ por arriba.

La **integral doble** de $f$ sobre la región $D$ se define y se calcula como una **integral iterada**:

$$
\iint_D f\,dA = \int_a^b \left( \int_{g(x)}^{h(x)} f(x,y)\,dy \right) dx
$$

Primero se resuelve la integral **interior** (respecto de $y$), tratando a $x$ como constante y usando como límites las funciones $g(x)$ y $h(x)$. Una vez resuelta, el resultado (que depende solo de $x$) se integra respecto de $x$ entre $a$ y $b$.

> Nota: la condición de que $g$ y $h$ sean continuas es necesaria para esta definición. Más adelante se verá qué hacer cuando las funciones que limitan la región no son continuas.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=Gz884lGtXrk&t=250s">04:10</a>: Integral doble de $6-x-y$ sobre un triángulo</summary>

Calcular la integral doble de la función $f(x,y) = 6 - x - y$ sobre la región $D$ del plano definida por

$$
0 \le x \le 2, \qquad 0 \le y \le 4 - 2x
$$

Es decir, $D$ es el triángulo formado por los puntos que están por encima de la recta $y=0$ y por debajo de la recta $y = 4 - 2x$, con $x$ variando entre $0$ y $2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Aplicar la definición de integral doble, planteando la integral iterada.

$$
\iint_D f\,dA = \int_0^2 \left( \int_0^{4-2x} (6 - x - y)\,dy \right) dx
$$

**Paso 2:** Resolver la integral interior respecto de $y$ (la integral de una suma es la suma de las integrales; $x$ se trata como constante).

$$
\int_0^{4-2x} (6 - x - y)\,dy = \left[ 6y - xy - \frac{y^2}{2} \right]_0^{4-2x}
$$

**Paso 3:** Reemplazar $y$ por $4-2x$ (al reemplazar por $0$ los tres términos se anulan).

$$
= 6(4-2x) - x(4-2x) - \frac{(4-2x)^2}{2}
$$

**Paso 4:** Operar algebraicamente cada término.

$$
6(4-2x) = 24 - 12x, \qquad x(4-2x) = 4x - 2x^2
$$

$$
\frac{(4-2x)^2}{2} = \frac{16 - 16x + 4x^2}{2} = 8 - 8x + 2x^2
$$

**Paso 5:** Reunir los términos. Los términos cuadráticos se cancelan; quedan un término lineal y uno independiente.

$$
(24 - 12x) - (4x - 2x^2) - (8 - 8x + 2x^2) = -8x + 16
$$

**Paso 6:** Integrar el resultado respecto de $x$ entre $0$ y $2$.

$$
\int_0^2 (-8x + 16)\,dx = \left[ -4x^2 + 16x \right]_0^2
$$

**Paso 7:** Evaluar. Al reemplazar $x=2$: $-4\cdot 4 + 16\cdot 2 = -16 + 32 = 16$; al reemplazar $x=0$ da $0$.

$$
\iint_D (6 - x - y)\,dA = 16
$$

Resolver una integral doble se reduce a resolver **dos integrales simples sucesivas**, primero respecto de una variable y luego respecto de la otra.

</details>

</details>

## Propiedad de linealidad [14:09](https://www.youtube.com/watch?v=Gz884lGtXrk&t=849s)

Como resolver una integral doble equivale a resolver dos integrales simples sucesivas, muchas propiedades de las integrales simples se **extienden** a las integrales dobles. En particular, la **linealidad**:

$$
\iint_D (f + g)\,dA = \iint_D f\,dA + \iint_D g\,dA
$$

$$
\iint_D k\,f\,dA = k \iint_D f\,dA
$$

La integral de una suma es la suma de las integrales, y cualquier constante $k$ dentro del integrando puede extraerse fuera de él, igual que en las integrales simples.

## Área de una región como integral doble de la función unitaria [15:14](https://www.youtube.com/watch?v=Gz884lGtXrk&t=914s)

Para una región de integración $D$ de la forma habitual, se tiene

$$
\iint_D f\,dA = \int_a^b \int_{g(x)}^{h(x)} f(x,y)\,dy\,dx
$$

Si la función que se integra es la **función unitaria** ($f \equiv 1$), la integral interior da

$$
\int_{g(x)}^{h(x)} 1\,dy = \Big[ y \Big]_{g(x)}^{h(x)} = h(x) - g(x)
$$

de modo que

$$
\iint_D 1\,dA = \int_a^b \big( h(x) - g(x) \big)\,dx = \text{Área}(D)
$$

Este último resultado ya se conocía de Análisis I: la integral de $h - g$ entre $a$ y $b$ es el **área** de la región comprendida entre las dos curvas. Por lo tanto, la integral doble de la función unitaria sobre $D$ da el **área de la región de integración**.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=Gz884lGtXrk&t=1115s">18:35</a>: Área de la región del Ejercicio 1</summary>

Calcular el área de la región $D$ del Ejercicio 1 (el triángulo de base $2$ y altura $4$ limitado por la recta $y = 4 - 2x$) usando una integral doble.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear la integral doble de la función unitaria sobre $D$.

$$
\text{Área}(D) = \int_0^2 \int_0^{4-2x} 1\,dy\,dx
$$

**Paso 2:** Resolver la integral interior respecto de $y$.

$$
\int_0^{4-2x} 1\,dy = \Big[ y \Big]_0^{4-2x} = (4 - 2x) - 0 = 4 - 2x
$$

**Paso 3:** Integrar respecto de $x$ entre $0$ y $2$.

$$
\int_0^2 (4 - 2x)\,dx = \Big[ 4x - x^2 \Big]_0^2
$$

**Paso 4:** Evaluar en $x=2$: $4\cdot 2 - 2^2 = 8 - 4 = 4$; en $x=0$ da $0$.

$$
\text{Área}(D) = 4
$$

El resultado es razonable: el área del triángulo es $\dfrac{\text{base}\cdot\text{altura}}{2} = \dfrac{2\cdot 4}{2} = 4$.

</details>

</details>

## Valor medio de una función de dos variables [21:17](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1277s)

Se define el **valor medio** (o valor promedio) de una función $f$ continua en una región $D$ como el cociente entre la integral doble de la función y el área de $D$:

$$
\bar{f} = \frac{\displaystyle \iint_D f\,dA}{\text{Área}(D)} = \frac{\displaystyle \iint_D f\,dA}{\displaystyle \iint_D 1\,dA}
$$

El denominador es el área de la región $D$, que a su vez puede escribirse como la integral doble de la función unitaria sobre $D$.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=Gz884lGtXrk&t=1339s">22:19</a>: Valor medio de $6-x-y$ en el triángulo</summary>

Calcular el valor medio de la función $f(x,y) = 6 - x - y$ en la región triangular $D$ de los ejercicios anteriores.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Usar los resultados ya calculados: la integral de $f$ sobre $D$ vale $16$ (Ejercicio 1) y el área de $D$ vale $4$ (Ejercicio 2).

**Paso 2:** Aplicar la definición de valor medio.

$$
\bar{f} = \frac{\displaystyle \iint_D f\,dA}{\text{Área}(D)} = \frac{16}{4} = 4
$$

El valor medio de $f$ en el triángulo es $4$. Es un valor razonable: como la función es continua sobre $D$ y toma valores entre $4$ (en el vértice $(2,0)$: $6-2-0=4$) y $6$ (en el vértice $(0,0)$: $6$), llegando incluso a valer $12$ en $(0,4)$ [poco claro en la transcripción], su promedio es un valor intermedio.

</details>

</details>

## Interpretación geométrica: la integral doble como volumen [30:18](https://www.youtube.com/watch?v=Gz884lGtXrk&t=1818s)

En el caso particular en que la gráfica de $f$ sea **positiva** (la superficie $z = f(x,y)$ está por encima del plano $xy$), la integral doble

$$
\iint_D f\,dA
$$

representa el **volumen** del sólido limitado:

- por **arriba**, por la gráfica $z = f(x,y)$;
- por **debajo**, por el plano $xy$;
- por **delante y detrás**, por los planos $x = a$ y $x = b$;
- por **izquierda y derecha**, por las superficies $y = g(x)$ y $y = h(x)$ (que son superficies normales al plano $xy$).

La justificación se ve en la integral iterada: la integral interior

$$
\int_{g(x)}^{h(x)} f(x,y)\,dy
$$

representa el **área de la sección** del sólido obtenida al cortarlo con un plano paralelo al plano $yz$ ubicado a una coordenada $x$ fija. Esa área depende de $x$; al integrarla entre $a$ y $b$ se obtiene el volumen total del sólido.

Volviendo al Ejemplo 1, el valor $16$ es el volumen del cuerpo limitado por el plano $z = 6 - x - y$ por arriba, el plano $xy$ por debajo, y los planos $x=0$ (plano $xz$), $x=2$, $y=0$ (plano $yz$) e $y = 4 - 2x$ por los laterales. Visto desde arriba, ese sólido proyecta el triángulo de la región $D$, con la "tapa" superior inclinada.

> Esta interpretación como volumen vale **solo** si la gráfica de $f$ está por encima del plano $xy$. Si la función toma valores positivos y negativos, se compensan áreas y la integral ya no representa un volumen (análogo a $\int_0^{2\pi}\sin x\,dx = 0$ en integrales simples).

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=Gz884lGtXrk&t=2294s">38:14</a>: Volumen de la esfera de radio $R$</summary>

Calcular el volumen limitado por una superficie esférica de radio $R$ centrada en el origen, usando integrales dobles.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Interpretar la esfera como dos gráficas de funciones de dos variables. La semiesfera superior es la gráfica de

$$
f_2(x,y) = \sqrt{R^2 - x^2 - y^2}
$$

y la semiesfera inferior es la gráfica de

$$
f_1(x,y) = -\sqrt{R^2 - x^2 - y^2}
$$

(despejando $z$ de la ecuación de la esfera $x^2 + y^2 + z^2 = R^2$: $z = \pm\sqrt{R^2 - x^2 - y^2}$).

**Paso 2:** El volumen es la integral doble de la función de arriba menos la de abajo sobre la región $D$, igual que el área entre dos curvas en Análisis I (la de arriba menos la de abajo).

$$
V = \iint_D \big( f_2 - f_1 \big)\,dA
$$

**Paso 3:** La región $D$ es el interior de la circunferencia de radio $R$ en el plano $xy$ (intersección de la esfera con $z=0$: $x^2 + y^2 = R^2$). Así, $x$ varía entre $-R$ y $R$, y para cada $x$ fijo, $y$ varía entre las dos ramas de la circunferencia.

$$
-R \le x \le R, \qquad -\sqrt{R^2 - x^2} \le y \le \sqrt{R^2 - x^2}
$$

**Paso 4:** Como $f_2 - f_1 = 2\sqrt{R^2 - x^2 - y^2}$, plantear la integral iterada.

$$
V = \int_{-R}^{R} \int_{-\sqrt{R^2-x^2}}^{\sqrt{R^2-x^2}} 2\sqrt{R^2 - x^2 - y^2}\,dy\,dx
$$

**Paso 5:** Resolver la integral interior respecto de $y$ usando la fórmula de tabla

$$
\int \sqrt{a^2 - y^2}\,dy = \frac{y}{2}\sqrt{a^2 - y^2} + \frac{a^2}{2}\arcsin\!\left(\frac{y}{a}\right)
$$

donde, en este caso, $a^2 = R^2 - x^2$ (es decir, $a = \sqrt{R^2 - x^2}$) y la variable de integración es $y$.

**Paso 6:** Evaluar entre $y = -\sqrt{R^2-x^2}$ e $y = \sqrt{R^2-x^2}$. En el término con la raíz, al reemplazar $y$ por $\pm\sqrt{R^2-x^2}$ el radicando $R^2 - x^2 - y^2$ da $0$, por lo que ese término se anula en ambos extremos. Solo sobrevive el término del arcoseno.

$$
= \frac{R^2 - x^2}{2}\arcsin(1) - \frac{R^2 - x^2}{2}\arcsin(-1)
$$

**Paso 7:** Como $\arcsin(1) = \dfrac{\pi}{2}$ y $\arcsin(-1) = -\dfrac{\pi}{2}$ (el arcoseno está definido entre $-\tfrac{\pi}{2}$ y $\tfrac{\pi}{2}$), la integral interior queda

$$
\frac{R^2 - x^2}{2}\cdot\frac{\pi}{2} - \frac{R^2 - x^2}{2}\cdot\left(-\frac{\pi}{2}\right) = 2\cdot\frac{R^2 - x^2}{2}\cdot\frac{\pi}{2} = \frac{\pi}{2}(R^2 - x^2)
$$

**Paso 8:** Volver a la integral exterior (con el factor $2$ del Paso 4). Simplificando las constantes queda

$$
V = \pi \int_{-R}^{R} (R^2 - x^2)\,dx
$$

**Paso 9:** Integrar respecto de $x$.

$$
V = \pi \left[ R^2 x - \frac{x^3}{3} \right]_{-R}^{R}
$$

**Paso 10:** Evaluar. En $x=R$: $R^3 - \dfrac{R^3}{3} = \dfrac{2}{3}R^3$; en $x=-R$: $-\dfrac{2}{3}R^3$. Restando (menos por menos da más):

$$
V = \pi\left( \frac{2}{3}R^3 + \frac{2}{3}R^3 \right) = \frac{4}{3}\pi R^3
$$

Se recupera la fórmula conocida del volumen de la esfera de radio $R$.

</details>

</details>

## Aditividad respecto de la región de integración [1:00:56](https://www.youtube.com/watch?v=Gz884lGtXrk&t=3656s)

Si se **particiona** una región $D$ en dos subregiones $D_1$ y $D_2$ (que no se solapen, al menos en sus interiores), la integral de una función continua $f$ sobre $D$ es la suma de las integrales sobre cada parte:

$$
\iint_D f\,dA = \iint_{D_1} f\,dA + \iint_{D_2} f\,dA
$$

Es análogo al caso de una variable: si $I_1$ e $I_2$ son dos intervalos que no se solapan,

$$
\int_{I_1 \cup I_2} f = \int_{I_1} f + \int_{I_2} f
$$

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=Gz884lGtXrk&t=3749s">1:02:29</a>: Integral de $x+y$ sobre una región partida en dos</summary>

Calcular la integral doble de $f(x,y) = x + y$ sobre la región $D$ del plano limitada por las rectas

$$
x + y = 1, \quad x + y = 3, \quad y - x = 1, \quad y - x = -1
$$

Estas cuatro rectas forman un cuadrado (rotado): $D$ es su interior.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la región. Las rectas $x+y=1$ y $x+y=3$ son paralelas (cortan a los ejes en $1$ y en $3$); las rectas $y = x + 1$ (o sea $y-x=1$) e $y = x - 1$ (o sea $y-x=-1$) tienen pendiente $1$ y ordenadas al origen $1$ y $-1$. $D$ es el cuadrado encerrado entre ellas, con vértices donde se cortan (por ejemplo, un vértice en $x=1$ y otro en $x=2$).

**Paso 2:** Como los límites de $y$ cambian de expresión según el valor de $x$, se **subdivide** $D$ en dos partes $D_1$ y $D_2$ y se usa la aditividad.

$$
\iint_D f\,dA = \iint_{D_1} f\,dA + \iint_{D_2} f\,dA
$$

**Paso 3:** Plantear la integral sobre $D_1$. Allí $x$ varía entre $0$ y $1$; para cada $x$, $y$ va desde la recta $y = 1 - x$ (mínimo) hasta la recta $y = x + 1$ (máximo).

$$
\iint_{D_1} f\,dA = \int_0^1 \int_{1-x}^{x+1} (x + y)\,dy\,dx
$$

**Paso 4:** Plantear la integral sobre $D_2$. Allí $x$ varía entre $1$ y $2$; para cada $x$, $y$ va desde la recta $y = x - 1$ (mínimo) hasta la recta $y = 3 - x$ (máximo).

$$
\iint_{D_2} f\,dA = \int_1^2 \int_{x-1}^{3-x} (x + y)\,dy\,dx
$$

**Paso 5:** Resolver cada integral iterada (primero respecto de $y$, luego respecto de $x$). Los resultados son [paso en el pizarrón, ver video]:

$$
\iint_{D_1} f\,dA = \frac{5}{3}, \qquad \iint_{D_2} f\,dA = \frac{7}{3}
$$

**Paso 6:** Sumar.

$$
\iint_D f\,dA = \frac{5}{3} + \frac{7}{3} = \frac{12}{3} = 4
$$

**Verificación (al pasar):** como $f$ es lineal, la integral puede calcularse como el valor medio de la función por el área de $D$. Cada lado del cuadrado es la hipotenusa de un triángulo rectángulo de catetos $1$ y $1$, de modo que el lado mide $\sqrt{2}$ y el área es $\sqrt{2}\cdot\sqrt{2} = 2$. El valor medio de la función lineal se alcanza en el centro del cuadrado, el punto $(1,1)$, donde $f(1,1) = 2$. Así, $\text{Área}(D)\cdot \bar{f} = 2 \cdot 2 = 4$, coincidiendo con el resultado.

</details>

</details>
