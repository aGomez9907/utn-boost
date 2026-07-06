# Divergencia

> Fuente: https://www.youtube.com/watch?v=LLxa2v7Pjoo

---

## Índice
- [00:35](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=35s) — Divergencia de un campo vectorial
- [02:41](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=161s) — Ejemplos de cálculo de divergencia
- [04:18](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=258s) — La divergencia como campo escalar
- [05:22](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=322s) — 📝 Ejercicio 1: Divergencia de un campo radial inverso-cuadrático
- [12:16](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=736s) — Campos solenoidales
- [13:54](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=834s) — Región simple del espacio
- [16:00](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=960s) — Orientación positiva de la frontera
- [17:32](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1052s) — Teorema de la Divergencia
- [19:36](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1176s) — 📝 Ejercicio 2: Flujo a través de un tetraedro
- [27:07](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1627s) — 📝 Ejercicio 3: Flujo a través de una superficie esférica
- [35:33](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=2133s) — Teorema de Gauss para una carga puntual

---

## Divergencia de un campo vectorial [00:35](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=35s)

Si tenemos un campo vectorial definido de algún subconjunto de $\mathbb{R}^3$ en $\mathbb{R}^3$, cuyas componentes son $f_1$, $f_2$ y $f_3$ y sus variables independientes son $x$, $y$, $z$ (a cada $(x,y,z)$ le corresponde un vector de componentes $f_1, f_2, f_3$), se define la **divergencia** de ese campo vectorial como la suma de la derivada parcial de la primera función componente respecto de $x$, más la derivada de la segunda función componente respecto de $y$, más la derivada de la tercera función componente respecto de $z$:

$$
\operatorname{div} \vec{F} = \frac{\partial f_1}{\partial x} + \frac{\partial f_2}{\partial y} + \frac{\partial f_3}{\partial z}
$$

Esa divergencia se puede interpretar como el **producto escalar del vector operador nabla** $\nabla$ aplicado al campo vectorial $(f_1, f_2, f_3)$. Es como si resolviéramos el producto escalar entre el vector operador y el campo, con la particularidad de que en lugar de multiplicar las componentes se aplican las derivadas parciales. Por eso la divergencia a veces se encuentra escrita con esta notación:

$$
\operatorname{div} \vec{F} = \nabla \cdot \vec{F} = \left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \cdot (f_1, f_2, f_3)
$$

## Ejemplos de cálculo de divergencia [02:41](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=161s)

Por ejemplo, para el campo vectorial con $f_1 = x$, $f_2 = y$, $f_3 = z$, es decir $\vec{F} = (x, y, z)$:

$$
\operatorname{div} \vec{F} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z) = 1 + 1 + 1 = 3
$$

En este caso, sea cual sea la coordenada $(x,y,z)$ que consideremos, la divergencia vale $3$.

Otro ejemplo, para $\vec{F} = (x^3, y^3, z^3)$:

$$
\operatorname{div} \vec{F} = 3x^2 + 3y^2 + 3z^2 = 3(x^2 + y^2 + z^2)
$$

## La divergencia como campo escalar [04:18](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=258s)

En este último caso la divergencia de un campo vectorial **resulta ser un campo escalar**: a cada punto del espacio le corresponde un escalar, un valor numérico real.

La divergencia de un campo vectorial siempre resulta ser un campo escalar. En el ejemplo anterior ($\vec{F}=(x,y,z)$) a cada punto del espacio le corresponde un valor numérico que es constante ($3$); en cambio, para $\vec{F}=(x^3,y^3,z^3)$ ese valor depende del punto $(x,y,z)$.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=322s">05:22</a>: Divergencia de un campo radial inverso-cuadrático</summary>

Calcular la divergencia del campo vectorial cuyas tres componentes son $c\,x$, $c\,y$ y $c\,z$ divididas por la raíz cuadrada de $x^2+y^2+z^2$ elevada al cubo, o lo que es lo mismo, $(x^2+y^2+z^2)^{3/2}$, que es la norma de $(x,y,z)$ al cubo:

$$
\vec{F}(x,y,z) = c\,\frac{(x, y, z)}{\left(x^2 + y^2 + z^2\right)^{3/2}}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Escribir las funciones componentes. La primera componente es $\dfrac{cx}{(x^2+y^2+z^2)^{3/2}}$, la segunda $\dfrac{cy}{(x^2+y^2+z^2)^{3/2}}$ y la tercera $\dfrac{cz}{(x^2+y^2+z^2)^{3/2}}$.

$$
f_1 = \frac{cx}{(x^2+y^2+z^2)^{3/2}}, \quad f_2 = \frac{cy}{(x^2+y^2+z^2)^{3/2}}, \quad f_3 = \frac{cz}{(x^2+y^2+z^2)^{3/2}}
$$

**Paso 2:** Derivar la primera componente respecto de $x$. Se mantiene $c$ constante y se usa la regla de la derivada de un cociente: derivada del numerador ($1$) por el denominador sin derivar, menos el numerador por la derivada del denominador respecto de $x$, todo dividido por el denominador al cuadrado. Al derivar el denominador se deriva el paréntesis elevado a $3/2$ y luego su argumento, apareciendo el factor $2x$.

$$
\frac{\partial f_1}{\partial x} = c\,\frac{(x^2+y^2+z^2)^{3/2} - x \cdot \frac{3}{2}(x^2+y^2+z^2)^{1/2} \cdot 2x}{\left[(x^2+y^2+z^2)^{3/2}\right]^2}
$$

Al elevar el denominador al cuadrado queda $(x^2+y^2+z^2)^{3}$. Sacando factor común $(x^2+y^2+z^2)^{1/2}$ en el numerador:

$$
\frac{\partial f_1}{\partial x} = c\,\frac{(x^2+y^2+z^2)^{1/2}\left[(x^2+y^2+z^2) - 3x^2\right]}{(x^2+y^2+z^2)^{3}}
$$

**Paso 3:** Al derivar respecto de $y$ y de $z$ se obtiene prácticamente la misma forma, cambiando el $3x^2$ por $3y^2$ y $3z^2$ respectivamente. El denominador es el mismo en los tres casos.

$$
\frac{\partial f_2}{\partial y} = c\,\frac{(x^2+y^2+z^2)^{1/2}\left[(x^2+y^2+z^2) - 3y^2\right]}{(x^2+y^2+z^2)^{3}}
$$

$$
\frac{\partial f_3}{\partial z} = c\,\frac{(x^2+y^2+z^2)^{1/2}\left[(x^2+y^2+z^2) - 3z^2\right]}{(x^2+y^2+z^2)^{3}}
$$

**Paso 4:** Sumar los tres términos. El denominador común es el mismo ($(x^2+y^2+z^2)^3$) y se puede sacar factor común $3\,c\,(x^2+y^2+z^2)^{1/2}$ en el numerador. En el corchete queda $(x^2+y^2+z^2)$ menos la suma $x^2+y^2+z^2$.

$$
\operatorname{div}\vec{F} = \frac{3c\,(x^2+y^2+z^2)^{1/2}\left[(x^2+y^2+z^2) - (x^2+y^2+z^2)\right]}{(x^2+y^2+z^2)^{3}}
$$

**Paso 5:** El corchete se anula, por lo que la divergencia es nula en cualquier punto del espacio donde el campo está definido.

$$
\operatorname{div}\vec{F} = 0
$$

Cuando la divergencia es cero, este tipo de campos se llaman **solenoidales**.

</details>

</details>

## Campos solenoidales [12:16](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=736s)

Cuando la divergencia de un campo vectorial vale **cero en cualquier punto** del espacio, el campo se llama **solenoidal**:

$$
\operatorname{div} \vec{F} = 0
$$

- Es una característica que tienen, por ejemplo, los campos eléctricos generados por solenoides (bobinas): generan a su alrededor campos eléctricos cuya divergencia es cero en cualquier punto.
- En el caso de los campos de velocidades de líquidos, cuando se evalúan flujos y la divergencia es cero se dice que el campo es **incompresible**. La interpretación física de por qué se dice que es incompresible queda [poco claro en la transcripción] (el profesor la deja en standby para verla en Física 2).

## Región simple del espacio [13:54](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=834s)

Una **región simple del espacio** (en $\mathbb{R}^3$) es una región de integración del espacio tridimensional —donde se podrían resolver integrales triples— que está encerrada por superficies en sus laterales, de manera tal que toda su frontera o borde es una **superficie simple y orientable por partes**.

Para hacerlo fácil, imaginemos un dado: es un elemento sólido, macizo, que ocupa una región del espacio (un volumen). Sus seis caras son seis trozos de plano que, unidos, forman una superficie simple y orientable por partes que encierra a ese sólido. Ese sólido es lo que llamamos región simple en $\mathbb{R}^3$.

## Orientación positiva de la frontera [16:00](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=960s)

La frontera de una región simple de $\mathbb{R}^3$ (la superficie simple y orientable por partes que envuelve a la región) está **orientada en forma positiva** si sus vectores normales apuntan **hacia el exterior** de la región.

Por ejemplo, si tenemos una superficie esférica que encierra una región del espacio, la frontera está orientada en forma positiva cuando los vectores normales apuntan hacia el exterior de la región encerrada por la superficie esférica.

## Teorema de la Divergencia [17:32](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1052s)

**Hipótesis:**
- Tenemos un campo vectorial definido de algún subconjunto $A \subseteq \mathbb{R}^3 \to \mathbb{R}^3$, de **clase $C^1$** (cada una de las tres funciones componentes tiene derivadas parciales respecto de cada una de las tres variables).
- $\Omega$ es una **región simple del espacio**, incluida dentro del dominio del campo, de manera tal que se pueda evaluar el campo en cualquier punto de esa región.
- $\partial\Omega$ es la superficie frontera de $\Omega$ (por ejemplo, las seis caras del dado, o la superficie esférica), orientada en forma positiva (normales hacia el exterior). El círculo en la integral identifica a la superficie cerrada.

**Tesis:** el flujo del campo a través de la superficie frontera cerrada $\partial\Omega$ es igual a la integral triple de la divergencia de $\vec{F}$ extendida a la región $\Omega$:

$$
\oiint_{\partial\Omega} \vec{F} \cdot d\vec{S} = \iiint_{\Omega} \operatorname{div} \vec{F} \,dx\,dy\,dz
$$

Este teorema relaciona el cálculo de un flujo a través de una superficie cerrada (una integral de superficie) con una integral triple.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1176s">19:36</a>: Flujo a través de un tetraedro</summary>

Tenemos el campo vectorial $\vec{F}(x,y,z) = (x, y, z)$. Calcular el flujo de este campo a través del borde (frontera) del conjunto $\Omega$, dado por todos los puntos del espacio con coordenadas $x, y, z \ge 0$ (primer octante) que además están limitados por el plano $x + y + z = 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Identificar la región. El plano $x + y + z = 1$ corta a los ejes $x$, $y$, $z$ en $1$. El conjunto $\Omega$ es el conjunto de puntos a la derecha del plano $xz$, por delante del plano $yz$, por arriba del plano $xy$ y por detrás del plano $x+y+z=1$. Es una región simple del espacio: un sólido (tetraedro) con volumen.

**Paso 2:** La frontera $\partial\Omega$ está compuesta por cuatro superficies (cuatro trozos de plano): un triángulo sobre el plano $xz$, otro sobre el plano $yz$, el piso (plano $xy$) y la cara delantera inclinada. Una alternativa sería calcular el flujo a través de cada una de las cuatro caras y sumar, pero es laborioso. En cambio, aplicamos el teorema de la divergencia con la frontera positivamente orientada (normales hacia el exterior).

$$
\oiint_{\partial\Omega} \vec{F} \cdot d\vec{S} = \iiint_{\Omega} \operatorname{div}\vec{F} \,dx\,dy\,dz
$$

**Paso 3:** Calcular la divergencia del campo, que ya se había obtenido antes.

$$
\operatorname{div}\vec{F} = \frac{\partial}{\partial x}(x) + \frac{\partial}{\partial y}(y) + \frac{\partial}{\partial z}(z) = 3
$$

**Paso 4:** Como la divergencia es $3$ (constante), sale fuera de la integral. La integral triple de la función unitaria sobre la región es el volumen de la región.

$$
\iiint_{\Omega} 3 \,dx\,dy\,dz = 3 \iiint_{\Omega} dx\,dy\,dz = 3 \cdot V_\Omega
$$

**Paso 5:** El volumen encerrado por el tetraedro es cateto por cateto por cateto dividido $6$.

$$
V_\Omega = \frac{1 \cdot 1 \cdot 1}{6} = \frac{1}{6}
$$

**Paso 6:** Calcular el flujo final.

$$
\oiint_{\partial\Omega} \vec{F} \cdot d\vec{S} = 3 \cdot \frac{1}{6} = \frac{1}{2}
$$

Como el flujo es positivo, si $\vec{F}$ representa el campo de velocidades de un líquido, hay más agua saliendo de la región (atravesando la frontera) que entrando: en la región hay una **fuente**.

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=1627s">27:07</a>: Flujo a través de una superficie esférica</summary>

Tenemos el campo vectorial $\vec{F}(x,y,z) = (x^3, y^3, z^3)$. Calcular el flujo a través de una superficie esférica de radio $R$ centrada en el origen, con la frontera positivamente orientada (normales hacia el exterior).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Aplicar el teorema de la divergencia. Llamamos $S$ a la superficie esférica y $\Omega$ a la región simple del espacio encerrada por ella; $S$ es la frontera positivamente orientada.

$$
\oiint_{S} \vec{F} \cdot d\vec{S} = \iiint_{\Omega} \operatorname{div}\vec{F} \,dx\,dy\,dz
$$

**Paso 2:** Calcular la divergencia, que ya se había obtenido para este campo.

$$
\operatorname{div}\vec{F} = 3x^2 + 3y^2 + 3z^2 = 3(x^2 + y^2 + z^2)
$$

Entonces hay que resolver:

$$
\iiint_{\Omega} 3\left(x^2 + y^2 + z^2\right) \,dx\,dy\,dz
$$

**Paso 3:** Como la región de integración es el interior de una esfera de radio $R$ y en el integrando aparece $x^2+y^2+z^2$, conviene usar **coordenadas esféricas**.

$$
x = \rho\cos\theta\cos\varphi, \quad y = \rho\cos\theta\sin\varphi, \quad z = \rho\sin\theta
$$

El módulo del jacobiano es $|J| = \rho^2\cos\theta$ y se cumple $x^2+y^2+z^2 = \rho^2$ (la distancia al origen al cuadrado).

**Paso 4:** Determinar los límites de integración para la esfera de radio $R$:
- $\rho$ varía entre $0$ y $R$.
- $\theta$ (el ángulo con el plano $xy$) varía entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$.
- $\varphi$ (el ángulo con el plano $xz$) varía entre $0$ y $2\pi$.

**Paso 5:** Sacar el $3$ fuera de la integral y reemplazar el integrando ($\rho^2$) y el jacobiano ($\rho^2\cos\theta$).

$$
\oiint_{S} \vec{F} \cdot d\vec{S} = 3 \int_{0}^{2\pi} \int_{-\pi/2}^{\pi/2} \int_{0}^{R} \rho^2 \cdot \rho^2\cos\theta \,d\rho\,d\theta\,d\varphi
$$

**Paso 6:** Como los límites son constantes y el integrando se factoriza, se separa en producto de tres integrales simples.

$$
= 3 \left( \int_{0}^{2\pi} d\varphi \right) \left( \int_{-\pi/2}^{\pi/2} \cos\theta \,d\theta \right) \left( \int_{0}^{R} \rho^4 \,d\rho \right)
$$

**Paso 7:** Resolver cada integral simple. La integral de $d\varphi$ da $2\pi$; la de $\cos\theta$ es $\sin\theta$ evaluado entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$, que da $1-(-1)=2$; y la de $\rho^4$ es $\frac{\rho^5}{5}$ evaluado entre $0$ y $R$.

$$
\int_{0}^{2\pi} d\varphi = 2\pi
$$

$$
\int_{-\pi/2}^{\pi/2} \cos\theta \,d\theta = \left[ \sin\theta \right]_{-\pi/2}^{\pi/2} = 1 - (-1) = 2
$$

$$
\int_{0}^{R} \rho^4 \,d\rho = \left[ \frac{\rho^5}{5} \right]_{0}^{R} = \frac{R^5}{5}
$$

**Paso 8:** Multiplicar los resultados ($3 \cdot 2\pi \cdot 2 \cdot \frac{R^5}{5}$). Queda $\frac{12}{5}\pi R^5$.

$$
\oiint_{S} \vec{F} \cdot d\vec{S} = 3 \cdot 2\pi \cdot 2 \cdot \frac{R^5}{5} = \frac{12}{5}\pi R^5
$$

Como $R$ es el radio de la esfera y es positivo, el flujo toma un valor positivo: el agua está saliendo de la región, es decir, hay una **fuente**. Esto se visualiza fácil: al representar el campo en puntos de la superficie, el campo apunta hacia el exterior (alejándose del origen), en la misma dirección que el normal, por lo que el flujo o caudal es positivo.

</details>

</details>

## Teorema de Gauss para una carga puntual [35:33](https://www.youtube.com/watch?v=LLxa2v7Pjoo&t=2133s)

Se considera el campo vectorial característico generado por una carga eléctrica ubicada en el origen:

$$
\vec{F}(x,y,z) = k\,\frac{(x, y, z)}{\|(x,y,z)\|^3}
$$

Si la carga eléctrica es positiva, la constante $k$ es positiva; si la carga es negativa, $k$ es negativa. El dominio del campo es $\mathbb{R}^3 - \{(0,0,0)\}$ (no está definido en el origen) y su divergencia vale $0$ en todo su dominio.

**Resultado:** si se considera una región simple del espacio $\Omega$ (un sólido), el flujo del campo a través de su frontera cerrada $\partial\Omega$ depende de si la región contiene o no al origen:

$$
\oiint_{\partial\Omega} \vec{F} \cdot d\vec{S} =
\begin{cases}
0 & \text{si } (0,0,0) \notin \Omega \\
4k\pi & \text{si } (0,0,0) \in \Omega
\end{cases}
$$

Cuando la región encierra la carga, el flujo vale $4k\pi$ y es totalmente **independiente de la forma** de la superficie que encierra a la carga.

**Idea de la demostración:**

**Caso 1 (el origen no pertenece a $\Omega_1$):** llamamos $\Omega_1$ a la región que no contiene al origen. Como en toda $\Omega_1$ el campo está definido, se aplica directamente el teorema de la divergencia. Recordando que la divergencia de este campo es $0$:

$$
\oiint_{\partial\Omega_1} \vec{F} \cdot d\vec{S} = \iiint_{\Omega_1} \operatorname{div}\vec{F} \,dx\,dy\,dz = \iiint_{\Omega_1} 0 \,dx\,dy\,dz = 0
$$

Sea cual sea la superficie cerrada que no contenga al origen, el flujo es cero: la cantidad de campo que entra por un lado sale por el otro.

**Caso 2 (el origen pertenece a $\Omega_2$):** el campo no está definido en el origen ($\mathbb{R}^3 - \{(0,0,0)\}$), así que no se puede aplicar el teorema de la divergencia directamente sobre $\Omega_2$. La idea es tomar una superficie esférica $S$ centrada en el origen, totalmente contenida dentro de $\Omega_2$, y considerar la región sólida $\Omega_3$ encerrada por la frontera de $\Omega_2$ pero por fuera de la superficie esférica (como un durazno cuyo carozo es la esfera). La frontera de $\Omega_3$ es la frontera de $\Omega_2$ unión la superficie esférica $S$.

Si $\partial\Omega_3$ se orienta en forma positiva (normales hacia el exterior de $\Omega_3$), sobre $\partial\Omega_2$ los normales apuntan hacia afuera, y sobre $S$ los normales apuntan hacia el origen (hacia el interior de la esfera). Entonces el flujo a través de $\partial\Omega_3$ se descompone:

$$
\oiint_{\partial\Omega_3} \vec{F} \cdot d\vec{S} = \oiint_{\partial\Omega_2} \vec{F} \cdot d\vec{S} + \iint_{S} \vec{F} \cdot d\vec{S}
$$

donde en $S$ el normal apunta hacia el origen. El flujo a través de la esfera con el normal apuntando hacia el origen ya se había calculado en la presentación anterior y vale $-4k\pi$ (si el normal hubiera apuntado hacia afuera, habría dado $4k\pi$ positivo).

En $\Omega_3$ sí vale el teorema de la divergencia, porque $\Omega_3$ esquiva al origen donde el campo no está definido. Como $\operatorname{div}\vec{F} = 0$:

$$
\oiint_{\partial\Omega_3} \vec{F} \cdot d\vec{S} = \iiint_{\Omega_3} 0 \,dx\,dy\,dz = 0
$$

Por lo tanto:

$$
0 = \oiint_{\partial\Omega_2} \vec{F} \cdot d\vec{S} - 4k\pi
$$

de donde se despeja el flujo a través de $\partial\Omega_2$:

$$
\oiint_{\partial\Omega_2} \vec{F} \cdot d\vec{S} = 4k\pi
$$

que era lo que se quería demostrar.
