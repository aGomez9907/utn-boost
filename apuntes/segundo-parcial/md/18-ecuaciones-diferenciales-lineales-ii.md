# Ecuaciones diferenciales lineales II

> Fuente: https://www.youtube.com/watch?v=4HbBxQb8bpE

---

## Índice

- [00:00](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=0s) — Ecuación diferencial lineal de segundo orden: forma general
- [01:03](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=63s) — Solución de una EDO: verificación por reemplazo
- 📝 [02:40](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=160s) — Ejercicio 1: verificar que $y=\sin x$ es solución
- [03:43](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=223s) — Ecuación diferencial homogénea
- [04:13](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=253s) — Teorema: combinación lineal de soluciones
- 📝 [06:19](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=379s) — Ejercicio 2: demostración del teorema de superposición
- [10:33](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=633s) — Dependencia e independencia lineal de soluciones
- [12:40](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=760s) — Criterio del cociente para independencia lineal
- 📝 [13:12](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=792s) — Ejercicio 3: clasificar pares de funciones por el cociente
- [14:44](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=884s) — Solución general de la EDO homogénea
- [15:49](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=949s) — Reducción a coeficientes constantes
- [18:27](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1107s) — Coeficientes constantes: solución exponencial y ecuación característica
- 📝 [19:32](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1172s) — Ejercicio 4: verificar $y=e^{mx}$ y deducir la ecuación característica
- [24:20](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1460s) — Caso 1: raíces reales y distintas
- 📝 [27:05](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1625s) — Ejercicio 5: solución general con raíces reales distintas
- [30:16](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1816s) — Caso 2: raíz doble (real)
- 📝 [38:37](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2317s) — Ejercicio 6: solución general con raíz doble
- [39:43](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2383s) — Caso 3: raíces complejas conjugadas
- 📝 [45:04](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2704s) — Ejercicio 7: solución general con raíces complejas conjugadas

---

## Ecuación diferencial lineal de segundo orden: forma general — [00:00](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=0s)

La clase se dedica al estudio de las **ecuaciones diferenciales lineales de segundo orden**. La ecuación es *lineal* porque es una combinación lineal de la función incógnita $y$ y sus derivadas, donde los coeficientes que afectan tanto a la función incógnita como a sus derivadas son funciones de la variable $x$. En el miembro de la derecha hay un término independiente de la función incógnita.

$$
a_2(x)\, y'' + a_1(x)\, y' + a_0(x)\, y = f(x)
$$

- El **dominio de definición** de la ecuación (y por lo tanto de su función solución) es el conjunto de valores de $x$ en que está definida.
- Se supone que las funciones $f(x)$, $a_2(x)$, $a_1(x)$, $a_0(x)$ son todas continuas.
- Además, el coeficiente que afecta a la derivada de mayor orden, $a_2(x)$, **no vale cero** en ningún punto del dominio.

Estas hipótesis (continuidad de los coeficientes y $a_2(x)\neq 0$) garantizan que exista una **solución general** de la ecuación diferencial y que, dadas condiciones iniciales, la **solución particular** que las satisfaga exista.

## Solución de una EDO: verificación por reemplazo — [01:03](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=63s)

La solución de una ecuación diferencial es una función que, al reemplazarla en la ecuación, la transforma en una **identidad** (satisfecha para cualquier valor de la variable independiente).

Para verificar que una función es solución, hay que calcular las derivadas necesarias (por ejemplo la derivada segunda) y reemplazarlas en la ecuación.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=160s">02:40</a>: verificar que $y=\sin x$ es solución</summary>

Verificar que la función $y=\sin x$ es solución de una ecuación diferencial en la que interviene $y''$ y la propia función.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se calcula la derivada primera de $y=\sin x$.

$$
y' = \cos x
$$

**Paso 2:** Se calcula la derivada segunda.

$$
y'' = -\sin x
$$

**Paso 3:** Se reemplaza $y''$ por su valor y $y$ por $\sin x$ en la ecuación. Se comprueba que, para cualquier valor real de $x$, la ecuación se transforma en una **identidad**. La identidad se satisface para cualquier valor de la variable independiente. [paso en el pizarrón, ver video]

</details>

</details>

## Ecuación diferencial homogénea — [03:43](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=223s)

Se empieza por el caso sencillo en que $f(x)$ (el término independiente de la función incógnita) es igual a $0$ para **cualquier** valor del dominio de definición. Este tipo de ecuación se denomina **ecuación diferencial homogénea**:

$$
a_2(x)\, y'' + a_1(x)\, y' + a_0(x)\, y = 0
$$

## Teorema: combinación lineal de soluciones — [04:13](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=253s)

**Teorema (superposición).** Si $y_1$ e $y_2$ son soluciones de una ecuación diferencial lineal de segundo orden homogénea, entonces la **combinación lineal** de esas dos soluciones también es solución de la ecuación:

$$
y = c_1\, y_1 + c_2\, y_2
$$

Este teorema permite encontrar la solución general de este tipo de ecuaciones. Como la ecuación es de segundo orden, su solución general debe depender de **tantas constantes arbitrarias como el orden**, es decir, de **dos** constantes (si fuera de tercer orden dependería de tres, etc.). La estrategia será buscar dos soluciones particulares y formar su combinación lineal.

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=379s">06:19</a>: demostración del teorema de superposición</summary>

Demostrar que si $y_1$ e $y_2$ son soluciones de la ecuación homogénea $a_2\,y'' + a_1\,y' + a_0\,y = 0$, entonces $y = c_1 y_1 + c_2 y_2$ también es solución.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se calcula la derivada primera, usando que la derivada de una suma es la suma de las derivadas y que la derivada de una constante por una función es la constante por la derivada.

$$
y' = c_1\, y_1' + c_2\, y_2'
$$

**Paso 2:** Se deriva nuevamente para obtener la derivada segunda.

$$
y'' = c_1\, y_1'' + c_2\, y_2''
$$

**Paso 3:** Se reemplaza en el miembro izquierdo de la ecuación diferencial.

$$
a_2\left(c_1 y_1'' + c_2 y_2''\right) + a_1\left(c_1 y_1' + c_2 y_2'\right) + a_0\left(c_1 y_1 + c_2 y_2\right)
$$

**Paso 4:** Se distribuye. Quedan seis términos; en los tres que dependen de $c_1$ se saca factor común $c_1$, y en los tres que dependen de $c_2$ se saca factor común $c_2$.

$$
c_1\left(a_2 y_1'' + a_1 y_1' + a_0 y_1\right) + c_2\left(a_2 y_2'' + a_1 y_2' + a_0 y_2\right)
$$

**Paso 5:** Por hipótesis, $y_1$ es solución, así que la suma de los tres términos que la contienen vale $0$; lo mismo con $y_2$. Por lo tanto, sea cual sea el valor de $c_1$ y de $c_2$, toda la sumatoria da $0$.

$$
c_1 \cdot 0 + c_2 \cdot 0 = 0
$$

**Paso 6:** Al reemplazar $y = c_1 y_1 + c_2 y_2$ en la ecuación diferencial, la transforma en una identidad; por lo tanto es solución.

</details>

</details>

## Dependencia e independencia lineal de soluciones — [10:33](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=633s)

Aunque $y = c_1 y_1 + c_2 y_2$ tiene dos constantes, hay que tener en cuenta un caso: **qué pasa si una función es múltiplo de la otra**, es decir $y_2 = k\, y_1$. En ese caso, reemplazando en la combinación lineal:

$$
c_1 y_1 + c_2 (k\, y_1) = y_1\,(c_1 + c_2\, k)
$$

Como $c_1 + c_2 k$ es una **única constante arbitraria**, la combinación lineal termina dependiendo de una sola constante y **no** puede ser la solución general (que necesita dos constantes).

- Cuando una función es múltiplo de la otra, se dice que son **linealmente dependientes**.
- Cuando ninguna es múltiplo de la otra, se dice que son **linealmente independientes**.

## Criterio del cociente para independencia lineal — [12:40](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=760s)

Se puede verificar la dependencia lineal mediante el **cociente** entre las dos funciones:

$$
\frac{y_2}{y_1} = \text{constante} \;\Rightarrow\; \text{linealmente dependientes}
$$

$$
\frac{y_2}{y_1} = \text{función de } x \;\Rightarrow\; \text{linealmente independientes}
$$

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=792s">13:12</a>: clasificar pares de funciones por el cociente</summary>

Clasificar como linealmente dependientes o independientes los siguientes pares de funciones usando el criterio del cociente:

1. $y_1 = e^{x}$, $y_2 = e^{-x}$
2. $y_1 = e^{-x}$, $y_2 = -e^{-x}$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Para el primer par, se hace el cociente (cociente de potencias de igual base: se restan los exponentes).

$$
\frac{y_2}{y_1} = \frac{e^{-x}}{e^{x}} = e^{-x-x} = e^{-2x}
$$

**Paso 2:** El resultado queda en función de $x$, no es constante $\Rightarrow$ las funciones son **linealmente independientes**.

**Paso 3:** Para el segundo par, se hace el cociente.

$$
\frac{y_2}{y_1} = \frac{-e^{-x}}{e^{-x}} = -1
$$

**Paso 4:** El cociente es $-1$ (constante) para todo $x$ real $\Rightarrow$ las funciones son **linealmente dependientes** (aquí $y_2 = -y_1$).

</details>

</details>

## Solución general de la EDO homogénea — [14:44](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=884s)

Para hallar la solución general de una EDO lineal de segundo orden homogénea, es deseable contar con **dos funciones $y_1$ e $y_2$ que sean soluciones y que además sean linealmente independientes** (una no múltiplo de la otra). Entonces su combinación lineal es la **solución general**:

$$
y = c_1\, y_1 + c_2\, y_2
$$

## Reducción a coeficientes constantes — [15:49](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=949s)

Partiendo de la ecuación con coeficientes $a_2(x)$, $a_1(x)$, $a_0(x)$ (funciones de $x$, cada una toma un valor real determinado), y recordando la hipótesis de que $a_2 \neq 0$, se puede **dividir toda la ecuación por $a_2$**:

$$
y'' + \frac{a_1}{a_2}\, y' + \frac{a_0}{a_2}\, y = 0
$$

Llamando $p = \dfrac{a_1}{a_2}$ y $q = \dfrac{a_0}{a_2}$ (cocientes que dan valores reales bajo la hipótesis de coeficientes constantes con $a_2\neq 0$):

$$
y'' + p\, y' + q\, y = 0
$$

## Coeficientes constantes: solución exponencial y ecuación característica — [18:27](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1107s)

Nos concentramos en las **ecuaciones diferenciales lineales de segundo orden homogéneas con coeficientes constantes** ($p$ y $q$ constantes):

$$
y'' + p\, y' + q\, y = 0
$$

Se propone que una solución tiene la forma de una función exponencial:

$$
y = e^{m x}
$$

donde $m$ debe satisfacer una **ecuación algebraica de segundo grado** (la **ecuación característica**), cuyos coeficientes son los de la ecuación diferencial:

$$
m^2 + p\, m + q = 0
$$

Una vez hallada la raíz $m$, al reemplazar $e^{mx}$ se obtiene una solución de la ecuación diferencial.

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1172s">19:32</a>: verificar $y=e^{mx}$ y deducir la ecuación característica</summary>

Verificar que $y=e^{mx}$ es solución de $y'' + p\,y' + q\,y = 0$ y deducir la condición que debe cumplir $m$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se calculan las derivadas de $y = e^{mx}$.

$$
y' = m\, e^{mx}, \qquad y'' = m^2\, e^{mx}
$$

**Paso 2:** Se reemplaza en la ecuación diferencial.

$$
m^2 e^{mx} + p\, m\, e^{mx} + q\, e^{mx} = 0
$$

**Paso 3:** Se saca factor común $e^{mx}$.

$$
e^{mx}\left(m^2 + p\, m + q\right) = 0
$$

**Paso 4:** La función exponencial $e^{mx}$ es siempre distinta de cero (sea $m>0$ o $m<0$, la gráfica de $e^{mx}$ nunca vale $0$). Por lo tanto, para que el producto sea $0$, debe anularse el paréntesis.

$$
m^2 + p\, m + q = 0
$$

**Paso 5:** Conclusión: $y=e^{mx}$ es solución **solo si** $m$ satisface esta ecuación de segundo grado, llamada **ecuación característica**. Los valores de $p$ y $q$ pueden ser cualquier real; si $p=0$ falta el término de primer grado y si $q=0$ falta el término independiente.

</details>

</details>

## Caso 1: raíces reales y distintas — [24:20](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1460s)

Dada la EDO lineal de segundo orden homogénea con coeficientes constantes, se plantea la ecuación característica y se calculan sus raíces $m_1$ y $m_2$.

Una posibilidad es que las dos raíces sean **reales y distintas**. Entonces las soluciones son:

$$
y_1 = e^{m_1 x}, \qquad y_2 = e^{m_2 x}
$$

Estas dos funciones son **linealmente independientes**, ya que su cociente

$$
\frac{y_2}{y_1} = e^{(m_2 - m_1)x}
$$

depende de $x$ (porque $m_2 - m_1 \neq 0$). Por lo tanto, la solución general es su combinación lineal:

$$
y = c_1\, e^{m_1 x} + c_2\, e^{m_2 x}
$$

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1625s">27:05</a>: solución general con raíces reales distintas</summary>

Hallar la solución general de la ecuación diferencial

$$
y'' + y' - 2y = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se identifica: EDO lineal, de segundo orden, homogénea, con coeficientes constantes. Aquí $p=1$ y $q=-2$.

**Paso 2:** Se construye la ecuación característica.

$$
m^2 + m - 2 = 0
$$

**Paso 3:** Se resuelve con la fórmula de la ecuación de segundo grado.

$$
m = \frac{-1 \pm \sqrt{1^2 - 4\cdot 1 \cdot(-2)}}{2\cdot 1} = \frac{-1 \pm \sqrt{1+8}}{2} = \frac{-1 \pm 3}{2}
$$

**Paso 4:** Se obtienen las dos raíces.

$$
m_1 = \frac{-1+3}{2} = 1, \qquad m_2 = \frac{-1-3}{2} = -2
$$

**Paso 5:** Como $m_1$ y $m_2$ son reales y distintas, las soluciones son $y_1 = e^{x}$ e $y_2 = e^{-2x}$ (linealmente independientes). La solución general es su combinación lineal.

$$
y = c_1\, e^{x} + c_2\, e^{-2x}
$$

</details>

</details>

## Caso 2: raíz doble (real) — [30:16](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1816s)

Cuando el **discriminante** de la ecuación característica es igual a cero, se obtiene una **raíz doble**:

$$
m = -\frac{p}{2}
$$

(en la fórmula general, $-b/2a$ con $b=p$ y $a=1$). En lugar de dos soluciones, se obtiene **una sola**: $y_1 = e^{mx} = e^{-\frac{p}{2}x}$. Falta la segunda solución.

Se propone como segunda solución una función con la misma forma que $y_1$ pero **multiplicada por $x$**:

$$
y_2 = x\, e^{m x}
$$

Estas son linealmente independientes, ya que su cociente $\dfrac{y_2}{y_1} = \dfrac{x\,e^{mx}}{e^{mx}} = x$ no es constante. La solución general es:

$$
y = c_1\, e^{m x} + c_2\, x\, e^{m x}
$$

La verificación de que $y_2 = x\,e^{mx}$ es solución (mostrada en el video entre [31:48](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=1908s) y [38:37](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2317s)):

<details>
<summary>Ver verificación de $y_2 = x\,e^{mx}$</summary>

**Paso 1:** Se calcula la derivada primera (regla del producto).

$$
y_2' = e^{m x} + x\, m\, e^{m x}
$$

**Paso 2:** Se calcula la derivada segunda.

$$
y_2'' = m\, e^{m x} + \left(m\, e^{m x} + x\, m^2 e^{m x}\right) = 2m\, e^{m x} + x\, m^2 e^{m x}
$$

**Paso 3:** Se reemplazan $y_2$, $y_2'$ e $y_2''$ en la ecuación $y'' + p\,y' + q\,y = 0$ y se saca factor común $e^{mx}$, separando los términos que tienen $x$ de los que no.

$$
e^{m x}\left[\, x\left(m^2 + p\, m + q\right) + \left(2m + p\right)\,\right] = 0
$$

**Paso 4:** El factor $e^{mx}$ nunca vale $0$. Los tres términos con $x$ se anulan porque $m$ es raíz (doble) de la ecuación característica: $m^2 + pm + q = 0$.

**Paso 5:** Queda por verificar $2m + p = 0$. Como $m = -\dfrac{p}{2}$ (raíz doble), al reemplazar:

$$
2\left(-\frac{p}{2}\right) + p = -p + p = 0
$$

**Paso 6:** Conclusión: $y_2 = x\,e^{mx}$ reemplazada en la ecuación la transforma en una identidad, por lo que es solución (y linealmente independiente de $y_1$).

</details>

<details>
<summary>📝 Ejercicio 6 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2317s">38:37</a>: solución general con raíz doble</summary>

Resolver la ecuación diferencial

$$
y'' - 4y' + 4y = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se identifica: EDO lineal de segundo orden, homogénea, con coeficientes constantes. Se plantea la ecuación característica.

$$
m^2 - 4m + 4 = 0
$$

**Paso 2:** Se resuelve (por ejemplo completando cuadrados): $(m-2)^2 = 0$, de donde se obtiene una **raíz doble**.

$$
m = 2
$$

**Paso 3:** Como es raíz doble, la solución general es la combinación lineal de $y_1 = e^{2x}$ e $y_2 = x\,e^{2x}$.

$$
y = c_1\, e^{2x} + c_2\, x\, e^{2x}
$$

</details>

</details>

## Caso 3: raíces complejas conjugadas — [39:43](https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2383s)

Cuando el **discriminante** de la ecuación característica es **negativo**, las raíces son **complejas conjugadas**. En este caso, la solución general tiene la forma:

$$
y_1 = e^{\alpha x}\cos(\beta x), \qquad y_2 = e^{\alpha x}\sin(\beta x)
$$

donde:

$$
\alpha = -\frac{p}{2}, \qquad \beta = \frac{\sqrt{4 - p^2}}{2}
$$

Como $p^2 - 4 < 0$, entonces $4 - p^2 > 0$ y $\beta$ es un número real positivo perfectamente determinado.

Estas dos funciones son linealmente independientes: su cociente es $\dfrac{y_2}{y_1} = \tan(\beta x)$, que no es constante. La solución general es:

$$
y = e^{\alpha x}\left[\, c_1 \cos(\beta x) + c_2 \sin(\beta x)\,\right]
$$

La demostración (por reemplazo de $y_1$ e $y_2$ en la ecuación) se muestra en el video: se calculan $y'$ e $y''$, se reemplazan en la ecuación, se saca factor común y, usando $\alpha = -p/2$ y la definición de $\beta$, se agrupan los coeficientes de $\sin(\beta x)$ y $\cos(\beta x)$, verificándose que toda la suma es cero. [paso en el pizarrón, ver video]

<details>
<summary>📝 Ejercicio 7 — <a href="https://www.youtube.com/watch?v=4HbBxQb8bpE&t=2704s">45:04</a>: solución general con raíces complejas conjugadas</summary>

Dada una EDO de segundo orden con coeficientes constantes cuya ecuación característica es

$$
m^2 + 2m + 5 = 0
$$

hallar la solución general.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Se resuelve la ecuación característica con la fórmula.

$$
m = \frac{-2 \pm \sqrt{2^2 - 4\cdot 1 \cdot 5}}{2} = \frac{-2 \pm \sqrt{4 - 20}}{2} = \frac{-2 \pm \sqrt{-16}}{2}
$$

**Paso 2:** Se distribuye el $2$ en cada término y se extrae $\sqrt{16}=4$ de la raíz, dejando $\sqrt{-1}$ dentro.

$$
m = -1 \pm \frac{4}{2}\sqrt{-1} = -1 \pm 2\sqrt{-1}
$$

**Paso 3:** Se identifican las partes.

$$
\alpha = -1, \qquad \beta = 2
$$

**Paso 4:** La solución general es la combinación lineal correspondiente al caso de raíces complejas conjugadas.

$$
y = e^{-x}\left[\, c_1 \cos(2x) + c_2 \sin(2x)\,\right]
$$

**Nota (aclaración del profesor):** $\beta$ es siempre el coeficiente **positivo** que multiplica a $x$ dentro de las funciones trigonométricas; la raíz $\sqrt{\cdot}$ se toma positiva porque $4 - p^2 > 0$.

</details>

</details>
