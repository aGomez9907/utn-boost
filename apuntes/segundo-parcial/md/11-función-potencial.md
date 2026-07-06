# Función potencial

> Fuente: https://www.youtube.com/watch?v=A20l3JCSSAU

---

## Índice
- [00:01](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1s) — Objetivo: calcular la función potencial de un campo conservativo
- [01:02](https://www.youtube.com/watch?v=A20l3JCSSAU&t=62s) — Método 1: ecuación diferencial total exacta
- [03:11](https://www.youtube.com/watch?v=A20l3JCSSAU&t=191s) — 📝 Ejercicio 1: Primitiva por ecuación diferencial exacta
- [09:41](https://www.youtube.com/watch?v=A20l3JCSSAU&t=581s) — Resumen del método 1
- [11:46](https://www.youtube.com/watch?v=A20l3JCSSAU&t=706s) — Método 2: primitiva mediante integral de línea
- [15:59](https://www.youtube.com/watch?v=A20l3JCSSAU&t=959s) — 📝 Ejercicio 2: Primitiva por integral de línea
- [19:43](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1183s) — Limitación del método 2
- [21:50](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1310s) — Líneas de campo
- [24:26](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1466s) — Líneas de igual potencial (equipotenciales)
- [27:08](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1628s) — 📝 Ejercicio 3: Líneas de campo y equipotenciales

---

## Objetivo: calcular la función potencial de un campo conservativo [00:01](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1s)

En la clase anterior se determinó **si** un campo era o no conservativo, a partir de las propiedades de los campos conservativos (equivalentemente, si un campo vectorial admitía primitiva o **función potencial**).

Ahora el objetivo es, para los campos que **ya se sabe** que son conservativos, encontrar una **metodología para calcular sus funciones primitivas o potenciales**.

Se parte de un campo vectorial de componentes $f_1$ y $f_2$

$$
\vec{F} = (f_1, f_2)
$$

que **ya se sabe que es conservativo**. Se busca cómo calcular su primitiva o función potencial $g$.

## Método 1: ecuación diferencial total exacta [01:02](https://www.youtube.com/watch?v=A20l3JCSSAU&t=62s)

Una forma es resolver la **ecuación diferencial total exacta**, donde $f_1$ y $f_2$ son las componentes del campo:

$$
f_1\,dx + f_2\,dy = 0
$$

Recordemos que el **diferencial de una función** $g$ es

$$
dg = \frac{\partial g}{\partial x}\,dx + \frac{\partial g}{\partial y}\,dy
$$

Como el campo es conservativo, $g$ es la primitiva y sus derivadas parciales son las componentes del campo: $g'_x = f_1$ y $g'_y = f_2$. Por lo tanto la expresión $f_1\,dx + f_2\,dy$ es exactamente el diferencial $dg$.

Si ese diferencial es igual a cero,

$$
dg = 0
$$

entonces la función $g$ es **constante**. La forma de determinar la función primitiva o potencial de un campo conservativo es entonces resolviendo esta ecuación diferencial total exacta, ya que la expresión es el diferencial de una función de las variables.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=A20l3JCSSAU&t=191s">03:11</a>: Primitiva por ecuación diferencial exacta</summary>

Se sabe que el campo vectorial

$$
\vec{F}(x,y) = \left( \frac{x}{\sqrt{x^2+y^2}},\; \frac{y}{\sqrt{x^2+y^2}} \right)
$$

es conservativo. Calcular su función primitiva o potencial $g$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Como el campo es conservativo, $\vec{F} = \nabla g$, es decir cada componente es una derivada parcial de la primitiva. En particular:

$$
g'_x = \frac{x}{\sqrt{x^2+y^2}}
$$

**Paso 2:** Integrar respecto de $x$ miembro a miembro.

$$
g = \int \frac{x}{\sqrt{x^2+y^2}}\,dx
$$

**Paso 3:** Resolver la integral por sustitución. Se toma $u = x^2 + y^2$, de donde $du = 2x\,dx$, o sea $x\,dx = \dfrac{du}{2}$.

$$
\int \frac{x}{\sqrt{x^2+y^2}}\,dx = \int \frac{1}{\sqrt{u}}\cdot\frac{du}{2} = \frac{1}{2}\int u^{-1/2}\,du = \frac{1}{2}\cdot\frac{u^{1/2}}{1/2} = u^{1/2}
$$

Volviendo a las variables originales:

$$
g = \sqrt{x^2+y^2} + h(y)
$$

**Paso 4:** Como se integró respecto de $x$, en lugar de una constante se suma una **función que depende de la variable $y$**, ya que al derivar respecto de $x$ una función de $y$ da cero. Falta determinar $h(y)$.

**Paso 5:** Derivar la $g$ obtenida respecto de $y$ y comparar con la segunda componente $f_2$.

$$
g'_y = \frac{y}{\sqrt{x^2+y^2}} + h'(y)
$$

Por simple comparación, esto debe ser igual a $f_2 = \dfrac{y}{\sqrt{x^2+y^2}}$.

**Paso 6:** De la comparación se deduce que

$$
h'(y) = 0
$$

Por lo tanto $h(y)$ es **constante**.

**Paso 7:** La función primitiva (potencial) es

$$
g(x,y) = \sqrt{x^2+y^2} + C
$$

**Paso 8 (verificación):** Calcular el gradiente de $g$ y comprobar que da el campo.

$$
g'_x = \frac{1}{2\sqrt{x^2+y^2}}\cdot 2x = \frac{x}{\sqrt{x^2+y^2}}, \qquad g'_y = \frac{y}{\sqrt{x^2+y^2}}
$$

$$
\nabla g = \left( \frac{x}{\sqrt{x^2+y^2}},\; \frac{y}{\sqrt{x^2+y^2}} \right) = \vec{F}
$$

Coincide con el campo conservativo, por lo que el cálculo es correcto. Se recomienda usar este procedimiento de verificación en un examen para chequear que no haya errores de derivación.

</details>

</details>

## Resumen del método 1 [09:41](https://www.youtube.com/watch?v=A20l3JCSSAU&t=581s)

Si se tiene un campo vectorial que se sabe conservativo, donde la primera componente es la derivada de la primitiva respecto de $x$ y la segunda respecto de $y$:

**Paso 1:** Tomar la primera componente ($g'_x = f_1$) e integrar respecto de $x$.

**Paso 2:** Sumar una función de la variable $y$ (la "constante" de integración).

**Paso 3:** Derivar esa expresión respecto de $y$ y comparar con la segunda componente $f_2$ del campo.

**Paso 4:** De esa comparación se despeja la función de $y$ (que quedó pendiente).

Sobre la función $h(y)$: su derivada $h'(y)$ puede dar una función de $y$, no necesariamente cero. En el Ejercicio 1 dio cero (constante), pero si por ejemplo diera $h'(y) = y$, se integra y da $h(y) = \dfrac{y^2}{2}$, y esa sería la función a sumar.

## Método 2: primitiva mediante integral de línea [11:46](https://www.youtube.com/watch?v=A20l3JCSSAU&t=706s)

Esta metodología se basa en que, si el campo es conservativo, el **trabajo realizado por el campo entre dos puntos es independiente del camino**. Tomando un punto $(x,y)$ y el origen $(0,0)$, para cualquier curva que los una la integral del campo a lo largo de la curva es igual a la primitiva evaluada en el punto final menos la primitiva evaluada en el punto inicial:

$$
\int_C \vec{F}\cdot d\vec{r} = g(x,y) - g(0,0)
$$

Como la integral es independiente del camino, conviene elegir el **segmento de recta** que va del origen a $(x,y)$, que es lo más sencillo de calcular. Se parametriza:

$$
\vec{r}(t) = (t\,x,\; t\,y), \qquad t \in [0,1]
$$

Cuando $t = 0$ el punto es $(0,0)$ (el origen) y cuando $t = 1$ es $(x,y)$ (el otro extremo). La derivada de la parametrización es

$$
\vec{r}\,'(t) = (x,\; y)
$$

Entonces la integral del campo conservativo entre $(0,0)$ y $(x,y)$ es

$$
\int_0^1 \vec{F}\big(\vec{r}(t)\big)\cdot \vec{r}\,'(t)\,dt = g(x,y) - g(0,0)
$$

Despejando (y como $g(0,0)$ es una constante), la función potencial resulta:

$$
g(x,y) = \int_0^1 \vec{F}\big(\vec{r}(t)\big)\cdot (x,y)\,dt + C
$$

donde $C = g(0,0)$ queda como constante arbitraria.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=A20l3JCSSAU&t=959s">15:59</a>: Primitiva por integral de línea</summary>

Calcular la función primitiva del campo vectorial conservativo

$$
\vec{F}(x,y) = (y,\; x)
$$

usando la fórmula de la integral de línea a lo largo del segmento de recta que va del origen a $(x,y)$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Aplicar la fórmula, con la parametrización $\vec{r}(t) = (t x, t y)$, $t\in[0,1]$, y $\vec{r}\,'(t) = (x,y)$.

$$
g(x,y) = \int_0^1 \vec{F}\big(\vec{r}(t)\big)\cdot (x,y)\,dt + C
$$

**Paso 2:** Evaluar el campo $\vec{F}=(y,x)$ en los puntos de la parametrización. En $(tx, ty)$ la primera componente ($y$) se vuelve $ty$ y la segunda ($x$) se vuelve $tx$:

$$
\vec{F}\big(\vec{r}(t)\big) = (t y,\; t x)
$$

**Paso 3:** Hacer el producto escalar con $(x,y)$.

$$
(t y,\; t x)\cdot (x, y) = t x y + t x y = 2 t x y
$$

**Paso 4:** Plantear la integral.

$$
g(x,y) = \int_0^1 2 t x y \, dt + C
$$

**Paso 5:** Como $x$ e $y$ son constantes respecto de $t$, integrar $t$.

$$
\int_0^1 2 t x y\, dt = 2 x y \left[\frac{t^2}{2}\right]_0^1 = 2xy\cdot\frac{1}{2} = xy
$$

**Paso 6:** La función primitiva (potencial) es

$$
g(x,y) = xy + C
$$

**Paso 7 (verificación):** $\vec{F} = \nabla g$. Derivando respecto de $x$ da $y$ y respecto de $y$ da $x$:

$$
\nabla g = (y,\; x) = \vec{F}
$$

Coincide con el campo, por lo que el resultado es correcto.

</details>

</details>

## Limitación del método 2 [19:43](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1183s)

El método consiste en calcular el trabajo del campo entre $(0,0)$ y un punto $(x,y)$ cualquiera a lo largo del segmento de recta. La condición para aplicarlo es que **ese segmento de recta esté incluido en el dominio del campo**.

Por ejemplo, si el $(0,0)$ **no** pertenece al dominio del campo (como en un campo cuyo dominio es $\mathbb{R}^2 - \{(0,0)\}$, es decir el campo no está definido en el origen), no se puede calcular el trabajo del campo a lo largo de ese segmento, porque el campo no está definido en un extremo de la curva. En ese caso este método **no se puede aplicar**.

La idea general: cualquier segmento de recta que vaya del origen a un punto $(x,y)$ debería estar incluido dentro del dominio del campo.

## Líneas de campo [21:50](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1310s)

Se definen las **líneas de campo** como una familia de curvas tales que, en cualquiera de sus puntos, el campo vectorial $\vec{F}$ evaluado en ese punto es **siempre tangente** a la curva de la familia.

Para determinarlas, se usa que el vector $\vec{F}$ tiene componentes $f_1$ (en $x$) y $f_2$ (en $y$). Armando un triángulo rectángulo de catetos $f_1$ (adyacente, sobre $x$) y $f_2$ (opuesto, sobre $y$), con hipotenusa $\vec{F}$, la **pendiente** del vector es la tangente del ángulo que forma con el eje $x$: cateto opuesto sobre cateto adyacente.

Como esa pendiente coincide con la derivada de la función de la familia de curvas, la ecuación diferencial de las líneas de campo es:

$$
y' = \frac{f_2}{f_1}
$$

Estas funciones dependen de un parámetro: para distintos valores del parámetro se obtienen distintas curvas de la familia.

## Líneas de igual potencial (equipotenciales) [24:26](https://www.youtube.com/watch?v=A20l3JCSSAU&t=1466s)

Se llaman **líneas de igual potencial** (equipotenciales, o líneas de igual valor de $g$) a la familia de curvas **ortogonales** a las líneas de campo.

La justificación: si el campo es conservativo, $\vec{F}$ es el gradiente de la función potencial $g$. Los gradientes de una función (de clase adecuada) son **ortogonales a las curvas de nivel** (conjuntos de nivel) de esa función. Las curvas de nivel de la función potencial $g$ son precisamente las líneas de igual potencial. Por lo tanto los campos vectoriales conservativos son ortogonales a las líneas de igual potencial, y como el campo es tangente a las líneas de campo, resulta que **las líneas de campo y las equipotenciales son ortogonales entre sí**.

La pendiente de las equipotenciales es la **inversa y cambiada de signo** de la pendiente de las líneas de campo. Si las líneas de campo cumplen $y' = \dfrac{f_2}{f_1}$, entonces las equipotenciales cumplen:

$$
y' = -\frac{f_1}{f_2}
$$

Esta es la ecuación diferencial correspondiente a las líneas equipotenciales o de igual potencial.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=A20l3JCSSAU&t=1628s">27:08</a>: Líneas de campo y equipotenciales</summary>

Para el campo vectorial conservativo

$$
\vec{F}(x,y) = (y,\; x)
$$

calcular las **líneas de campo** y las **líneas de igual potencial** (equipotenciales).

<details>
<summary>Ver resolución</summary>

**Parte A — Líneas de campo**

**Paso 1:** Plantear la ecuación diferencial de las líneas de campo, con $f_1 = y$ y $f_2 = x$.

$$
y' = \frac{f_2}{f_1} = \frac{x}{y}
$$

**Paso 2:** Es una ecuación con **variables separables**. Escribiendo $y' = \dfrac{dy}{dx}$:

$$
y\,dy = x\,dx
$$

**Paso 3:** Integrar miembro a miembro.

$$
\frac{y^2}{2} = \frac{x^2}{2} + C
$$

**Paso 4:** Para eliminar los denominadores se toma la constante como $\dfrac{C}{2}$, quedando:

$$
y^2 = x^2 + C
$$

**Paso 5:** Reescribiendo, $y^2 - x^2 = C$: es una **familia de hipérbolas**. Para cada valor de $C$ se obtiene una hipérbola distinta. Estas son las líneas de campo, y cualquier curva de la familia es tangente al campo.

**Parte B — Líneas de igual potencial**

**Paso 6:** Las equipotenciales son ortogonales, con ecuación diferencial $y' = -\dfrac{f_1}{f_2}$. Como $f_1 = y$ y $f_2 = x$:

$$
y' = -\frac{y}{x}
$$

**Paso 7:** Separar variables.

$$
\frac{dy}{y} = -\frac{dx}{x}
$$

**Paso 8:** Integrar miembro a miembro.

$$
\ln|y| = -\ln|x| + \ln|C|
$$

donde la constante se expresó como $\ln|C|$.

**Paso 9:** Agrupar los logaritmos (propiedad del producto de logaritmos) y eliminarlos.

$$
y = \frac{\pm C}{x}
$$

Esta es la familia de curvas de las líneas de igual potencial (curvas de nivel de la función potencial). Las líneas de campo (hipérbolas $y^2 - x^2 = C$) y las equipotenciales ($y = \pm C/x$) forman dos familias ortogonales entre sí.

</details>

</details>
