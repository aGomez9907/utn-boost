# Campos conservativos

> Fuente: https://www.youtube.com/watch?v=Z7MavOmpW8s

---

## Índice
- [00:01](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1s) — Definición de campo vectorial conservativo
- [01:38](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=98s) — Función primitiva o potencial
- [03:13](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=193s) — 📝 Ejercicio 1: Trabajo de un campo conservativo (recta, parábola y otra curva)
- [11:12](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=672s) — 📝 Ejercicio 2: Circulación alrededor de una circunferencia
- [17:39](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1059s) — Teorema: tres proposiciones equivalentes
- [25:44](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1544s) — 📝 Ejercicio 3: Verificar que un campo NO es conservativo
- [34:18](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=2058s) — Condición necesaria para que un campo sea conservativo
- [41:19](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=2479s) — 📝 Ejercicio 4: Condición necesaria cumplida pero campo NO conservativo
- [50:28](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3028s) — 📝 Ejercicio 5: Campo con dominio agujereado que SÍ es conservativo
- [57:17](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3437s) — Análisis con el teorema de Green y regiones agujereadas
- [1:05:41](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3941s) — Método práctico para decidir si un campo es conservativo
- [1:08:24](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=4104s) — Condición suficiente: dominio simplemente conexo

---

## Definición de campo vectorial conservativo [00:01](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1s)

Recordemos que denominamos **campos vectoriales** a las funciones vectoriales de varias variables en las que la dimensión del dominio es igual a la dimensión del conjunto de llegada (por ejemplo de $\mathbb{R}^2$ en $\mathbb{R}^2$, de $\mathbb{R}^3$ en $\mathbb{R}^3$, o en general de $\mathbb{R}^n$ en $\mathbb{R}^n$).

Consideremos el caso sencillo de un campo vectorial definido de un subconjunto de $\mathbb{R}^2$ en $\mathbb{R}^2$. Decimos que este campo vectorial es **conservativo** si existe un campo escalar (una función escalar de varias variables) tal que su gradiente es igual al campo vectorial:

$$
\nabla \varphi = \vec{F}
$$

Es decir, el campo vectorial es el resultado del gradiente de un campo escalar. En ese caso, el campo vectorial se denomina **campo conservativo**.

## Función primitiva o potencial [01:38](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=98s)

La función escalar de varias variables cuyo gradiente es el campo vectorial se denomina **función primitiva** o **función potencial** del campo.

Veamos un ejemplo sencillo. Queremos verificar que la función escalar

$$
\varphi(x,y) = x\,y
$$

es la primitiva del campo $\vec{F}(x,y) = (y, x)$. Calculamos el gradiente de $\varphi$, que es el vector formado por sus derivadas parciales:

$$
\nabla \varphi = \left( \frac{\partial \varphi}{\partial x}, \frac{\partial \varphi}{\partial y} \right) = (y, x)
$$

Como $\nabla \varphi = (y, x) = \vec{F}$, el campo $\vec{F} = (y, x)$ es un **campo vectorial conservativo**, y $\varphi(x,y) = x\,y$ es su función primitiva (o potencial).

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=Z7MavOmpW8s&t=193s">03:13</a>: Trabajo de un campo conservativo (recta, parábola y otra curva)</summary>

Para el campo vectorial conservativo $\vec{F}(x,y) = (y, x)$, calcular el trabajo (integral de línea) entre el punto $(0,0)$ y el punto $(1,1)$:

- a lo largo del segmento de recta $y = x$,
- a lo largo del arco de parábola $y = x^2$,
- y comprobar qué ocurre a lo largo de cualquier otra curva que una esos dos puntos.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar el segmento de recta $y = x$. Como $y = x$, tomamos

$$
\lambda(t) = (t, t), \qquad t \in [0, 1]
$$

Cuando $t = 0$ estamos en $(0,0)$ y cuando $t = 1$ estamos en $(1,1)$.

**Paso 2:** El trabajo a lo largo de la curva se calcula con la fórmula

$$
\int_{0}^{1} \vec{F}(\lambda(t)) \cdot \lambda'(t)\,dt
$$

El campo $\vec{F} = (y, x)$ evaluado en la curva es $(t, t)$, y la derivada de la parametrización es $\lambda'(t) = (1, 1)$.

**Paso 3:** Plantear y resolver la integral.

$$
\int_{0}^{1} (t, t) \cdot (1, 1)\,dt = \int_{0}^{1} (t + t)\,dt = \int_{0}^{1} 2t\,dt = \left[ t^2 \right]_{0}^{1} = 1
$$

El trabajo a lo largo del segmento de recta es $1$.

**Paso 4:** Parametrizar el arco de parábola $y = x^2$. Tomamos

$$
\lambda(t) = (t, t^2), \qquad t \in [0, 1]
$$

Cuando $t = 0$ estamos en $(0,0)$ y cuando $t = 1$ estamos en $(1,1)$.

**Paso 5:** Evaluar el campo en la curva: $\vec{F}(\lambda(t)) = (t^2, t)$ (la primera componente $y = t^2$, la segunda componente $x = t$). La derivada de la parametrización es $\lambda'(t) = (1, 2t)$.

**Paso 6:** Plantear y resolver la integral.

$$
\int_{0}^{1} (t^2, t) \cdot (1, 2t)\,dt = \int_{0}^{1} \left( t^2 + 2t^2 \right)dt = \int_{0}^{1} 3t^2\,dt = \left[ t^3 \right]_{0}^{1} = 1
$$

El trabajo a lo largo del arco de parábola también es $1$.

**Paso 7:** No es casualidad que ambas integrales den lo mismo: el campo vectorial es el mismo y los puntos extremos de ambas curvas son los mismos. En los **campos conservativos** las integrales entre dos puntos extremos son **independientes del camino recorrido**. Puede demostrarse que a lo largo de cualquier otra curva que vaya de $(0,0)$ a $(1,1)$ (recorrida en ese sentido) la integral siempre dará $1$. Esto es una característica de los campos conservativos, y no la cumplen los campos que no son conservativos.

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=Z7MavOmpW8s&t=672s">11:12</a>: Circulación de un campo conservativo alrededor de una circunferencia</summary>

Para el mismo campo conservativo $\vec{F}(x,y) = (y, x)$, calcular la circulación (trabajo alrededor de una curva cerrada) sobre una circunferencia de radio $r$ centrada en el origen.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar la circunferencia de radio $r$ recorrida en sentido antihorario.

$$
\lambda(t) = (r\cos t,\ r\sin t), \qquad t \in [0, 2\pi]
$$

Cuando $t = 0$ y cuando $t = 2\pi$ se llega al mismo punto $(r, 0)$: la curva es cerrada y simple.

**Paso 2:** Evaluar el campo $\vec{F} = (y, x)$ en la curva: $\vec{F}(\lambda(t)) = (r\sin t,\ r\cos t)$. La derivada de la parametrización es $\lambda'(t) = (-r\sin t,\ r\cos t)$.

**Paso 3:** Plantear la circulación como producto escalar de ambos vectores.

$$
\oint \vec{F} \cdot d\lambda = \int_{0}^{2\pi} (r\sin t,\ r\cos t) \cdot (-r\sin t,\ r\cos t)\,dt
$$

$$
= \int_{0}^{2\pi} \left( -r^2\sin^2 t + r^2\cos^2 t \right)dt
$$

**Paso 4:** Separar en dos integrales sacando $r^2$ como factor común.

$$
= -r^2 \int_{0}^{2\pi} \sin^2 t\,dt + r^2 \int_{0}^{2\pi} \cos^2 t\,dt
$$

**Paso 5:** Usar las primitivas de tabla del seno y del coseno al cuadrado.

$$
\int \sin^2 t\,dt = \frac{t}{2} - \frac{\sin 2t}{4}, \qquad \int \cos^2 t\,dt = \frac{t}{2} + \frac{\sin 2t}{4}
$$

**Paso 6:** Evaluar entre $0$ y $2\pi$. En ambos casos los términos con $\sin 4\pi = 0$ y $\sin 0 = 0$ se anulan, quedando

$$
-r^2 \pi + r^2 \pi = 0
$$

**Paso 7:** La circulación del campo conservativo alrededor de la circunferencia es $0$. En general, para todos los campos vectoriales conservativos las circulaciones (integrales alrededor de curvas cerradas simples) siempre dan $0$.

</details>

</details>

## Teorema: tres proposiciones equivalentes [17:39](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1059s)

Las propiedades vistas en los ejemplos anteriores se generalizan en el siguiente teorema. Si tenemos un campo vectorial definido en un subconjunto de $\mathbb{R}^2$ en $\mathbb{R}^2$ (también se generaliza para campos de $\mathbb{R}^n$ en $\mathbb{R}^n$), con la función campo vectorial **continua**, entonces las siguientes tres proposiciones son **equivalentes** (o se cumplen las tres, o no se cumple ninguna):

**Proposición 1:** El campo vectorial $\vec{F}$ es el gradiente de un campo escalar, es decir, $\vec{F}$ es **conservativo**.

**Proposición 2:** La integral del campo a lo largo de una curva contenida en el dominio del campo es igual al valor de la primitiva en el punto extremo final de la curva menos la primitiva en el punto inicial:

$$
\int_{\lambda} \vec{F} \cdot d\lambda = \varphi(B) - \varphi(A)
$$

donde $A = \lambda(a)$ y $B = \lambda(b)$ son los extremos de la curva. La integral depende exclusivamente de los puntos extremos y es totalmente independiente de la curva considerada.

**Proposición 3:** La circulación alrededor de cualquier curva cerrada (contenida en el dominio del campo) es cero:

$$
\oint \vec{F} \cdot d\lambda = 0
$$

**Nota de notación:** el profesor aclara que las notaciones

$$
\int_{\lambda} \vec{F} \cdot d\vec{\lambda} \qquad \text{y} \qquad \int_{\lambda} \vec{F} \cdot \check{s}\,d\lambda
$$

son equivalentes: escribir el diferencial de $\lambda$ como vector ($d\vec{\lambda}$) es lo mismo que usar el versor tangente $\check{s}$ por el diferencial escalar $d\lambda$. La forma de resolver la integral es la misma más allá de la notación empleada.

**Consecuencia práctica de la equivalencia:** como o se cumplen las tres proposiciones o no se cumple ninguna, si la circulación alrededor de una curva cerrada **no** es cero, el campo **no** es conservativo; y si la integral a lo largo de dos curvas distintas (con los mismos extremos) da valores distintos, el campo **no** es conservativo.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=Z7MavOmpW8s&t=1544s">25:44</a>: Verificar que el campo $\vec{F}=(1, x)$ NO es conservativo</summary>

Verificar que el campo vectorial $\vec{F}(x,y) = (1, x)$ (usado la clase pasada) **no** es conservativo, mediante:

- la circulación alrededor de una circunferencia de radio $r$ centrada en el origen,
- y la comparación de la integral entre $(0,0)$ y $(1,1)$ a lo largo de un segmento de recta y de un arco de parábola.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar la circunferencia de radio $r$ centrada en el origen recorrida en sentido antihorario.

$$
\lambda(t) = (r\cos t,\ r\sin t), \qquad t \in [0, 2\pi]
$$

**Paso 2:** Evaluar el campo $\vec{F} = (1, x)$ en la curva; como $x = r\cos t$, queda $\vec{F}(\lambda(t)) = (1,\ r\cos t)$. La derivada de la parametrización es $\lambda'(t) = (-r\sin t,\ r\cos t)$.

**Paso 3:** Plantear la circulación.

$$
\oint \vec{F} \cdot d\lambda = \int_{0}^{2\pi} (1,\ r\cos t) \cdot (-r\sin t,\ r\cos t)\,dt = \int_{0}^{2\pi} \left( -r\sin t + r^2\cos^2 t \right)dt
$$

**Paso 4:** La integral de $-r\sin t$ entre $0$ y $2\pi$ es $0$ (se compensan las áreas positivas y negativas). Para el coseno cuadrado se usa la primitiva de tabla.

$$
\int \cos^2 t\,dt = \frac{t}{2} + \frac{\sin 2t}{4}
$$

**Paso 5:** Evaluar. El término del seno se anula en los extremos, quedando

$$
\oint \vec{F} \cdot d\lambda = r^2 \pi
$$

**Paso 6:** La circulación es $r^2\pi \neq 0$. Como no es cero, por el teorema $\vec{F}$ **no** es conservativo (no es el gradiente de ningún campo escalar).

**Paso 7:** Como refuerzo, comparar las integrales entre $(0,0)$ y $(1,1)$. A lo largo de la recta $y = x$, con $\lambda(t) = (t, t)$ y $\lambda'(t) = (1,1)$, evaluando $\vec{F} = (1, x) = (1, t)$:

$$
\int_{0}^{1} (1, t) \cdot (1, 1)\,dt = \int_{0}^{1} (1 + t)\,dt = \left[ t + \frac{t^2}{2} \right]_{0}^{1} = \frac{3}{2}
$$

**Paso 8:** A lo largo del arco de parábola $y = x^2$, con $\lambda(t) = (t, t^2)$ y $\lambda'(t) = (1, 2t)$, evaluando $\vec{F} = (1, x) = (1, t)$:

$$
\int_{0}^{1} (1, t) \cdot (1, 2t)\,dt = \int_{0}^{1} \left( 1 + 2t^2 \right)dt = \left[ t + \frac{2t^3}{3} \right]_{0}^{1} = 1 + \frac{2}{3} = \frac{5}{3}
$$

**Paso 9:** Las dos integrales dan valores distintos ($\frac{3}{2} \neq \frac{5}{3}$) pese a tener los mismos extremos y el mismo campo. Esto confirma que $\vec{F}$ **no** es conservativo (si lo fuera, deberían ser iguales).

</details>

</details>

## Condición necesaria para que un campo sea conservativo [34:18](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=2058s)

Los campos conservativos tienen la siguiente característica. Si el campo vectorial $\vec{F} = (f_1, f_2)$ tiene dos componentes y es de **clase $C^1$** (las derivadas parciales de $f_1$ y $f_2$ son funciones continuas), entonces, **si el campo es conservativo**, se cumple que

$$
\frac{\partial f_1}{\partial y} = \frac{\partial f_2}{\partial x}
$$

**Demostración:** si $\vec{F}$ es conservativo, existe una función $\varphi$ tal que $\nabla \varphi = \vec{F}$, es decir

$$
\nabla \varphi = \left( \frac{\partial \varphi}{\partial x}, \frac{\partial \varphi}{\partial y} \right) = (f_1, f_2)
$$

Por lo tanto

$$
\frac{\partial \varphi}{\partial x} = f_1, \qquad \frac{\partial \varphi}{\partial y} = f_2
$$

Derivamos la primera ecuación respecto de $y$ y la segunda respecto de $x$. Como $\vec{F}$ es de clase $C^1$, la primitiva $\varphi$ es de clase $C^2$, y por el **teorema de Schwarz** (las hipótesis se cumplen porque $\varphi \in C^2$) el orden de derivación es irrelevante:

$$
\frac{\partial^2 \varphi}{\partial y\,\partial x} = \frac{\partial^2 \varphi}{\partial x\,\partial y}
$$

De donde resulta lo que queríamos demostrar:

$$
\frac{\partial f_1}{\partial y} = \frac{\partial f_2}{\partial x}
$$

Esta se llama **condición necesaria** para que un campo sea conservativo: si el campo es conservativo, se cumple esta relación entre las derivadas parciales cruzadas.

**Verificación con los ejemplos previos:**

- Para el campo conservativo $\vec{F} = (y, x)$: $f_1 = y$, $f_2 = x$; y se cumple $\dfrac{\partial f_2}{\partial x} = 1 = \dfrac{\partial f_1}{\partial y}$. La condición necesaria se verifica, como corresponde a un campo conservativo.

- Para el campo $\vec{F} = (1, x)$ (que no es conservativo): $f_1 = 1$, $f_2 = x$; se tiene $\dfrac{\partial f_2}{\partial x} = 1$ y $\dfrac{\partial f_1}{\partial y} = 0$. Las derivadas son distintas, lo que confirma que $\vec{F}$ no es conservativo.

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=Z7MavOmpW8s&t=2479s">41:19</a>: Condición necesaria cumplida pero campo NO conservativo</summary>

Dado el campo vectorial

$$
\vec{F}(x,y) = \left( \frac{-y}{x^2 + y^2},\ \frac{x}{x^2 + y^2} \right)
$$

definido en todos los puntos del plano menos el origen ($\mathbb{R}^2 - \{(0,0)\}$):

- verificar que cumple la condición necesaria para ser conservativo,
- y determinar (mediante la circulación sobre una circunferencia) si efectivamente lo es.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar las componentes: $f_1 = \dfrac{-y}{x^2+y^2}$ y $f_2 = \dfrac{x}{x^2+y^2}$.

**Paso 2:** Calcular $\dfrac{\partial f_2}{\partial x}$ con la regla del cociente (numerador derivado $\times$ denominador $-$ numerador $\times$ denominador derivado, sobre denominador al cuadrado).

$$
\frac{\partial f_2}{\partial x} = \frac{1 \cdot (x^2 + y^2) - x \cdot 2x}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}
$$

**Paso 3:** Calcular $\dfrac{\partial f_1}{\partial y}$ análogamente.

$$
\frac{\partial f_1}{\partial y} = \frac{-1 \cdot (x^2 + y^2) - (-y) \cdot 2y}{(x^2 + y^2)^2} = \frac{-x^2 - y^2 + 2y^2}{(x^2 + y^2)^2} = \frac{y^2 - x^2}{(x^2 + y^2)^2}
$$

**Paso 4:** Las dos derivadas cruzadas son iguales, por lo que el campo **cumple la condición necesaria** para ser conservativo. Pero esto no garantiza que lo sea; hay que verificarlo.

**Paso 5:** Calcular la circulación sobre una circunferencia de radio $r$ centrada en el origen, parametrizada en sentido antihorario.

$$
\lambda(t) = (r\cos t,\ r\sin t), \qquad t \in [0, 2\pi]
$$

**Paso 6:** Evaluar el campo en la curva. El denominador $x^2 + y^2 = r^2$. Entonces

$$
f_1 = \frac{-r\sin t}{r^2}, \qquad f_2 = \frac{r\cos t}{r^2}
$$

y la derivada de la parametrización es $\lambda'(t) = (-r\sin t,\ r\cos t)$.

**Paso 7:** Plantear la circulación como producto escalar.

$$
\oint \vec{F} \cdot d\lambda = \int_{0}^{2\pi} \left( \frac{-r\sin t}{r^2},\ \frac{r\cos t}{r^2} \right) \cdot (-r\sin t,\ r\cos t)\,dt
$$

$$
= \int_{0}^{2\pi} \left( \frac{r^2\sin^2 t}{r^2} + \frac{r^2\cos^2 t}{r^2} \right)dt = \int_{0}^{2\pi} \left( \sin^2 t + \cos^2 t \right)dt
$$

**Paso 8:** Como $\sin^2 t + \cos^2 t = 1$, la integral se simplifica.

$$
\oint \vec{F} \cdot d\lambda = \int_{0}^{2\pi} 1\,dt = 2\pi
$$

**Paso 9:** La circulación vale $2\pi \neq 0$, así que el campo **no es conservativo**. Conclusión importante: **cumplir la condición necesaria NO garantiza que el campo sea conservativo**. Este es un ejemplo de un campo que satisface la condición necesaria y sin embargo no es conservativo.

</details>

</details>

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3028s">50:28</a>: Campo con dominio agujereado que SÍ es conservativo</summary>

Analizar el campo vectorial

$$
\vec{F}(x,y) = \left( \frac{x}{\sqrt{x^2 + y^2}},\ \frac{y}{\sqrt{x^2 + y^2}} \right)
$$

con dominio en todos los puntos del plano menos el origen. Verificar la condición necesaria y decidir, mediante la circulación sobre una circunferencia, si es conservativo.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar las componentes: $f_1 = \dfrac{x}{\sqrt{x^2+y^2}}$ y $f_2 = \dfrac{y}{\sqrt{x^2+y^2}}$, escribiendo $\sqrt{x^2+y^2} = (x^2+y^2)^{1/2}$.

**Paso 2:** Calcular $\dfrac{\partial f_2}{\partial x}$. Como $f_2 = y\,(x^2+y^2)^{-1/2}$, derivando respecto de $x$ (la $y$ del numerador es constante):

$$
\frac{\partial f_2}{\partial x} = y \cdot \left( -\frac{1}{2} \right)(x^2+y^2)^{-3/2} \cdot 2x = \frac{-xy}{(x^2+y^2)^{3/2}}
$$

**Paso 3:** Calcular $\dfrac{\partial f_1}{\partial y}$. Como $f_1 = x\,(x^2+y^2)^{-1/2}$:

$$
\frac{\partial f_1}{\partial y} = x \cdot \left( -\frac{1}{2} \right)(x^2+y^2)^{-3/2} \cdot 2y = \frac{-xy}{(x^2+y^2)^{3/2}}
$$

**Paso 4:** Por simple comparación, las dos derivadas cruzadas son iguales: el campo **cumple la condición necesaria** para ser conservativo. Como en el ejemplo anterior, esto todavía no garantiza que lo sea.

**Paso 5:** Calcular la circulación sobre una circunferencia de radio $r$ centrada en el origen, en sentido antihorario.

$$
\lambda(t) = (r\cos t,\ r\sin t), \qquad t \in [0, 2\pi]
$$

**Paso 6:** Evaluar el campo en la curva. El denominador $\sqrt{x^2+y^2} = \sqrt{r^2} = r$, con $x = r\cos t$ e $y = r\sin t$:

$$
f_1 = \frac{r\cos t}{r} = \cos t, \qquad f_2 = \frac{r\sin t}{r} = \sin t
$$

y $\lambda'(t) = (-r\sin t,\ r\cos t)$.

**Paso 7:** Plantear la circulación.

$$
\oint \vec{F} \cdot d\lambda = \int_{0}^{2\pi} (\cos t,\ \sin t) \cdot (-r\sin t,\ r\cos t)\,dt = \int_{0}^{2\pi} \left( -r\sin t\cos t + r\sin t\cos t \right)dt
$$

**Paso 8:** Los dos términos se cancelan, por lo que la circulación es

$$
\oint \vec{F} \cdot d\lambda = 0
$$

**Paso 9:** El resultado es $0$ para cualquier circunferencia centrada en el origen (grande o chica). Pero atención: para afirmar que el campo es conservativo, la circulación debe ser cero sobre **cualquier** curva cerrada, no solo sobre circunferencias centradas en el origen. El análisis continúa a continuación.

</details>

</details>

## Análisis con el teorema de Green y regiones agujereadas [57:17](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3437s)

Para completar el análisis del Ejercicio 5 hay que verificar la circulación sobre **cualquier** curva cerrada simple, distinguiendo dos casos según encierre o no al origen (el punto donde el campo no está definido).

**Caso 1 — la curva no encierra el origen.** Sea $C_1$ una curva cerrada simple cualquiera que no encierra al origen, orientada positivamente (antihorario). Por el **teorema de Green**, la circulación es igual a la integral doble del rotor sobre la región $D_1$ encerrada por la curva:

$$
\oint_{C_1} \vec{F} \cdot d\lambda = \iint_{D_1} \operatorname{rot} \vec{F}\,dx\,dy
$$

donde el rotor (en el plano) es

$$
\operatorname{rot} \vec{F} = \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}
$$

Como el campo cumple la condición necesaria, $\dfrac{\partial f_2}{\partial x} = \dfrac{\partial f_1}{\partial y}$, el rotor es cero, y la integral doble vale $0$. Por lo tanto, la circulación sobre **cualquier** curva que no encierre el origen es cero (la región no contiene el agujero, así que todos sus puntos están en el dominio y Green es aplicable).

**Caso 2 — la curva encierra el origen.** Sea $C_2$ una curva cerrada que encierra al origen. No se puede aplicar Green directamente, porque para hacerlo todos los puntos encerrados deben pertenecer al dominio del campo, y el origen no pertenece. La técnica es tomar una **región tipo anillo** $D_2$: la comprendida entre $C_2$ (borde externo) y una circunferencia interior de radio $r$ centrada en el origen. En toda la región $D_2$ el campo está definido, así que se puede aplicar Green sobre su frontera $\partial D_2$.

Recordando que en una región regular por partes con forma de anillo el borde externo se recorre en sentido antihorario y el interno en sentido horario:

$$
\oint_{\partial D_2} \vec{F} \cdot d\lambda = \iint_{D_2} \operatorname{rot} \vec{F}\,dx\,dy = 0
$$

porque el rotor sigue valiendo $0$ (el campo es el mismo). Ahora bien, la circulación sobre la frontera $\partial D_2$ se descompone en la circulación sobre $C_2$ más la circulación sobre la circunferencia interior recorrida en sentido horario (con signo negativo):

$$
\oint_{\partial D_2} \vec{F} \cdot d\lambda = \oint_{C_2} \vec{F} \cdot d\lambda - \oint_{\text{circunf. } r} \vec{F} \cdot d\lambda = 0
$$

Como la circulación sobre la circunferencia de radio $r$ ya se había calculado (en el Ejercicio 5) y valía $0$, y la frontera del anillo da $0$, se concluye que

$$
\oint_{C_2} \vec{F} \cdot d\lambda = 0
$$

**Conclusión:** todas las curvas cerradas simples que no encierran el origen tienen circulación $0$, y todas las que encierran el origen también tienen circulación $0$. No queda ninguna curva sin analizar, por lo que la circulación sobre cualquier curva cerrada simple es cero. Esto **garantiza que el campo del Ejercicio 5 es conservativo**, a pesar de que su dominio tiene un agujero en el origen.

## Método práctico para decidir si un campo es conservativo [1:05:41](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=3941s)

Resumen del procedimiento para determinar si un campo vectorial es o no conservativo:

**Paso 1 — Condición necesaria.** Analizar si las derivadas cruzadas son iguales:

$$
\frac{\partial f_1}{\partial y} = \frac{\partial f_2}{\partial x}
$$

Si **no** son iguales, el campo **no es conservativo** y se termina el problema. Si son iguales, puede ser conservativo o no; hay que seguir analizando.

**Paso 2 — Analizar el dominio.** Si las derivadas dieron iguales, observar el dominio del campo:

- Si el dominio **no tiene ningún agujero** (es **simplemente conexo**), entonces sobre cualquier curva cerrada se puede aplicar el teorema de Green; como el rotor es cero (las derivadas cruzadas son iguales), la circulación da $0$ y el campo **es conservativo**.

- Si el dominio **tiene algún agujero**, basta calcular la circulación del campo alrededor de una curva cerrada que encierre al agujero (por ejemplo una circunferencia). Si esa circulación es **distinta de cero**, el campo **no es conservativo**; si es **cero**, el campo **es conservativo**.

## Condición suficiente: dominio simplemente conexo [1:08:24](https://www.youtube.com/watch?v=Z7MavOmpW8s&t=4104s)

Los dominios de los campos (en el plano) que no tienen agujeros se llaman **simplemente conexos**; cuando tienen un agujero, **no** son simplemente conexos.

**Teorema (condición suficiente):** si el campo vectorial $\vec{F} = (f_1, f_2)$ es de **clase $C^1$** (derivadas parciales continuas), cumple la **condición necesaria**

$$
\frac{\partial f_1}{\partial y} = \frac{\partial f_2}{\partial x}
$$

y además su dominio es **simplemente conexo** (sin agujeros), entonces el campo **es conservativo**.

**Advertencia sobre el recíproco:** la implicación **no** funciona a la inversa. Si un campo es conservativo, su dominio **no** tiene por qué ser simplemente conexo. Es decir, el teorema garantiza:

- (condición necesaria) $+$ (dominio simplemente conexo) $+$ ($C^1$) $\Rightarrow$ campo conservativo,

pero un campo conservativo puede tener dominio no simplemente conexo.

**Ejemplos que ilustran la advertencia:**

- El campo del **Ejercicio 4**, $\vec{F} = \left( \dfrac{-y}{x^2+y^2}, \dfrac{x}{x^2+y^2} \right)$, tiene dominio $\mathbb{R}^2 - \{(0,0)\}$: **no** es simplemente conexo y **no** es conservativo.

- El campo del **Ejercicio 5** tiene dominio $\mathbb{R}^2 - \{(0,0)\}$: tampoco es simplemente conexo, y **sin embargo sí es conservativo**.

Por lo tanto, que el dominio sea o no simplemente conexo no implica por sí solo que el campo sea o no conservativo. Lo que sí garantiza que el campo es conservativo es que el dominio sea simplemente conexo **junto con** la condición necesaria (y $\vec{F} \in C^1$).
