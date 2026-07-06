# Longitud de una curva

> Fuente: https://www.youtube.com/watch?v=xkmXvsaaR48

---

## Índice
- [00:00](https://www.youtube.com/watch?v=xkmXvsaaR48&t=0s) — Integrales sobre curvas
- [00:31](https://www.youtube.com/watch?v=xkmXvsaaR48&t=31s) — Curvas como imagen de una función vectorial
- [01:35](https://www.youtube.com/watch?v=xkmXvsaaR48&t=95s) — Curva regular
- [02:38](https://www.youtube.com/watch?v=xkmXvsaaR48&t=158s) — Curva simple
- [03:41](https://www.youtube.com/watch?v=xkmXvsaaR48&t=221s) — Definición de longitud de una curva simple
- [04:48](https://www.youtube.com/watch?v=xkmXvsaaR48&t=288s) — 📝 Ejercicio 1: Longitud de una circunferencia
- [10:41](https://www.youtube.com/watch?v=xkmXvsaaR48&t=641s) — Interpretación: diferencial de longitud
- [12:13](https://www.youtube.com/watch?v=xkmXvsaaR48&t=733s) — 📝 Ejercicio 2: Circunferencia con otra parametrización
- [17:35](https://www.youtube.com/watch?v=xkmXvsaaR48&t=1055s) — Independencia de la parametrización
- [18:37](https://www.youtube.com/watch?v=xkmXvsaaR48&t=1117s) — Teorema: reparametrización de una curva simple
- [24:25](https://www.youtube.com/watch?v=xkmXvsaaR48&t=1465s) — 📝 Ejercicio 3: Longitud del coseno hiperbólico
- [33:39](https://www.youtube.com/watch?v=xkmXvsaaR48&t=2019s) — Curva definida implícitamente
- [37:52](https://www.youtube.com/watch?v=xkmXvsaaR48&t=2272s) — 📝 Ejercicio 4: Longitud de una parábola

---

## Integrales sobre curvas [00:00](https://www.youtube.com/watch?v=xkmXvsaaR48&t=0s)

Se comienza el tratamiento de las **integrales sobre curvas**, en las que las regiones de integración son curvas. El caso más sencillo de estas integrales es el que se usa para **evaluar la longitud de una curva**.

## Curvas como imagen de una función vectorial [00:31](https://www.youtube.com/watch?v=xkmXvsaaR48&t=31s)

Las curvas se definen como el **conjunto imagen de una función vectorial de una variable**. Si $\lambda$ es la función vectorial que parametriza una curva, su dominio es un subconjunto de la recta real: al intervalo $[a,b]$ del dominio (con variable $t$) le corresponde, punto a punto, un punto en el espacio $n$-dimensional.

$$
\lambda : [a,b] \subseteq \mathbb{R} \to \mathbb{R}^n
$$

La curva puede estar definida en el plano, en $\mathbb{R}^3$, en $\mathbb{R}^4$ o en el espacio $n$-dimensional.

## Curva regular [01:35](https://www.youtube.com/watch?v=xkmXvsaaR48&t=95s)

La parametrización de una curva es **regular** cuando, desde el punto de vista geométrico, la curva **admite recta tangente en cualquiera de sus puntos**.

Para que $\lambda$ sea regular debe cumplirse:

- $\lambda$ es de **clase $C^1$** (tiene derivada continua).
- La derivada **no es el vector nulo**: $\lambda'(t) \neq \vec{0}$.

Estos dos requisitos (derivada continua y no nula) garantizan que exista recta tangente. Los puntos que los cumplen son **puntos regulares** de la curva.

## Curva simple [02:38](https://www.youtube.com/watch?v=xkmXvsaaR48&t=158s)

Tomando un intervalo cerrado incluido en el dominio de $\lambda$, si la función $\lambda$ es **inyectiva por lo menos en el interior** del intervalo, entonces la curva regular e inyectiva se denomina **curva simple**.

Que $\lambda$ sea inyectiva en el interior del dominio significa que elementos distintos del dominio tienen imágenes distintas, lo que implica que **la curva no se autointerseca**. Si una curva se autointersecara (dos elementos del dominio con la misma imagen), no sería inyectiva y no sería una curva simple.

Estas curvas simples, ya sea que estén en el plano o en el espacio $n$-dimensional, serán las **regiones de integración** de las integrales de línea.

## Definición de longitud de una curva simple [03:41](https://www.youtube.com/watch?v=xkmXvsaaR48&t=221s)

Sea una curva simple parametrizada por $\lambda$ en el intervalo $[a,b]$. Se define la **longitud** de esa curva como la integral entre $a$ y $b$ (extremos del intervalo del parámetro) de la **norma de la derivada** de la función:

$$
L = \int_a^b \left\| \lambda'(t) \right\| \, dt
$$

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=xkmXvsaaR48&t=288s">04:48</a>: Longitud de una circunferencia</summary>

Calcular la longitud de la curva parametrizada por $\lambda$, cuyas funciones componentes son

$$
x(t) = r\cos t, \qquad y(t) = r\sin t
$$

con $t$ variando en el intervalo $[0, 2\pi]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la curva. Elevando al cuadrado ambas componentes y sumando:

$$
x^2 + y^2 = r^2\cos^2 t + r^2\sin^2 t = r^2
$$

ya que $\cos^2 t + \sin^2 t = 1$. Las imágenes forman en el plano $xy$ una **circunferencia de radio $r$ centrada en el origen**.

**Paso 2:** Observar el recorrido. Cuando $t=0$ el punto es $(r,0)$; a medida que $t$ crece en $[0,2\pi]$ el punto se desplaza sobre la circunferencia, y cuando $t=2\pi$ se vuelve al mismo punto que en $t=0$. Es decir, $\lambda$ parametriza la **circunferencia completa** (su perímetro).

**Paso 3:** Aplicar la definición de longitud entre los valores extremos $0$ y $2\pi$.

$$
L = \int_0^{2\pi} \left\| \lambda'(t) \right\| \, dt
$$

**Paso 4:** Calcular el vector derivada.

$$
\lambda'(t) = \left( -r\sin t, \; r\cos t \right)
$$

**Paso 5:** Calcular la norma como raíz de la suma de los cuadrados de las componentes.

$$
\left\| \lambda'(t) \right\| = \sqrt{ r^2\sin^2 t + r^2\cos^2 t }
$$

**Paso 6:** Sacar factor común $r^2$ dentro de la raíz. Como $\sin^2 t + \cos^2 t = 1$, queda $\sqrt{r^2} = |r| = r$ (por ser $r$ positivo, el radio).

$$
\left\| \lambda'(t) \right\| = \sqrt{ r^2 \left( \sin^2 t + \cos^2 t \right) } = |r| = r
$$

**Paso 7:** Como $r$ es constante, sale fuera de la integral.

$$
L = \int_0^{2\pi} r \, dt = r \int_0^{2\pi} dt = r \cdot 2\pi = 2\pi r
$$

La longitud de la curva es $2\pi r$, es decir, el perímetro de una circunferencia de radio $r$, como ya se sabía previamente.

</details>

</details>

## Interpretación: diferencial de longitud [10:41](https://www.youtube.com/watch?v=xkmXvsaaR48&t=641s)

El vector $\lambda'(t)$ se denomina también **vector velocidad**, y es un vector **tangente** a la curva. Su norma $\left\| \lambda'(t) \right\|$ es simplemente la **velocidad**.

Al multiplicar la velocidad por un diferencial de tiempo $dt$ se obtiene un **diferencial de longitud**:

$$
dL = \left\| \lambda'(t) \right\| \, dt
$$

Una forma fácil de recordarlo: velocidad por tiempo es espacio recorrido (una pequeña longitud de la curva). Al integrar (sumar) todos esos diferenciales de longitud se obtiene la **longitud total** de la curva.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=xkmXvsaaR48&t=733s">12:13</a>: Circunferencia con otra parametrización</summary>

Calcular la longitud de la curva parametrizada por $\mu$, cuyas funciones componentes son

$$
x(s) = r\cos(2s), \qquad y(s) = r\sin(2s)
$$

con $s$ variando en el intervalo $[0, \pi]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la curva. Elevando al cuadrado y sumando ambas ecuaciones:

$$
x^2 + y^2 = r^2\cos^2(2s) + r^2\sin^2(2s) = r^2
$$

Es nuevamente una **circunferencia de radio $r$**. Cuando $s=0$ el punto es $(r,0)$, y cuando $s=\pi$ se obtiene $\cos(2\pi)=1$, $\sin(2\pi)=0$, o sea la misma imagen $(r,0)$. A medida que $s$ recorre $[0,\pi]$ el punto da una vuelta completa (en sentido antihorario).

**Nota:** con esta parametrización el punto tarda poco más de tres segundos en dar la vuelta completa (contra los poco más de seis segundos de la parametrización anterior): gira alrededor de la **misma** circunferencia, pero más rápido.

**Paso 2:** Plantear la longitud con la definición, entre $0$ y $\pi$.

$$
L = \int_0^{\pi} \left\| \mu'(s) \right\| \, ds
$$

**Paso 3:** Calcular el vector derivada (regla de la cadena, derivada de $2s$ es $2$).

$$
\mu'(s) = \left( -2r\sin(2s), \; 2r\cos(2s) \right)
$$

**Paso 4:** Calcular la norma.

$$
\left\| \mu'(s) \right\| = \sqrt{ 4r^2\sin^2(2s) + 4r^2\cos^2(2s) }
$$

**Paso 5:** Sacar factor común $4r^2$; como $\sin^2(2s)+\cos^2(2s)=1$, queda $\sqrt{4r^2}=2r$.

$$
\left\| \mu'(s) \right\| = \sqrt{ 4r^2 \left( \sin^2(2s) + \cos^2(2s) \right) } = 2r
$$

**Paso 6:** Extraer $2r$ fuera de la integral e integrar el diferencial entre $0$ y $\pi$.

$$
L = \int_0^{\pi} 2r \, ds = 2r \cdot \pi = 2\pi r
$$

La longitud de la circunferencia de radio $r$ es igual a $2\pi r$, exactamente igual que en el ejemplo anterior.

</details>

</details>

## Independencia de la parametrización [17:35](https://www.youtube.com/watch?v=xkmXvsaaR48&t=1055s)

Es lógico y razonable que la longitud de la circunferencia siempre valga lo mismo ($2\pi r$), sin importar de qué modo se la parametrice. En general, la **longitud de una curva** (el conjunto imagen de la función) tiene que ser **totalmente independiente** de cómo se parametrice esa curva simple: siempre debe valer lo mismo.

## Teorema: reparametrización de una curva simple [18:37](https://www.youtube.com/watch?v=xkmXvsaaR48&t=1117s)

**Teorema 1:** Cualquiera sea la parametrización de la curva, la **longitud de la curva es independiente de la parametrización**.

**Interpretación gráfica.** Se tiene un intervalo $I$ con variable $t$ y una función $\lambda$ que manda las imágenes al espacio $n$-dimensional, generando la curva. Si se toma otro intervalo $I^*$ de la recta real, con variable $s$, se puede parametrizar la **misma curva** con una función $\mu$ que a cada valor de $s$ le hace corresponder un punto de $\mathbb{R}^n$ sobre esa curva.

Se introduce una función $g$ de una variable que a cada $s$ le hace corresponder un valor $t$, de manera que $\mu$ sea la composición de $\lambda$ con $g$:

$$
\mu = \lambda \circ g
$$

A la función $\mu$ se la denomina **reparametrización** de $\lambda$, porque ambas tienen el mismo conjunto imagen.

**Requisitos sobre $g$** para que $\mu$ sea una reparametrización de una curva simple (siendo $\lambda$ de derivada continua y no nula):

- $g$ tiene **derivada continua** (es de clase $C^1$).
- $g'(s) \neq 0$. Como la derivada de una composición es el producto de las derivadas, y $\lambda'$ es no nula, pedir $g'\neq 0$ garantiza que $\mu'$ también sea un vector no nulo.
- $g$ es **biyectiva**: a cada elemento del intervalo $I^*$ le corresponde uno y solo un elemento del intervalo $I$.

Bajo estas hipótesis se garantiza que la longitud de la curva sea **exactamente la misma** con cualquiera de las parametrizaciones.

En los dos ejemplos de la circunferencia, la relación entre la variable $t$ (parametrización $\lambda$) y la variable $s$ (parametrización $\mu$) es

$$
t = 2s
$$

es decir, $g(s) = 2s$. Esta función tiene derivada continua, derivada distinta de $0$, y es biyectiva (llevaba el intervalo $[0,\pi]$ al $[0,2\pi]$). En síntesis: **la longitud de una curva es independiente de la parametrización** para curvas simples.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=xkmXvsaaR48&t=1465s">24:25</a>: Longitud del coseno hiperbólico</summary>

Calcular la longitud de la curva $y = \cosh x$ entre el punto de abscisa $x=0$ y el punto de abscisa $x=1$ (con sus alturas correspondientes).

Se recuerdan las definiciones:

$$
\cosh x = \frac{e^{x} + e^{-x}}{2}, \qquad \sinh x = \frac{e^{x} - e^{-x}}{2}
$$

La gráfica de $\cosh x$ tiene forma simétrica respecto al eje $y$, y en $x=0$ vale $1$ (queda entre medio de las gráficas de $\tfrac{e^x}{2}$ y $\tfrac{e^{-x}}{2}$).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar la curva. Al ser la gráfica de una función de una variable, se toma $x$ como parámetro:

$$
\lambda(x) = \left( x, \; \cosh x \right), \qquad x \in [0,1]
$$

**Paso 2:** Calcular la derivada de la parametrización. La derivada de $x$ es $1$; la derivada de $\cosh x$ es $\sinh x$.

$$
\lambda'(x) = \left( 1, \; \sinh x \right)
$$

**Paso 3:** Plantear la norma de la derivada (raíz de la suma de cuadrados de las componentes).

$$
\left\| \lambda'(x) \right\| = \sqrt{ 1 + \sinh^2 x }
$$

**Paso 4:** Usar la identidad hiperbólica $\cosh^2 x - \sinh^2 x = 1$, de donde $1 + \sinh^2 x = \cosh^2 x$.

$$
\left\| \lambda'(x) \right\| = \sqrt{ \cosh^2 x } = |\cosh x| = \cosh x
$$

ya que $\cosh x$ siempre toma valores positivos.

**Paso 5:** Plantear la longitud de la curva.

$$
L = \int_0^{1} \left\| \lambda'(x) \right\| \, dx = \int_0^{1} \cosh x \, dx
$$

**Paso 6:** Integrar. La primitiva de $\cosh x$ es $\sinh x$ (derivando $\sinh x$ se obtiene $\cosh x$).

$$
L = \Big[ \sinh x \Big]_0^{1} = \sinh(1) - \sinh(0)
$$

**Paso 7:** Evaluar. $\sinh(0) = 0$ y $\sinh(1) = \dfrac{e^{1} - e^{-1}}{2}$.

$$
L = \sinh(1) = \frac{e - e^{-1}}{2}
$$

</details>

</details>

## Curva definida implícitamente [33:39](https://www.youtube.com/watch?v=xkmXvsaaR48&t=2019s)

La longitud de la curva siempre se calcula como la integral de la norma de la derivada de la parametrización. Cuando la curva es la gráfica de una función $y$ que depende de $x$ (curva en el plano $xy$), siempre se puede parametrizar de la forma

$$
\lambda(x) = \left( x, \; y(x) \right)
$$

**Caso implícito.** Si la función $y(x)$ está definida **implícitamente** por una ecuación $g(x,y)=0$, por el **teorema de la función implícita** se puede calcular

$$
y'(x) = -\frac{g'_x}{g'_y}
$$

(siendo $y$ función de $x$). Entonces, para calcular la longitud se necesita la norma de $\lambda'$, donde

$$
\lambda'(x) = \left( 1, \; y'(x) \right) = \left( 1, \; -\frac{g'_x}{g'_y} \right)
$$

Calculando la norma:

$$
\left\| \lambda'(x) \right\| = \sqrt{ 1 + \frac{(g'_x)^2}{(g'_y)^2} } = \frac{ \sqrt{ (g'_y)^2 + (g'_x)^2 } }{ \sqrt{ (g'_y)^2 } }
$$

El numerador es la **norma del gradiente** de $g$, y el denominador es el módulo de $g'_y$:

$$
\left\| \lambda'(x) \right\| = \frac{ \left\| \nabla g \right\| }{ \left| g'_y \right| }
$$

En síntesis, cuando la curva está definida implícitamente por una ecuación donde se cumplen las hipótesis del teorema de la función implícita, la longitud se puede calcular como

$$
L = \int \frac{ \left\| \nabla g \right\| }{ \left| g'_y \right| } \, dx
$$

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=xkmXvsaaR48&t=2272s">37:52</a>: Longitud de una parábola</summary>

Calcular la longitud de la parábola cóncava hacia abajo con vértice en $(0,1)$, considerando solo la parte que se encuentra por encima del eje $x$ (es decir, con $y \ge 0$). La parábola corresponde a la ecuación

$$
x^2 + y - 1 = 0, \qquad y \ge 0
$$

Se toma $g(x,y) = x^2 + y - 1$, de modo que la parábola es su conjunto de nivel $0$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Determinar el intervalo de integración. Con $y \ge 0$, la parábola va desde $x=-1$ hasta $x=1$ (intersección $y=0$ con la parábola).

**Paso 2:** Plantear la longitud usando la fórmula para curva implícita.

$$
L = \int_{-1}^{1} \frac{ \left\| \nabla g \right\| }{ \left| g'_y \right| } \, dx
$$

**Paso 3:** Calcular el gradiente de $g$. Derivando respecto de $x$ se obtiene $2x$, y respecto de $y$ se obtiene $1$.

$$
\nabla g = \left( 2x, \; 1 \right)
$$

**Paso 4:** Calcular la norma del gradiente y el módulo de $g'_y$.

$$
\left\| \nabla g \right\| = \sqrt{ 4x^2 + 1 }, \qquad \left| g'_y \right| = |1| = 1
$$

**Paso 5:** Sustituir en la integral.

$$
L = \int_{-1}^{1} \frac{ \sqrt{ 4x^2 + 1 } }{ 1 } \, dx = \int_{-1}^{1} \sqrt{ 4x^2 + 1 } \, dx
$$

**Paso 6:** Usar la tabla de integrales, con la forma

$$
\int \sqrt{ x^2 + a^2 } \, dx = \frac{ x \sqrt{ x^2 + a^2 } }{2} + \frac{a^2}{2} \ln\left( x + \sqrt{ x^2 + a^2 } \right)
$$

Para adaptar el integrando a esa forma, se saca factor común $4$ dentro de la raíz; al sacarlo fuera de la raíz queda un $2$:

$$
\sqrt{ 4x^2 + 1 } = 2\sqrt{ x^2 + \tfrac{1}{4} }
$$

de modo que $a^2 = \tfrac{1}{4}$.

**Paso 7:** Aplicar la fórmula (con el factor $2$ por delante).

$$
L = 2\left[ \frac{ x \sqrt{ x^2 + \tfrac{1}{4} } }{2} + \frac{ \tfrac{1}{4} }{2} \ln\left( x + \sqrt{ x^2 + \tfrac{1}{4} } \right) \right]_{-1}^{1}
$$

**Paso 8:** Sacando factor común $2$ y simplificando, el primer término queda sin el denominador $2$ y el segundo con coeficiente $\tfrac{1}{4}$:

$$
L = \left[ x \sqrt{ x^2 + \tfrac{1}{4} } + \tfrac{1}{4} \ln\left( x + \sqrt{ x^2 + \tfrac{1}{4} } \right) \right]_{-1}^{1}
$$

**Paso 9:** Evaluar en $x=1$: $\sqrt{1 + \tfrac{1}{4}} = \sqrt{\tfrac{5}{4}} = \tfrac{\sqrt5}{2}$.

$$
\left. \right|_{x=1} = \frac{\sqrt5}{2} + \tfrac{1}{4} \ln\left( 1 + \frac{\sqrt5}{2} \right)
$$

**Paso 10:** Evaluar en $x=-1$ y restar. El término con la raíz da $-\tfrac{\sqrt5}{2}$; al restarlo se suma, quedando dos veces $\tfrac{\sqrt5}{2}$, que simplifica a $\sqrt5$:

$$
L = \sqrt5 + \tfrac{1}{4}\left[ \ln\left( 1 + \frac{\sqrt5}{2} \right) - \ln\left( -1 + \frac{\sqrt5}{2} \right) \right]
$$

Asignando valores numéricos se podría calcular aproximadamente la longitud de la parábola.

</details>

</details>
