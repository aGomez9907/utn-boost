# Área de una superficie

> Fuente: https://www.youtube.com/watch?v=NL0A1Tyn2Nk

---

## Índice
- [00:35](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=35s) — Superficies simples
- [02:40](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=160s) — Área de una superficie simple
- [03:44](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=224s) — Interpretación geométrica del diferencial de área
- [05:55](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=355s) — 📝 Ejercicio 1: Área de un plano en el primer octante
- [17:11](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1031s) — 📝 Ejercicio 2: Misma superficie con otra parametrización
- [25:55](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1555s) — El área no depende de la parametrización
- [30:14](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1814s) — 📝 Ejercicio 3: Área de una superficie esférica
- [47:10](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=2830s) — Área de la gráfica de una función definida implícitamente
- [54:32](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=3272s) — 📝 Ejercicio 4: Área de un paraboloide
- [1:03:39](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=3819s) — Requisito para usar la fórmula de la gráfica

---

## Superficies simples [00:35](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=35s)

Para hablar de integrales evaluadas sobre superficies, primero se define sobre qué superficies se va a operar: las **superficies simples**.

Una superficie es simple cuando está **parametrizada en forma regular** por una función $\sigma$ que cumple estos requisitos:

- **$\sigma$ es de clase $C^1$**: sus tres funciones componentes tienen derivadas parciales continuas (dos derivadas parciales cada una, pues hay dos variables).
- El subconjunto $D$ del dominio de $\sigma$ corresponde a una **región de integración** con las formas que se adoptan para funciones de dos variables.
- **$\sigma$ es inyectiva**, al menos en el interior de $D$: elementos distintos del dominio (por lo menos del interior) tienen imágenes distintas en el espacio. Es decir, la superficie parametrizada solo puede tener puntos en común cuando corresponden a elementos del dominio ubicados en su borde.

Se llama **superficie simple** parametrizada por $\sigma$ al conjunto imagen de $\sigma$ para todos los elementos del conjunto $D$.

## Área de una superficie simple [02:40](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=160s)

El **área de una superficie simple** parametrizada por $\sigma$ se define como la integral doble, extendida a la región de integración $D$, de la norma del producto vectorial de las derivadas parciales de $\sigma$:

$$
A = \iint_{D} \left\| \sigma'_u \times \sigma'_v \right\| \, du \, dv
$$

## Interpretación geométrica del diferencial de área [03:44](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=224s)

Las derivadas parciales de $\sigma$ en cualquier punto se interpretan como **vectores tangentes** a la superficie. Como $\sigma'_u$ y $\sigma'_v$ son tangentes, su producto vectorial resulta un **vector normal** a la superficie:

$$
\sigma'_u \times \sigma'_v = \vec{N}
$$

Por ser la superficie regular, este vector es **no nulo** (no puede ser el vector $(0,0,0)$): ese es justamente un requisito de las superficies regulares.

La norma del producto vectorial tiene como interpretación geométrica el **área del paralelogramo** determinado por los dos vectores. Multiplicada por los diferenciales de las variables, da el **diferencial de área** $d\sigma$ de la superficie en el punto analizado: el área de un paralelogramo tangente a la superficie, de dimensión diferencial.

$$
d\sigma = \left\| \sigma'_u \times \sigma'_v \right\| \, du \, dv
$$

La suma (integral) de todas las áreas de esos paralelogramos tangentes define el área de la superficie total.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=355s">05:55</a>: Área de un plano en el primer octante</summary>

Calcular el área de la superficie plana de ecuación cartesiana $z = 4 - 2x - 2y$ (equivalentemente $2x + 2y + z = 4$), limitada al **primer octante** ($x, y, z \ge 0$). El plano corta a los ejes $x$, $y$, $z$ en $2$, $2$ y $4$ respectivamente, formando un triángulo. La superficie se parametriza tomando $x = u$, $y = v$, $z = 4 - 2u - 2v$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear el área de la superficie parametrizada.

$$
A = \iint_{S_{uv}} \left\| \sigma'_u \times \sigma'_v \right\| \, du \, dv
$$

**Paso 2:** Calcular el producto vectorial $\sigma'_u \times \sigma'_v$ como un determinante. La derivada de $\sigma = (u,\, v,\, 4 - 2u - 2v)$ respecto de $u$ es $(1, 0, -2)$ y respecto de $v$ es $(0, 1, -2)$.

$$
\sigma'_u \times \sigma'_v =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
1 & 0 & -2 \\
0 & 1 & -2
\end{vmatrix}
$$

**Paso 3:** Resolver el determinante componente a componente.

$$
\sigma'_u \times \sigma'_v = \big(\, 0\cdot(-2) - (-2)\cdot 1,\; -\left[1\cdot(-2) - (-2)\cdot 0\right],\; 1\cdot 1 - 0\cdot 0 \,\big) = (2,\, 2,\, 1)
$$

**Paso 4:** Calcular la norma de ese vector, que es el integrando.

$$
\left\| \sigma'_u \times \sigma'_v \right\| = \sqrt{2^2 + 2^2 + 1^2} = \sqrt{4 + 4 + 1} = \sqrt{9} = 3
$$

**Paso 5:** Identificar la región de integración. Como $x = u$ y $y = v$, y la superficie es el trozo de plano del primer octante, se tiene $u \ge 0$ y $v \ge 0$. Además, $x$ toma valores entre $0$ y $2$ (lo mismo $u$). Para un $u$ fijo, $v$ llega hasta la recta que se obtiene haciendo $z = 0$ en el plano: $2x + 2y = 4$, es decir $x + y = 2$, o sea $u + v = 2$. Por lo tanto $v$ varía entre $0$ y $2 - u$. La región $S_{uv}$ es un triángulo en el piso.

**Paso 6:** El integrando es constante, así que sale de la integral: el área es $3$ por el área de la región de integración.

$$
A = \iint_{S_{uv}} 3 \, du \, dv = 3 \cdot (\text{área de } S_{uv})
$$

**Paso 7:** El área de la región de integración (triángulo de base $2$ y altura $2$) es base por altura sobre $2$.

$$
\text{área de } S_{uv} = \frac{2 \cdot 2}{2} = 2
$$

**Paso 8:** Calcular el área de la superficie.

$$
A = 3 \cdot 2 = 6
$$

El área del triángulo ubicado en el espacio (la superficie) vale $6$. No hay que confundirlo con el área de la región de integración en el piso, que vale $2$.

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1031s">17:11</a>: Misma superficie con otra parametrización</summary>

Calcular el área de la **misma superficie** del ejercicio anterior, pero usando otra parametrización: $\tau(s,t)$ con $x = 2 - s - \tfrac{t}{2}$, $y = s$, $z = t$ (según la transcripción, $x = 2 - s - \tfrac{t}{2}$, $y = s$, $z = t$). Reagrupando se obtiene $2x + 2y + z = 4$, que es el mismo plano visto antes. Como la superficie es la misma, es de esperar que el área también sea $6$, con independencia de la parametrización.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Plantear el área con la nueva parametrización.

$$
A = \iint_{S_{st}} \left\| \tau'_s \times \tau'_t \right\| \, ds \, dt
$$

**Paso 2:** Calcular el producto vectorial $\tau'_s \times \tau'_t$. La derivada respecto de $s$ es $(-1, 1, 0)$ y la derivada respecto de $t$ es $\left(-\tfrac{1}{2}, 0, 1\right)$.

$$
\tau'_s \times \tau'_t =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k} \\
-1 & 1 & 0 \\
-\tfrac{1}{2} & 0 & 1
\end{vmatrix}
$$

**Paso 3:** Resolver el determinante componente a componente.

$$
\tau'_s \times \tau'_t = \big(\, 1\cdot 1 - 0\cdot 0,\; -\left[(-1)\cdot 1 - 0\cdot(-\tfrac{1}{2})\right],\; (-1)\cdot 0 - 1\cdot(-\tfrac{1}{2}) \,\big) = \left(1,\, 1,\, \tfrac{1}{2}\right)
$$

**Paso 4:** Calcular la norma. Con denominador común $4$: $1 = \tfrac{4}{4}$, con lo que queda $\tfrac{4}{4} + \tfrac{4}{4} + \tfrac{1}{4} = \tfrac{9}{4}$.

$$
\left\| \tau'_s \times \tau'_t \right\| = \sqrt{1^2 + 1^2 + \left(\tfrac{1}{2}\right)^2} = \sqrt{\frac{4}{4} + \frac{4}{4} + \frac{1}{4}} = \sqrt{\frac{9}{4}} = \frac{3}{2}
$$

**Paso 5:** El integrando es constante $\tfrac{3}{2}$: sale de la integral y queda por el área de la región de integración $S_{st}$ (proyección de la superficie sobre el plano $st$, un triángulo de base $2$ y altura $4$).

$$
A = \frac{3}{2} \iint_{S_{st}} ds \, dt = \frac{3}{2} \cdot (\text{área de } S_{st})
$$

**Paso 6:** El área del triángulo de la región es base por altura sobre $2$.

$$
\text{área de } S_{st} = \frac{2 \cdot 4}{2} = 4
$$

**Paso 7:** Calcular el área de la superficie.

$$
A = \frac{3}{2} \cdot 4 = 6
$$

Tal como se suponía, el área vuelve a ser $6$: no depende de cómo se parametrice la superficie.

</details>

</details>

## El área no depende de la parametrización [25:55](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1555s)

El valor del área de una superficie **no depende de la parametrización** elegida. La parametrización es solo una función que se usa para definir la superficie, y el área es una propiedad de la superficie en sí.

Formalmente: si $\sigma$ parametriza una superficie simple y $\tau$ parametriza la **misma** superficie simple, el área calculada con una u otra es la misma.

Esto se entiende viendo a $\tau$ como una **reparametrización**. Dada una función vectorial $g$ (de clase $C^1$, con dos derivadas parciales continuas) que va de un subconjunto $D^*$ (en un nuevo sistema de coordenadas $(v', w')$) a un subconjunto $D$ (en el plano $(u,v)$), con **jacobiano distinto de cero** —el mismo jacobiano que aparece en el cambio de variables de las integrales dobles— y que admite función inversa (a cada elemento de $D^*$ le corresponde uno y solo uno de $D$), se define:

$$
\tau = \sigma \circ g
$$

Como la superficie es la misma, es natural que las áreas calculadas con $\sigma$ o con $\tau$ den exactamente lo mismo.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=1814s">30:14</a>: Área de una superficie esférica</summary>

Calcular el área de una **superficie esférica de radio $r$** centrada en el origen, de ecuación cartesiana $x^2 + y^2 + z^2 = r^2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Buscar una parametrización usando **coordenadas esféricas**, donde $\rho$ es la distancia del origen al punto, $\theta$ el ángulo del segmento con el plano $xy$, y $\varphi$ el ángulo de la proyección sobre el plano $xy$ respecto del eje $x$.

$$
x = \rho \cos\theta \cos\varphi, \quad y = \rho \cos\theta \sin\varphi, \quad z = \rho \sin\theta
$$

**Paso 2:** En la superficie esférica, la distancia al origen es constante e igual a $r$, es decir $\rho = r$. Así, la ecuación cartesiana $x^2 + y^2 + z^2 = r^2$ se expresa en coordenadas esféricas simplemente como $\rho = r$. La parametrización queda en función de $\theta$ y $\varphi$:

$$
\sigma(\theta, \varphi) = \big(\, r \cos\theta \cos\varphi,\; r \cos\theta \sin\varphi,\; r \sin\theta \,\big)
$$

con $\theta \in \left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right]$ y $\varphi \in [0, 2\pi]$.

**Paso 3:** Derivar la parametrización respecto de $\theta$.

$$
\sigma'_\theta = \big(\, -r \sin\theta \cos\varphi,\; -r \sin\theta \sin\varphi,\; r \cos\theta \,\big)
$$

**Paso 4:** Derivar la parametrización respecto de $\varphi$ (la tercera componente no depende de $\varphi$, por eso es $0$).

$$
\sigma'_\varphi = \big(\, -r \cos\theta \sin\varphi,\; r \cos\theta \cos\varphi,\; 0 \,\big)
$$

**Paso 5:** Calcular el producto vectorial $\sigma'_\theta \times \sigma'_\varphi$ resolviendo el determinante.

$$
\sigma'_\theta \times \sigma'_\varphi = \big(\, -r^2 \cos^2\theta \cos\varphi,\; -r^2 \cos^2\theta \sin\varphi,\; -r^2 \sin\theta \cos\theta \,\big)
$$

En la tercera componente se sacó factor común: $-r^2 \sin\theta \cos\theta\,(\cos^2\varphi + \sin^2\varphi) = -r^2 \sin\theta \cos\theta$.

**Paso 6:** Calcular la norma del producto vectorial. Al elevar al cuadrado, los signos negativos desaparecen y todos los términos tienen factor $r^4$.

$$
\left\| \sigma'_\theta \times \sigma'_\varphi \right\| = \sqrt{ r^4 \cos^4\theta \cos^2\varphi + r^4 \cos^4\theta \sin^2\varphi + r^4 \sin^2\theta \cos^2\theta }
$$

**Paso 7:** Sacar factor común $r^4$ (y $r^2$ fuera de la raíz, positivo por ser $r > 0$). En los dos primeros términos se saca factor común $\cos^4\theta$, y $\cos^2\varphi + \sin^2\varphi = 1$.

$$
= r^2 \sqrt{ \cos^4\theta + \sin^2\theta \cos^2\theta }
$$

**Paso 8:** De los dos términos restantes sacar factor común $\cos^2\theta$, que sale de la raíz como $|\cos\theta|$; dentro queda $\cos^2\theta + \sin^2\theta = 1$.

$$
= r^2 \, |\cos\theta| \, \sqrt{\cos^2\theta + \sin^2\theta} = r^2 \, |\cos\theta|
$$

**Paso 9:** Como $\theta$ es un ángulo del primer o cuarto cuadrante, $\cos\theta \ge 0$, por lo que $|\cos\theta| = \cos\theta$. La norma queda:

$$
\left\| \sigma'_\theta \times \sigma'_\varphi \right\| = r^2 \cos\theta
$$

**Paso 10:** Plantear el área como integral doble sobre el campo de variación de $\theta$ y $\varphi$.

$$
A = \iint \left\| \sigma'_\theta \times \sigma'_\varphi \right\| \, d\theta \, d\varphi = \int_{-\pi/2}^{\pi/2} \int_{0}^{2\pi} r^2 \cos\theta \, d\varphi \, d\theta
$$

**Paso 11:** $r^2$ es constante y sale de la integral. Como el integrando no depende de $\varphi$, se separa: la integral de $d\varphi$ entre $0$ y $2\pi$ da $2\pi$, y queda la integral de $\cos\theta$ entre $-\tfrac{\pi}{2}$ y $\tfrac{\pi}{2}$.

$$
A = r^2 \cdot 2\pi \cdot \int_{-\pi/2}^{\pi/2} \cos\theta \, d\theta
$$

**Paso 12:** Resolver la integral en $\theta$: $\sin\left(\tfrac{\pi}{2}\right) - \sin\left(-\tfrac{\pi}{2}\right) = 1 - (-1) = 2$.

$$
A = r^2 \cdot 2\pi \cdot 2 = 4\pi r^2
$$

El área de la superficie esférica de radio $r$ es $4\pi r^2$. Este ejemplo muestra que $x$, $y$, $z$ no siempre están asociados directamente a una variable de la parametrización: la parametrización puede ser más compleja (aquí, ligada a las coordenadas esféricas).

</details>

</details>

## Área de la gráfica de una función definida implícitamente [47:10](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=2830s)

Supongamos una superficie simple parametrizada por $\sigma(x,y) = (x,\, y,\, z(x,y))$, donde $z$ depende de $x$ e $y$. En este caso el dominio de $\sigma$ coincide con el dominio de las variables $x, y$, así que la superficie es la **gráfica de una función escalar de dos variables** $z(x,y)$, definida sobre un conjunto $D \subseteq \mathbb{R}^2$.

Supongamos además que la superficie es el **conjunto de nivel cero** de una función $g$ de tres variables, es decir que $z$ está definida implícitamente por $g(x, y, z) = 0$. Bajo esas circunstancias, el área se calcula con:

$$
A = \iint_{D} \frac{\left\| \nabla g \right\|}{\left| g'_z \right|} \, dx \, dy
$$

**Justificación (de dónde sale la fórmula):**

Al derivar la parametrización $\sigma(x,y) = (x, y, z(x,y))$ se obtiene $\sigma'_x = (1, 0, z'_x)$ y $\sigma'_y = (0, 1, z'_y)$. Su producto vectorial es:

$$
\sigma'_x \times \sigma'_y = (-z'_x,\, -z'_y,\, 1)
$$

Por el **teorema de la función implícita** (con $g'_z \neq 0$), se tiene $z'_x = -\dfrac{g'_x}{g'_z}$ y $z'_y = -\dfrac{g'_y}{g'_z}$. Reemplazando, las componentes quedan $\dfrac{g'_x}{g'_z}$, $\dfrac{g'_y}{g'_z}$ y $1 = \dfrac{g'_z}{g'_z}$. Al calcular la norma con denominador común $g'^2_z$:

$$
\left\| \sigma'_x \times \sigma'_y \right\| = \frac{\sqrt{g'^2_x + g'^2_y + g'^2_z}}{\left| g'_z \right|} = \frac{\left\| \nabla g \right\|}{\left| g'_z \right|}
$$

ya que el numerador es la norma del gradiente $\nabla g = (g'_x, g'_y, g'_z)$. Integrando ese cociente sobre el dominio $D$ de las variables independientes se obtiene el área de la superficie $S$.

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=3272s">54:32</a>: Área de un paraboloide</summary>

Calcular el área del paraboloide $z = 1 - x^2 - y^2$ (paraboloide con concavidad hacia abajo, vértice en $(0, 0, 1)$), tomando solo el trozo con $z \ge 0$, es decir la parte por encima del plano $xy$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Ver la superficie como el conjunto de nivel cero de una función $g$ de tres variables. Tomando $g(x,y,z) = x^2 + y^2 + z - 1$, el nivel $g = 0$ da $x^2 + y^2 + z - 1 = 0$, que corresponde a los puntos del paraboloide.

**Paso 2:** Plantear el área con la fórmula de la gráfica definida implícitamente.

$$
A = \iint_{D} \frac{\left\| \nabla g \right\|}{\left| g'_z \right|} \, dx \, dy
$$

**Paso 3:** Calcular el gradiente de $g$ y su norma.

$$
\nabla g = (2x,\, 2y,\, 1), \qquad \left\| \nabla g \right\| = \sqrt{4x^2 + 4y^2 + 1}
$$

**Paso 4:** Como $g'_z = 1$, su módulo es $1$, así que el integrando es directamente $\left\| \nabla g \right\|$.

$$
A = \iint_{D} \sqrt{4x^2 + 4y^2 + 1} \, dx \, dy
$$

**Paso 5:** Determinar la región $D$: la proyección de la superficie sobre el plano $xy$. Como $z \ge 0$, entonces $1 - x^2 - y^2 \ge 0$, es decir $x^2 + y^2 \le 1$: el interior de una circunferencia de radio $1$.

**Paso 6:** Como la región es el interior de una circunferencia y el integrando depende de $x^2 + y^2$ (sacando factor común $4$: $4(x^2 + y^2) + 1$), conviene usar **coordenadas polares** $x = \rho\cos\varphi$, $y = \rho\sin\varphi$, con módulo del jacobiano igual a $\rho$.

$$
A = \iint \sqrt{4\rho^2 + 1} \; \rho \, d\varphi \, d\rho, \qquad \rho \in [0, 1], \; \varphi \in [0, 2\pi]
$$

**Paso 7:** El integrando no depende de $\varphi$, así que la integral de $d\varphi$ entre $0$ y $2\pi$ da $2\pi$.

$$
A = 2\pi \int_{0}^{1} \sqrt{4\rho^2 + 1} \; \rho \, d\rho
$$

**Paso 8:** Resolver la integral en $\rho$ por sustitución. Llamando $s = 4\rho^2 + 1$, se tiene $ds = 8\rho \, d\rho$, o sea $\rho \, d\rho = \dfrac{ds}{8}$.

$$
\int \sqrt{s} \, \frac{ds}{8} = \frac{1}{8} \cdot \frac{s^{3/2}}{3/2} = \frac{s^{3/2}}{12} = \frac{(4\rho^2 + 1)^{3/2}}{12}
$$

**Paso 9:** Reincorporar el $2\pi$: $\dfrac{2\pi}{12} = \dfrac{\pi}{6}$. El área queda evaluada entre $\rho = 0$ y $\rho = 1$.

$$
A = \frac{\pi}{6} \left[ (4\rho^2 + 1)^{3/2} \right]_{0}^{1}
$$

**Paso 10:** Reemplazar los límites: en $\rho = 1$, $4\cdot 1 + 1 = 5$, da $5^{3/2}$; en $\rho = 0$, $1^{3/2} = 1$.

$$
A = \frac{\pi}{6} \left( 5^{3/2} - 1 \right)
$$

El área del paraboloide es $\dfrac{\pi}{6}\left(5^{3/2} - 1\right)$.

</details>

</details>

## Requisito para usar la fórmula de la gráfica [1:03:39](https://www.youtube.com/watch?v=NL0A1Tyn2Nk&t=3819s)

Para usar la fórmula del área de la gráfica definida implícitamente

$$
A = \iint_{D} \frac{\left\| \nabla g \right\|}{\left| g'_z \right|} \, dx \, dy
$$

es **requisito** que la superficie se vea realmente como la **gráfica de una función de dos variables** $z(x,y)$ y que la función $g$ (cuyo conjunto de nivel cero define la superficie) defina a $z$ como función de $x, y$ cumpliendo el **teorema de la función implícita** (con $g'_z \neq 0$).

Por ejemplo, esta fórmula **no** se puede usar para la superficie esférica completa, porque no es la gráfica de una función de dos variables: para un mismo par $(x,y)$ habría una imagen por encima del plano $xy$ y otra por debajo.

Cuando la superficie tiene cierta **simetría**, se puede trabajar con una mitad (por ejemplo, media esfera, que sí es gráfica de una función), calcular su área y multiplicar por $2$. Lo mismo aplicaría al paraboloide si por algún motivo conviniera calcular una mitad.
