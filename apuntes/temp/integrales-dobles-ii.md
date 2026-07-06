# Integrales dobles II

> Fuente: https://www.youtube.com/watch?v=H4IQhAS0y9I

---

Claro, aquí tienes el análisis de la transcripción, estructurado como un apunte de estudio.

## Índice
- [00:09](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=9s) — Jacobiano de una Transformación
- [04:29](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=269s) — Teorema de Cambio de Variables para Integrales Dobles
- [29:25](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1765s) — Interpretación Geométrica del Jacobiano
- [32:02](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1922s) — Propiedad del Jacobiano de la Función Inversa
- [36:17](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=2177s) — Cambio en el Orden de Integración (Regiones Tipo I y II)

---

## [00:09](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=9s) Jacobiano de una Transformación

### [00:41](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=41s) Matriz Jacobiana
Dada una función de transformación de coordenadas $G(u,v) = (x(u,v), y(u,v))$, la matriz conformada por todas las derivadas parciales de las funciones componentes se denomina **Matriz Jacobiana**.

$$
\begin{pmatrix}
\frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\
\frac{\partial y}{\partial u} & \frac{\partial y}{\partial v}
\end{pmatrix}
$$

### [01:11](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=71s) Jacobiano
Se denomina **Jacobiano** al determinante de la Matriz Jacobiana. Se denota como $J(u,v)$ o $\frac{\partial(x,y)}{\partial(u,v)}$.

### Fórmulas Importantes

#### [01:42](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=102s) Transformación de Coordenadas Polares a Cartesianas
- $x = \rho \cos(\phi)$
- $y = \rho \sin(\phi)$

#### [03:55](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=235s) Jacobiano de la Transformación a Coordenadas Polares
El Jacobiano de la transformación de coordenadas polares a cartesianas es:
$$
J(\rho, \phi) = \rho
$$

## [04:29](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=269s) Teorema de Cambio de Variables para Integrales Dobles

Este teorema proporciona las herramientas para calcular integrales dobles mediante cambios de variables, análogo al método de sustitución para integrales simples.

### [05:02](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=302s) Hipótesis
- Sea $f(x,y)$ una función continua en una región de integración $D$.
- Sea $G(u,v) = (x,y)$ una función de transformación de coordenadas que mapea una región $D^*$ en el plano $uv$ a la región $D$ en el plano $xy$.
- La transformación $G$ debe ser **biyectiva** (admite función inversa $G^{-1}$).
- La transformación $G$ debe tener **derivadas parciales continuas**.
- El **Jacobiano** $J(u,v)$ de la transformación debe ser **distinto de cero** en el interior de la región $D^*$.
    - **Nota [35:47](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=2147s):** El Jacobiano puede ser cero en la frontera del conjunto de integración, pero no en su interior.

### [06:39](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=399s) Tesis
Bajo las hipótesis anteriores, la integral doble se puede calcular de la siguiente manera:
$$
\iint_D f(x,y) \,dx\,dy = \iint_{D^*} f(x(u,v), y(u,v)) \cdot |J(u,v)| \,du\,dv
$$
Donde $|J(u,v)|$ es el valor absoluto (módulo) del Jacobiano de la transformación.

## [29:25](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1765s) Interpretación Geométrica del Jacobiano

El módulo del Jacobiano actúa como un factor de corrección que relaciona las áreas de las regiones de integración antes y después de la transformación de coordenadas. Mide cómo la transformación deforma o escala los diferenciales de área.

- [30:59](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1859s) El módulo del Jacobiano corrige las áreas de las regiones de integración.
- Si la transformación es lineal, el Jacobiano es una constante. Si no es lineal, el Jacobiano es una función variable.

## [32:02](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1922s) Propiedad del Jacobiano de la Función Inversa

Si se conoce la transformación inversa $G^{-1}(x,y) = (u,v)$ en lugar de la transformación directa $G(u,v) = (x,y)$, el Jacobiano de la transformación directa se puede calcular como el inverso del Jacobiano de la transformación inversa.

- **Definición [32:35](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=1955s):** El Jacobiano de $G$ es igual a 1 dividido el Jacobiano de $G^{-1}$.
$$
J_G = \frac{\partial(x,y)}{\partial(u,v)} = \frac{1}{\frac{\partial(u,v)}{\partial(x,y)}} = \frac{1}{J_{G^{-1}}}
$$

## [36:17](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=2177s) Cambio en el Orden de Integración (Regiones Tipo I y II)

Es posible definir y calcular una integral doble permutando el orden de integración de las variables.

### [37:53](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=2273s) Tipos de Regiones de Integración

- **Región Tipo I:** La variable $x$ varía entre dos constantes y la variable $y$ varía entre dos funciones de $x$.
    - $a \le x \le b$
    - $g_1(x) \le y \le g_2(x)$
    - La integral se plantea como: $\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \,dy\,dx$

- **Región Tipo II:** La variable $y$ varía entre dos constantes y la variable $x$ varía entre dos funciones de $y$.
    - $c \le y \le d$
    - $h_1(y) \le x \le h_2(y)$
    - La integral se plantea como: $\int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) \,dx\,dy$

### [46:26](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=2786s) Teorema Principal (Consecuencia del Teorema de Fubini)

El orden de integración no altera el resultado de la integral doble, siempre que la función sea continua sobre la región de integración.
$$
\int_a^b \int_{g_1(x)}^{g_2(x)} f(x,y) \,dy\,dx = \int_c^d \int_{h_1(y)}^{h_2(y)} f(x,y) \,dx\,dy
$$
- **Nota [56:02](https://www.youtube.com/watch?v=H4IQhAS0y9I&t=3362s):** El orden en que se plantea la integración puede ser determinante en la posibilidad de resolver analíticamente una integral, ya que una de las integrales iteradas puede no tener una primitiva elemental.
