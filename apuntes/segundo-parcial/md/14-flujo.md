# Flujo

> Fuente: https://www.youtube.com/watch?v=djt3sX5V2lk

---

## Índice
- [00:01](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1s) — Introducción: flujo de un campo vectorial a través de una superficie
- [01:36](https://www.youtube.com/watch?v=djt3sX5V2lk&t=96s) — Repaso: parametrización de superficies simples y regulares
- [04:49](https://www.youtube.com/watch?v=djt3sX5V2lk&t=289s) — Superficies orientables
- [08:26](https://www.youtube.com/watch?v=djt3sX5V2lk&t=506s) — Borde de la superficie y orientación positiva de la frontera
- [13:37](https://www.youtube.com/watch?v=djt3sX5V2lk&t=817s) — Regla de la mano derecha
- [14:40](https://www.youtube.com/watch?v=djt3sX5V2lk&t=880s) — Superficies simples y orientables por partes
- [18:53](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1133s) — Definición de integral de un campo vectorial a través de una superficie (flujo)
- [21:30](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1290s) — 📝 Ejercicio 1: Flujo a través de un plano en el primer octante
- [35:14](https://www.youtube.com/watch?v=djt3sX5V2lk&t=2114s) — Interpretación física: flujo y caudal
- [44:12](https://www.youtube.com/watch?v=djt3sX5V2lk&t=2652s) — 📝 Ejercicio 2: El mismo plano con orientación opuesta
- [1:00:03](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3603s) — Propiedad: dependencia del flujo con la orientación
- [1:01:42](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3702s) — 📝 Ejercicio 3: Flujo a través de una superficie esférica
- [1:20:08](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4808s) — Superficie dada por ecuación cartesiana (variable dependiente)
- [1:22:49](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4969s) — 📝 Ejercicio 4: Flujo a través de un paraboloide
- [1:18:33](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4713s) — Fuentes y sumideros en superficies cerradas

---

## Introducción: flujo de un campo vectorial a través de una superficie [00:01](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1s)

El tema es la **integral de campos vectoriales sobre superficies**, que se denomina **flujo de un campo vectorial a través de una superficie**.

Se ubica dentro del recorrido de integrales sobre superficies, en paralelo con lo hecho para curvas:

- Para curvas: primero se definió la longitud de una curva, luego la integral de campos escalares a lo largo de curvas y finalmente la integral de campos vectoriales a lo largo de curvas.
- Para superficies: primero se definió el área de una superficie, luego la integral de un campo escalar sobre una superficie y ahora se aborda la **integral de campos vectoriales a través de superficies**.

## Repaso: parametrización de superficies simples y regulares [01:36](https://www.youtube.com/watch?v=djt3sX5V2lk&t=96s)

Una **superficie** es el conjunto imagen de una función vectorial $\sigma$ definida en un subconjunto del plano cuyas imágenes caen en $\mathbb{R}^3$. A cada par $(u,v)$ del plano le corresponde un punto $(x,y,z)$ del espacio tridimensional.

$$
\sigma: D \subseteq \mathbb{R}^2 \to \mathbb{R}^3, \quad (u,v) \mapsto (x,y,z)
$$

Requisitos:

- $\sigma$ **continua** para que sea superficie.
- $\sigma$ de **clase $C^1$** (las tres funciones componentes $x, y, z$ tienen derivadas parciales continuas respecto de cada variable) para que la superficie sea **regular** (admita vectores normales, recta normal y plano tangente).
- El **producto vectorial de las derivadas parciales** $\sigma'_u \times \sigma'_v$ es un vector normal a la superficie, y se pide que sea un **vector no nulo**. Si es no nulo, hay garantía de recta normal y por lo tanto plano tangente.
- Para que la superficie sea **simple**, la función $\sigma$ debe ser inyectiva por lo menos en el interior de la región $D$ donde está definida.

Los vectores $\sigma'_u \times \sigma'_v$ son normales a la superficie. Divididos por su norma dan los **versores normales**. A cada punto de la superficie le corresponde así un versor normal.

## Superficies orientables [04:49](https://www.youtube.com/watch?v=djt3sX5V2lk&t=289s)

Dada una superficie simple $S$ parametrizada por $\sigma$ con su campo de versores normales, se dice que $S$ es **orientable** si ese campo de versores normales es **continuo** sobre la superficie.

Intuitivamente: para pequeñas variaciones en la posición de un punto sobre $S$, la variación del versor normal también es pequeña (tan pequeña como se quiera).

Que el campo de versores normales sea continuo garantiza que quedan definidas claramente **dos orientaciones posibles**:

- Una orientación en la dirección del campo de versores normales.
- La otra orientación, opuesta.

Analogía: una sábana en el espacio tiene dos lados; uno se podría pintar de un color y el opuesto de otro, sin lugar a duda de cuál es cada uno. Es análogo a las curvas simples, que tenían dos orientaciones posibles (recorrerlas en un sentido o en el opuesto). En curvas la orientación se asociaba al campo de **versores tangentes**; en superficies, al campo de **versores normales**.

## Borde de la superficie y orientación positiva de la frontera [08:26](https://www.youtube.com/watch?v=djt3sX5V2lk&t=506s)

Se llama **borde de la superficie** al conjunto imagen de todos los puntos que se encuentran en la **frontera de $D$** (el dominio de la parametrización $\sigma$). Es una curva cerrada en el espacio, como el borde de la sábana. El **interior de la superficie** corresponde a las imágenes de los puntos del interior de $D$.

En el plano, una curva cerrada está **orientada en forma positiva** si se recorre en **sentido antihorario**.

Una curva cerrada **en el espacio** no permite decir directamente si está orientada en sentido horario o antihorario, porque depende del lado desde el que se mire. Si nos paramos sobre la superficie como si fuéramos el versor normal (con la cabeza donde está la punta de la flecha) y miramos desde ese extremo, veremos el borde recorrido en cierto sentido; si nos paráramos con la cabeza apuntando hacia el lado opuesto, el sentido antihorario sería el opuesto.

**Solución:** la orientación positiva (antihoraria) de la frontera de $D$ **induce** una orientación positiva en el borde de la superficie, referida a la parametrización $\sigma$ y por lo tanto al campo de versores normales asociado.

Geométricamente: si el campo de versores normales apunta en un sentido, desde el extremo de la flecha se ve la frontera de $S$ orientada en sentido antihorario. Si el campo apuntara en sentido opuesto, la frontera quedaría orientada en sentido contrario.

## Regla de la mano derecha [13:37](https://www.youtube.com/watch?v=djt3sX5V2lk&t=817s)

Otra forma de identificar la orientación del borde correspondiente al campo de versores normales:

Imaginar agarrar con la **mano derecha** el vector normal a la superficie de manera que el **pulgar apunte en la dirección de la flecha**. Entonces los otros cuatro dedos apuntan en la dirección en que queda **orientado el borde** de la superficie en relación a ese campo de versores normales.

## Superficies simples y orientables por partes [14:40](https://www.youtube.com/watch?v=djt3sX5V2lk&t=880s)

Si tenemos varias superficies simples y orientables y las **pegamos en sus bordes**, obtenemos una **superficie simple y orientable por partes** (idea análoga a lo hecho con el teorema de Green, pero allí todo estaba en el plano $xy$).

Cada superficie simple tiene su campo de versores normales continuo, que induce en su borde una orientación. Para que las orientaciones sean **consistentes/coherentes**, en la curva donde se unen dos superficies simples las orientaciones inducidas deben ser **opuestas**.

Ejemplo: las **seis caras de un dado**. Cada cara es plana; caras tomadas de a dos comparten una arista. Para que toda la superficie quede orientada coherentemente, los seis versores normales deben apuntar **todos hacia el exterior** del dado, o **todos hacia el interior** (una u otra opción).

Cuando todas las superficies orientables están orientadas de forma coherente (sus bordes con orientaciones opuestas), el campo de versores normales de cada una se corresponde con la orientación de la superficie simple y orientable por partes.

## Definición de integral de un campo vectorial a través de una superficie (flujo) [18:53](https://www.youtube.com/watch?v=djt3sX5V2lk&t=1133s)

Sea $\vec{F}$ un campo vectorial definido en un conjunto $A \subseteq \mathbb{R}^3$, que a cada punto del espacio le asigna un vector. Sea $S$ una superficie simple y orientable (por partes) parametrizada por $\sigma$, **incluida dentro del dominio del campo** (para poder evaluar $\vec{F}$ en cualquier punto de $S$).

Evaluar un campo vectorial sobre una superficie es hacerle corresponder a cada punto de $S$ un vector de $\mathbb{R}^3$.

Se define la **integral del campo vectorial $\vec{F}$ a través de la superficie $S$ parametrizada por $\sigma$** como:

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_D \vec{F}(\sigma(u,v)) \cdot \left( \sigma'_u \times \sigma'_v \right) \, du \, dv
$$

Los primeros miembros indican la **nomenclatura** (integral del campo $\vec{F}$ a través de $S$ parametrizada por $\sigma$); el último miembro indica **cómo se calcula**: la integral doble sobre $D$ del campo evaluado en los puntos de la superficie, por el producto vectorial de las derivadas parciales de la parametrización.

**Comentario sobre simbología:** si la superficie es **cerrada** (por ejemplo una superficie esférica, o las seis caras de un dado), a veces se agrega un **circulito** sobre el signo integral, pero se ponga o no, la integral doble es la misma.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=1290s">21:30</a>: Flujo a través de un plano en el primer octante</summary>

Calcular el flujo del campo vectorial $\vec{F}(x,y,z) = (0, x, 0)$ a través de la superficie $S$ (un trozo de plano en el primer octante), parametrizada por

$$
\sigma(u,v) = \left(u,\; v,\; 1 - \frac{u}{a} - \frac{v}{b}\right)
$$

con $a, b > 0$. Como $x = u$, $y = v$ y $z = 1 - \frac{u}{a} - \frac{v}{b}$, la superficie satisface

$$
\frac{x}{a} + \frac{y}{b} + z = 1
$$

es decir un plano que corta a los ejes $x, y, z$ en $a$, $b$ y $1$ respectivamente, restringido al primer octante.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Aplicar la definición de flujo. Hay que calcular la integral doble del campo evaluado en los puntos de la superficie por el producto vectorial de las derivadas parciales, sobre el dominio $D$ de variación de $(u,v)$.

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_D \vec{F}(\sigma(u,v)) \cdot \left( \sigma'_u \times \sigma'_v \right) \, du \, dv
$$

**Paso 2:** Calcular el producto vectorial $\sigma'_u \times \sigma'_v$ mediante un determinante. Las derivadas parciales son:

$$
\sigma'_u = \left(1,\; 0,\; -\frac{1}{a}\right), \quad \sigma'_v = \left(0,\; 1,\; -\frac{1}{b}\right)
$$

**Paso 3:** Resolver el determinante componente a componente.

$$
\sigma'_u \times \sigma'_v = \left( 0\cdot\left(-\tfrac{1}{b}\right) - 1\cdot\left(-\tfrac{1}{a}\right),\; \left(-\tfrac{1}{a}\right)\cdot 0 - 1\cdot\left(-\tfrac{1}{b}\right),\; 1\cdot 1 - 0\cdot 0 \right)
$$

$$
\sigma'_u \times \sigma'_v = \left(\frac{1}{a},\; \frac{1}{b},\; 1\right)
$$

**Paso 4:** Evaluar el campo en la superficie. Como $x = u$, el campo $\vec{F} = (0, x, 0)$ se evalúa en $(0,\, u,\, 0)$. Hacer el producto escalar con el producto vectorial:

$$
(0,\, u,\, 0) \cdot \left(\frac{1}{a},\, \frac{1}{b},\, 1\right) = \frac{u}{b}
$$

**Paso 5:** Determinar la región de integración. Como $x = u$ e $y = v$, el campo de variación de $(u,v)$ coincide con el de $(x,y)$: el triángulo donde $u$ varía entre $0$ y $a$, y para cada $u$, $v$ varía entre $0$ y el valor sobre la recta $\frac{x}{a} + \frac{y}{b} = 1$ (el plano con $z=0$).

$$
v = \left(1 - \frac{u}{a}\right) b
$$

**Paso 6:** Plantear la integral (primero respecto de $v$, luego de $u$).

$$
\int_0^a \int_0^{\left(1-\frac{u}{a}\right)b} \frac{u}{b} \, dv \, du
$$

**Paso 7:** Integrar respecto de $v$ ($\frac{u}{b}$ es constante respecto de $v$).

$$
\int_0^a \frac{u}{b}\left(1 - \frac{u}{a}\right)b \, du = \int_0^a u\left(1 - \frac{u}{a}\right) du
$$

**Paso 8:** Distribuir e integrar respecto de $u$.

$$
\int_0^a \left(u - \frac{u^2}{a}\right) du = \left[ \frac{u^2}{2} - \frac{u^3}{3a} \right]_0^a = \frac{a^2}{2} - \frac{a^2}{3}
$$

**Paso 9:** Con denominador común $6$:

$$
\frac{a^2}{2} - \frac{a^2}{3} = \frac{3a^2 - 2a^2}{6} = \frac{a^2}{6}
$$

El flujo de $\vec{F}$ a través de $S$ es $\dfrac{a^2}{6}$, un valor numérico **positivo** e **independiente de $b$**.

</details>

</details>

## Interpretación física: flujo y caudal [35:14](https://www.youtube.com/watch?v=djt3sX5V2lk&t=2114s)

Si $\vec{F}$ representa un **campo de fuerzas**, la integral representa el **flujo de un campo a través de una superficie** (por ejemplo, el flujo de campos eléctricos que se ve en Física 2). Si $\vec{F}$ representa el **campo de velocidades de un fluido**, la integral representa el **caudal** de ese fluido a través de la superficie.

**Deducción del elemento de flujo.** Se toma un trozo diferencial de la superficie. El **diferencial de área** es:

$$
dS = \left\| \sigma'_u \times \sigma'_v \right\| \, du \, dv
$$

que es el área de un pequeño paralelogramo tangente a la superficie.

El **versor normal** a la superficie es:

$$
\check{n} = \frac{\sigma'_u \times \sigma'_v}{\left\| \sigma'_u \times \sigma'_v \right\|}
$$

Al evaluar el campo $\vec{F}$ en un punto de la superficie $\sigma(u,v)$ (por ejemplo la velocidad de un líquido allí), la **proyección de $\vec{F}$ en la dirección normal** es:

$$
\vec{F} \cdot \check{n}
$$

Multiplicando esa componente normal por el diferencial de área se obtiene una expresión de **flujo o caudal**. Análisis de unidades: si $\vec{F}$ es velocidad (m/s) y el área es m², entonces $\vec{F}\cdot\check{n}\, dS$ tiene unidades de:

$$
\frac{\text{m}}{\text{s}} \cdot \text{m}^2 = \frac{\text{m}^3}{\text{s}}
$$

que son unidades de **caudal**. Interesa la **componente normal** a la superficie: el agua que circula tangente a la superficie no la atraviesa y no genera caudal.

Al desarrollar $\vec{F}\cdot\check{n}\, dS$, las normas del producto vectorial se cancelan:

$$
\vec{F} \cdot \frac{\sigma'_u \times \sigma'_v}{\left\| \sigma'_u \times \sigma'_v \right\|} \cdot \left\| \sigma'_u \times \sigma'_v \right\| \, du \, dv = \vec{F} \cdot \left( \sigma'_u \times \sigma'_v \right) \, du \, dv
$$

que es el **diferencial de flujo**. Integrando sobre toda la superficie se obtiene el **flujo total** (caudal total) con su respectiva orientación.

**Signo del flujo:** si el agua va en una dirección y orientamos la superficie en esa misma dirección, el caudal es **positivo**; si la orientamos en sentido opuesto, el caudal es **negativo**. No hay problema mientras se tenga claro cómo se orientó la superficie.

**Propiedades:** como el flujo se define con una integral doble, se cumplen todas las propiedades de linealidad: el flujo de una suma es la suma de los flujos y toda constante se puede extraer fuera de la integral.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=2652s">44:12</a>: El mismo plano con orientación opuesta</summary>

Calcular el flujo del **mismo** campo vectorial $\vec{F}(x,y,z) = (0, x, 0)$ a través de la **misma** superficie (el trozo de plano en el primer octante), pero parametrizada por una función distinta $\tau$ que la orienta en sentido opuesto:

$$
\tau(s,t) = \left(s,\; -t,\; 1 - s\right) \quad \text{[poco claro en la transcripción]}
$$

donde $x = s$, $y = -t$, $z = 1 - x$, de modo que se sigue cumpliendo $\frac{x}{a} + \frac{y}{b} + z = 1$: es exactamente la misma superficie del Ejercicio 1, pero la **parametrización cambia** (el conjunto imagen es el mismo, la función es otra).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear el flujo con la definición, usando el dominio $D^\*$ de las variables $(s,t)$.

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_{D^\*} \vec{F}(\tau(s,t)) \cdot \left( \tau'_s \times \tau'_t \right) \, ds \, dt
$$

**Paso 2:** Calcular el producto vectorial $\tau'_s \times \tau'_t$ con el determinante. Las derivadas parciales son:

$$
\tau'_s = \left(1,\; 0,\; -\frac{1}{a}\right), \quad \tau'_t = \left(0,\; -1,\; -\frac{1}{b}\right) \quad \text{[paso en el pizarrón, ver video]}
$$

**Paso 3:** Resolver el determinante.

$$
\tau'_s \times \tau'_t = \left(-\frac{1}{a},\; -\frac{1}{b},\; -1\right)
$$

Este vector normal es el **opuesto** del obtenido en el Ejercicio 1 ($\left(\frac{1}{a}, \frac{1}{b}, 1\right)$): sus tres componentes son negativas, así que apunta hacia el lado opuesto (hacia atrás de la pantalla y hacia abajo). La superficie queda orientada en sentido **opuesto** al del Ejercicio 1.

**Paso 4:** Evaluar el campo en $\tau$. Como $x = s$, el campo $\vec{F} = (0,x,0)$ vale $(0,\, s,\, 0)$. Producto escalar con el producto vectorial:

$$
(0,\, s,\, 0) \cdot \left(-\frac{1}{a},\, -\frac{1}{b},\, -1\right) = -\frac{s}{b}
$$

**Paso 5:** Determinar el campo de variación de $(s,t)$. Como $x = s$ varía entre $0$ y $a$, e $y = -t$ con $y$ variando entre $0$ y $\left(1-\frac{x}{a}\right)b$, se tiene:

$$
-t \in \left[0,\; \left(1-\frac{s}{a}\right)b\right]
$$

Multiplicando por $-1$ (se invierte la desigualdad), $t$ varía entre $\left(\frac{s}{a}-1\right)b$ y $0$.

**Paso 6:** Plantear la integral.

$$
\int_0^a \int_{\left(\frac{s}{a}-1\right)b}^{0} -\frac{s}{b} \, dt \, ds
$$

**Paso 7:** Integrar respecto de $t$ ($-\frac{s}{b}$ no depende de $t$).

$$
\int_0^a -\frac{s}{b}\left(1 - \frac{s}{a}\right)b \, ds = -\int_0^a s\left(1-\frac{s}{a}\right) ds
$$

**Paso 8:** Distribuir e integrar respecto de $s$.

$$
-\int_0^a \left(s - \frac{s^2}{a}\right) ds = -\left[ \frac{s^2}{2} - \frac{s^3}{3a} \right]_0^a
$$

**Paso 9:** Evaluar (la parte entre corchetes es $\frac{a^2}{6}$, como en el Ejercicio 1) y aplicar el signo negativo.

$$
-\frac{a^2}{6}
$$

**Conclusión:** con el mismo campo y la misma superficie, pero orientación opuesta, el flujo es **igual en valor absoluto pero con signo opuesto** al del Ejercicio 1. Como el campo $(0,x,0)$ apunta en la dirección $+y$ (más grande cuanto mayor es $x$), el agua atraviesa la superficie hacia la derecha; al orientar la superficie en sentido opuesto, el flujo da negativo. El resultado no depende de $b$; si $a = 0$ el flujo sería $0$ (el plano quedaría contenido en el plano $yz$, tangente al campo, y el agua no lo atravesaría).

</details>

</details>

## Propiedad: dependencia del flujo con la orientación [1:00:03](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3603s)

Esta **propiedad de las integrales de campos vectoriales a través de superficies** resume los Ejercicios 1 y 2:

- Si dos parametrizaciones $\sigma$ y $\tau$ de una misma superficie tienen la **misma orientación** (sus campos de versores normales apuntan en la misma dirección), entonces el flujo calculado con cualquiera de las dos da **exactamente lo mismo**.
- Si una parametrización **invierte la orientación** respecto de la otra, el flujo a través de la misma superficie del mismo campo da **igual en valor absoluto pero con signo opuesto**.

## Ejercicio 3: preparación (flujo a través de una superficie esférica) [1:01:42](https://www.youtube.com/watch?v=djt3sX5V2lk&t=3702s)

Este resultado se reutilizará en algún ejercicio posterior.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=3702s">1:01:42</a>: Flujo a través de una superficie esférica</summary>

Calcular el flujo del campo vectorial

$$
\vec{F}(x,y,z) = k\,\frac{(x, y, z)}{\|(x,y,z)\|^3}
$$

(con $k$ constante) a través de una **superficie esférica de radio $r$** centrada en el origen.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Parametrizar la superficie esférica con coordenadas esféricas.

$$
\sigma(\theta,\varphi) = \left(r\cos\theta\cos\varphi,\; r\cos\theta\sin\varphi,\; r\sin\theta\right)
$$

con $\theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ y $\varphi \in [0, 2\pi]$.

**Paso 2:** Calcular el producto vectorial de las derivadas parciales con el determinante. Las derivadas parciales son:

$$
\sigma'_\theta = \left(-r\sin\theta\cos\varphi,\; -r\sin\theta\sin\varphi,\; r\cos\theta\right)
$$

$$
\sigma'_\varphi = \left(-r\cos\theta\sin\varphi,\; r\cos\theta\cos\varphi,\; 0\right)
$$

**Paso 3:** Resolver el determinante componente a componente.

$$
\sigma'_\theta \times \sigma'_\varphi = \left( -r^2\cos^2\theta\cos\varphi,\; -r^2\cos^2\theta\sin\varphi,\; \ast \right)
$$

Para la tercera componente se saca factor común $-r^2\sin\theta\cos\theta$ del término $-r^2\sin\theta\cos\theta(\cos^2\varphi + \sin^2\varphi)$, y como $\cos^2\varphi + \sin^2\varphi = 1$:

$$
\text{tercera componente} = -r^2\sin\theta\cos\theta
$$

Por lo tanto:

$$
\sigma'_\theta \times \sigma'_\varphi = \left( -r^2\cos^2\theta\cos\varphi,\; -r^2\cos^2\theta\sin\varphi,\; -r^2\sin\theta\cos\theta \right)
$$

**Paso 4:** Analizar la orientación. Para un punto del primer octante, $\theta \in \left(0,\frac{\pi}{2}\right)$ y $\varphi \in \left(0,\frac{\pi}{2}\right)$, todos los senos y cosenos son positivos; por lo tanto las **tres componentes del vector normal son negativas**. El vector normal apunta **hacia el interior** de la superficie esférica (hacia el origen). Como el campo de versores normales es continuo, todos apuntan hacia adentro. (Con otra parametrización podrían apuntar hacia el exterior; es una u otra opción.)

**Paso 5:** Plantear el flujo. Al evaluar el campo en la superficie, la norma $\|(x,y,z)\| = r$ (todos los puntos están a distancia $r$ del centro), por lo que $\|(x,y,z)\|^3 = r^3$.

$$
\iint_S \vec{F}\cdot d\vec{S} = \iint_D k\,\frac{(r\cos\theta\cos\varphi,\; r\cos\theta\sin\varphi,\; r\sin\theta)}{r^3} \cdot \left(\sigma'_\theta \times \sigma'_\varphi\right) d\varphi\, d\theta
$$

**Paso 6:** Sacar $k$ y simplificar $r$ del numerador con $r^3$. Hacer el producto escalar. Cada término lleva $r$ (del campo) por $-r^2$ (del vector normal), dando $-r^3$, que se simplifica con el $r^3$ del denominador. Se saca factor común $-\dfrac{kr^3}{r^3} = -k$ y se agrupan los términos:

- De las dos primeras componentes se saca factor común $\cos^3\theta$, y queda $\cos^3\theta(\cos^2\varphi + \sin^2\varphi) = \cos^3\theta$.
- Con la tercera componente se saca factor común $\cos\theta$: queda $\cos\theta(\cos^2\theta + \sin^2\theta) = \cos\theta$.

$$
\iint_S \vec{F}\cdot d\vec{S} = -k \int_0^{2\pi}\int_{-\pi/2}^{\pi/2} \cos\theta \, d\theta \, d\varphi
$$

**Paso 7:** Como $\cos\theta$ no depende de $\varphi$, la integral en $\varphi$ da $2\pi$.

$$
\int_0^{2\pi} d\varphi = 2\pi
$$

**Paso 8:** Integrar $\cos\theta$ entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$.

$$
\int_{-\pi/2}^{\pi/2} \cos\theta \, d\theta = \left[\sin\theta\right]_{-\pi/2}^{\pi/2} = 1 - (-1) = 2
$$

**Paso 9:** Multiplicar los resultados.

$$
\iint_S \vec{F}\cdot d\vec{S} = -k \cdot 2\pi \cdot 2 = -4k\pi
$$

**Conclusión:** el flujo a través de la superficie esférica, orientada con el normal apuntando hacia el **interior**, es $-4k\pi$. Si $k > 0$, el flujo es negativo: el agua está yendo en la dirección **opuesta** al normal (que apunta hacia adentro), es decir **saliendo** de la superficie. En superficies cerradas, un flujo positivo significa que sale más agua de la que entra (**fuente**); un flujo negativo, que entra más de la que sale (**sumidero**).

</details>

</details>

## Fuentes y sumideros en superficies cerradas [1:18:33](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4713s)

Cuando se tienen **superficies cerradas** y se evalúan estos flujos:

- Si el flujo (sobre toda la superficie cerrada) es **positivo**, sale más agua de la que entra: hay una **fuente** encerrada dentro de la superficie.
- Si el flujo es **negativo**, entra más agua de la que sale: hay un **sumidero**.

En el Ejercicio 3, con $k > 0$ el flujo dio negativo (el normal apuntaba hacia el interior y el agua salía). Con $k < 0$ el flujo sería positivo, el agua iría en la dirección del normal (entrando), y habría un **sumidero**.

## Superficie dada por ecuación cartesiana (variable dependiente) [1:20:08](https://www.youtube.com/watch?v=djt3sX5V2lk&t=4808s)

Observación análoga a la vista para áreas de superficies e integrales de campos escalares. Si la superficie está definida por una **ecuación cartesiana** $g(x,y,z) = 0$ (el conjunto de nivel cero de una función de tres variables) donde una variable **depende de las otras dos** (por ejemplo $z$ como función de $x, y$, cumpliendo las hipótesis del teorema de la función implícita), el flujo se puede calcular como:

$$
\iint_S \vec{F} \cdot d\vec{S} = \iint_{D_{xy}} \vec{F} \cdot \frac{\nabla g}{\left| g'_z \right|} \, dx \, dy \quad \text{[poco claro en la transcripción]}
$$

donde $\vec{F}$ se evalúa en los puntos de la superficie (con $z$ expresado en términos de $x,y$) y $D_{xy}$ es la **proyección** de la superficie al plano $xy$. Es muy similar a la expresión para campos escalares y áreas, pero en lugar de multiplicar por la **norma** del gradiente, se multiplica **directamente por el gradiente** $\nabla g$.

**Restricción:** una variable (aquí $z$) debe depender de las otras dos. Esta expresión **no** sirve para una superficie esférica, porque una esfera completa no se puede ver como la gráfica de una función de $(x,y)$ (a un mismo $(x,y)$ le corresponderían dos imágenes, una por encima y otra por debajo del plano $xy$).

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=djt3sX5V2lk&t=4969s">1:22:49</a>: Flujo a través de un paraboloide</summary>

Calcular el flujo del campo vectorial $\vec{F}(x,y,z) = (x, y, z)$ a través del **paraboloide circular** $z = x^2 + y^2$, tomando solo el trozo por **debajo del plano $z = 1$** (puntos con $z \le 1$). Es una **superficie abierta** (como un vaso sin pie).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Considerar la superficie como el conjunto de nivel cero de $g$.

$$
g(x,y,z) = z - x^2 - y^2
$$

El conjunto $g = 0$ corresponde al paraboloide $z = x^2 + y^2$.

**Paso 2:** Aplicar la fórmula para superficies con $z$ dependiente de $x,y$.

$$
\iint_S \vec{F}\cdot d\vec{S} = \iint_{D_{xy}} \vec{F} \cdot \frac{\nabla g}{\left| g'_z \right|} \, dx \, dy
$$

**Paso 3:** Calcular el gradiente de $g$.

$$
\nabla g = (-2x,\; -2y,\; 1), \qquad g'_z = 1
$$

**Paso 4:** Evaluar el campo en la superficie, expresando $z = x^2 + y^2$.

$$
\vec{F} = \left(x,\; y,\; x^2 + y^2\right)
$$

**Paso 5:** Plantear el producto escalar $\vec{F}\cdot\nabla g$ (con $|g'_z| = 1$).

$$
\vec{F}\cdot\nabla g = x(-2x) + y(-2y) + (x^2+y^2)(1) = -2x^2 - 2y^2 + x^2 + y^2
$$

$$
\vec{F}\cdot\nabla g = -x^2 - y^2
$$

**Paso 6:** Determinar la región de integración. Como $z \le 1$, se cumple $x^2 + y^2 \le 1$: la proyección al plano $xy$ es el interior de una circunferencia de radio $1$.

$$
\iint_{x^2+y^2\le 1} \left(-x^2 - y^2\right) dx\, dy
$$

**Paso 7:** Pasar a **coordenadas polares** por la forma de la región y del integrando: $x = \rho\cos\varphi$, $y = \rho\sin\varphi$, con módulo del jacobiano $\rho$, y $x^2+y^2 = \rho^2$.

$$
\int_0^{2\pi}\int_0^1 \left(-\rho^2\right)\rho \, d\rho \, d\varphi
$$

con $\rho \in [0,1]$ y $\varphi \in [0, 2\pi]$.

**Paso 8:** Separar. La integral en $\varphi$ da $2\pi$; sacar el signo negativo e integrar $\rho^3$.

$$
-\,2\pi \int_0^1 \rho^3 \, d\rho = -2\pi \left[\frac{\rho^4}{4}\right]_0^1 = -2\pi \cdot \frac{1}{4}
$$

**Paso 9:** Resultado.

$$
\iint_S \vec{F}\cdot d\vec{S} = -\frac{\pi}{2}
$$

**Interpretación:** el gradiente $\nabla g$ es un vector normal a la superficie con componente $z$ positiva (apunta hacia arriba, hacia el eje $z$). Como el flujo dio **negativo**, el agua atraviesa la superficie en el sentido opuesto al normal. El campo $\vec{F} = (x,y,z)$ es **radial** (los vectores van del origen alejándose de él).

</details>

</details>
