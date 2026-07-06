# Flujo

> Fuente: https://www.youtube.com/watch?v=djt3sX5V2lk

---

## Índice
- [00:01](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1s) — Introducción al Flujo de un Campo Vectorial
- [01:36](https://www.youtube.com/watch?v=djt3sX5V2lk&t=96s) — Superficies Simples, Regulares y Orientables
- [08:26](https://www.youtube.com/watch?v=djt3sX5V2lk&t=506s) — Borde de una Superficie y Orientación Inducida
- [18:53](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1133s) — Definición de Integral de un Campo Vectorial (Flujo)
- [35:14](https://www.youtube.com/watch?v=djt3sX5V2lk&t=2114s) — Interpretación Física del Flujo
- [1:00:03](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3603s) — Propiedades del Flujo según la Orientación
- [1:20:08](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4808s) — Cálculo de Flujo para Superficies Cartesianas

---

# PARTE 1 — TEORÍA

## Introducción al Flujo de un Campo Vectorial [00:01](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1s)

Las integrales de campos vectoriales sobre superficies, también conocidas como **flujo de un campo vectorial a través de una superficie**, son el análogo en superficies a las integrales de línea de campos vectoriales. Para poder definirlas, primero es necesario establecer las características de las superficies sobre las que trabajaremos.

## Superficies Simples, Regulares y Orientables [01:36](https://www.youtube.com/watch?v=djt3sX5V2lk&t=96s)

Una superficie $S$ es el conjunto imagen de una función vectorial $\sigma(u, v)$ definida en una región $D$ del plano $uv$.

$$
\sigma: D \subset \mathbb{R}^2 \to \mathbb{R}^3, \quad \sigma(u,v) = (x(u,v), y(u,v), z(u,v))
$$

Para que podamos trabajar con ella, la superficie debe cumplir ciertas condiciones:

-   **Regularidad:** La función $\sigma$ debe ser de clase $C^1$ (con derivadas parciales continuas) y el producto vectorial de sus derivadas parciales debe ser no nulo. Este producto vectorial representa un **vector normal** a la superficie.

$$
\sigma'_u \times \sigma'_v \neq \vec{0}
$$

-   **Simplicidad:** La función $\sigma$ debe ser inyectiva en el interior de su dominio $D$.

### Superficies Orientables [04:49](https://www.youtube.com/watch?v=djt3sX5V2lk&t=289s)

A partir del vector normal, podemos definir un campo de **versores normales** a la superficie:

$$
\vec{n}(u,v) = \frac{\sigma'_u(u,v) \times \sigma'_v(u,v)}{\|\sigma'_u(u,v) \times \sigma'_v(u,v)\|}
$$

**Definición (Superficie Orientable):** Una superficie $S$ se dice **orientable** si el campo de versores normales $\vec{n}$ es continuo sobre toda la superficie.

Intuitivamente, una superficie orientable es aquella que tiene "dos lados" o "dos caras" bien definidas. La elección de una de estas caras se conoce como **orientación** de la superficie, y está determinada por la dirección del campo de versores normales.

### Borde de una Superficie y Orientación Inducida [08:26](https://www.youtube.com/watch?v=djt3sX5V2lk&t=506s)

-   **Borde de la superficie ($\partial S$):** Es el conjunto imagen de la frontera del dominio de la parametrización ($\partial D$).
-   **Orientación Inducida:** Una orientación positiva (sentido antihorario) en la frontera del dominio $\partial D$ induce una orientación en el borde de la superficie $\partial S$. Esta orientación se considera positiva con respecto al campo de versores normales $\vec{n}$.

**Regla de la mano derecha:** Si se toma un vector normal $\vec{n}$ con la mano derecha de forma que el pulgar apunte en la dirección de $\vec{n}$, los otros cuatro dedos indicarán el sentido de la orientación positiva del borde de la superficie.

### Superficies Simples y Orientables por Partes [14:40](https://www.youtube.com/watch?v=djt3sX5V2lk&t=880s)

Una superficie es **simple y orientable por partes** si está formada por la unión de varias superficies simples y orientables pegadas en sus bordes. Para que la orientación sea coherente, en las curvas de unión, las orientaciones inducidas por cada superficie deben ser opuestas. Un ejemplo son las seis caras de un cubo, donde todos los vectores normales apuntan hacia afuera (o todos hacia adentro).

## Definición de Integral de un Campo Vectorial (Flujo) [18:53](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1133s)

Sea $\vec{F}$ un campo vectorial continuo definido en una región que contiene a una superficie $S$ simple, orientable y parametrizada por $\sigma(u,v)$ con dominio $D$.

**Definición (Flujo):** La integral del campo vectorial $\vec{F}$ a través de la superficie $S$ (o flujo de $\vec{F}$ a través de $S$) se define y calcula como:

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_S \vec{F} \cdot \vec{n} \, dS = \iint_D \vec{F}(\sigma(u,v)) \cdot (\sigma'_u \times \sigma'_v) \, du \, dv
$$

-   Si la superficie $S$ es cerrada (como una esfera), la integral a veces se denota con un círculo: $\oiint_S \vec{F} \cdot d\vec{S}$.

## Interpretación Física del Flujo [35:14](https://www.youtube.com/watch?v=djt3sX5V2lk&t=2114s)

El concepto de flujo tiene importantes aplicaciones físicas:

-   **Campo de velocidades de un fluido:** Si $\vec{F}$ representa el campo de velocidades de un fluido, el flujo $\iint_S \vec{F} \cdot d\vec{S}$ representa el **caudal** del fluido que atraviesa la superficie $S$ por unidad de tiempo (ej: m³/s).
    -   El producto escalar $\vec{F} \cdot \vec{n}$ aísla la componente de la velocidad que es perpendicular a la superficie, que es la que efectivamente contribuye al caudal.
    -   Un flujo positivo indica que el fluido neto atraviesa la superficie en la misma dirección que la orientación elegida (el vector normal $\vec{n}$).
    -   Un flujo negativo indica que el fluido neto atraviesa en la dirección opuesta.
-   **Superficies cerradas:**
    -   Si el flujo total a través de una superficie cerrada es **positivo**, significa que sale más fluido del que entra. Se dice que hay una **fuente** dentro de la superficie.
    -   Si el flujo total es **negativo**, entra más fluido del que sale. Se dice que hay un **sumidero**.

## Propiedades del Flujo según la Orientación [1:00:03](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3603s)

El valor del flujo depende de la orientación elegida para la superficie.

**Teorema:** Sean $\sigma$ y $\tau$ dos parametrizaciones de la misma superficie $S$.
1.  Si $\sigma$ y $\tau$ inducen la **misma orientación** en $S$, entonces el flujo calculado con ambas es el mismo.
2.  Si $\sigma$ y $\tau$ inducen **orientaciones opuestas** en $S$, entonces los flujos son opuestos en signo.

$$
\iint_S \vec{F} \cdot d\vec{S}_{\sigma} = - \iint_S \vec{F} \cdot d\vec{S}_{\tau}
$$

## Cálculo de Flujo para Superficies Cartesianas [1:20:08](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4808s)

Si una superficie $S$ está definida por una ecuación cartesiana $g(x,y,z) = 0$, donde una variable puede ser despejada en función de las otras (por ejemplo, $z = f(x,y)$), el flujo se puede calcular sin necesidad de una parametrización explícita.

La orientación de la superficie estará dada por el vector gradiente $\nabla g$.

**Fórmula para superficies cartesianas:** Si $S$ es la gráfica de $z = f(x,y)$ y la región de integración es su proyección $S_{xy}$ sobre el plano $xy$, el flujo se calcula como:

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_{S_{xy}} \vec{F}(x, y, f(x,y)) \cdot \frac{\nabla g}{|\frac{\partial g}{\partial z}|} \, dx \, dy
$$

Donde $g(x,y,z) = z - f(x,y)$. El signo de la integral dependerá de si la orientación dada por $\nabla g$ coincide con la deseada.

---

## Ejercicios

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=1290s">21:30</a>: Flujo a través de un plano</summary>

Calcular el flujo del campo vectorial $\vec{F}(x,y,z) = (0, x, 0)$ a través de la superficie $S$ dada por el plano $\frac{x}{a} + \frac{y}{b} + z = 1$ en el primer octante, con $a, b > 0$.

La superficie está parametrizada por:
$$
\sigma(u,v) = (u, v, 1 - \frac{u}{a} - \frac{v}{b})
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Calcular el vector normal a la superficie, $\sigma'_u \times \sigma'_v$.

Primero, calculamos las derivadas parciales de $\sigma$:
$$
\sigma'_u = (1, 0, -\frac{1}{a})
$$
$$
\sigma'_v = (0, 1, -\frac{1}{b})
$$
Luego, su producto vectorial:
$$
\sigma'_u \times \sigma'_v = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & -1/a \\ 0 & 1 & -1/b \end{vmatrix} = (\frac{1}{a}, \frac{1}{b}, 1)
$$

**Paso 2:** Evaluar el campo vectorial $\vec{F}$ en los puntos de la superficie, es decir, en $\sigma(u,v)$.

$$
\vec{F}(\sigma(u,v)) = \vec{F}(u, v, 1 - \frac{u}{a} - \frac{v}{b}) = (0, u, 0)
$$

**Paso 3:** Calcular el producto escalar $\vec{F}(\sigma(u,v)) \cdot (\sigma'_u \times \sigma'_v)$.

$$
(0, u, 0) \cdot (\frac{1}{a}, \frac{1}{b}, 1) = 0 \cdot \frac{1}{a} + u \cdot \frac{1}{b} + 0 \cdot 1 = \frac{u}{b}
$$

**Paso 4:** Determinar la región de integración $D$ en el plano $uv$.

La región $D$ es la proyección de la superficie sobre el plano $xy$ (o $uv$, ya que $x=u, y=v$). Es un triángulo con vértices en $(0,0)$, $(a,0)$ y $(0,b)$. Los límites de integración son:
-   $0 \le u \le a$
-   $0 \le v \le b(1 - \frac{u}{a})$

**Paso 5:** Plantear y resolver la integral de flujo.

$$
\iint_S \vec{F} \cdot d\vec{S} = \int_{0}^{a} \int_{0}^{b(1 - u/a)} \frac{u}{b} \, dv \, du
$$

Integramos primero respecto a $v$:
$$
\int_{0}^{a} \left[ \frac{u}{b} v \right]_{0}^{b(1 - u/a)} \, du = \int_{0}^{a} \frac{u}{b} \cdot b(1 - \frac{u}{a}) \, du = \int_{0}^{a} (u - \frac{u^2}{a}) \, du
$$

Integramos respecto a $u$:
$$
\left[ \frac{u^2}{2} - \frac{u^3}{3a} \right]_{0}^{a} = (\frac{a^2}{2} - \frac{a^3}{3a}) - 0 = \frac{a^2}{2} - \frac{a^2}{3} = \frac{3a^2 - 2a^2}{6} = \frac{a^2}{6}
$$

El flujo es $\frac{a^2}{6}$.

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=2682s">44:42</a>: Flujo con orientación invertida</summary>

Calcular el flujo del mismo campo vectorial $\vec{F}(x,y,z) = (0, x, 0)$ a través de la misma superficie $S$ del ejercicio anterior, pero usando una parametrización diferente que invierte la orientación:
$$
\tau(s,t) = (s, -t, 1 - \frac{s}{a} + \frac{t}{b})
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Calcular el nuevo vector normal, $\tau'_s \times \tau'_t$.

Derivadas parciales de $\tau$:
$$
\tau'_s = (1, 0, -\frac{1}{a})
$$
$$
\tau'_t = (0, -1, \frac{1}{b})
$$
Producto vectorial:
$$
\tau'_s \times \tau'_t = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & 0 & -1/a \\ 0 & -1 & 1/b \end{vmatrix} = (-\frac{1}{a}, -\frac{1}{b}, -1)
$$
Este vector es el opuesto al del Ejercicio 1, lo que confirma que la orientación está invertida.

**Paso 2:** Evaluar el campo $\vec{F}$ en $\tau(s,t)$.

$$
\vec{F}(\tau(s,t)) = \vec{F}(s, -t, ...) = (0, s, 0)
$$

**Paso 3:** Calcular el producto escalar $\vec{F}(\tau(s,t)) \cdot (\tau'_s \times \tau'_t)$.

$$
(0, s, 0) \cdot (-\frac{1}{a}, -\frac{1}{b}, -1) = -\frac{s}{b}
$$

**Paso 4:** Determinar la nueva región de integración.

Las variables son $s=x$ y $t=-y$. Los límites para $s$ son los mismos que para $u$: $0 \le s \le a$.
Para $t$, partimos de $0 \le y \le b(1 - x/a)$. Sustituyendo $y=-t$ y $x=s$:
$0 \le -t \le b(1 - s/a)$. Multiplicando por -1 e invirtiendo las desigualdades:
$0 \ge t \ge -b(1 - s/a) \implies b(s/a - 1) \le t \le 0$.

**Paso 5:** Plantear y resolver la integral.

$$
\iint_S \vec{F} \cdot d\vec{S} = \int_{0}^{a} \int_{b(s/a - 1)}^{0} -\frac{s}{b} \, dt \, ds
$$

Integramos respecto a $t$:
$$
\int_{0}^{a} \left[ -\frac{s}{b} t \right]_{b(s/a - 1)}^{0} \, ds = \int_{0}^{a} (0 - (-\frac{s}{b} \cdot b(\frac{s}{a} - 1))) \, ds = \int_{0}^{a} s(\frac{s}{a} - 1) \, ds = \int_{0}^{a} (\frac{s^2}{a} - s) \, ds
$$

Integramos respecto a $s$:
$$
\left[ \frac{s^3}{3a} - \frac{s^2}{2} \right]_{0}^{a} = (\frac{a^3}{3a} - \frac{a^2}{2}) - 0 = \frac{a^2}{3} - \frac{a^2}{2} = -\frac{a^2}{6}
$$
El resultado es el opuesto al del Ejercicio 1, como se esperaba.

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=3702s">1:01:42</a>: Flujo a través de una esfera</summary>

Calcular el flujo del campo vectorial $\vec{F}(x,y,z) = k \frac{(x,y,z)}{\|(x,y,z)\|^3}$ a través de una superficie esférica $S$ de radio $R$ centrada en el origen.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar la superficie esférica usando coordenadas esféricas.

$$
\sigma(\theta, \phi) = (R\cos\theta\cos\phi, R\cos\theta\sin\phi, R\sin\theta)
$$
Con dominio $\theta \in [-\pi/2, \pi/2]$ y $\phi \in [0, 2\pi]$.

**Paso 2:** Calcular el vector normal $\sigma'_\theta \times \sigma'_\phi$.

[paso en el pizarrón, ver video] El cálculo de las derivadas parciales y el producto vectorial es extenso. El resultado es:
$$
\sigma'_\theta \times \sigma'_\phi = (-R^2\cos^2\theta\cos\phi, -R^2\cos^2\theta\sin\phi, -R^2\sin\theta\cos\theta)
$$
Nota: Para un punto en el primer octante (donde senos y cosenos son positivos), todas las componentes son negativas. Esto significa que el vector normal apunta hacia el interior de la esfera.

**Paso 3:** Evaluar el campo $\vec{F}$ en la superficie.

En cualquier punto de la esfera, $\|(x,y,z)\| = R$. Por lo tanto:
$$
\vec{F}(\sigma(\theta,\phi)) = k \frac{(R\cos\theta\cos\phi, R\cos\theta\sin\phi, R\sin\theta)}{R^3} = \frac{k}{R^2} (\cos\theta\cos\phi, \cos\theta\sin\phi, \sin\theta)
$$

**Paso 4:** Calcular el producto escalar para el integrando.

$$
\vec{F}(\sigma) \cdot (\sigma'_\theta \times \sigma'_\phi) = \frac{k}{R^2} \left( (\cos\theta\cos\phi)(-R^2\cos^2\theta\cos\phi) + (\cos\theta\sin\phi)(-R^2\cos^2\theta\sin\phi) + (\sin\theta)(-R^2\sin\theta\cos\theta) \right)
$$

Simplificando:
$$
= -k \left( \cos^3\theta\cos^2\phi + \cos^3\theta\sin^2\phi + \sin^2\theta\cos\theta \right)
$$
$$
= -k \left( \cos^3\theta(\cos^2\phi + \sin^2\phi) + \sin^2\theta\cos\theta \right)
$$
$$
= -k \left( \cos^3\theta + \sin^2\theta\cos\theta \right) = -k \cos\theta (\cos^2\theta + \sin^2\theta) = -k \cos\theta
$$

**Paso 5:** Plantear y resolver la integral de flujo.

$$
\iint_S \vec{F} \cdot d\vec{S} = \int_{0}^{2\pi} \int_{-\pi/2}^{\pi/2} (-k \cos\theta) \, d\theta \, d\phi
$$

Integramos respecto a $\theta$:
$$
\int_{0}^{2\pi} \left[ -k \sin\theta \right]_{-\pi/2}^{\pi/2} \, d\phi = \int_{0}^{2\pi} -k (\sin(\pi/2) - \sin(-\pi/2)) \, d\phi
$$
$$
= \int_{0}^{2\pi} -k (1 - (-1)) \, d\phi = \int_{0}^{2\pi} -2k \, d\phi
$$

Integramos respecto a $\phi$:
$$
\left[ -2k\phi \right]_{0}^{2\pi} = -2k(2\pi) = -4k\pi
$$

El flujo es $-4k\pi$.

</details>

</details>

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=4969s">1:22:49</a>: Flujo a través de un paraboloide (método cartesiano)</summary>

Calcular el flujo del campo vectorial $\vec{F}(x,y,z) = (x, y, z)$ a través de la porción del paraboloide $z = x^2 + y^2$ que se encuentra por debajo del plano $z=1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Definir la superficie como el conjunto de nivel de una función $g(x,y,z)$.

La superficie es $z - x^2 - y^2 = 0$. Definimos:
$$
g(x,y,z) = z - x^2 - y^2
$$

**Paso 2:** Calcular el gradiente de $g$, que servirá como vector normal.

$$
\nabla g = (\frac{\partial g}{\partial x}, \frac{\partial g}{\partial y}, \frac{\partial g}{\partial z}) = (-2x, -2y, 1)
$$
La componente $z$ es positiva, por lo que este vector apunta hacia arriba.

**Paso 3:** Usar la fórmula para superficies cartesianas.

La variable dependiente es $z$, y $\frac{\partial g}{\partial z} = 1$. La fórmula es:
$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_{S_{xy}} \vec{F}(x, y, x^2+y^2) \cdot \frac{\nabla g}{|\frac{\partial g}{\partial z}|} \, dx \, dy
$$

**Paso 4:** Calcular el producto escalar del integrando.

$$
\vec{F}(x, y, x^2+y^2) \cdot \frac{(-2x, -2y, 1)}{|1|} = (x, y, x^2+y^2) \cdot (-2x, -2y, 1)
$$
$$
= -2x^2 - 2y^2 + (x^2+y^2) = -(x^2+y^2)
$$

**Paso 5:** Determinar la región de integración $S_{xy}$.

La superficie está limitada por $z=1$. La proyección sobre el plano $xy$ es la región donde $x^2+y^2 \le 1$, que es un disco de radio 1 centrado en el origen.

**Paso 6:** Convertir la integral a coordenadas polares.

En polares, $x^2+y^2 = \rho^2$ y $dx\,dy = \rho\,d\rho\,d\phi$. El integrando es $-\rho^2$.
Los límites son $0 \le \rho \le 1$ y $0 \le \phi \le 2\pi$.

**Paso 7:** Resolver la integral.

$$
\iint_{S_{xy}} -(x^2+y^2) \, dx \, dy = \int_{0}^{2\pi} \int_{0}^{1} (-\rho^2) \cdot \rho \, d\rho \, d\phi
$$
$$
= \int_{0}^{2\pi} \int_{0}^{1} -\rho^3 \, d\rho \, d\phi
$$

Integramos respecto a $\rho$:
$$
\int_{0}^{2\pi} \left[ -\frac{\rho^4}{4} \right]_{0}^{1} \, d\phi = \int_{0}^{2\pi} -\frac{1}{4} \, d\phi
$$

Integramos respecto a $\phi$:
$$
\left[ -\frac{1}{4}\phi \right]_{0}^{2\pi} = -\frac{1}{4}(2\pi) = -\frac{\pi}{2}
$$

El flujo es $-\frac{\pi}{2}$.

</details>

</details>
