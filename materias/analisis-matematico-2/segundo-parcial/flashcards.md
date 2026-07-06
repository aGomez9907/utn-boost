# Flashcards teóricas — Segundo Parcial AM2

> **Cómo usarlas:** leé la pregunta, respondé en voz alta o por escrito (las demostraciones, ESCRIBILAS), y recién después desplegá la respuesta. Marcá las que fallan y volvé a ellas al final.

## 1. Campos conservativos y función potencial — aparece en el **100 %** de los parciales

### 1. [enunciado] ¿Cuándo un campo vectorial $\vec{F}$ es **conservativo**? Definí función potencial (primitiva).

<details><summary>Ver respuesta</summary>

$\vec{F}: A\subseteq\mathbb{R}^n \to \mathbb{R}^n$ es **conservativo** si existe un campo escalar $\varphi$ tal que su gradiente es el campo:

$$
\nabla\varphi = \vec{F}
$$

Esa $\varphi$ se llama **función primitiva o potencial** de $\vec{F}$.

Ejemplo: $\varphi(x,y)=xy$ es potencial de $\vec{F}=(y,x)$, porque $\nabla\varphi = (y,x) = \vec{F}$.

_Fuente: 10-campos-conservativos.md_

</details>

### 2. [enunciado] Teorema de las **tres proposiciones equivalentes** para un campo $\vec{F}$ continuo: enuncialas y decí la consecuencia práctica.

<details><summary>Ver respuesta</summary>

Si $\vec{F}$ es continuo, son **equivalentes** (o valen las tres o ninguna):

1. $\vec{F}$ es conservativo ($\vec{F} = \nabla\varphi$).
2. $\int_\lambda \vec{F}\cdot d\lambda = \varphi(B) - \varphi(A)$ para toda curva contenida en el dominio: la integral depende **solo de los extremos** (independencia del camino).
3. $\oint \vec{F}\cdot d\lambda = 0$ sobre **cualquier** curva cerrada contenida en el dominio.

**Consecuencia práctica:** una circulación cerrada $\neq 0$, o dos caminos con los mismos extremos e integrales distintas, prueban que $\vec{F}$ **no** es conservativo.

_Fuente: 10-campos-conservativos.md_

</details>

### 3. [demostración] **El T1 más tomado:** enunciá y demostrá la condición NECESARIA para que $\vec{F}=(f_1,f_2)$ admita función potencial. Indicá las hipótesis.

<details><summary>Ver respuesta</summary>

**Enunciado.** Hipótesis: $\vec{F}=(f_1,f_2)$ de clase $C^1$ y conservativo. Tesis:

$$
\frac{\partial f_1}{\partial y} = \frac{\partial f_2}{\partial x}
$$

**Demostración.**

**Paso 1:** $\vec{F}$ conservativo $\Rightarrow$ existe $\varphi$ con $\nabla\varphi=\vec{F}$, es decir $\dfrac{\partial\varphi}{\partial x}=f_1$ y $\dfrac{\partial\varphi}{\partial y}=f_2$.

**Paso 2:** derivar la primera respecto de $y$ y la segunda respecto de $x$:

$$
\frac{\partial^2\varphi}{\partial y\,\partial x} = \frac{\partial f_1}{\partial y}, \qquad \frac{\partial^2\varphi}{\partial x\,\partial y} = \frac{\partial f_2}{\partial x}
$$

**Paso 3:** como $\vec{F}\in C^1$, $\varphi\in C^2$, y por el **teorema de Schwarz** las derivadas cruzadas coinciden.

**Paso 4:** por lo tanto $\dfrac{\partial f_1}{\partial y} = \dfrac{\partial f_2}{\partial x}$. $\blacksquare$

Ojo: es solo **necesaria** — cumplirla NO garantiza que el campo sea conservativo (ver la carta del contraejemplo).

_Fuente: 10-campos-conservativos.md_

</details>

### 4. [enunciado] Condición SUFICIENTE para que $\vec{F}=(f_1,f_2)$ sea conservativo. ¿Vale el recíproco?

<details><summary>Ver respuesta</summary>

Si $\vec{F}\in C^1$, cumple la condición necesaria $\dfrac{\partial f_1}{\partial y}=\dfrac{\partial f_2}{\partial x}$ **y** su dominio es **simplemente conexo** (sin agujeros) $\Rightarrow$ $\vec{F}$ es conservativo.

**El recíproco NO vale:** un campo conservativo puede tener dominio no simplemente conexo. Ejemplo del apunte: $\vec{F} = \left(\dfrac{x}{\sqrt{x^2+y^2}},\ \dfrac{y}{\sqrt{x^2+y^2}}\right)$ con dominio $\mathbb{R}^2-\{(0,0)\}$ es conservativo (su potencial es $\sqrt{x^2+y^2}+C$).

_Fuente: 10-campos-conservativos.md_

</details>

### 5. [demostración] Demostrá que si $\vec{F}$ es conservativo con potencial $\varphi$, entonces $\int_{A\to B}\vec{F}\cdot d\lambda = \varphi(B)-\varphi(A)$ (T1 de 2022-11-24).

<details><summary>Ver respuesta</summary>

Sea $\lambda:[a,b]\to\mathbb{R}^n$ una curva $C^1$ contenida en el dominio, con $\lambda(a)=A$, $\lambda(b)=B$, y $\vec{F}=\nabla\varphi$.

**Paso 1:** definí $h(t) = \varphi(\lambda(t))$. Por **regla de la cadena**:

$$
h'(t) = \nabla\varphi(\lambda(t))\cdot\lambda'(t) = \vec{F}(\lambda(t))\cdot\lambda'(t)
$$

**Paso 2:** entonces la integral de línea es la integral de $h'$:

$$
\int_\lambda \vec{F}\cdot d\lambda = \int_a^b \vec{F}(\lambda(t))\cdot\lambda'(t)\,dt = \int_a^b h'(t)\,dt
$$

**Paso 3:** por **regla de Barrow**:

$$
= h(b) - h(a) = \varphi(\lambda(b)) - \varphi(\lambda(a)) = \varphi(B) - \varphi(A) \quad\blacksquare
$$

La integral no depende de la curva, solo de los extremos. *(En el apunte 10 es la Proposición 2 del teorema de equivalencia; esta es la demostración estándar: regla de la cadena + Barrow.)*

_Fuente: 10-campos-conservativos.md (Prop. 2)_

</details>

### 6. [método] Método práctico completo para decidir si $\vec{F}=(f_1,f_2)$ es conservativo (con y sin agujeros en el dominio).

<details><summary>Ver respuesta</summary>

**Paso 1 — condición necesaria:** ¿$\dfrac{\partial f_1}{\partial y} = \dfrac{\partial f_2}{\partial x}$? Si **no** $\Rightarrow$ no es conservativo, fin.

**Paso 2 — mirar el dominio** (si la condición se cumplió):

- Dominio **sin agujeros** (simplemente conexo) $\Rightarrow$ **ES conservativo** (sobre cualquier curva cerrada se aplica Green y el rotor es $0$).
- Dominio **con agujero** $\Rightarrow$ calcular la circulación sobre una curva cerrada que encierre el agujero (una circunferencia): si da $\neq 0$ $\Rightarrow$ NO es conservativo; si da $0$ $\Rightarrow$ SÍ lo es.

_Fuente: 10-campos-conservativos.md_

</details>

### 7. [enunciado] Contraejemplo clave: $\vec{F} = \left(\dfrac{-y}{x^2+y^2},\ \dfrac{x}{x^2+y^2}\right)$ en $\mathbb{R}^2-\{(0,0)\}$. ¿Cumple la condición necesaria? ¿Es conservativo?

<details><summary>Ver respuesta</summary>

**Cumple** la condición necesaria: ambas derivadas cruzadas dan $\dfrac{y^2-x^2}{(x^2+y^2)^2}$.

**Pero NO es conservativo:** sobre una circunferencia de radio $r$ centrada en el origen,

$$
\oint \vec{F}\cdot d\lambda = \int_0^{2\pi}(\sin^2 t + \cos^2 t)\,dt = 2\pi \neq 0
$$

**Moraleja de examen:** cuando el dominio tiene agujeros, la condición necesaria no alcanza — hay que chequear la circulación alrededor del agujero.

_Fuente: 10-campos-conservativos.md (Ej. 4)_

</details>

### 8. [método] **Método 1** para calcular la función potencial (ecuación diferencial total exacta): pasos.

<details><summary>Ver respuesta</summary>

Sabiendo que $\vec{F}=(f_1,f_2)$ es conservativo ($g'_x = f_1$, $g'_y = f_2$):

**Paso 1:** integrar $f_1$ respecto de $x$: $g = \int f_1\,dx + h(y)$ — la "constante" de integración es una **función de $y$**.

**Paso 2:** derivar esa $g$ respecto de $y$.

**Paso 3:** comparar con $f_2$ $\Rightarrow$ despejar $h'(y)$.

**Paso 4:** integrar $h'(y)$ para obtener $h(y)$. Resultado: $g(x,y) = \dots + C$.

**Verificación (recomendada en el examen):** calcular $\nabla g$ y comprobar que da $\vec{F}$.

_Fuente: 11-función-potencial.md_

</details>

### 9. [método] **Método 2** para calcular la función potencial (integral de línea): fórmula y limitación.

<details><summary>Ver respuesta</summary>

Por independencia del camino, se integra sobre el **segmento** $\vec{r}(t)=(tx,\,ty)$, $t\in[0,1]$, con $\vec{r}\,'(t)=(x,y)$:

$$
g(x,y) = \int_0^1 \vec{F}(tx,\,ty)\cdot(x,y)\,dt + C
$$

($C = g(0,0)$ queda como constante arbitraria).

**Limitación:** el segmento del origen a $(x,y)$ debe estar **incluido en el dominio** del campo. Si $(0,0)$ no pertenece al dominio (p. ej. dominio $\mathbb{R}^2-\{(0,0)\}$), este método con ese punto base **no se puede aplicar**.

_Fuente: 11-función-potencial.md_

</details>

### 10. [método] El clásico del parcial: «verificar que $\vec{F}$ es conservativo y calcular su potencial sabiendo que vale $k$ en el punto $P$». Pasos.

<details><summary>Ver respuesta</summary>

**Paso 1:** condición necesaria (y dominio simplemente conexo, típicamente $\mathbb{R}^2$) $\Rightarrow$ conservativo.

**Paso 2:** potencial genérico $\varphi(x,y)+C$ por el método 1 (o el 2).

**Paso 3:** imponer $\varphi(P)=k$ $\Rightarrow$ despejar $C$.

**Paso 4:** escribir el potencial final (y evaluarlo en otro punto si lo piden).

Con esta mecánica exacta cae en **2015-11-25, 2019-11-21, 2022-07-15 y 2022-11-24**.

_Fuente: 10/11 + banco del INDICE_

</details>

## 2. Integrales múltiples, curvas y superficies — núcleo de P1 (**92 %**)

### 11. [fórmula] Coordenadas cilíndricas: escribí la transformación completa, el rango de cada variable y su jacobiano.

<details><summary>Ver respuesta</summary>

Combinan polares en el plano $xy$ con la altura $z$ sin cambios:

$$x = \rho\cos\varphi, \quad y = \rho\sin\varphi, \quad z = z$$

con $\rho \ge 0$ y $\varphi \in [0, 2\pi]$.

**Jacobiano:**

$$J = \rho, \qquad |J| = \rho$$

(se obtiene desarrollando el determinante $3\times 3$ por la columna de $z$, que tiene muchos ceros; equivale al jacobiano de las polares).

**Cuándo usarlas:** simetría respecto del eje $z$ (aparece $x^2+y^2$ en la región o el integrando). Al transformar: $x^2+y^2 = \rho^2$ y $\sqrt{x^2+y^2} = \rho$ (pues $\rho \ge 0$).

_Fuente: 04-integrales-triples-i.md_

</details>

### 12. [fórmula] Coordenadas esféricas (versión de la cátedra, con $\theta$ medido desde el plano $xy$): transformación completa, rangos y jacobiano. ¿Cuánto vale $|J|$ y por qué se pueden sacar las barras de módulo?

<details><summary>Ver respuesta</summary>

- $\rho$: distancia del punto al origen, $\rho \ge 0$.
- $\theta$: ángulo del segmento con el **plano $xy$**, $\theta \in \left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$ (positivo por encima del plano).
- $\varphi$: ángulo de la proyección sobre el plano $xy$ con el eje $x$, $\varphi \in [0, 2\pi]$.

$$x = \rho\cos\theta\cos\varphi, \quad y = \rho\cos\theta\sin\varphi, \quad z = \rho\sin\theta$$

**Jacobiano** (recordarlo de memoria):

$$J = -\rho^2\cos\theta \qquad\Rightarrow\qquad |J| = \rho^2\cos\theta$$

porque $\rho^2 \ge 0$ siempre y $\cos\theta \ge 0$ al ser $\theta \in \left[-\frac{\pi}{2},\frac{\pi}{2}\right]$.

**Chequeo clásico:** volumen de la esfera de radio $R$: $\rho\in[0,R]$, $\theta\in[-\frac{\pi}{2},\frac{\pi}{2}]$, $\varphi\in[0,2\pi]$ da $2\pi \cdot 2 \cdot \frac{R^3}{3} = \frac{4}{3}\pi R^3$.

_Fuente: 04-integrales-triples-i.md_

</details>

### 13. [fórmula] ¿Cómo se calcula un volumen (a) con una integral doble y (b) con una integral triple? ¿Cuándo vale la interpretación como volumen en el caso doble?

<details><summary>Ver respuesta</summary>

**(a) Con integral doble:** si la gráfica de $f$ es **positiva** (está por encima del plano $xy$), $\iint_D f\,dA$ es el volumen del sólido entre $z=f(x,y)$ y el plano $xy$ sobre $D$. Entre dos gráficas (la de arriba menos la de abajo):

$$V = \iint_D (f_2 - f_1)\,dA$$

⚠️ Solo vale si $f$ está por encima del plano $xy$; si toma valores positivos y negativos, se compensan y ya no representa un volumen.

**(b) Con integral triple:** integrar la **función unitaria** sobre la región $E$:

$$V_E = \iiint_E 1\,dV = \iint_D \left[h_2(x,y) - h_1(x,y)\right] dA$$

(la integral interior en $z$ da techo menos piso). No confundir el volumen de la región con la integral de una función sobre esa región: solo coinciden cuando la función es la unitaria.

_Fuente: 04-integrales-triples-i.md_

</details>

### 14. [fórmula] Masa de un cuerpo $\Omega$ con densidad $\delta(x,y,z)$: fórmula y pasos típicos de resolución (caso con simetría respecto del eje $z$).

<details><summary>Ver respuesta</summary>

El diferencial de masa es $dm = \delta\,dx\,dy\,dz$, y la masa es la integral triple de la densidad sobre todo el cuerpo:

$$m_\Omega = \iiint_{\Omega} \delta\,dx\,dy\,dz$$

**Método típico** (ej.: $x^2+y^2\le 9$, $0\le z\le 16-x^2-y^2$, $\delta = k\sqrt{x^2+y^2}$):
1. Por la simetría respecto del eje $z$ usar **cilíndricas** con $|J| = \rho$.
2. Transformar región: $\rho \le 3$, $0 \le z \le 16-\rho^2$, $\varphi\in[0,2\pi]$; y densidad: $\delta = k\rho$.
3. Integrar primero en $z$ (da techo menos piso), luego la integral en $\varphi$ aporta $2\pi$ si el integrando no depende de $\varphi$:

$$m = \int_0^{2\pi}\!\!\int_0^3\!\!\int_0^{16-\rho^2} (k\rho)\cdot\rho\,dz\,d\rho\,d\varphi = \frac{954}{5}\pi k$$

**No olvidar:** densidad **por** jacobiano en el integrando.

_Fuente: 04-integrales-triples-i.md_

</details>

### 15. [fórmula] ¿Cómo se expresan el área de una región plana $D$ y la masa de una placa con densidad $\delta(x,y)$ como integrales dobles?

<details><summary>Ver respuesta</summary>

**Área:** integral doble de la función unitaria sobre $D$:

$$\text{Área}(D) = \iint_D 1\,dA = \int_a^b \big(h(x) - g(x)\big)\,dx$$

(la integral interior de $1\,dy$ da $h(x)-g(x)$, y se recupera el área entre dos curvas de Análisis I).

**Masa de una placa plana** con densidad $\delta(x,y)$:

$$m = \iint_D \delta(x,y)\,dx\,dy$$

Si $\delta = 1$ la integral da el área; si no, la masa. Con densidad, los momentos estáticos y baricentros se redefinen agregando $\delta$ en el integrando, y en el baricentro el denominador pasa de ser el área $A_D$ a ser la masa $m$.

_Fuente: 01-integrales-dobles-i.md_

</details>

### 16. [fórmula] Momentos estáticos $M_x$, $M_y$ de una región plana $D$ y coordenadas del baricentro $(x_G, y_G)$. ¡Ojo con cuál momento va en cada coordenada!

<details><summary>Ver respuesta</summary>

**Momentos estáticos (primer orden):**

$$M_x = \iint_D y\,dx\,dy \qquad M_y = \iint_D x\,dx\,dy$$

(respecto al eje $x$ se integra $y$, y viceversa).

**Baricentro** (cada coordenada usa el momento respecto del eje *contrario*):

$$x_G = \frac{M_y}{A_D} = \frac{\iint_D x\,dx\,dy}{A_D} \qquad y_G = \frac{M_x}{A_D} = \frac{\iint_D y\,dx\,dy}{A_D}$$

**Atajos que ahorran cuentas:**
- Si la región es simétrica respecto de un eje, el integrando antisimétrico da integral $0$ (ej.: semicírculo simétrico respecto del eje $y$ ⟹ $x_G = 0$).
- El momento estático respecto de un eje **baricéntrico** vale $0$ ($M_x = y_G\cdot A_D = 0$).
- Resultados de referencia: triángulo rectángulo: baricentro a $\frac{b}{3}$ y $\frac{h}{3}$ de los catetos; semicírculo: $y_G = \frac{4R}{3\pi}$.

_Fuente: 03-integrales-dobles-iii.md_

</details>

### 17. [fórmula] Momentos estáticos de un cuerpo respecto a los planos coordenados y coordenadas del centro de masa $(x_c, y_c, z_c)$.

<details><summary>Ver respuesta</summary>

**Momentos estáticos respecto a los planos coordenados** (distancia al plano por densidad):

$$M_{x=0} = \iiint_{\Omega} x\,\delta\,dx\,dy\,dz, \quad M_{y=0} = \iiint_{\Omega} y\,\delta\,dx\,dy\,dz, \quad M_{z=0} = \iiint_{\Omega} z\,\delta\,dx\,dy\,dz$$

**Centro de masa** (momento sobre masa):

$$x_c = \frac{M_{x=0}}{m_\Omega}, \qquad y_c = \frac{M_{y=0}}{m_\Omega}, \qquad z_c = \frac{M_{z=0}}{m_\Omega}$$

con $m_\Omega = \iiint_\Omega \delta\,dx\,dy\,dz$.

**Atajo:** si $\Omega$ es simétrico respecto de un plano y el integrando es antisimétrico, la integral vale $0$ (ej.: paraboloide $z = 1-x^2-y^2$ sobre $z=0$ ⟹ $M_{x=0} = M_{y=0} = 0$ y el centro de masa queda sobre el eje $z$: $(0, 0, \frac{1}{3})$).

_Fuente: 05-integrales-triples-ii.md_

</details>

### 18. [fórmula] Área de una superficie simple: fórmula para una parametrización $\sigma(u,v)$ y fórmula cuando la superficie es la gráfica de $z(x,y)$ definida implícitamente por $g(x,y,z)=0$. ¿Qué requisito tiene la segunda?

<details><summary>Ver respuesta</summary>

**Caso paramétrico:**

$$A = \iint_{D} \left\| \sigma'_u \times \sigma'_v \right\| du\,dv$$

donde $\sigma'_u \times \sigma'_v = \vec{N}$ es normal a la superficie y su norma es el área del paralelogramo tangente: $d\sigma = \|\sigma'_u \times \sigma'_v\|\,du\,dv$. El área **no depende de la parametrización**.

**Caso gráfica / conjunto de nivel $g(x,y,z)=0$:**

$$A = \iint_{D} \frac{\left\| \nabla g \right\|}{\left| g'_z \right|} dx\,dy$$

con $D$ la proyección sobre el plano $xy$. Sale de que para $\sigma = (x, y, z(x,y))$: $\sigma'_x \times \sigma'_y = (-z'_x, -z'_y, 1)$ y, por función implícita, $z'_x = -\frac{g'_x}{g'_z}$, $z'_y = -\frac{g'_y}{g'_z}$.

**Requisito:** la superficie debe verse realmente como gráfica de una función $z(x,y)$ con $g'_z \ne 0$ (no sirve para la esfera completa: para un mismo $(x,y)$ habría dos imágenes; se calcula media y se multiplica por 2).

**Referencia:** esfera de radio $r$: $\|\sigma'_\theta \times \sigma'_\varphi\| = r^2\cos\theta$ y $A = 4\pi r^2$.

_Fuente: 12-área-de-una-superficie.md_

</details>

### 19. [fórmula] Masa de una chapa: ¿cómo se integra un campo escalar $f$ sobre una superficie $S$ (forma paramétrica y forma de gráfica)? ¿Y el valor medio?

<details><summary>Ver respuesta</summary>

**Forma paramétrica** (campo evaluado en la superficie por diferencial de área):

$$\iint_S f\,dS = \iint_V f(\sigma(u,v))\,\left\| \sigma'_u \times \sigma'_v \right\| du\,dv$$

**Superficie dada como conjunto de nivel** $g(x,y,z)=0$ (gráfica de $z(x,y)$):

$$\iint_S f\,dS = \iint_R f(x, y, z(x,y))\,\frac{\left\| \nabla g \right\|}{\left| g'_z \right|}\,dx\,dy$$

con $R$ la proyección sobre el plano $xy$. El resultado **no depende de la parametrización**.

**Valor medio:**

$$f_{\text{medio}} = \frac{\iint_S f\,dS}{\text{Área}(S)}$$

**Referencia** (masa de la semiesfera de radio $r$ con $f = kz$): en esféricas $f(\sigma) = kr\sin\theta$, diferencial $r^2\cos\theta$, y da $k\pi r^3$ por cualquiera de los dos caminos.

_Fuente: 13-masa-de-una-chapa.md_

</details>

### 20. [fórmula] Integral de un campo vectorial $\vec{F}$ a lo largo de una curva $C$ parametrizada por $\lambda(t)$, $t\in[a,b]$: definición, cómo se reduce a integral simple y notación diferencial.

<details><summary>Ver respuesta</summary>

**Definición:**

$$\int_C \vec{F} \cdot d\vec{\lambda} = \int_a^b \vec{F}(\lambda(t)) \cdot \lambda'(t)\,dt$$

Si la curva es **cerrada** se escribe $\oint_C \vec{F}\cdot d\vec{\lambda}$ y se llama **circulación**. Físicamente es el **trabajo** del campo de fuerza: $dW = (\vec{F}\cdot\breve{T})\,d\lambda = \vec{F}(\lambda(t))\cdot\lambda'(t)\,dt$.

**Reducción a integral simple** — pasos:
1. Derivar la parametrización: $\lambda'(t)$.
2. Evaluar el campo en los puntos de la curva: $\vec{F}(\lambda(t))$.
3. Hacer el producto escalar → función de una sola variable.
4. Integrar respecto de $t$ entre $a$ y $b$.

**Notación diferencial** (curva gráfica de $y=f(x)$, con $\lambda(x)=(x,f(x))$ y $y'dx = dy$):

$$\int_C f_1\,dx + f_2\,dy$$

⚠️ El resultado depende de la **curva** (no solo de los extremos) y de la **orientación**.

_Fuente: 08-trabajo-de-un-campo-vectorial.md_

</details>

### 21. [método] ¿Cómo se determina el sentido de recorrido de una curva parametrizada y cómo se invierte? ¿Qué le pasa a la integral del campo al invertir la orientación?

<details><summary>Ver respuesta</summary>

**Determinar el sentido (2 formas):**
1. **Asignar valores crecientes** a la variable y ver cómo se desplaza el punto. Ej.: en $\beta(t) = (r\cos t, r\sin t)$, en $t=0$ el punto es $(r,0)$ y en $t=\pi/2$ es $(0,r)$ → recorrido **antihorario**.
2. **Analizar el vector velocidad** $\lambda'(t)$: apunta en la dirección del movimiento; ubicándolo en un punto de la curva se ve hacia dónde avanza.

**Invertir la parametrización:**
- Sustituir la variable: en $[0,1]$, reemplazar $t = 1-s$ (las imágenes se recorren en orden inverso).
- En la circunferencia: **cambiar el signo de la coordenada $y$**: $\gamma(t) = (r\cos t, -r\sin t)$ → sentido horario.

**Efecto en la integral (teorema de reparametrización):** si la reparametrización conserva la orientación, la integral es **igual**; si la invierte, la integral tiene el **signo opuesto** (mismo valor absoluto). Ej.: la parábola de $(0,0)$ a $(1,1)$ con $\vec{F}=(1,x)$ da $\frac{5}{3}$; recorrida al revés da $-\frac{5}{3}$.

_Fuente: 08-trabajo-de-un-campo-vectorial.md_

</details>

### 22. [fórmula] Longitud de una curva simple parametrizada por $\lambda(t)$, $t\in[a,b]$: fórmula (la única a retener de este apunte).

<details><summary>Ver respuesta</summary>

$$L = \int_a^b \left\| \lambda'(t) \right\| dt$$

Es la integral de la **norma de la derivada** de la parametrización entre los extremos del intervalo del parámetro. El diferencial de longitud es $d\lambda = \|\lambda'(t)\|\,dt$, y el resultado no depende de la parametrización.

**Chequeo:** circunferencia $\lambda(t) = (r\cos t, r\sin t)$, $t\in[0,2\pi]$: $\lambda'(t) = (-r\sin t, r\cos t)$, $\|\lambda'\| = r$ y $L = 2\pi r$.

_Fuente: 06-longitud-de-una-curva.md_

</details>

### 23. [enunciado] Enunciá el teorema de cambio de variables para integrales triples: hipótesis sobre la transformación $g$ y tesis.

<details><summary>Ver respuesta</summary>

**Hipótesis:** $g$ es una transformación de coordenadas del conjunto $E^*$ (en las variables $u,v,w$) al conjunto $E$ (en $x,y,z$) tal que, en el **interior** de $E^*$:
- $g$ es **inyectiva** (a puntos distintos les corresponden imágenes distintas),
- $g$ es de **clase $C^1$** (las tres componentes con derivadas parciales continuas),
- el **jacobiano no se anula**, donde

$$J = \frac{\partial(x,y,z)}{\partial(u,v,w)} = \det \begin{pmatrix} x'_u & x'_v & x'_w \\ y'_u & y'_v & y'_w \\ z'_u & z'_v & z'_w \end{pmatrix}$$

**Tesis:**

$$\iiint_E f(x,y,z)\,dx\,dy\,dz = \iiint_{E^*} f\big(g(u,v,w)\big)\,|J|\,du\,dv\,dw$$

Es el mismo teorema de las integrales dobles agregando una variable. ⚠️ En la integral va el **módulo** del jacobiano.

_Fuente: 04-integrales-triples-i.md_

</details>

### 24. [fórmula] Valor medio de una función sobre una región del plano ($D$) y sobre una región del espacio ($E$).

<details><summary>Ver respuesta</summary>

**En el plano** (integrales dobles):

$$\bar{f} = \frac{\iint_D f\,dA}{\text{Área}(D)} = \frac{\iint_D f\,dA}{\iint_D 1\,dA}$$

**En el espacio** (integrales triples):

$$\bar{f} = \frac{\iiint_E f\,dV}{\iiint_E 1\,dV} = \frac{1}{V_E}\iiint_E f\,dV$$

Equivalentemente $\iiint_E f\,dV = \bar{f}\cdot V_E$: sirve como verificación rápida (ej.: función lineal sobre un cuadrado → valor medio en el centro por el área).

_Fuente: 04-integrales-triples-i.md_

</details>

## 3. Flujo, divergencia y Stokes — núcleo de P3 (**85 %**)

### 25. [enunciado] Enunciá formalmente el **Teorema de la Divergencia (Gauss)**, con hipótesis y tesis.

<details><summary>Ver respuesta</summary>

**Hipótesis:**
- $\vec{F}: A \subseteq \mathbb{R}^3 \to \mathbb{R}^3$ campo vectorial de **clase $C^1$** (cada función componente tiene derivadas parciales continuas respecto de las tres variables).
- $\Omega$ es una **región simple del espacio**, incluida dentro del dominio del campo (se puede evaluar $\vec{F}$ en cualquier punto de la región).
- $\partial\Omega$ es la superficie frontera de $\Omega$ (superficie simple y orientable por partes, cerrada), **orientada en forma positiva**: normales hacia el exterior.

**Tesis:** el flujo del campo a través de la frontera cerrada es igual a la integral triple de la divergencia sobre la región:
$$\oiint_{\partial\Omega} \vec{F} \cdot d\vec{S} = \iiint_{\Omega} \operatorname{div}\vec{F}\,dx\,dy\,dz$$

Relaciona una integral de superficie (flujo por superficie cerrada) con una integral triple.

_Fuente: 15-divergencia.md_

</details>

### 26. [enunciado] Enunciá el **Teorema del rotor (Stokes)**, con hipótesis y tesis.

<details><summary>Ver respuesta</summary>

**Hipótesis:**
- $\vec{F}$ campo vectorial de (un subconjunto de) $\mathbb{R}^3 \to \mathbb{R}^3$, de **clase $C^1$** (todas sus derivadas parciales continuas).
- $S$ superficie **simple y orientable** incluida en el dominio del campo, con parametrización $\sigma$ (sobre una región $D$ del plano) tal que el **borde de $S$ es una curva regular y simple**.
- El **borde de $S$ orientado en correspondencia** con el campo de versores normales $\vec{n}$: caminando con la cabeza en la dirección de $\vec{n}$ y dejando la superficie a la izquierda.

**Tesis:** la circulación (trabajo) de $\vec{F}$ a lo largo del borde de $S$ es igual al **flujo del rotor** de $\vec{F}$ a través de $S$:
$$\oint_{\partial S} \vec{F} \cdot d\vec{r} = \iint_{S} \operatorname{rot}\vec{F} \cdot d\vec{S}$$

_Fuente: 16-rotor-en-el-espacio.md_

</details>

### 27. [fórmula] ¿Cómo se define el **flujo de un campo vectorial $\vec{F}$ a través de una superficie $S$** parametrizada por $\sigma$? (fórmula con el producto vectorial fundamental)

<details><summary>Ver respuesta</summary>

Sea $\vec{F}$ definido en $A \subseteq \mathbb{R}^3$ y $S$ una superficie simple y orientable (por partes) parametrizada por $\sigma: D \subseteq \mathbb{R}^2 \to \mathbb{R}^3$, **incluida en el dominio del campo**:
$$\iint_S \vec{F} \cdot d\vec{S} = \iint_D \vec{F}(\sigma(u,v)) \cdot \left( \sigma'_u \times \sigma'_v \right) du\,dv$$

Es la integral doble sobre $D$ del campo **evaluado en los puntos de la superficie**, producto escalar con el **producto vectorial de las derivadas parciales** de la parametrización ($\sigma'_u \times \sigma'_v$ = vector normal a $S$, no nulo si $S$ es regular).

Interpretación física: si $\vec{F}$ es el campo de velocidades de un fluido, el flujo es el **caudal** ($\vec{F}\cdot\check{n}\,dS$ con $dS = \|\sigma'_u \times \sigma'_v\|\,du\,dv$; las normas se cancelan). Si $S$ es cerrada se puede agregar un circulito al signo integral, pero la integral es la misma.

_Fuente: 14-flujo.md_

</details>

### 28. [fórmula] Definí la **divergencia** de un campo vectorial $\vec{F} = (f_1, f_2, f_3)$. ¿Qué tipo de objeto resulta?

<details><summary>Ver respuesta</summary>

$$\operatorname{div}\vec{F} = \frac{\partial f_1}{\partial x} + \frac{\partial f_2}{\partial y} + \frac{\partial f_3}{\partial z}$$

Se interpreta como el **producto escalar del operador nabla** con el campo:
$$\operatorname{div}\vec{F} = \nabla \cdot \vec{F} = \left( \frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z} \right) \cdot (f_1, f_2, f_3)$$

La divergencia de un campo vectorial **siempre resulta un campo escalar**: a cada punto del espacio le corresponde un número real.

Ejemplos: $\vec{F}=(x,y,z) \Rightarrow \operatorname{div}\vec{F} = 1+1+1 = 3$ (constante); $\vec{F}=(x^3,y^3,z^3) \Rightarrow \operatorname{div}\vec{F} = 3(x^2+y^2+z^2)$.

_Fuente: 15-divergencia.md_

</details>

### 29. [fórmula] ¿Cómo se calcula el **rotor** de $\vec{F} = (f_1, f_2, f_3)$ con la regla del determinante? Escribí el determinante y el vector resultante.

<details><summary>Ver respuesta</summary>

El rotor es el **producto vectorial del operador nabla con el campo**; se resuelve con un determinante (nabla en el segundo renglón, componentes del campo en el tercero):
$$\operatorname{rot}\vec{F} = \nabla \times \vec{F} = \begin{vmatrix} \vec{i} & \vec{j} & \vec{k} \\ \dfrac{\partial}{\partial x} & \dfrac{\partial}{\partial y} & \dfrac{\partial}{\partial z} \\ f_1 & f_2 & f_3 \end{vmatrix}$$

$$\operatorname{rot}\vec{F} = \left( \frac{\partial f_3}{\partial y} - \frac{\partial f_2}{\partial z},\; \frac{\partial f_1}{\partial z} - \frac{\partial f_3}{\partial x},\; \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y} \right)$$

Si $\operatorname{rot}\vec{F} = (0,0,0)$ el campo se llama **irrotacional**. Ejemplo: $\vec{F} = (-y, x, 0) \Rightarrow \operatorname{rot}\vec{F} = (0, 0, 2)$.

_Fuente: 16-rotor-en-el-espacio.md_

</details>

### 30. [método] ¿Cómo se calcula el flujo cuando la superficie viene dada por una **ecuación cartesiana** $g(x,y,z) = 0$ (con $z$ dependiente de $x,y$)? ¿Cuándo NO sirve esta fórmula?

<details><summary>Ver respuesta</summary>

Si la superficie es el conjunto de nivel cero de $g$ y una variable depende de las otras dos (p. ej. $z = z(x,y)$, cumpliendo el teorema de la función implícita):
$$\iint_S \vec{F} \cdot d\vec{S} = \iint_{D_{xy}} \vec{F} \cdot \frac{\nabla g}{\left| g'_z \right|}\, dx\, dy$$

donde $\vec{F}$ se **evalúa en los puntos de la superficie** (reemplazando $z$ en términos de $x,y$) y $D_{xy}$ es la **proyección** de la superficie al plano $xy$.

Ojo: a diferencia de campos escalares/áreas, NO se usa la norma del gradiente sino **el gradiente directamente** ($\nabla g$ es un vector normal; su sentido fija la orientación).

**Restricción:** una variable debe depender de las otras dos. **No sirve** para una esfera completa: a un mismo $(x,y)$ le corresponderían dos imágenes (una arriba y otra abajo del plano $xy$).

Ejemplo (paraboloide $z = x^2+y^2$, $z\le 1$): $g = z - x^2 - y^2$, $\nabla g = (-2x, -2y, 1)$, $g'_z = 1$, se integra sobre $x^2+y^2 \le 1$ pasando a polares.

_Fuente: 14-flujo.md_

</details>

### 31. [método] ¿Qué es un campo **solenoidal**? ¿Cómo se resuelve "hallar $g$ para que $\vec{F}$ sea solenoidal"?

<details><summary>Ver respuesta</summary>

Un campo es **solenoidal** cuando su divergencia vale **cero en cualquier punto** del espacio:
$$\operatorname{div}\vec{F} = 0$$

En campos de velocidades de líquidos, divergencia cero se dice que el campo es **incompresible**. Ejemplo clave del apunte: el campo radial $\vec{F} = c\,\dfrac{(x,y,z)}{(x^2+y^2+z^2)^{3/2}}$ tiene $\operatorname{div}\vec{F} = 0$ en todo su dominio ($\mathbb{R}^3 - \{(0,0,0)\}$).

**Método para "hallar $g$"** (ej.: $\vec{F} = (f_1, f_2, g)$):

1. Plantear $\operatorname{div}\vec{F} = \frac{\partial f_1}{\partial x} + \frac{\partial f_2}{\partial y} + \frac{\partial g}{\partial z} = 0$.
2. Despejar $\frac{\partial g}{\partial z} = -\left(\frac{\partial f_1}{\partial x} + \frac{\partial f_2}{\partial y}\right)$.
3. Integrar respecto de la variable correspondiente para obtener $g$ (aparece una "constante" de integración que puede depender de las otras variables).

_Fuente: 15-divergencia.md_

</details>

### 32. [enunciado] ¿Cómo depende el flujo de la **orientación** de la superficie? ¿Qué dice la **regla de la mano derecha** para el borde?

<details><summary>Ver respuesta</summary>

**Propiedad (dependencia con la orientación):**
- Si dos parametrizaciones $\sigma$ y $\tau$ de la misma superficie tienen la **misma orientación** (versores normales en la misma dirección), el flujo da **exactamente lo mismo**.
- Si una parametrización **invierte la orientación**, el flujo da **igual en valor absoluto pero con signo opuesto**.

**Signo físico:** si el fluido va en la dirección del normal, caudal **positivo**; en sentido opuesto, **negativo**. En superficies **cerradas**: flujo positivo $\Rightarrow$ sale más de lo que entra (**fuente** adentro); flujo negativo $\Rightarrow$ entra más de lo que sale (**sumidero**).

**Regla de la mano derecha:** agarrando con la mano derecha el vector normal con el **pulgar apuntando en la dirección de la flecha**, los otros cuatro dedos indican la orientación del **borde** de la superficie correspondiente a ese campo de versores normales.

$S$ es **orientable** si su campo de versores normales $\check{n} = \dfrac{\sigma'_u \times \sigma'_v}{\|\sigma'_u \times \sigma'_v\|}$ es **continuo** sobre la superficie (quedan definidas dos orientaciones posibles).

_Fuente: 14-flujo.md_

</details>

### 33. [método] ¿Cuándo conviene calcular un flujo con el **Teorema de la Divergencia** y cuándo por **definición** (flujo directo)?

<details><summary>Ver respuesta</summary>

**Conviene Gauss cuando:**
- La superficie es **cerrada** (frontera de una región simple $\Omega$) y está orientada con normales al exterior — o se puede cerrar fácilmente.
- La frontera tiene **varias caras** (ej. tetraedro: 4 trozos de plano): calcular el flujo cara por cara y sumar es laborioso; con Gauss es una sola integral triple.
- La **divergencia es simple** (constante o factorizable). Si $\operatorname{div}\vec{F} = c$ constante: $\oiint_{\partial\Omega} \vec{F}\cdot d\vec{S} = c \cdot V_\Omega$ (constante por volumen). Ej.: $\vec{F}=(x,y,z)$ por el tetraedro de $x+y+z=1$ en el primer octante: $3 \cdot \frac{1}{6} = \frac{1}{2}$.
- La región y el integrando sugieren esféricas/cilíndricas (ej. $\vec{F}=(x^3,y^3,z^3)$ por esfera de radio $R$: $\operatorname{div} = 3(x^2+y^2+z^2) = 3\rho^2$, resultado $\frac{12}{5}\pi R^5$).

**Flujo directo (definición) cuando:**
- La superficie es **abierta** (no encierra región) y no conviene cerrarla.
- El campo **no está definido en algún punto interior** de la región (ej. carga en el origen): Gauss no se puede aplicar directamente sobre esa región.

_Fuente: 15-divergencia.md_

</details>

### 34. [demostración] **Teorema de Gauss para una carga puntual:** demostrá que para $\vec{F} = k\,\dfrac{(x,y,z)}{\|(x,y,z)\|^3}$ el flujo por $\partial\Omega$ vale $0$ si el origen no está en $\Omega$, y $4k\pi$ si está.

<details><summary>Ver respuesta</summary>

Datos previos: el dominio del campo es $\mathbb{R}^3 - \{(0,0,0)\}$ y $\operatorname{div}\vec{F} = 0$ en todo el dominio.

**Paso 1 (Caso $(0,0,0) \notin \Omega_1$):** el campo está definido en toda $\Omega_1$, se aplica el teorema de la divergencia directamente:
$$\oiint_{\partial\Omega_1} \vec{F}\cdot d\vec{S} = \iiint_{\Omega_1} \operatorname{div}\vec{F}\,dx\,dy\,dz = \iiint_{\Omega_1} 0 = 0$$

**Paso 2 (Caso $(0,0,0) \in \Omega_2$):** no se puede aplicar Gauss directamente (el campo no está definido en el origen). Se toma una superficie esférica $S$ centrada en el origen, contenida en $\Omega_2$, y la región $\Omega_3$ entre $\partial\Omega_2$ y la esfera ("durazno sin carozo"). Su frontera es $\partial\Omega_2 \cup S$.

**Paso 3:** Orientando $\partial\Omega_3$ positivamente: en $\partial\Omega_2$ los normales apuntan hacia afuera y en $S$ **hacia el origen**. El flujo se descompone:
$$\oiint_{\partial\Omega_3} \vec{F}\cdot d\vec{S} = \oiint_{\partial\Omega_2} \vec{F}\cdot d\vec{S} + \iint_{S} \vec{F}\cdot d\vec{S}$$

**Paso 4:** El flujo por la esfera con normal hacia el origen ya se calculó (apunte 14, Ej. 3): vale $-4k\pi$.

**Paso 5:** En $\Omega_3$ sí vale Gauss (esquiva al origen) y $\operatorname{div}\vec{F}=0$:
$$\oiint_{\partial\Omega_3} \vec{F}\cdot d\vec{S} = \iiint_{\Omega_3} 0 = 0$$

**Paso 6:** Entonces $0 = \oiint_{\partial\Omega_2} \vec{F}\cdot d\vec{S} - 4k\pi$, de donde:
$$\oiint_{\partial\Omega_2} \vec{F}\cdot d\vec{S} = 4k\pi$$
independiente de la **forma** de la superficie que encierra la carga.

_Fuente: 15-divergencia.md_

</details>

### 35. [enunciado] Definí **región simple del espacio** y **orientación positiva de su frontera** (las hipótesis geométricas del Teorema de la Divergencia).

<details><summary>Ver respuesta</summary>

**Región simple del espacio** ($\mathbb{R}^3$): región de integración del espacio tridimensional (donde se podrían resolver integrales triples) encerrada por superficies, de manera tal que toda su frontera es una **superficie simple y orientable por partes**. Imagen: un dado — sólido macizo cuyas seis caras, unidas, forman la superficie que lo encierra.

**Orientación positiva de la frontera:** la superficie que envuelve a la región está orientada en forma positiva si sus vectores normales apuntan **hacia el exterior** de la región.

**Superficie simple y orientable por partes:** varias superficies simples y orientables **pegadas en sus bordes**; las orientaciones son coherentes cuando en la curva de unión de dos piezas las orientaciones inducidas en los bordes son **opuestas** (ej. dado: los seis normales todos hacia el exterior, o todos hacia el interior).

_Fuente: 15-divergencia.md_

</details>

### 36. [demostración] Demostrá que si $\vec{F}$ es **conservativo** entonces es **irrotacional**, y que su circulación sobre el borde de una superficie que cumple las hipótesis de Stokes es $0$. ¿Vale el recíproco?

<details><summary>Ver respuesta</summary>

**Paso 1:** Si $\vec{F} = (f_1, f_2, f_3)$ es conservativo, las derivadas cruzadas de sus componentes coinciden:
$$\frac{\partial f_2}{\partial x} = \frac{\partial f_1}{\partial y}, \quad \frac{\partial f_1}{\partial z} = \frac{\partial f_3}{\partial x}, \quad \frac{\partial f_2}{\partial z} = \frac{\partial f_3}{\partial y}$$

**Paso 2:** En la definición del rotor, cada componente es una de esas diferencias:
$$\operatorname{rot}\vec{F} = \left( \frac{\partial f_3}{\partial y} - \frac{\partial f_2}{\partial z},\; \frac{\partial f_1}{\partial z} - \frac{\partial f_3}{\partial x},\; \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y} \right)$$
como las derivadas son iguales, cada diferencia se anula: $\operatorname{rot}\vec{F} = (0,0,0)$ ($\vec{F}$ es **irrotacional**).

**Paso 3:** Por el teorema del rotor, la circulación sobre el borde es el flujo del rotor, que es nulo:
$$\oint_{\partial S} \vec{F} \cdot d\vec{r} = \iint_{S} \operatorname{rot}\vec{F} \cdot d\vec{S} = \iint_{S} \vec{0} \cdot d\vec{S} = 0$$

**Recíproco:** irrotacional es **necesario pero NO suficiente** para conservativo: si $\vec{F}$ es conservativo entonces $\operatorname{rot}\vec{F} = \vec{0}$, pero el recíproco no siempre vale.

_Fuente: 16-rotor-en-el-espacio.md_

</details>

### 37. [método] **Método:** calcular una circulación en el espacio usando el **Teorema de Stokes** (pasos, con el ejemplo de la intersección cilindro–plano).

<details><summary>Ver respuesta</summary>

**Paso 1:** Calcular $\operatorname{rot}\vec{F}$ con el determinante. (Ej.: $\vec{F} = (x^2, xy, z^2) \Rightarrow \operatorname{rot}\vec{F} = (0, 0, y)$.)

**Paso 2:** Elegir una superficie $S$ cuyo **borde sea la curva** dada. (Ej.: curva intersección de $x^2+y^2=1$ y $x+y+z=1$ → se elige el trozo del plano encerrado dentro del cilindro.)

**Paso 3:** Escribir $S$ como conjunto de nivel cero de $g$ y calcular el normal. (Ej.: $g = x+y+z-1$, $\nabla g = (1,1,1)$, $g'_z = 1$.) El flujo del rotor queda:
$$\iint_{S} \operatorname{rot}\vec{F} \cdot \frac{\nabla g}{|g'_z|}\, dx\, dy \quad \text{sobre la proyección } S_{xy}$$

**Paso 4:** Integrar sobre la proyección, pasando a **polares** si conviene. (Ej.: $\iint_{x^2+y^2\le 1} y\,dx\,dy = \int_0^{2\pi}\int_0^1 r^2\sin\varphi\,dr\,d\varphi = 0$ porque $\int_0^{2\pi}\sin\varphi\,d\varphi = 0$.)

**Cuándo conviene:** cuando parametrizar la curva por definición genera integrandos trigonométricos laboriosos; con Stokes suele salir "en un renglón" (ej. del plano: flujo de $(0,0,2)$ → $2 \times$ área del triángulo proyectado $= 1$).

**Verificar** que la orientación del borde esté en correspondencia con el normal elegido (superficie a la izquierda).

_Fuente: 16-rotor-en-el-espacio.md_

</details>

## 4. Green y cambio de variables — los T1 recurrentes (**69 % / 38 %**)

### 38. [enunciado] Enunciá el Teorema de Green (teorema del rotor en el plano) con hipótesis y tesis, incluyendo qué significa orientación positiva.

<details><summary>Ver respuesta</summary>

**Hipótesis:**
- $\vec{F} = (f_1, f_2)$ es un campo vectorial en el plano, definido en un subconjunto de $\mathbb{R}^2$, de **clase $C^1$** (las derivadas parciales de las funciones componentes son continuas).
- $D$ es una **región regular del plano** (limitada por curvas regulares que admiten recta tangente en cada punto), incluida dentro del dominio del campo, de modo que $\vec{F}$ pueda evaluarse en cada punto de $D$.

**Tesis:** la integral del campo a lo largo de la curva frontera $\partial D$, orientada en sentido **positivo (antihorario)**, es igual a la integral doble del rotor de $\vec{F}$ sobre $D$:

$$\oint_{\partial D} \vec{F} \cdot d\vec{r} = \iint_{D} \operatorname{rot} \vec{F} \, dx \, dy$$

**Orientación positiva:** la región está orientada en sentido positivo si su borde $\partial D$ se recorre en sentido **antihorario** (convención); en sentido horario la orientación es negativa y la circulación cambia de signo. Relaciona una **integral de línea** sobre una curva cerrada con una **integral doble**.

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 39. [enunciado] Enunciá el corolario del Teorema de Green para el cálculo de áreas. ¿Cómo se calcula el área de una región usando una circulación?

<details><summary>Ver respuesta</summary>

Si se elige **arbitrariamente** un campo vectorial $\vec{F}$ tal que su rotor valga $1$:

$$\operatorname{rot} \vec{F} = 1$$

entonces por Green la integral doble del rotor sobre $D$ es la integral de la función unitaria, que es el **área** de $D$:

$$\oint_{\partial D} \vec{F} \cdot d\vec{r} = \iint_{D} 1 \, dx \, dy = \text{área}(D)$$

**Conclusión:** para calcular el área de una región del plano, se elige un campo cuyo rotor valga $1$ (por ejemplo $\vec{F}(x,y) = (0, x)$, cuyo rotor es $\frac{\partial}{\partial x}(x) - \frac{\partial}{\partial y}(0) = 1$) y se calcula la circulación de ese campo alrededor del borde de la región, **orientado positivamente**.

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 40. [método] Te dan una curva cerrada parametrizada $\lambda(t)$ y te piden el área que encierra. ¿Cuáles son los pasos? (Ejemplo: elipse de semiejes $a$ y $b$.)

<details><summary>Ver respuesta</summary>

**Paso 1:** Elegir un campo con rotor $1$, por ejemplo $\vec{F}(x,y) = (0, x)$: $\operatorname{rot}\vec{F} = \frac{\partial}{\partial x}(x) - \frac{\partial}{\partial y}(0) = 1$.

**Paso 2:** Por el corolario de Green: $\text{área}(D) = \oint_{\partial D} \vec{F} \cdot d\vec{r}$, con $\partial D$ positivamente orientada.

**Paso 3:** Parametrizar la curva. Para la elipse: $\lambda(t) = (a\cos t, \, b\sin t)$, $t \in [0, 2\pi]$ (verificar: $\frac{x^2}{a^2} + \frac{y^2}{b^2} = \cos^2 t + \sin^2 t = 1$; con $t$ de $0$ a $2\pi$ se recorre en sentido antihorario).

**Paso 4:** Plantear $\int \vec{F}(\lambda(t)) \cdot \lambda'(t)\,dt$ con $\lambda'(t) = (-a\sin t, \, b\cos t)$. Como $\vec{F} = (0,x)$ sólo sobrevive el producto de la segunda componente:

$$\oint_{\partial D} \vec{F} \cdot d\vec{r} = \int_{0}^{2\pi} a\cos t \cdot b\cos t \, dt = \int_{0}^{2\pi} a\,b\,\cos^2 t \, dt$$

**Paso 5:** Integrar con la primitiva $\int \cos^2 t\,dt = \frac{t}{2} + \frac{\sin(2t)}{4}$; evaluando entre $0$ y $2\pi$ queda $\pi$.

**Paso 6:** Resultado: $\text{área}(D) = \pi\,a\,b$.

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 41. [fórmula] ¿Cómo se define el rotor de un campo vectorial $\vec{F} = (f_1, f_2)$ en el plano? ¿Cuándo se dice que el campo es irrotacional?

<details><summary>Ver respuesta</summary>

Dado un campo vectorial $\vec{F} = (f_1, f_2)$ definido en un subconjunto del plano (cada componente función de $x, y$), el **rotor** es el **escalar** que resulta de la diferencia entre la derivada parcial de la segunda componente respecto de $x$ y la derivada parcial de la primera componente respecto de $y$:

$$\operatorname{rot} \vec{F} = \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}$$

Cuando el rotor es igual a **cero**, el campo se dice **irrotacional** ($\operatorname{rot}\vec{F} = 0$).

*Ejemplo:* para $\vec{F}(x,y) = (-y, x)$: $\operatorname{rot}\vec{F} = 1 - (-1) = 2$ en todo punto.

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 42. [enunciado] Enunciá el teorema de cambio de variables en integrales dobles: hipótesis sobre la transformación $g$ y tesis (fórmula con el jacobiano).

<details><summary>Ver respuesta</summary>

Se tiene una función continua $f$ sobre la región $D$ (variables $x, y$) y una transformación de coordenadas $g$ definida en $D^*$ (variables $u, v$) que manda los puntos de $D^*$ a $D$.

**Hipótesis sobre $g$:**
- Es **inyectiva**: a cada elemento de $D^*$ le corresponde uno y solo uno de $D$ (equivale a que admite inversa $g^{-1}$).
- Tiene **derivadas parciales continuas**.
- Su **jacobiano** (determinante de la matriz jacobiana) es **distinto de cero**, al menos en el **interior** de $D^*$ (lo que ocurra en el borde no importa).

**Tesis:**

$$\iint_{D} f(x,y)\,dx\,dy = \iint_{D^*} f\big(x(u,v),\, y(u,v)\big)\,\left| J \right|\,du\,dv$$

Es el equivalente al método de sustitución de las integrales simples: se integra la función evaluada en las nuevas variables sobre $D^*$, multiplicando el integrando por el **módulo del jacobiano**.

_Fuente: 02-integrales-dobles-ii.md_

</details>

### 43. [fórmula] ¿Qué es la matriz jacobiana y el jacobiano de una transformación? Deducí que el jacobiano de las coordenadas polares vale $\rho$.

<details><summary>Ver respuesta</summary>

La **matriz jacobiana** es la matriz formada por todas las derivadas parciales de todas las funciones componentes. Para $x = x(\rho,\varphi)$, $y = y(\rho,\varphi)$:

$$J = \begin{pmatrix} \dfrac{\partial x}{\partial \rho} & \dfrac{\partial x}{\partial \varphi} \\ \dfrac{\partial y}{\partial \rho} & \dfrac{\partial y}{\partial \varphi} \end{pmatrix}$$

Al **determinante** de esa matriz se lo llama **jacobiano**.

**Coordenadas polares:** $x = \rho\cos\varphi$, $y = \rho\sin\varphi$:

$$J = \begin{vmatrix} \cos\varphi & -\rho\sin\varphi \\ \sin\varphi & \rho\cos\varphi \end{vmatrix} = \rho\cos^2\varphi + \rho\sin^2\varphi = \rho(\cos^2\varphi + \sin^2\varphi) = \rho$$

Por lo tanto $J = \rho$. (Vale cero en el origen, pero eso no importa porque el jacobiano se exige distinto de cero sólo en el interior de $D^*$, no en la frontera.)

_Fuente: 02-integrales-dobles-ii.md_

</details>

### 44. [fórmula] Si en un cambio de variables el dato es la transformación inversa $g^{-1}$ (de las coordenadas originales a las nuevas), ¿cómo se obtiene el jacobiano de $g$?

<details><summary>Ver respuesta</summary>

Se invierte el jacobiano de $g^{-1}$, apoyándose en la propiedad análoga a la derivada de la función inversa de Análisis I:

$$J_{g} = \frac{1}{J_{g^{-1}}}$$

*Ejemplo:* con $u = x+y$, $v = x-y$ (esta es $g^{-1}$):

$$J_{g^{-1}} = \begin{vmatrix} 1 & 1 \\ 1 & -1 \end{vmatrix} = (1)(-1) - (1)(1) = -2 \quad\Rightarrow\quad J_g = \frac{1}{-2} = -\frac{1}{2}$$

**Ojo con la orientación:** las coordenadas *originales* son las de la integral doble planteada; $g$ es la función que a las coordenadas *nuevas* les hace corresponder las originales. En la integral se usa el **módulo**: $|J_g| = \frac{1}{2}$.

_Fuente: 02-integrales-dobles-ii.md_

</details>

### 45. [método] Ejercicio tipo T1: te dan área$(D)$ y una transformación (por ejemplo lineal), y te piden área$(D^*)$. ¿Qué rol cumple el módulo del jacobiano y cómo se razona?

<details><summary>Ver respuesta</summary>

El módulo del jacobiano **corrige las áreas** de las regiones de integración cuando la transformación las deforma: está asociado a la **relación entre los tamaños de las áreas** de $D$ y $D^*$.

*Ejemplo del apunte* (cambio $u = x+y$, $v = x-y$, con $|J_g| = \frac{1}{2}$):
- Área de $D$ (cuadrado de lado $\sqrt{2}$): $\text{área}(D) = 2$.
- Área de $D^*$ (base de $1$ a $3$ mide $2$, altura de $-1$ a $1$ mide $2$): $\text{área}(D^*) = 4$.
- Al pasar a $D^*$ el área **se agrandó** (de $2$ a $4$); para que la integral dé lo mismo hubo que multiplicar por $\frac{1}{2}$, que es exactamente el módulo del jacobiano.

**Regla práctica:** como la transformación es **lineal**, el jacobiano es una **constante**, y entonces

$$\text{área}(D) = \iint_{D^*} |J|\,du\,dv = |J| \cdot \text{área}(D^*)$$

(caso $f \equiv 1$ del teorema). Conocida una de las dos áreas y $|J|$, se despeja la otra. Si el jacobiano no es constante (ej. polares, $J = \rho$), no se puede sacar de la integral.

_Fuente: 02-integrales-dobles-ii.md_

</details>

### 46. [método] Formato 2024-2025: te dan una integral en polares tipo $\int_0^{\pi/2}\int_0^{2\cos\varphi} \rho^3 \,d\rho\,d\varphi$. ¿Cómo identificás la región (graficarla) y la pasás a cartesianas? ¿Qué curva es $\rho = 2\cos\varphi$?

<details><summary>Ver respuesta</summary>

**Paso 1 — Identificar la curva frontera:** la cota $\rho \le 2R\cos\varphi$ proviene de la circunferencia desplazada sobre el eje $x$. En el apunte: la región $x^2 + y^2 \le 2Rx$ se identifica **completando cuadrados**:

$$x^2 - 2Rx + R^2 + y^2 \le R^2 \;\Rightarrow\; (x-R)^2 + y^2 \le R^2$$

interior de una circunferencia de radio $R$ centrada en $(R, 0)$ (llega hasta $2R$ sobre el eje $x$). Con $R = 1$: $\rho = 2\cos\varphi \leftrightarrow x^2 + y^2 = 2x \leftrightarrow (x-1)^2 + y^2 = 1$.

**Paso 2 — De cartesianas a polares (y viceversa):** reemplazando $x = \rho\cos\varphi$, $y = \rho\sin\varphi$: $\rho^2 \le 2R\rho\cos\varphi$, y simplificando $\rho \ne 0$: $\rho \le 2R\cos\varphi$. (Análogo: $\rho = 2R\sin\varphi \leftrightarrow x^2 + (y-R)^2 = R^2$, circunferencia tangente al eje $x$ desplazada en $y$.)

**Paso 3 — Rango del ángulo:** para la circunferencia desplazada sobre el eje $x$, $\varphi$ varía entre $-\frac{\pi}{2}$ y $\frac{\pi}{2}$; si además $\varphi \in [0, \frac{\pi}{2}]$, es sólo la **mitad superior** (primer cuadrante).

**Paso 4 — Reescribir el integrando:** deshacer el cambio recordando que el integrando en polares ya incluye el jacobiano $\rho$: por ejemplo $\rho^3 = \rho^2 \cdot \rho = (x^2+y^2)\cdot|J|$, así que en cartesianas el integrando es $x^2+y^2$. Describir la región como tipo 1 o tipo 2 con las cotas de la circunferencia.

_Fuente: 03-integrales-dobles-iii.md_

</details>

### 47. [enunciado] ¿Qué es una región regular del plano y cuál es la convención de orientación positiva para su frontera? ¿Y para regiones con agujeros (múltiplemente conexas)?

<details><summary>Ver respuesta</summary>

**Región regular:** una región $D$ del plano delimitada de manera que su **frontera resulta de la unión de curvas regulares** (curvas que admiten recta tangente en cada uno de sus puntos). $\partial D$ denota el borde o frontera.

**Orientación (convención):**
- Borde recorrido en sentido **antihorario** → orientación **positiva**.
- Borde recorrido en sentido **horario** → orientación **negativa**.
- Sólo tiene sentido para **curvas cerradas**.

**Regiones regulares por partes:** el teorema de Green también vale; en los bordes comunes entre pedazos las orientaciones se **compensan** y sólo quedan los bordes externos, orientados antihorario.

**Conjuntos múltiplemente conexos (ej. anillo):** la región está orientada en forma **positiva** cuando el **borde externo** va en sentido **antihorario** y el **borde interno** en sentido **horario**.

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 48. [método] ¿Cuándo conviene usar el Teorema de Green para calcular una circulación y cuáles son los pasos? (Ejemplo tipo: $\vec{F}$ alrededor del borde de un triángulo.)

<details><summary>Ver respuesta</summary>

**Cuándo:** para calcular circulaciones (integrales de campos vectoriales alrededor de **curvas cerradas**), transformándolas en integrales dobles a menudo más sencillas — evita parametrizar cada tramo del borde y sumar las integrales de línea (mucho más laborioso).

**Pasos (ejercicio del triángulo, $D$ en el primer cuadrante limitada por $x+y=3$):**

**Paso 1:** Verificar hipótesis: $\vec{F}$ de clase $C^1$ definida en toda $D$, región regular, borde orientado positivamente (antihorario).

**Paso 2:** Aplicar el teorema: $\oint_{\partial D} \vec{F} \cdot d\vec{r} = \iint_{D} \operatorname{rot} \vec{F} \, dx \, dy$.

**Paso 3:** Calcular $\operatorname{rot}\vec{F} = \frac{\partial f_2}{\partial x} - \frac{\partial f_1}{\partial y}$. Si es constante $c$, sale de la integral: $\iint_D c\,dx\,dy = c \cdot \text{área}(D)$.

**Paso 4:** Calcular el área con geometría (triángulo: $\frac{\text{base}\cdot\text{altura}}{2} = \frac{3\cdot 3}{2} = \frac{9}{2}$) o con la integral doble.

**Ojo con el sentido:** Green da la circulación en sentido **antihorario**; si piden sentido **horario**, el resultado es el **opuesto** (si en positivo dio $9$, en horario da $-9$).

_Fuente: 09-rotor-en-el-plano.md_

</details>

### 49. [fórmula] ¿Cuál es la interpretación física del rotor en el plano como límite? (fórmula del cociente circulación/área)

<details><summary>Ver respuesta</summary>

Sea $\vec{F}$ de clase $C^1$ y $(x_0, y_0)$ un punto de su dominio. Tomando una región $D$ con forma de circunferencia de radio $r$ centrada en $(x_0, y_0)$, el cociente entre la circulación del campo alrededor de $\partial D$ positivamente orientada y el área encerrada, cuando $r \to 0$, coincide con el rotor en ese punto:

$$\operatorname{rot} \vec{F}(x_0, y_0) = \lim_{r \to 0} \frac{\displaystyle\oint_{\partial D} \vec{F} \cdot d\vec{r}}{\text{área}(D)}$$

Tanto el trabajo como el área tienden a cero, pero el cociente de esos dos infinitésimos tiende al valor del rotor: el rotor se interpreta como el cociente entre una **circulación (trabajo)** y el **área encerrada**.

*Verificación con $\vec{F} = (-y,x)$:* circulación sobre circunferencia de radio $r$ da $2\pi r^2$; área $\pi r^2$; el cociente da $2 = \operatorname{rot}\vec{F}$.

_Fuente: 09-rotor-en-el-plano.md_

</details>

## 5. Ecuaciones diferenciales — P4 (**54 %**) y T2 de superposición (**38 %**)

### 50. [enunciado] Forma general de la EDO lineal de 2° orden. ¿Qué hipótesis se piden sobre los coeficientes y qué garantizan?

<details><summary>Ver respuesta</summary>

$$
a_2(x)\,y'' + a_1(x)\,y' + a_0(x)\,y = f(x)
$$

**Homogénea** si $f(x)=0$ para todo $x$ del dominio.

**Hipótesis:** $f, a_2, a_1, a_0$ continuas y $a_2(x)\neq 0$ en el dominio. Garantizan que exista la **solución general** y que, dadas condiciones iniciales, exista la **solución particular** que las satisface.

Dividiendo por $a_2\neq 0$ queda la forma reducida $y'' + p\,y' + q\,y = f/a_2$.

_Fuente: 18-ecuaciones-diferenciales-lineales-ii.md_

</details>

### 51. [enunciado] Definí **solución general** y **solución particular** de una EDO de orden $n$ (T2 del 2025-07-18).

<details><summary>Ver respuesta</summary>

**Solución general:** familia de soluciones que depende de **tantas constantes arbitrarias como el orden** de la ecuación ($n$ constantes; 2° orden $\Rightarrow$ 2).

**Solución particular:** una solución concreta sin constantes arbitrarias — se obtiene fijando las constantes de la general, típicamente imponiendo condiciones iniciales $y(x_0)=y_0$, $y'(x_0)=y_1$.

Una función es **solución** si al reemplazarla (con sus derivadas) transforma la ecuación en una **identidad**, satisfecha para todo valor de la variable.

_Fuente: 18 (y 17)_

</details>

### 52. [método] ¿De dónde sale la **ecuación característica** $m^2+pm+q=0$? Deducción completa.

<details><summary>Ver respuesta</summary>

Para $y''+p\,y'+q\,y=0$ se propone $y=e^{mx}$:

**Paso 1:** $y'=m\,e^{mx}$, $y''=m^2 e^{mx}$.

**Paso 2:** reemplazar: $m^2 e^{mx} + p\,m\,e^{mx} + q\,e^{mx} = 0$.

**Paso 3:** factor común: $e^{mx}\left(m^2+p\,m+q\right)=0$.

**Paso 4:** $e^{mx}\neq 0$ siempre $\Rightarrow$ debe anularse el paréntesis:

$$
m^2 + p\,m + q = 0
$$

$y=e^{mx}$ es solución **solo si** $m$ es raíz de esta ecuación (la **característica**).

_Fuente: 18 (Ej. 4)_

</details>

### 53. [fórmula] Los **3 casos de raíces** de la ecuación característica y la solución general de cada uno.

<details><summary>Ver respuesta</summary>

**Caso 1 — raíces reales distintas** ($m_1\neq m_2$):

$$
y = c_1\,e^{m_1 x} + c_2\,e^{m_2 x}
$$

**Caso 2 — raíz real doble** ($m=-p/2$):

$$
y = c_1\,e^{mx} + c_2\,x\,e^{mx}
$$

**Caso 3 — raíces complejas conjugadas** ($m = \alpha\pm\beta i$, con $\alpha=-\dfrac{p}{2}$, $\beta=\dfrac{\sqrt{4q-p^2}}{2}$):

$$
y = e^{\alpha x}\left[c_1\cos(\beta x) + c_2\sin(\beta x)\right]
$$

En la práctica: resolvé la característica y leé $\alpha$ y $\beta$ directo de las raíces ($\beta$ = coeficiente positivo de $x$ en las trigonométricas). Ejemplo: $m^2+2m+5=0 \Rightarrow m=-1\pm 2i \Rightarrow y=e^{-x}[c_1\cos 2x + c_2\sin 2x]$.

_Fuente: 18 (con corrección de β)_

</details>

### 54. [demostración] T2 (2015-11-25): demostrá que si $y_1$ e $y_2$ son soluciones de la homogénea, entonces $y=c_1 y_1+c_2 y_2$ es solución. ¿Cuándo es LA solución general?

<details><summary>Ver respuesta</summary>

**Paso 1:** $y' = c_1 y_1' + c_2 y_2'$.

**Paso 2:** $y'' = c_1 y_1'' + c_2 y_2''$.

**Paso 3:** reemplazar en el miembro izquierdo de $a_2 y''+a_1 y'+a_0 y = 0$:

$$
a_2(c_1 y_1''+c_2 y_2'') + a_1(c_1 y_1'+c_2 y_2') + a_0(c_1 y_1+c_2 y_2)
$$

**Paso 4:** distribuir y sacar factor común $c_1$ y $c_2$:

$$
c_1(a_2 y_1''+a_1 y_1'+a_0 y_1) + c_2(a_2 y_2''+a_1 y_2'+a_0 y_2)
$$

**Paso 5:** cada paréntesis vale $0$ porque $y_1$ e $y_2$ son soluciones (hipótesis) $\Rightarrow$ $c_1\cdot 0 + c_2\cdot 0 = 0$: es solución. $\blacksquare$

Es **LA solución general** si además $y_1, y_2$ son **linealmente independientes** ($y_2/y_1$ no constante): así la combinación tiene 2 constantes efectivas, tantas como el orden.

_Fuente: 18 (Ej. 2)_

</details>

### 55. [demostración] Demostrá que $y = y_c + y_p$ es la **solución general de la no homogénea** ($y_c$ = general de la homogénea asociada, $y_p$ = particular de la no homogénea).

<details><summary>Ver respuesta</summary>

**Paso 1:** $y' = y_c' + y_p'$, $\quad y'' = y_c'' + y_p''$.

**Paso 2:** reemplazar en $a_2 y''+a_1 y'+a_0 y$:

$$
a_2(y_c''+y_p'') + a_1(y_c'+y_p') + a_0(y_c+y_p)
$$

**Paso 3:** distribuir y reagrupar:

$$
\big(a_2 y_c''+a_1 y_c'+a_0 y_c\big) + \big(a_2 y_p''+a_1 y_p'+a_0 y_p\big)
$$

**Paso 4:** el primer paréntesis vale $0$ ($y_c$ es solución de la homogénea) y el segundo vale $f(x)$ ($y_p$ es solución de la no homogénea):

$$
0 + f(x) = f(x) \quad\blacksquare
$$

Y es **la general** porque $y_c$ aporta las 2 constantes arbitrarias.

_Fuente: 19_

</details>

### 56. [demostración] Las 3 variantes de T2 de superposición NO homogénea: (a) $y_1+y_2$; (b) $y_1-y_2$; (c) $k\,y_p$. Demostralas.

<details><summary>Ver respuesta</summary>

Hipótesis: $y_1$ es solución de $a_2 y''+a_1 y'+a_0 y = f_1(x)$ e $y_2$ de $\dots = f_2(x)$ (mismos coeficientes).

**(a) $y_1+y_2$ es solución de $\dots = f_1+f_2$** *(2017-07-05)*:

**Paso 1:** $(y_1+y_2)' = y_1'+y_2'$ y $(y_1+y_2)'' = y_1''+y_2''$.

**Paso 2:** reemplazar, distribuir y reagrupar:

$$
\big(a_2 y_1''+a_1 y_1'+a_0 y_1\big) + \big(a_2 y_2''+a_1 y_2'+a_0 y_2\big) = f_1(x) + f_2(x) \quad\blacksquare
$$

**(b) $y_1-y_2$ es solución de $\dots = f_1-f_2$** *(2017-11-16, 2022-11-24)*: idéntico, restando los grupos: $f_1(x)-f_2(x)$. $\blacksquare$

**(c) si $y_p$ es solución de $\dots = g(x)$, entonces $k\,y_p$ es solución de $\dots = k\,g(x)$** *(2022-07-15)*: $(k y_p)'=k y_p'$, $(k y_p)''=k y_p''$; al reemplazar sale factor común $k$:

$$
k\big(a_2 y_p''+a_1 y_p'+a_0 y_p\big) = k\,g(x) \quad\blacksquare
$$

Las tres usan la misma técnica del apunte: **derivar → reemplazar → distribuir → agrupar → usar la hipótesis de cada grupo**.

_Fuente: 19 (superposición) + técnica del 18_

</details>

### 57. [método] **Coeficientes indeterminados:** ¿qué $y_p$ proponés según la forma de $f(x)$, y por qué funciona?

<details><summary>Ver respuesta</summary>

Requiere coeficientes constantes y $f(x)$ de forma "linda":

- $f$ = **polinomio de grado $n$** $\Rightarrow$ proponer polinomio completo de grado $n$: $y_p = ax^n+\dots+b$.
- $f$ = **seno o coseno** $\Rightarrow$ proponer $A\cos(\omega x)+B\sin(\omega x)$ (los dos, aunque $f$ tenga uno solo).
- $f$ = **exponencial** $e^{kx}$ $\Rightarrow$ proponer $A\,e^{kx}$.
- $f$ = **suma** de varios $\Rightarrow$ por superposición, proponer una $y_p$ para cada término y sumar.

**Por qué funciona:** las derivadas conservan el formato (un polinomio deriva a polinomios, una exponencial a exponenciales), así que al reemplazar se pueden **comparar coeficientes** y despejar. En estos parciales el término derecho es siempre polinomio/constante/exponencial/coseno: coeficientes indeterminados alcanza para todos.

_Fuente: 19_

</details>

### 58. [método] **Resonancia:** ¿cuándo multiplicás la propuesta de $y_p$ por $x$ o por $x^2$? ¿Cuál es la señal práctica?

<details><summary>Ver respuesta</summary>

Cuando $f(x)$ contiene $e^{m_1 x}$ con $m_1$ **raíz de la ecuación característica**:

- raíz **simple** $\Rightarrow$ multiplicar la propuesta por $x$: $y_p = x\cdot(\text{propuesta})$.
- raíz **doble** ($m_1=m_2$) $\Rightarrow$ multiplicar por $x^2$.

**Señal práctica:** si al comparar coeficientes el sistema da **incompatible**, multiplicá por $x$; si vuelve a dar incompatible, por $x^2$.

(Ojo: una constante en $f$ es $e^{0x}$ — hay resonancia si $m=0$ es raíz, como en $y''+4y'=8$.)

_Fuente: 19_

</details>

### 59. [método] Receta completa del P4 del parcial: «resolver $y''+p\,y'+q\,y=f(x)$ con $y(0)=a$, $y'(0)=b$».

<details><summary>Ver respuesta</summary>

**Paso 1:** homogénea asociada: característica $m^2+pm+q=0$ → identificar el caso de raíces → $y_c$ (con $c_1, c_2$).

**Paso 2:** $y_p$ por coeficientes indeterminados según la forma de $f(x)$ (atención a la resonancia).

**Paso 3:** solución general $y = y_c + y_p$.

**Paso 4:** calcular $y'$ e imponer $y(0)=a$, $y'(0)=b$ $\Rightarrow$ sistema $2\times 2$ en $c_1, c_2$.

**Paso 5:** escribir la solución particular final (y verificar reemplazando, si hay tiempo).

P4 reales del banco: $y''+4y'=8$ · $y''-6y'+9y=2x$ · $y''-2y'+5y=2x$ · $y''-4y'+13y=26$ · $y''+y'-2y=\cos x$ · $y''-3y'=2-6x$.

_Fuente: 18/19 + banco del INDICE_

</details>

### 60. [enunciado] Teorema de **existencia y unicidad** para la EDO lineal de 2° orden: hipótesis y tesis.

<details><summary>Ver respuesta</summary>

**Hipótesis:** $a_2, a_1, a_0$ (y $f$) **continuas** en un conjunto abierto, y $a_2\neq 0$ en dicho conjunto.

**Tesis:** la solución de la ecuación que satisface las dos condiciones iniciales

$$
y(x_0)=y_0, \qquad y'(x_0)=y_1
$$

**existe y es única**.

_Fuente: 19_

</details>

### 61. [fórmula] Criterio del cociente para **independencia lineal** de dos soluciones. ¿Por qué importa para la solución general?

<details><summary>Ver respuesta</summary>

$$
\frac{y_2}{y_1} = \text{constante} \Rightarrow \text{linealmente dependientes}; \qquad \frac{y_2}{y_1} = \text{función de } x \Rightarrow \text{independientes}
$$

Importa porque la solución general de la homogénea necesita $y_1, y_2$ **LI**: si $y_2 = k\,y_1$, la combinación $c_1 y_1 + c_2 k y_1 = y_1(c_1+c_2 k)$ colapsa a **una sola** constante y no puede ser la general (que necesita 2).

_Fuente: 18_

</details>

---

*Generado el 2026-07-06 desde `estrategia.md` (checklist teórico) y `apuntes/md/` (61 cartas). Regenerable/ampliable con `/flashcards`.*
