# Integrales dobles III

> Fuente: https://www.youtube.com/watch?v=v6XSV4ohEtY

---

## Índice
- [00:00](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=0s) — Momento estático (momento de primer orden)
- [01:07](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=67s) — 📝 Ejercicio 1: Momento estático de un sector circular
- [15:09](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=909s) — Baricentro de una región del plano
- [16:11](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=971s) — 📝 Ejercicio 2: Baricentro de un triángulo rectángulo
- [25:57](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=1557s) — 📝 Ejercicio 3: Baricentro de un semicírculo
- [35:03](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2103s) — Momento estático respecto a un eje baricéntrico
- [38:48](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2328s) — Momentos de inercia (momentos de segundo orden)
- [39:19](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2359s) — 📝 Ejercicio 4: Momento de inercia de una sección rectangular
- [45:14](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2714s) — 📝 Ejercicio 5: Momento de inercia de una sección circular
- [55:36](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=3336s) — Momento de inercia polar
- [58:43](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=3523s) — Teorema de Steiner
- [1:07:22](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=4042s) — Densidad, masa y momentos de regiones con densidad
- [1:08:28](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=4108s) — 📝 Ejercicio 6: Masa de una placa con densidad variable

---

## Momento estático (momento de primer orden) [00:00](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=0s)

Dada una región de integración $D$ definida en el plano $xy$, se define el **momento estático** (o **momento de primer orden**) de esa región respecto a un eje.

El momento estático de $D$ **respecto al eje $x$** se define como:

$$
M_x = \iint_D y \,dx\,dy
$$

El momento estático de $D$ **respecto al eje $y$** se define como:

$$
M_y = \iint_D x \,dx\,dy
$$

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=67s">01:07</a>: Momento estático de un sector circular</summary>

Calcular el momento estático (momento de primer orden) de una región circular de radio $R$ respecto a un eje tangente a su perímetro.

Se ubica la circunferencia tangente al eje $x$, de modo que queda desplazada $R$ unidades en la dirección del eje $y$. La región $D$ está formada por todos los puntos del plano que satisfacen:

$$
x^2 + (y - R)^2 \le R^2
$$

Se pide el momento estático respecto al eje $x$ (el eje tangente).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear el momento estático respecto al eje $x$.

$$
M_x = \iint_D y \,dx\,dy
$$

**Paso 2:** Como la región es el interior de una circunferencia, conviene trabajar en **coordenadas polares** con $x = \rho\cos\varphi$, $y = \rho\sin\varphi$. El módulo del jacobiano es $|J| = \rho$ (se usa el módulo porque $\rho$ no siempre es positivo, aunque aquí lo es). Hay que multiplicar el integrando por $\rho$, y como $y = \rho\sin\varphi$, queda $\rho^2\sin\varphi$.

**Paso 3:** Determinar los límites de integración. El ángulo $\varphi$ varía entre $0$ y $\pi$ (no hay puntos del conjunto en el tercer ni el cuarto cuadrante). Para el radio $\rho$, el máximo se obtiene reemplazando $x = \rho\cos\varphi$, $y = \rho\sin\varphi$ en la ecuación de la circunferencia:

$$
x^2 + (y - R)^2 \le R^2 \;\Rightarrow\; x^2 + y^2 - 2Ry + R^2 \le R^2
$$

$$
\rho^2 - 2R\,\rho\sin\varphi \le 0 \;\Rightarrow\; \rho\,(\rho - 2R\sin\varphi) \le 0
$$

**Paso 4:** Como $\rho \ge 0$, el factor $\rho - 2R\sin\varphi$ debe ser $\le 0$, es decir $\rho \le 2R\sin\varphi$. Así, $\rho$ varía entre $0$ y $2R\sin\varphi$ (por ejemplo, en $\varphi = \pi/2$ la distancia máxima al origen es $2R$).

$$
M_x = \int_0^{\pi} \int_0^{2R\sin\varphi} \rho^2\sin\varphi \,d\rho\,d\varphi
$$

**Paso 5:** Integrar primero respecto de $\rho$. La integral de $\rho^2$ es $\rho^3/3$, evaluada entre $0$ y $2R\sin\varphi$:

$$
M_x = \int_0^{\pi} \frac{(2R\sin\varphi)^3}{3}\,\sin\varphi \,d\varphi = \frac{8R^3}{3}\int_0^{\pi} \sin^4\varphi \,d\varphi
$$

**Paso 6:** La integral de $\sin^4\varphi$ se busca en la tabla de integrales:

$$
\int \sin^4\varphi \,d\varphi = \frac{3}{8}\varphi - \frac{\sin(2\varphi)}{4} + \frac{\sin(4\varphi)}{32}
$$

**Paso 7:** Evaluar entre $0$ y $\pi$. Al reemplazar $\varphi = \pi$ quedan $\sin(2\pi) = 0$ y $\sin(4\pi) = 0$, y al reemplazar $\varphi = 0$ todo se anula, por lo que solo sobrevive el término $\frac{3}{8}\pi$:

$$
M_x = \frac{8R^3}{3} \cdot \frac{3}{8}\pi = \pi R^3
$$

El $\frac{8}{3}$ se simplifica con el $\frac{3}{8}$, y queda el momento estático de la región respecto al eje tangente:

$$
M_x = \pi R^3
$$

</details>

</details>

## Baricentro de una región del plano [15:09](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=909s)

Definido el momento estático de una región del plano, se puede definir el **baricentro** (centro de gravedad) de esa región respecto a un eje.

La coordenada $x$ del baricentro se define como el cociente entre el momento estático respecto al eje $y$ y el área de la región:

$$
x_G = \frac{M_y}{A_D} = \frac{\displaystyle\iint_D x \,dx\,dy}{A_D}
$$

La coordenada $y$ del baricentro se define como el cociente entre el momento estático respecto al eje $x$ y el área de la región:

$$
y_G = \frac{M_x}{A_D} = \frac{\displaystyle\iint_D y \,dx\,dy}{A_D}
$$

Estas definiciones permiten ubicar el baricentro de una región del plano. Corresponden al método físico de determinar el baricentro de una chapa plana homogénea colgándola desde distintos puntos y trazando verticales (visto en Física I).

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=971s">16:11</a>: Baricentro de un triángulo rectángulo</summary>

Determinar el baricentro de una región triangular del plano: un triángulo rectángulo de base $b$ y altura $h$, con los catetos apoyados sobre el eje $x$ y el eje $y$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** La coordenada $x$ del baricentro es el cociente entre el momento estático respecto al eje $y$ y el área:

$$
x_G = \frac{M_y}{A_D}
$$

**Paso 2:** El área del triángulo rectángulo es inmediata (no requiere integral):

$$
A_D = \frac{b\,h}{2}
$$

**Paso 3:** Describir la región. Para $x$ entre $0$ y $b$, la variable $y$ va desde $0$ hasta la recta que corta el eje $x$ en $b$ y el eje $y$ en $h$, cuya ecuación es $\frac{x}{b} + \frac{y}{h} = 1$. Despejando:

$$
D = \left\{ (x,y) : 0 \le x \le b,\; 0 \le y \le \left(1 - \tfrac{x}{b}\right)h \right\}
$$

**Paso 4:** Plantear el momento estático respecto al eje $y$, integrando primero respecto de $y$:

$$
M_y = \int_0^{b} \int_0^{(1 - x/b)h} x \,dy\,dx
$$

**Paso 5:** Como $x$ no depende de $y$, la integral interior da el extremo superior:

$$
M_y = \int_0^{b} x\left(1 - \frac{x}{b}\right)h \,dx = h\int_0^{b}\left(x - \frac{x^2}{b}\right)dx
$$

**Paso 6:** Integrar respecto de $x$:

$$
M_y = h\left[\frac{x^2}{2} - \frac{x^3}{3b}\right]_0^{b} = h\left(\frac{b^2}{2} - \frac{b^2}{3}\right)
$$

**Paso 7:** Sacar denominador común $6$:

$$
M_y = h\,\frac{b^2(3 - 2)}{6} = \frac{h\,b^2}{6}
$$

**Paso 8:** Calcular la coordenada $x$ del baricentro dividiendo por el área:

$$
x_G = \frac{M_y}{A_D} = \frac{h\,b^2/6}{b\,h/2} = \frac{b}{3}
$$

**Paso 9:** El baricentro está a una distancia $\frac{b}{3}$ del cateto vertical. Por simetría del problema, análogamente:

$$
y_G = \frac{h}{3}
$$

El baricentro del triángulo rectángulo se encuentra a un tercio de cada cateto.

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=1557s">25:57</a>: Baricentro de un semicírculo</summary>

Calcular el baricentro de un sector circular de radio $R$ y ángulo interno $\pi$ (media circunferencia), ubicado con su diámetro sobre el eje $x$ y simétrico respecto al eje $y$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Por simetría del conjunto respecto al eje $y$, se anticipa que el baricentro está sobre el eje $y$. La coordenada $x$ se calcula como:

$$
x_G = \frac{\displaystyle\iint_D x \,dx\,dy}{A_D}
$$

**Paso 2:** La función $x$ es **antisimétrica** respecto al eje $y$: por cada diferencial de área a la derecha del eje (con $x > 0$) hay otro simétrico a la izquierda (con $x < 0$) del mismo valor absoluto. Los productos $x\,dx\,dy$ se compensan y la integral vale $0$:

$$
\iint_D x \,dx\,dy = 0 \;\Rightarrow\; x_G = 0
$$

**Paso 3:** La coordenada $y$ del baricentro sí requiere resolver la integral (la función $y$ no es simétrica). En coordenadas polares, con $y = \rho\sin\varphi$ y jacobiano $\rho$:

$$
M_x = \iint_D y \,dx\,dy = \int_0^{\pi}\int_0^{R} \rho\sin\varphi \cdot \rho \,d\rho\,d\varphi
$$

**Paso 4:** $\rho$ varía entre $0$ y $R$, y $\varphi$ entre $0$ y $\pi$. Integrar respecto de $\varphi$ el $\sin\varphi$ da $-\cos\varphi$:

$$
\int_0^{\pi} \sin\varphi \,d\varphi = -\cos\varphi \Big|_0^{\pi} = -(\cos\pi - \cos 0) = -(-1 - 1) = 2
$$

**Paso 5:** Integrar respecto de $\rho$ el $\rho^2$ da $\rho^3/3$ entre $0$ y $R$:

$$
\int_0^{R} \rho^2 \,d\rho = \frac{R^3}{3}
$$

Por lo tanto el momento estático es:

$$
M_x = 2 \cdot \frac{R^3}{3} = \frac{2}{3}R^3
$$

**Paso 6:** El área de la región es media circunferencia:

$$
A_D = \frac{\pi R^2}{2}
$$

**Paso 7:** Calcular $y_G$ dividiendo el momento estático por el área:

$$
y_G = \frac{M_x}{A_D} = \frac{\tfrac{2}{3}R^3}{\tfrac{\pi R^2}{2}} = \frac{4}{3}\frac{R}{\pi} \approx 0{,}42\,R
$$

El valor exacto es $y_G = \dfrac{4R}{3\pi}$. La altura del baricentro queda un poco por debajo de la mitad del radio, lo cual es razonable porque hay más área en la parte inferior que en la superior.

</details>

</details>

## Momento estático respecto a un eje baricéntrico [35:03](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2103s)

Es fácil demostrar que si se calcula el momento estático de una región $D$ respecto a un eje que **pasa por su baricentro**, ese momento estático vale **cero**.

Si el eje $x$ pasa por el baricentro de la sección, entonces la coordenada $y_G = 0$. Como

$$
y_G = \frac{M_x}{A_D}
$$

y $A_D$ es un número distinto de cero, necesariamente:

$$
M_x = y_G \cdot A_D = 0
$$

Del mismo modo, si ambos ejes pasan por el baricentro, el momento estático respecto a cualquiera de los dos ejes es cero. Es una propiedad de los momentos estáticos respecto a ejes baricéntricos.

## Momentos de inercia (momentos de segundo orden) [38:48](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2328s)

Así como se definen los momentos estáticos de primer orden, se pueden definir **momentos de segundo orden**: en lugar de multiplicar el integrando por $x$ o por $y$, se multiplica por $x^2$ o por $y^2$. Estos momentos de segundo orden se conocen como **momentos de inercia** (usados en mecánica y en resistencia de materiales).

**Momento de inercia respecto al eje $x$** (distancias al eje $x$ al cuadrado):

$$
I_x = \iint_D y^2 \,dx\,dy
$$

**Momento de inercia respecto al eje $y$** (distancias al eje $y$ al cuadrado):

$$
I_y = \iint_D x^2 \,dx\,dy
$$

**Momento de inercia polar** (integrando $x^2 + y^2$):

$$
I_p = \iint_D (x^2 + y^2) \,dx\,dy
$$

También se define el **momento centrífugo** (integrando $x\,y$).

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2359s">39:19</a>: Momento de inercia de una sección rectangular</summary>

Calcular el momento de inercia de una sección rectangular de base $b$ y altura $h$ respecto a un eje baricéntrico paralelo a su base.

El baricentro está a media altura y media base. Se toma el eje $x$ pasando por el baricentro, de modo que la región se extiende entre $-\frac{h}{2}$ y $\frac{h}{2}$ en la dirección vertical.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Describir la región: $x$ varía entre $0$ y $b$, e $y$ entre $-\frac{h}{2}$ y $\frac{h}{2}$. Plantear el momento de inercia respecto al eje $x$ (multiplicando por $y^2$):

$$
I_x = \int_0^{b}\int_{-h/2}^{h/2} y^2 \,dy\,dx
$$

**Paso 2:** Integrar primero respecto de $y$. La integral de $y^2$ es $y^3/3$, evaluada entre $-\frac{h}{2}$ y $\frac{h}{2}$:

$$
\int_{-h/2}^{h/2} y^2 \,dy = \frac{1}{3}\left[\left(\frac{h}{2}\right)^3 - \left(-\frac{h}{2}\right)^3\right] = \frac{1}{3}\left(\frac{h^3}{8} + \frac{h^3}{8}\right)
$$

**Paso 3:** Sumar los dos términos:

$$
\int_{-h/2}^{h/2} y^2 \,dy = \frac{1}{3}\cdot\frac{2h^3}{8} = \frac{h^3}{12}
$$

**Paso 4:** Integrar respecto de $x$. Como $\frac{h^3}{12}$ es constante, la integral del diferencial de $x$ entre $0$ y $b$ da $b$:

$$
I_x = \int_0^{b} \frac{h^3}{12} \,dx = \frac{h^3}{12}\,b
$$

**Paso 5:** El momento de inercia de la sección rectangular respecto a un eje baricéntrico paralelo a la base es:

$$
I_x = \frac{b\,h^3}{12}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=2714s">45:14</a>: Momento de inercia de una sección circular</summary>

Calcular el momento de inercia de una sección circular de radio $R$ respecto a un eje baricéntrico (que pasa por el centro de la circunferencia). El conjunto $D$ está definido por $x^2 + y^2 \le R^2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear el momento de inercia respecto al eje $x$ (multiplicando por $y^2$):

$$
I_x = \iint_D y^2 \,dx\,dy
$$

**Paso 2:** Resolver en coordenadas polares. La distancia $\rho$ varía entre $0$ y $R$, y el ángulo $\varphi$ entre $0$ y $2\pi$. Con $y = \rho\sin\varphi$, se tiene $y^2 = \rho^2\sin^2\varphi$, y hay que multiplicar por el jacobiano $\rho$, quedando $\rho^3\sin^2\varphi$:

$$
I_x = \int_0^{2\pi}\int_0^{R} \rho^3\sin^2\varphi \,d\rho\,d\varphi
$$

**Paso 3:** Como el integrando se factoriza en una función de $\rho$ por una de $\varphi$ y los extremos son constantes, la integral doble se expresa como producto de integrales simples:

$$
I_x = \left(\int_0^{2\pi} \sin^2\varphi \,d\varphi\right)\left(\int_0^{R} \rho^3 \,d\rho\right)
$$

**Paso 4:** La integral de $\sin^2\varphi$ se busca en la tabla:

$$
\int \sin^2\varphi \,d\varphi = \frac{\varphi}{2} - \frac{\sin(2\varphi)}{4}
$$

Evaluada entre $0$ y $2\pi$: al reemplazar $\varphi = 2\pi$ queda $\frac{2\pi}{2} = \pi$ (y $\sin(4\pi) = 0$), y en $\varphi = 0$ todo es cero, por lo que da $\pi$.

**Paso 5:** La integral de $\rho^3$ es $\rho^4/4$ entre $0$ y $R$:

$$
\int_0^{R} \rho^3 \,d\rho = \frac{R^4}{4}
$$

**Paso 6:** Multiplicar ambos resultados:

$$
I_x = \pi \cdot \frac{R^4}{4} = \frac{\pi R^4}{4}
$$

**Paso 7:** Expresar en términos del diámetro $d = 2R$, es decir $R = \frac{d}{2}$:

$$
I_x = \frac{\pi \left(\frac{d}{2}\right)^4}{4} = \frac{\pi\,d^4}{2^4 \cdot 4} = \frac{\pi\,d^4}{64}
$$

El momento de inercia de la sección circular respecto a un eje baricéntrico es $\dfrac{\pi\,d^4}{64}$.

</details>

</details>

## Momento de inercia polar [55:36](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=3336s)

El **momento de inercia polar** respecto al origen de coordenadas es igual a la suma de los momentos de inercia respecto a los ejes $x$ e $y$, porque el integrando $x^2 + y^2$ y la integral de una suma es la suma de las integrales:

$$
I_p = \iint_D (x^2 + y^2) \,dx\,dy = I_x + I_y
$$

Para una **sección circular**, como el momento de inercia respecto a cualquier eje baricéntrico es el mismo ($I_x = I_y = \frac{\pi d^4}{64}$), el momento de inercia polar resulta:

$$
I_p = \frac{\pi d^4}{64} + \frac{\pi d^4}{64} = \frac{\pi d^4}{32}
$$

Es decir, el doble del momento de inercia respecto a un eje baricéntrico. Físicamente, el momento de inercia polar caracteriza la oposición de una barra a deformarse por **torsión**: cuanto mayor sea el momento de inercia polar, menor será la deformación por torsión.

## Teorema de Steiner [58:43](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=3523s)

El **teorema de Steiner** permite calcular momentos de inercia de secciones respecto a ejes arbitrarios (paralelos) una vez que se conoce el momento de inercia respecto a un eje baricéntrico.

Sea $D$ una región con su baricentro, y sean:
- un eje $x_G$ baricéntrico (que pasa por el baricentro),
- un eje $x$ arbitrario, paralelo al anterior, a una distancia $d$ del eje baricéntrico.

Se quiere el momento de inercia respecto al eje $x$ arbitrario:

$$
I_x = \iint_D y^2 \,dx\,dy
$$

donde $y$ es la distancia medida desde el eje $x$. Si $y_G$ es la distancia medida desde el eje baricéntrico, se cumple $y = y_G - d$ (con $d$ constante). Reemplazando y desarrollando el binomio:

$$
I_x = \iint_D (y_G - d)^2 \,dx\,dy = \iint_D y_G^2 \,dx\,dy - 2d\iint_D y_G \,dx\,dy + d^2\iint_D dx\,dy
$$

Analizando cada término:
- $\displaystyle\iint_D y_G^2 \,dx\,dy = I_{x_G}$ es el **momento de inercia respecto al eje baricéntrico**.
- $\displaystyle\iint_D y_G \,dx\,dy$ es el **momento estático respecto al eje baricéntrico**, que vale **cero**, por lo que el término del medio se anula.
- $\displaystyle d^2\iint_D dx\,dy = d^2 \cdot A_D$ es la distancia al cuadrado por el área.

El resultado es el **teorema de Steiner**:

$$
I_x = I_{x_G} + d^2\,A_D
$$

Relaciona los momentos de inercia respecto a ejes paralelos, principalmente cuando uno es baricéntrico y el otro no.

## Densidad, masa y momentos de regiones con densidad [1:07:22](https://www.youtube.com/watch?v=v6XSV4ohEtY&t=4042s)

A una región del plano $D$ se le puede asignar una **función escalar de densidad** $\delta(x,y)$: a cada punto le corresponde un valor (por ejemplo, una placa plana con densidad variable en su dominio).

Integrando la función densidad sobre la región se obtiene la **masa** de la placa plana:

$$
m = \iint_D \delta(x,y) \,dx\,dy
$$

Si la densidad es unitaria ($\delta = 1$), la integral da el **área** de la región; si toma un valor distinto de la unidad, representa la masa.

Con la densidad se redefinen los momentos estáticos, los baricentros y los momentos de inercia de placas con masa: se agrega la función densidad en el integrando, y en los baricentros el denominador pasa de ser el área $A_D$ a ser la masa $m$.

<details>
<summary>📝 Ejercicio 6 — <a href="https://www.youtube.com/watch?v=v6XSV4ohEtY&t=4108s">1:08:28</a>: Masa de una placa con densidad variable</summary>

Calcular la masa de una placa con función densidad $\delta(x,y) = k\,x$ (con $k$ constante) sobre la región $D$ definida por:

$$
x^2 + y^2 \le 2R\,x
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la región completando cuadrados. Pasando $2Rx$ al miembro de la izquierda y sumando $R^2$ en ambos miembros:

$$
x^2 - 2Rx + R^2 + y^2 \le R^2 \;\Rightarrow\; (x - R)^2 + y^2 \le R^2
$$

Es el interior de una circunferencia de radio $R$ desplazada $R$ unidades en la dirección del eje $x$ (llega hasta $2R$ sobre ese eje). En el origen la densidad es cero, y en el punto $(2R, 0)$ vale $\delta = 2kR$.

**Paso 2:** La masa se define como la integral de la densidad sobre la región:

$$
m = \iint_D k\,x \,dx\,dy = k\iint_D x \,dx\,dy
$$

**Paso 3:** Como la región es el interior de una circunferencia, usar coordenadas polares con $x = \rho\cos\varphi$, $y = \rho\sin\varphi$ y jacobiano $\rho$. El integrando $x = \rho\cos\varphi$ multiplicado por el jacobiano da $\rho^2\cos\varphi$:

$$
m = k\iint_D \rho^2\cos\varphi \,d\rho\,d\varphi
$$

**Paso 4:** Determinar los límites. Ahora la circunferencia está desplazada sobre el eje $x$, por lo que $\varphi$ varía entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$ (primer y cuarto cuadrante). El radio máximo se obtiene de $\rho^2 \le 2R\rho\cos\varphi$; simplificando $\rho$ (distinto de cero), $\rho \le 2R\cos\varphi$:

$$
m = k\int_{-\pi/2}^{\pi/2}\int_0^{2R\cos\varphi} \rho^2\cos\varphi \,d\rho\,d\varphi
$$

**Paso 5:** Integrar primero respecto de $\rho$. La integral de $\rho^2$ es $\rho^3/3$, evaluada entre $0$ y $2R\cos\varphi$:

$$
m = k\int_{-\pi/2}^{\pi/2} \frac{(2R\cos\varphi)^3}{3}\,\cos\varphi \,d\varphi
$$

**Paso 6:** Con $(2R)^3 = 8R^3$ (constante) y $\cos^3\varphi\cdot\cos\varphi = \cos^4\varphi$:

$$
m = \frac{8kR^3}{3}\int_{-\pi/2}^{\pi/2} \cos^4\varphi \,d\varphi
$$

**Paso 7:** La integral de $\cos^4\varphi$ se busca en la tabla:

$$
\int \cos^4\varphi \,d\varphi = \frac{3}{8}\varphi + \frac{\sin(2\varphi)}{4} + \frac{\sin(4\varphi)}{32}
$$

**Paso 8:** Evaluar entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$. En $\varphi = \frac{\pi}{2}$ queda $\frac{3\pi}{16}$ (con $\sin\pi = 0$, $\sin 2\pi = 0$); en $\varphi = -\frac{\pi}{2}$ queda $-\frac{3\pi}{16}$. La diferencia es dos veces $\frac{3\pi}{16}$:

$$
\int_{-\pi/2}^{\pi/2} \cos^4\varphi \,d\varphi = 2\cdot\frac{3\pi}{16} = \frac{3\pi}{8}
$$

**Paso 9:** Multiplicar por el factor de afuera:

$$
m = \frac{8kR^3}{3}\cdot\frac{3\pi}{8} = k\,\pi\,R^3
$$

La masa de la placa es $m = k\,\pi\,R^3$.

</details>

</details>
