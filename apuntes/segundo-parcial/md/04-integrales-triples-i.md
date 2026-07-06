# Integrales triples I

> Fuente: https://www.youtube.com/watch?v=yraeybjD3jg

---

## Índice
- [00:01](https://www.youtube.com/watch?v=yraeybjD3jg&t=1s) — Definición de integral triple sobre una región proyectable
- [03:13](https://www.youtube.com/watch?v=yraeybjD3jg&t=193s) — 📝 Ejercicio 1: Integral de $xyz$ sobre un paralelepípedo
- [10:57](https://www.youtube.com/watch?v=yraeybjD3jg&t=657s) — La integral triple como volumen
- [15:17](https://www.youtube.com/watch?v=yraeybjD3jg&t=917s) — 📝 Ejercicio 2: Integral de $x$ sobre un tetraedro
- [28:15](https://www.youtube.com/watch?v=yraeybjD3jg&t=1695s) — El orden de integración es indistinto
- [30:21](https://www.youtube.com/watch?v=yraeybjD3jg&t=1821s) — Valor medio de una función en una región
- [31:24](https://www.youtube.com/watch?v=yraeybjD3jg&t=1884s) — 📝 Ejercicio 3: Valor medio (ejemplos 1 y 2)
- [40:32](https://www.youtube.com/watch?v=yraeybjD3jg&t=2432s) — Volumen del tetraedro genérico
- [41:36](https://www.youtube.com/watch?v=yraeybjD3jg&t=2496s) — 📝 Ejercicio 4: Volumen entre dos paraboloides
- [58:47](https://www.youtube.com/watch?v=yraeybjD3jg&t=3527s) — 📝 Ejercicio 5: Integral de $x^2+y^2$ sobre región cono-plano (coordenadas polares)
- [1:11:48](https://www.youtube.com/watch?v=yraeybjD3jg&t=4308s) — Teoremas: linealidad y aditividad
- [1:12:20](https://www.youtube.com/watch?v=yraeybjD3jg&t=4340s) — Cambio de variables en integrales triples
- [1:13:21](https://www.youtube.com/watch?v=yraeybjD3jg&t=4401s) — Coordenadas esféricas y su jacobiano
- [1:30:00](https://www.youtube.com/watch?v=yraeybjD3jg&t=5400s) — 📝 Ejercicio 6: Volumen de una esfera con coordenadas esféricas
- [1:37:38](https://www.youtube.com/watch?v=yraeybjD3jg&t=5858s) — Coordenadas cilíndricas
- [1:38:52](https://www.youtube.com/watch?v=yraeybjD3jg&t=5932s) — 📝 Ejercicio 7: Masa de un cuerpo con densidad variable

---

## Definición de integral triple sobre una región proyectable [00:01](https://www.youtube.com/watch?v=yraeybjD3jg&t=1s)

Se parte de dos funciones $g_1$ y $g_2$ continuas, definidas en el intervalo $[a,b] \subseteq \mathbb{R}$, tales que

$$
g_1(x) \le g_2(x) \quad \text{para todo } x \in [a,b]
$$

Con ellas se define en el plano una región de integración $D$ (la típica región de las integrales dobles), limitada por detrás por el plano $x=a$, por delante por $x=b$, por izquierda por la superficie $y=g_1(x)$ y por derecha por $y=g_2(x)$ (superficies normales al plano $xy$).

Se agregan además dos funciones de dos variables $h_1$ y $h_2$, continuas, tales que

$$
h_1(x,y) \le h_2(x,y) \quad \text{para todo } (x,y) \in D
$$

Con esto se define el conjunto sólido $E$ en $\mathbb{R}^3$: la región $D$ del plano, limitada por debajo por la gráfica de $h_1(x,y)$ y por arriba por la gráfica de $h_2(x,y)$.

Si $f$ es una función de tres variables **continua** en $E$, se define la **integral triple** de $f$ sobre $E$ como el resultado de tres integrales sucesivas: primero respecto de $z$, luego respecto de $y$ y por último respecto de $x$, usando como límites las funciones o constantes definidas:

$$
\iiint_E f\,dV = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)} f(x,y,z)\,dz\,dy\,dx
$$

Lo importante es identificar claramente la forma de la región de integración.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=193s">03:13</a>: Integral de $xyz$ sobre un paralelepípedo</summary>

Calcular la integral de la función $f(x,y,z) = x\,y\,z$ sobre la región $E$ en la que $x$ varía de $0$ a $2$, $y$ varía de $0$ a $3$ y $z$ varía de $0$ a $4$ (un paralelepípedo de lados $2$, $3$ y $4$).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la región. Es un paralelepípedo; su proyección $D$ sobre el plano $xy$ es el rectángulo de lados $2 \times 3$. Los límites son $x \in [0,2]$, $y \in [0,3]$, $z \in [0,4]$.

**Paso 2:** Plantear la integral triple, integrando primero respecto de $z$.

$$
\int_0^2 \int_0^3 \int_0^4 x\,y\,z \,dz\,dy\,dx
$$

**Paso 3:** Integrar respecto de $z$ (con $x$ e $y$ constantes). La integral de $z$ es $\frac{z^2}{2}$ evaluada entre $0$ y $4$.

$$
\int_0^4 z\,dz = \left[\frac{z^2}{2}\right]_0^4 = \frac{16}{2} - 0 = 8
$$

**Paso 4:** El $8$ sale fuera de la integral doble. Queda por integrar $x\,y$ respecto de $y$ (con $x$ constante); la integral de $y$ es $\frac{y^2}{2}$ entre $0$ y $3$.

$$
\int_0^3 y\,dy = \left[\frac{y^2}{2}\right]_0^3 = \frac{9}{2}
$$

**Paso 5:** Ese $\frac{9}{2}$ sale fuera de la integral en $x$. Queda

$$
8 \cdot \frac{9}{2} \int_0^2 x\,dx
$$

Simplificando el $8$ con el $2$ queda $4$, y $9 \cdot 4 = 36$.

**Paso 6:** Integrar respecto de $x$: $\int_0^2 x\,dx = \left[\frac{x^2}{2}\right]_0^2 = \frac{4}{2} = 2$.

$$
\iiint_E x\,y\,z\,dV = 36 \cdot 2 = 72
$$

</details>

</details>

## La integral triple como volumen [10:57](https://www.youtube.com/watch?v=yraeybjD3jg&t=657s)

En lugar de resolver dos integrales sucesivas (como en las dobles), una integral triple resulta de tres integrales sucesivas, una tras otra.

En el caso particular en que la **función a integrar es la constante $1$**, la integral triple se interpreta como el **volumen de la región** de integración. Partiendo de la definición general del conjunto $E$:

$$
\iiint_E 1\,dV = \int_a^b \int_{g_1(x)}^{g_2(x)} \int_{h_1(x,y)}^{h_2(x,y)} dz\,dy\,dx
$$

La integral interior en $z$ vale $h_2 - h_1$, con lo que se reduce a una integral doble:

$$
\iiint_E 1\,dV = \iint_D \left[ h_2(x,y) - h_1(x,y) \right] dA = V_E
$$

que es exactamente el volumen limitado por arriba por $h_2$, por debajo por $h_1$ y lateralmente por las superficies normales al plano que contienen la frontera de $D$.

**No hay que confundir** el volumen de la región con la integral de una función sobre esa región. Por ejemplo, en el Ejercicio 1 el volumen del paralelepípedo es $2 \cdot 3 \cdot 4 = 24$, mientras que la integral de $x\,y\,z$ sobre esa misma región dio $72$. Ambos valores solo coinciden cuando la función integrada es la unitaria.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=917s">15:17</a>: Integral de $x$ sobre un tetraedro</summary>

Calcular la integral de la función $f(x,y,z) = x$ sobre la región de integración definida por $x \ge 0$, $y \ge 0$, $z \ge 0$ (primer octante) y limitada por el plano $x + y + z = 6$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la región. Al estar todas las coordenadas en el primer octante y por debajo del plano $x+y+z=6$ (que corta a los ejes $x$, $y$, $z$ en $6$), la región es un tetraedro.

**Paso 2:** Determinar los límites. Para $x \in [0,6]$; la recta intersección del plano con $z=0$ es $x+y=6$, de donde $y = 6-x$, así que $y \in [0, 6-x]$. Para $(x,y)$ en la región, $z$ va del piso al plano $z = 6-x-y$, así que $z \in [0, 6-x-y]$.

$$
\iiint_E x\,dV = \int_0^6 \int_0^{6-x} \int_0^{6-x-y} x \,dz\,dy\,dx
$$

**Paso 3:** Integrar respecto de $z$ ($x$ constante): $\int_0^{6-x-y} x\,dz = x(6-x-y)$.

$$
\int_0^6 \int_0^{6-x} x(6-x-y)\,dy\,dx = \int_0^6 \int_0^{6-x} (6x - x^2 - xy)\,dy\,dx
$$

**Paso 4:** Integrar respecto de $y$ entre $0$ y $6-x$.

$$
\int_0^{6-x} (6x - x^2 - xy)\,dy = \left[ 6xy - x^2 y - \frac{x y^2}{2} \right]_0^{6-x}
$$

**Paso 5:** Reemplazar $y = 6-x$ (en $y=0$ todo se anula) y desarrollar. Operando queda el integrando en $x$:

$$
\frac{x^3}{2} - 6x^2 + 18x
$$

[paso en el pizarrón, ver video]

**Paso 6:** Integrar respecto de $x$ entre $0$ y $6$.

$$
\int_0^6 \left( \frac{x^3}{2} - 6x^2 + 18x \right) dx = \left[ \frac{x^4}{8} - 2x^3 + 9x^2 \right]_0^6
$$

**Paso 7:** Reemplazar $x=6$. Sacando factor común $x^2=36$:

$$
= 36\left( \frac{36}{8} - 12 + 9 \right) = 36 \cdot \frac{3}{2} = 54
$$

$$
\iiint_E x\,dV = 54
$$

</details>

</details>

## El orden de integración es indistinto [28:15](https://www.youtube.com/watch?v=yraeybjD3jg&t=1695s)

Igual que en las integrales dobles, el **orden de integración es totalmente indistinto**, siempre que se expresen correctamente los extremos de integración.

La condición clave es que:

- La **última** integral a resolver (la exterior) debe estar entre **dos constantes**.
- La **segunda** debe estar entre **dos funciones de una variable**.
- La **primera** (interior) entre **dos funciones de dos variables**.

Cumpliendo esto se pueden hacer las $6$ combinaciones posibles de orden (por ejemplo: $y$ entre constantes, $x$ entre funciones de $y$, $z$ entre funciones de $x,y$; o $z$ entre constantes, $y$ entre funciones de $z$, $x$ entre funciones de $z,y$; etc.).

## Valor medio de una función en una región [30:21](https://www.youtube.com/watch?v=yraeybjD3jg&t=1821s)

El **valor medio** de una función $f$ de tres variables en una región $E$ se define como el cociente entre la integral triple de $f$ sobre $E$ y el volumen de $E$:

$$
\bar{f} = \frac{\displaystyle\iiint_E f\,dV}{\displaystyle\iiint_E 1\,dV} = \frac{1}{V_E}\iiint_E f\,dV
$$

donde el volumen $V_E$ surge de integrar la función unitaria sobre $E$. Equivalentemente:

$$
\iiint_E f\,dV = \bar{f}\cdot V_E
$$

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=1884s">31:24</a>: Valor medio (ejemplos 1 y 2)</summary>

Calcular el valor medio de las funciones de los Ejercicios 1 y 2 sobre sus respectivas regiones:
1. $f(x,y,z) = x\,y\,z$ sobre el paralelepípedo de lados $2,3,4$.
2. $f(x,y,z) = x$ sobre el tetraedro del primer octante limitado por $x+y+z=6$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (ejemplo 1):** La integral ya dio $72$ y el volumen del paralelepípedo es $2 \cdot 3 \cdot 4 = 24$.

$$
\bar{f} = \frac{72}{24} = 3
$$

La función $x\,y\,z$ vale $0$ en el origen y $24$ en el vértice $(2,3,4)$; en promedio sobre la región vale $3$.

**Paso 2 (ejemplo 2):** La integral dio $54$. Falta el volumen del tetraedro, que se calcula integrando la función unitaria.

$$
V = \int_0^6 \int_0^{6-x} \int_0^{6-x-y} dz\,dy\,dx
$$

**Paso 3:** Integrar en $z$ y luego en $y$ entre $0$ y $6-x$.

$$
\int_0^{6-x}(6-x-y)\,dy = \left[ 6y - xy - \frac{y^2}{2}\right]_0^{6-x}
$$

Reemplazando $y=6-x$ y desarrollando queda, respecto de $x$:

$$
\frac{x^2}{2} - 6x + 18
$$

[paso en el pizarrón, ver video]

**Paso 4:** Integrar respecto de $x$ entre $0$ y $6$.

$$
V = \int_0^6 \left( \frac{x^2}{2} - 6x + 18 \right) dx = \left[ \frac{x^3}{6} - 3x^2 + 18x \right]_0^6
$$

Reemplazando $x=6$ (sacando factor común $x=6$): $6\left(\frac{36}{6} - 18 + 18\right)$… operando da $V = 36$.

**Paso 5:** El valor medio del ejemplo 2:

$$
\bar{f} = \frac{54}{36} = \frac{3}{2} = 1{,}5
$$

La función $x$ vale $0$ atrás (sobre el plano $yz$) y $6$ adelante; en promedio sobre la región vale $1{,}5$.

</details>

</details>

## Volumen del tetraedro genérico [40:32](https://www.youtube.com/watch?v=yraeybjD3jg&t=2432s)

Para un tetraedro genérico cuyos catetos (sobre los tres ejes) valen $a$, $b$ y $c$, el volumen es

$$
V = \frac{a\,b\,c}{6}
$$

En el ejemplo del tetraedro los catetos eran $6$, $6$ y $6$, de modo que

$$
V = \frac{6 \cdot 6 \cdot 6}{6} = 36
$$

tal cual dio la integral de la función unitaria.

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=2496s">41:36</a>: Volumen entre dos paraboloides</summary>

Calcular el volumen del conjunto $E$ de los puntos $(x,y,z) \in \mathbb{R}^3$ tales que

$$
x^2 + y^2 \le z \le 4x^2 + 4y^2, \qquad x^2 \le y \le 3x
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Interpretar las condiciones. $z$ está entre el paraboloide $z = x^2+y^2$ (por debajo) y el paraboloide más "cerrado" $z = 4x^2+4y^2$ (por arriba, crece más rápido). En el plano $xy$, la región $D$ está entre la parábola $y = x^2$ y la recta $y = 3x$.

**Paso 2:** Determinar el rango de $x$. De $x^2 \le y \le 3x$ se deduce $x^2 \le 3x$, es decir $x^2 - 3x \le 0$, o sea $x(x-3) \le 0$. El producto es $\le 0$ cuando los factores tienen distinto signo, lo que da $0 \le x \le 3$.

**Paso 3:** Plantear el volumen. La variable entre constantes es $x \in [0,3]$; $y$ entre las funciones $x^2$ y $3x$; $z$ entre los dos paraboloides.

$$
V = \int_0^3 \int_{x^2}^{3x} \int_{x^2+y^2}^{4x^2+4y^2} dz\,dy\,dx
$$

**Paso 4:** Integrar en $z$: el límite superior menos el inferior.

$$
(4x^2+4y^2) - (x^2+y^2) = 3x^2 + 3y^2
$$

$$
V = \int_0^3 \int_{x^2}^{3x} (3x^2 + 3y^2)\,dy\,dx
$$

**Paso 5:** Integrar respecto de $y$ entre $x^2$ y $3x$.

$$
\int_{x^2}^{3x} (3x^2 + 3y^2)\,dy = \left[ 3x^2 y + y^3 \right]_{x^2}^{3x}
$$

**Paso 6:** Reemplazar. Con $y=3x$: $9x^3 + 27x^3 = 36x^3$. Con $y=x^2$: $3x^4 + x^6$. Restando:

$$
36x^3 - 3x^4 - x^6
$$

**Paso 7:** Integrar respecto de $x$ entre $0$ y $3$.

$$
V = \int_0^3 (36x^3 - 3x^4 - x^6)\,dx = \left[ 9x^4 - \frac{3x^5}{5} - \frac{x^7}{7} \right]_0^3
$$

**Paso 8:** Reemplazar $x=3$ (sacando factor común $x^4 = 81$).

$$
V = 81\left( 9 - \frac{9}{5}\cdot 3 - \frac{27}{7} \right) = \frac{9477}{35}
$$

El resultado del volumen es $\dfrac{9477}{35}$ [poco claro en la transcripción: el profesor duda del valor exacto y lo confirma con el apunte].

</details>

</details>

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=3527s">58:47</a>: Integral de $x^2+y^2$ sobre región cono-plano</summary>

Evaluar la integral de la función $f(x,y,z) = x^2 + y^2$ sobre la región limitada por debajo por el cono $z = \sqrt{x^2+y^2}$ y por arriba por el plano $z = 2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reconocer las superficies. $z = \sqrt{x^2+y^2}$ es un cono (si $y=0$, $z=|x|$, dos rectas). La región $E$ está por arriba del cono y por debajo del plano $z=2$.

**Paso 2:** Hallar la proyección $D$ en el plano $xy$. La intersección del plano con el cono cumple $2 = \sqrt{x^2+y^2}$, y elevando al cuadrado:

$$
x^2 + y^2 = 4
$$

que es una circunferencia de radio $2$. Luego $D$ es el disco $x^2+y^2 \le 4$.

**Paso 3:** Plantear con $z$ del cono al plano.

$$
\iiint_E (x^2+y^2)\,dV = \iint_D \int_{\sqrt{x^2+y^2}}^{2} (x^2+y^2)\,dz\,dA
$$

**Paso 4:** Integrar en $z$ ($x^2+y^2$ es constante respecto de $z$).

$$
= \iint_D (x^2+y^2)\left(2 - \sqrt{x^2+y^2}\right) dA
$$

**Paso 5:** Como $D$ es el interior de una circunferencia y aparece $x^2+y^2$, se usan **coordenadas polares**: $x = \rho\cos\varphi$, $y = \rho\sin\varphi$, con $|J| = \rho$, $x^2+y^2 = \rho^2$ y $\sqrt{x^2+y^2}=\rho$. Los límites: $\rho \in [0,2]$, $\varphi \in [0,2\pi]$.

$$
= \int_0^{2\pi} \int_0^2 \rho^2 (2 - \rho)\,\rho \,d\rho\,d\varphi
$$

**Paso 6:** El integrando no depende de $\varphi$: la integral en $\varphi$ da $2\pi$. Distribuyendo queda $2\rho^3 - \rho^4$.

$$
= 2\pi \int_0^2 (2\rho^3 - \rho^4)\,d\rho
$$

**Paso 7:** Integrar respecto de $\rho$.

$$
= 2\pi \left[ \frac{\rho^4}{2} - \frac{\rho^5}{5} \right]_0^2 = 2\pi \left( 8 - \frac{32}{5} \right)
$$

**Paso 8:** Operar: $8 = \frac{40}{5}$, así que $\frac{40}{5} - \frac{32}{5} = \frac{8}{5}$.

$$
\iiint_E (x^2+y^2)\,dV = 2\pi \cdot \frac{8}{5} = \frac{16}{5}\pi
$$

</details>

</details>

## Teoremas: linealidad y aditividad [1:11:48](https://www.youtube.com/watch?v=yraeybjD3jg&t=4308s)

Los teoremas básicos son:

- **Linealidad:** la integral de una suma es la suma de las integrales, y las constantes se pueden sacar fuera de la integral.
- **Aditividad respecto de la región:** si el conjunto $E$ se divide en dos partes y se integra la función sobre cada parte, el resultado es el mismo que integrar sobre la totalidad de $E$.

## Cambio de variables en integrales triples [1:12:20](https://www.youtube.com/watch?v=yraeybjD3jg&t=4340s)

En ocasiones conviene resolver integrales triples mediante un cambio de variables directo (sobre las tres variables, sin pasar antes por una integral doble). Para una transformación de coordenadas de tres variables en tres variables, el **jacobiano** se define como el determinante de la matriz jacobiana $3\times 3$:

$$
J = \frac{\partial(x,y,z)}{\partial(u,v,w)} = \det \begin{pmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} & \frac{\partial x}{\partial w} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} & \frac{\partial y}{\partial w} \\ \frac{\partial z}{\partial u} & \frac{\partial z}{\partial v} & \frac{\partial z}{\partial w} \end{pmatrix}
$$

**Teorema del cambio de variables (integrales triples):** si $g$ es una transformación de coordenadas del conjunto $E^*$ (en las variables $u,v,w$) al conjunto $E$ (en $x,y,z$) tal que, en el **interior** de $E^*$:

- $g$ es **inyectiva** (a puntos distintos les corresponden imágenes distintas),
- $g$ es de **clase $C^1$** (las tres funciones componentes tienen derivadas parciales continuas),
- el **jacobiano no se anula**,

entonces

$$
\iiint_E f(x,y,z)\,dx\,dy\,dz = \iiint_{E^*} f\big(g(u,v,w)\big)\,\left| J \right|\,du\,dv\,dw
$$

Es el mismo teorema de las integrales dobles agregando una variable. No se demuestra; solo se usa.

## Coordenadas esféricas y su jacobiano [1:13:21](https://www.youtube.com/watch?v=yraeybjD3jg&t=4401s)

Las **coordenadas esféricas** asignan a un punto de $\mathbb{R}^3$:

- $\rho$: distancia del punto al origen, siempre $\rho \ge 0$.
- $\theta$: ángulo que forma el segmento (desde el origen hasta el punto) con el plano $xy$. Toma valores $\theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ (positivo por encima del plano $xy$, negativo por debajo).
- $\varphi$: ángulo que forma la proyección de ese segmento sobre el plano $xy$ con el eje $x$. Toma valores $\varphi \in [0, 2\pi]$.

Las relaciones con las cartesianas son:

$$
x = \rho\cos\theta\cos\varphi, \quad y = \rho\cos\theta\sin\varphi, \quad z = \rho\sin\theta
$$

El jacobiano de esta transformación resulta:

$$
J = -\rho^2 \cos\theta
$$

Conviene recordarlo de memoria para no tener que desarrollar el determinante cada vez.

<details>
<summary>📝 Ejercicio (deducción) — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=4689s">1:18:09</a>: Cálculo del jacobiano de las coordenadas esféricas</summary>

Calcular el jacobiano de la transformación a coordenadas esféricas $x = \rho\cos\theta\cos\varphi$, $y = \rho\cos\theta\sin\varphi$, $z = \rho\sin\theta$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Armar la matriz jacobiana, derivando cada componente respecto de $\rho$, $\theta$, $\varphi$.

$$
\begin{pmatrix}
\cos\theta\cos\varphi & -\rho\sin\theta\cos\varphi & -\rho\cos\theta\sin\varphi \\
\cos\theta\sin\varphi & -\rho\sin\theta\sin\varphi & \rho\cos\theta\cos\varphi \\
\sin\theta & \rho\cos\theta & 0
\end{pmatrix}
$$

**Paso 2:** Desarrollar el determinante por la tercera fila (el último elemento es $0$).

**Paso 3:** El término con $\sin\theta$ da (menor correspondiente):

$$
\sin\theta\left( -\rho^2\sin\theta\cos\theta\cos^2\varphi - \rho^2\sin\theta\cos\theta\sin^2\varphi \right)
$$

Sacando factor común $-\rho^2\sin\theta\cos\theta$ y usando $\cos^2\varphi + \sin^2\varphi = 1$, queda $-\rho^2\sin^2\theta\cos\theta$.

**Paso 4:** El término con $-\rho\cos\theta$ da, análogamente, $-\rho^2\cos^3\theta$ [paso en el pizarrón, ver video].

**Paso 5:** Sumar ambos y sacar factor común $-\rho^2\cos\theta$.

$$
J = -\rho^2\cos\theta\left( \sin^2\theta + \cos^2\theta \right) = -\rho^2\cos\theta
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=5400s">1:30:00</a>: Volumen de una esfera con coordenadas esféricas</summary>

Calcular el volumen limitado por una superficie esférica de radio $R$ centrada en el origen.

<details>
<summary>Ver resolución</summary>

**Paso 1:** El volumen es $V = \iiint_E 1\,dV$. En lugar de plantear límites cartesianos, se usan coordenadas esféricas con $x = \rho\cos\theta\cos\varphi$, $y = \rho\cos\theta\sin\varphi$, $z = \rho\sin\theta$.

**Paso 2:** El módulo del jacobiano. Como $J = -\rho^2\cos\theta$:

$$
|J| = |-1|\cdot|\rho^2|\cdot|\cos\theta| = \rho^2\cos\theta
$$

($\rho^2 \ge 0$ siempre, y $\cos\theta \ge 0$ porque $\theta \in \left[-\frac{\pi}{2},\frac{\pi}{2}\right]$).

**Paso 3:** Plantear la integral. Los límites para la esfera: $\rho \in [0,R]$, $\theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$, $\varphi \in [0, 2\pi]$.

$$
V = \int_0^{2\pi} \int_{-\pi/2}^{\pi/2} \int_0^{R} \rho^2\cos\theta \,d\rho\,d\theta\,d\varphi
$$

**Paso 4:** El integrando no depende de $\varphi$: la integral en $\varphi$ da $2\pi$.

**Paso 5:** La integral en $\theta$ del coseno.

$$
\int_{-\pi/2}^{\pi/2} \cos\theta\,d\theta = \left[\sin\theta\right]_{-\pi/2}^{\pi/2} = 1 - (-1) = 2
$$

**Paso 6:** La integral en $\rho$.

$$
\int_0^R \rho^2\,d\rho = \left[\frac{\rho^3}{3}\right]_0^R = \frac{R^3}{3}
$$

**Paso 7:** Multiplicar los tres factores.

$$
V = 2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac{4}{3}\pi R^3
$$

que es el volumen conocido de la esfera. Resulta mucho más sencillo con coordenadas esféricas que con cartesianas o polares.

</details>

</details>

## Coordenadas cilíndricas [1:37:38](https://www.youtube.com/watch?v=yraeybjD3jg&t=5858s)

Las **coordenadas cilíndricas** combinan coordenadas polares en el plano $xy$ con la altura $z$ sin cambios:

$$
x = \rho\cos\varphi, \quad y = \rho\sin\varphi, \quad z = z
$$

con $\rho \ge 0$ y $\varphi \in [0, 2\pi]$. El jacobiano de esta transformación es

$$
J = \rho, \qquad |J| = \rho
$$

(se obtiene desarrollando el determinante $3\times 3$ por la tercera columna, que tiene muchos ceros; equivale al jacobiano de las polares con la fila/columna de $z$ dando $1$).

<details>
<summary>📝 Ejercicio 7 — <a href="https://www.youtube.com/watch?v=yraeybjD3jg&t=5932s">1:38:52</a>: Masa de un cuerpo con densidad variable</summary>

(Final del 4 de diciembre de 2018.) Dado el cuerpo definido por

$$
x^2 + y^2 \le 9, \qquad 0 \le z \le 16 - x^2 - y^2
$$

calcular la masa sabiendo que en cada punto su densidad es proporcional a la distancia del punto al eje $z$. Es decir, la densidad es

$$
\delta(x,y,z) = k\sqrt{x^2+y^2}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** La masa es la integral triple de la densidad sobre la región. Por la simetría respecto del eje $z$ (aparece $x^2+y^2$) conviene usar **coordenadas cilíndricas**: $x = \rho\cos\varphi$, $y = \rho\sin\varphi$, $z = z$, con $|J| = \rho$.

**Paso 2:** Transformar la región. De $x^2+y^2 \le 9$ queda $\rho^2 \le 9$, o sea $\rho \le 3$. De $0 \le z \le 16 - x^2 - y^2$ queda $0 \le z \le 16 - \rho^2$. Además $\varphi \in [0, 2\pi]$.

**Paso 3:** Transformar la densidad. $\sqrt{x^2+y^2} = \sqrt{\rho^2} = |\rho| = \rho$ (pues $\rho \ge 0$), así que $\delta = k\rho$.

**Paso 4:** Plantear la integral de la masa (densidad por jacobiano), integrando primero en $z$.

$$
m = \int_0^{2\pi}\int_0^3 \int_0^{16-\rho^2} (k\rho)\cdot \rho \,dz\,d\rho\,d\varphi
$$

(La restricción $\rho^2 \le 16$, es decir $\rho \le 4$, es redundante frente a $\rho \le 3$, y se descarta.)

**Paso 5:** Integrar en $z$: la integral de $dz$ da $16 - \rho^2$.

$$
m = k\int_0^{2\pi}\int_0^3 \rho^2 (16-\rho^2)\,d\rho\,d\varphi
$$

**Paso 6:** El integrando no depende de $\varphi$: la integral en $\varphi$ da $2\pi$.

$$
m = 2\pi k \int_0^3 (16\rho^2 - \rho^4)\,d\rho
$$

**Paso 7:** Integrar respecto de $\rho$.

$$
\int_0^3 (16\rho^2 - \rho^4)\,d\rho = \left[ \frac{16\rho^3}{3} - \frac{\rho^5}{5}\right]_0^3 = \frac{16\cdot 27}{3} - \frac{3^5}{5} = 144 - \frac{243}{5} = \frac{477}{5}
$$

[paso en el pizarrón, ver video: la simplificación intermedia]

**Paso 8:** Multiplicar por $2\pi k$.

$$
m = 2\pi k \cdot \frac{477}{5} = \frac{954}{5}\pi\,k
$$

Geométricamente, el cuerpo es el interior de un cilindro de radio $3$, con piso en $z=0$ y techo en el paraboloide $z = 16 - x^2 - y^2$; la masa crece con la distancia al eje $z$ (más maciza hacia la cáscara).

</details>

</details>
