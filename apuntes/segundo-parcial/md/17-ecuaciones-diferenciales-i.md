# Ecuaciones diferenciales I

> Fuente: https://www.youtube.com/watch?v=ZXFsUIyYYvs

---

## Índice

- [00:02](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2s) — Introducción: caída libre y planteo de una ecuación diferencial
- [06:58](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=418s) — Ecuación diferencial y solución
- [08:03](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=483s) — Condiciones iniciales y solución particular
- [12:17](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=737s) — Solución general y orden de una ecuación diferencial
- [13:54](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=834s) — Definición general de ecuación diferencial ordinaria
- [15:27](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=927s) — Verificación de soluciones
- 📝 [15:27](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=927s) — Ejercicio 1: verificar que $y=\cos x$ es solución de $y''+y=0$
- 📝 [19:16](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1156s) — Ejercicio 2: verificar que $y=\sin x$ es solución de $y''+y=0$
- [21:20](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1280s) — Ecuaciones diferenciales de primer orden y forma normal
- 📝 [21:53](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1313s) — Ejercicio 3: resolver $y'=-\dfrac{y}{x}$ (variables separables)
- 📝 [28:47](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1727s) — Ejercicio 4: solución particular con $y(1)=2$
- [29:55](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1795s) — Interpretación geométrica: familias de curvas
- [33:11](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1991s) — Teorema de existencia y unicidad
- [36:17](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2177s) — Ecuaciones con variables separables
- [37:25](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2245s) — Ecuaciones lineales de primer orden
- 📝 [39:28](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2368s) — Ejercicio 5: resolver $y'-\dfrac{2}{x}y=x^3$ (lineal de primer orden)
- 📝 [48:22](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2902s) — Ejercicio 6: solución particular con $y(2)=4$
- [50:32](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3032s) — Metodología de resolución de una lineal de primer orden
- [53:41](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3221s) — Ecuaciones homogéneas de primer orden
- 📝 [54:44](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3284s) — Ejercicio 7: resolver $y'=\dfrac{x^2+y^2}{xy}$ (homogénea de primer orden)
- [1:04:15](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3855s) — Repaso de los tres tipos de ecuaciones
- [1:04:46](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3886s) — Construcción de la ecuación diferencial a partir de la solución general
- 📝 [1:05:17](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3917s) — Ejercicio 8: ecuación diferencial de una familia de circunferencias
- [1:10:05](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4205s) — Soluciones singulares
- 📝 [1:10:05](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4205s) — Ejercicio 9: verificar la solución singular $y=2$
- [1:14:51](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4491s) — Trayectorias ortogonales
- 📝 [1:20:44](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4844s) — Ejercicio 10: trayectorias ortogonales a $y=cx^2$

---

## Introducción: caída libre y planteo de una ecuación diferencial — [00:02](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2s)

El tema se introduce con el ejemplo de un cuerpo de masa $m$ en caída libre. A una altura $y$, la fuerza gravitatoria vale $F = m\,g$, donde $g$ es la aceleración de la gravedad, con valor aproximado

$$
g = -9{,}81 \ \frac{\text{m}}{\text{s}^2}
$$

El signo negativo se asigna porque la aceleración de la gravedad tiene dirección opuesta al sentido en que se miden las alturas. Este valor se considera bajo ciertas condiciones (latitud de 45 grados y a nivel del mar) y despreciando la fricción con el aire.

Por la segunda ley de Newton, masa por aceleración es igual a la fuerza. La aceleración es la derivada de la velocidad, o la derivada segunda de la posición respecto al tiempo:

$$
m\,\frac{d^2 y}{dt^2} = m\,g
$$

de donde resulta la ecuación diferencial

$$
\frac{d^2 y}{dt^2} = g
$$

Para hallar la altura $y(t)$, se escribe la derivada segunda como la derivada de la derivada de la posición y se integra sucesivamente:

$$
d\!\left(\frac{dy}{dt}\right) = g\, dt
$$

Integrando ambos miembros (cada integral indefinida obliga a sumar una constante):

$$
\frac{dy}{dt} = g\,t + C
$$

Integrando nuevamente y agrupando las constantes:

$$
y(t) = \frac{g\,t^2}{2} + C_3\,t + C_6
$$

Esta función $y(t)$ es la altura del cuerpo en función del tiempo, y es la solución de la ecuación diferencial planteada.

## Ecuación diferencial y solución — [06:58](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=418s)

- La **ecuación diferencial** relaciona una función incógnita con sus derivadas. En el ejemplo: $\dfrac{d^2y}{dt^2}=g$.
- La **solución de la ecuación diferencial** es la función que la satisface: al derivarla y reemplazarla en la ecuación, la transforma en una identidad.

En el ejemplo, sea cual sea el valor de $C_3$ y de $C_6$, la función $y(t)=\dfrac{g\,t^2}{2}+C_3\,t+C_6$ siempre es solución de la ecuación diferencial.

## Condiciones iniciales y solución particular — [08:03](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=483s)

Se imponen restricciones en el instante inicial. Para $t=0$: la posición $y(0)=0$ y la velocidad $\dfrac{dy}{dt}\Big|_{t=0}=v_0=0$.

Evaluando $y(0)$: los términos con $t$ se anulan, por lo que $C_6 = y(0) = 0$.

Evaluando la derivada en $t=0$: $\dfrac{dy}{dt}\Big|_{t=0}=g\cdot 0 + C_3 = C_3 = v_0$.

Estas restricciones asociadas a un valor de la variable independiente se llaman **condiciones iniciales**, y permiten determinar los valores de las constantes. La solución que satisface las condiciones iniciales se denomina **solución particular** de la ecuación diferencial.

Con $C_3=v_0$ y $C_6=y_0$, la solución de la caída libre queda:

$$
y(t) = \frac{g\,t^2}{2} + v_0\,t + y_0
$$

donde $g$ es la aceleración de la gravedad, $v_0$ la velocidad inicial e $y_0$ la posición o altura inicial.

## Solución general y orden de una ecuación diferencial — [12:17](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=737s)

- La **solución general** es la función solución que depende de constantes arbitrarias.
- Depende de **tantas constantes arbitrarias como sea el orden** de la ecuación diferencial.
- El **orden** de la ecuación diferencial está dado por la derivada de mayor orden que interviene en ella.

En el ejemplo de caída libre, la derivada de mayor orden es la segunda, por lo que la ecuación es de segundo orden y su solución general depende de dos constantes arbitrarias. Al asignar valores determinados a esas constantes se obtiene una solución particular.

## Definición general de ecuación diferencial ordinaria — [13:54](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=834s)

Una **ecuación diferencial** es una expresión que relaciona una variable independiente, una función incógnita y sus respectivas derivadas.

Cuando la función incógnita depende de **una sola variable**, la ecuación se llama **ecuación diferencial ordinaria**. En el curso se estudian ecuaciones diferenciales ordinarias.

La **solución (o integral)** de una ecuación diferencial es una función que, reemplazada en la misma, la transforma en una identidad.

## Verificación de soluciones — [15:27](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=927s)

Para verificar si una función es solución de una ecuación diferencial, se la reemplaza en la ecuación y se comprueba si la transforma en una identidad. Esto es análogo a verificar que un valor es solución de una ecuación algebraica.

<details>
<summary>📝 Ejercicio 1 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=927s">15:27</a>: verificar que y = cos x es solución de y'' + y = 0</summary>

Verificar si la función $y=\cos x$ satisface la ecuación diferencial

$$
y'' + y = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Calcular la derivada primera.

$$
y' = -\sin x
$$

**Paso 2:** Calcular la derivada segunda.

$$
y'' = -\cos x
$$

**Paso 3:** Reemplazar en la ecuación diferencial.

$$
y'' + y = -\cos x + \cos x = 0
$$

**Paso 4:** Como la igualdad se cumple para todo $x$ real, la ecuación se transforma en una identidad. Por lo tanto $y=\cos x$ es solución de la ecuación diferencial.

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1156s">19:16</a>: verificar que y = sin x es solución de y'' + y = 0</summary>

Verificar si la función $y=\sin x$ satisface la misma ecuación diferencial

$$
y'' + y = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Calcular las derivadas primera y segunda.

$$
y' = \cos x \qquad y'' = -\sin x
$$

**Paso 2:** Reemplazar en la ecuación diferencial.

$$
y'' + y = -\sin x + \sin x = 0
$$

**Paso 3:** Vale $0$ sea cual sea el valor de $x$, por lo que la función $y=\sin x$ también es solución de la ecuación diferencial.

**Observación:** dos funciones distintas ($\cos x$ y $\sin x$) pueden ser solución de la misma ecuación diferencial, del mismo modo que una ecuación algebraica de segundo grado puede tener dos raíces reales distintas.

</details>

</details>

## Ecuaciones diferenciales de primer orden y forma normal — [21:20](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1280s)

Una ecuación diferencial es de **primer orden** cuando la derivada de mayor orden que interviene es la primera. Si en la ecuación se puede despejar $y'$,

$$
y' = g(x,y)
$$

se dice que la ecuación está en su **forma normal**. A veces se puede despejar $y'$ y a veces no.

<details>
<summary>📝 Ejercicio 3 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1313s">21:53</a>: resolver y' = -y/x (variables separables)</summary>

Resolver la ecuación diferencial

$$
y' = -\frac{y}{x}
$$

hallando su solución general.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Escribir $y'$ como cociente de diferenciales.

$$
\frac{dy}{dx} = -\frac{y}{x}
$$

**Paso 2:** Tratar los diferenciales como elementos algebraicos y separar variables: todo lo que depende de $y$ en un miembro y todo lo que depende de $x$ en el otro.

$$
\frac{dy}{y} = -\frac{dx}{x}
$$

**Paso 3:** Integrar miembro a miembro.

$$
\ln|y| = -\ln|x| + C
$$

**Paso 4:** Expresar la constante como $C=\ln|C|$ y usar la propiedad de la diferencia de logaritmos.

$$
\ln|y| = \ln\left|\frac{C}{x}\right|
$$

**Paso 5:** Cancelar los logaritmos e igualar los argumentos.

$$
|y| = \left|\frac{C}{x}\right|
$$

**Paso 6:** Para quitar las barras de módulo se escribe $y=\pm\dfrac{C}{x}$; como $C$ es una constante real cualquiera, cambiar su signo sigue dando una constante arbitraria, por lo que la **solución general** es

$$
y = \frac{C}{x}
$$

Como la ecuación es de primer orden y la solución depende de una única constante arbitraria, esta es la solución general.

</details>

</details>

<details>
<summary>📝 Ejercicio 4 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1727s">28:47</a>: solución particular con y(1)=2</summary>

Dada la ecuación $y'=-\dfrac{y}{x}$ con solución general $y=\dfrac{C}{x}$, hallar la solución particular sujeta a la condición inicial $y=2$ cuando $x=1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reemplazar la condición inicial en la solución general.

$$
2 = \frac{C}{1}
$$

**Paso 2:** Despejar la constante.

$$
C = 2
$$

**Paso 3:** La solución particular es

$$
y = \frac{2}{x}
$$

</details>

</details>

## Interpretación geométrica: familias de curvas — [29:55](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1795s)

Para la ecuación $y'=-\dfrac{y}{x}$:

- La solución general $y=\dfrac{C}{x}$ corresponde a una **familia de curvas** (hipérbolas), una para cada valor de $C$.
- La solución particular $y=\dfrac{2}{x}$ corresponde a **una** curva de esa familia: la que pasa por el punto de coordenadas $(1,2)$ dado por las condiciones iniciales.

## Teorema de existencia y unicidad — [33:11](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=1991s)

Bajo ciertas condiciones se puede garantizar la existencia de una solución particular y que esa solución sea única.

**Hipótesis:** dada la ecuación diferencial en forma normal $y'=g(x,y)$, si la función $g$ que relaciona $x$ e $y$ tiene derivadas parciales continuas (es de clase $C^1$) al menos en un entorno de un punto $(x_0,y_0)$,

**Tesis:** entonces existe y es única la función solución particular de la ecuación diferencial sujeta a la condición inicial $y(x_0)=y_0$.

Por ejemplo, en $y'=-\dfrac{y}{x}$ la función $g(x,y)=-\dfrac{y}{x}$ es un cociente de polinomios con denominador no nulo, de clase $C^1$ en todo su dominio. Esto garantiza que existe una única solución que satisface $y(1)=2$: de todas las hipérbolas de la familia, hay una sola que pasa por $(1,2)$.

## Ecuaciones con variables separables — [36:17](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2177s)

Son las más sencillas de resolver. Si la derivada de la función incógnita se puede escribir como el producto de una función de $x$ por una función de $y$,

$$
y' = h(x)\, k(y)
$$

se resuelve **agrupando todo lo que depende de $y$ en un miembro y todo lo que depende de $x$ en el otro**, e integrando miembro a miembro. Por ejemplo, $y'=-\dfrac{y}{x}$ se puede ver como $y'=\left(-\dfrac{1}{x}\right)\,y$, y ya fue resuelta de esta forma.

## Ecuaciones lineales de primer orden — [37:25](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2245s)

Son las que tienen la forma

$$
y' + P(x)\,y = Q(x)
$$

Se resuelven reemplazando la función incógnita $y$ por el producto de dos funciones de $x$, $y=u\,v$. Entonces la derivada es

$$
y' = u'\,v + u\,v'
$$

y se reemplaza en la ecuación diferencial.

<details>
<summary>📝 Ejercicio 5 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2368s">39:28</a>: resolver y' - (2/x) y = x³ (lineal de primer orden)</summary>

Resolver la ecuación diferencial lineal de primer orden

$$
y' - \frac{2}{x}\,y = x^3
$$

donde $P(x)=-\dfrac{2}{x}$ y $Q(x)=x^3$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reemplazar $y=u\,v$ y $y'=u'\,v+u\,v'$ en la ecuación.

$$
u'\,v + u\,v' - \frac{2}{x}\,u\,v = x^3
$$

**Paso 2:** Sacar factor común $u$ en el segundo y tercer término.

$$
u'\,v + u\left(v' - \frac{2}{x}\,v\right) = x^3
$$

**Paso 3:** Imponer arbitrariamente que el paréntesis valga cero para hallar $v$.

$$
v' - \frac{2}{x}\,v = 0
$$

**Paso 4:** Es una ecuación con variables separables. Escribir $v'=\dfrac{dv}{dx}$ y separar.

$$
\frac{dv}{v} = \frac{2}{x}\,dx
$$

**Paso 5:** Integrar miembro a miembro.

$$
\ln|v| = 2\ln|x| + \ln|C_1|
$$

**Paso 6:** Aplicar propiedades de los logaritmos (pasar el $2$ como exponente y agrupar) y cancelar logaritmos.

$$
v = C_1\,x^2
$$

**Paso 7:** Como el paréntesis vale cero, la ecuación se reduce a $u'\,v=x^3$. Reemplazar $v$.

$$
u'\,C_1\,x^2 = x^3
$$

**Paso 8:** Escribir $u'=\dfrac{du}{dx}$, simplificar y separar variables.

$$
dv \ \text{(de } u\text{): } \quad du = \frac{x}{C_1}\,dx
$$

**Paso 9:** Integrar miembro a miembro.

$$
u = \frac{x^2}{2\,C_1} + C_2
$$

**Paso 10:** Formar $y=u\,v$.

$$
y = \left(\frac{x^2}{2\,C_1} + C_2\right)\,C_1\,x^2
$$

**Paso 11:** Distribuir: en el primer término se simplifica $C_1$, quedando la **solución general** con una única constante arbitraria $C_3=C_1\,C_2$.

$$
y = \frac{x^4}{2} + C_3\,x^2
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=2902s">48:22</a>: solución particular con y(2)=4</summary>

Para la ecuación anterior, con solución general $y=\dfrac{x^4}{2}+C_3\,x^2$, hallar la solución particular sujeta a la condición inicial $y=4$ cuando $x=2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reemplazar $x=2$, $y=4$ en la solución general.

$$
4 = \frac{2^4}{2} + C_3\,\cdot 2^2
$$

**Paso 2:** Operar.

$$
4 = 8 + 4\,C_3
$$

**Paso 3:** Despejar la constante.

$$
C_3 = \frac{4-8}{4} = -1
$$

**Paso 4:** Reemplazar $C_3=-1$ para obtener la solución particular.

$$
y = \frac{x^4}{2} - x^2
$$

Geométricamente, la solución general es una familia de curvas y la particular es la que pasa por el punto $(2,4)$.

</details>

</details>

## Metodología de resolución de una lineal de primer orden — [50:32](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3032s)

Resumen del método:

- **Paso 1:** verificar que la ecuación tiene (o se puede llevar a) la forma $y'+P(x)\,y=Q(x)$; entonces es lineal de primer orden.
- **Paso 2:** reemplazar $y=u\,v$ y $y'=u'\,v+u\,v'$.
- **Paso 3:** en el miembro izquierdo, sacar factor común $u$ del segundo y tercer término.
- **Paso 4:** imponer que el paréntesis valga cero; queda una ecuación con variables separables de la que se calcula $v$ en términos de $x$.
- **Paso 5:** volver a la ecuación, donde ahora $u'\,v=Q(x)$; reemplazar $v$ y resolver por variables separables para obtener $u$ en términos de $x$.
- **Paso 6:** multiplicar $y=u\,v$ para obtener la solución general. Las dos constantes que van apareciendo se reducen siempre a una sola (la ecuación es de primer orden).
- **Paso 7:** si hay condiciones iniciales, reemplazar los valores para determinar la constante y hallar la solución particular.

## Ecuaciones homogéneas de primer orden — [53:41](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3221s)

Se tiene una ecuación en forma normal $y'=g(x,y)$ donde la función de dos variables cumple el requisito

$$
g(\lambda x, \lambda y) = g(x, y)
$$

Cuando cumple esta propiedad, la ecuación se llama **homogénea de primer orden** y se resuelve con el reemplazo de la función incógnita por otra función incógnita por $x$:

$$
y = u\,x
$$

<details>
<summary>📝 Ejercicio 7 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3284s">54:44</a>: resolver y' = (x²+y²)/(xy) (homogénea de primer orden)</summary>

Resolver la ecuación diferencial

$$
y' = \frac{x^2 + y^2}{x\,y}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Verificar la homogeneidad calculando $g(\lambda x,\lambda y)$.

$$
g(\lambda x,\lambda y) = \frac{\lambda^2 x^2 + \lambda^2 y^2}{\lambda x\,\lambda y} = \frac{\lambda^2(x^2+y^2)}{\lambda^2\,x\,y} = \frac{x^2+y^2}{x\,y} = g(x,y)
$$

Se cumple $g(\lambda x,\lambda y)=g(x,y)$, por lo que la ecuación es homogénea de primer orden.

**Paso 2:** Hacer el reemplazo $y=u\,x$, de donde $y'=u'\,x + u$.

**Paso 3:** Reemplazar en la ecuación (poniendo $y=u\,x$, $y^2=u^2x^2$).

$$
u'\,x + u = \frac{x^2 + u^2 x^2}{x\,\cdot u\,x}
$$

**Paso 4:** Sacar factor común $x^2$ en el numerador y simplificar con el denominador $x^2 u$.

$$
u'\,x + u = \frac{1 + u^2}{u}
$$

**Paso 5:** Pasar $u$ al miembro derecho y sacar denominador común; los términos $u^2$ se cancelan.

$$
\frac{dv}{dx}\,x = \frac{1}{u}
$$

(aquí $\dfrac{dv}{dx}$ es $\dfrac{du}{dx}$)

**Paso 6:** Separar variables.

$$
u\,du = \frac{dx}{x}
$$

**Paso 7:** Integrar miembro a miembro.

$$
\frac{u^2}{2} = \ln|x| + C
$$

**Paso 8:** Deshacer el cambio con $u=\dfrac{y}{x}$.

$$
\frac{1}{2}\left(\frac{y}{x}\right)^2 = \ln|x| + C
$$

**Paso 9:** La **solución general** (que puede quedar en forma implícita) es

$$
\frac{y^2}{2x^2} = \ln|x| + C
$$

No es necesario despejar $y$ explícitamente; si no se pide lo contrario, se deja así.

</details>

</details>

## Repaso de los tres tipos de ecuaciones — [1:04:15](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3855s)

Hasta aquí se vieron tres tipos de ecuaciones diferenciales:

- **Variables separables:** se agrupan las variables con sus diferenciales y se integra miembro a miembro.
- **Lineales de primer orden:** $y'+P(x)y=Q(x)$; se resuelven con el reemplazo $y=u\,v$.
- **Homogéneas de primer orden:** $g(\lambda x,\lambda y)=g(x,y)$; se resuelven con el reemplazo $y=u\,x$.

## Construcción de la ecuación diferencial a partir de la solución general — [1:04:46](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3886s)

Problema inverso: dada la solución general (una expresión que relaciona $x$, $y$ y una constante arbitraria), construir la ecuación diferencial correspondiente.

Metodología: si la solución general depende de **una** constante arbitraria, la ecuación diferencial es de primer orden, así que se **deriva una vez** la ecuación; luego se combinan la ecuación original y la derivada para **eliminar la constante**. Si dependiera de dos constantes, la ecuación sería de segundo orden y habría que derivar dos veces para obtener tres ecuaciones y eliminar las dos constantes.

<details>
<summary>📝 Ejercicio 8 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=3917s">1:05:17</a>: ecuación diferencial de una familia de circunferencias</summary>

Hallar la ecuación diferencial que tiene por solución general a la familia de circunferencias

$$
(x - c)^2 + y^2 = 4
$$

(circunferencias de radio $2$ centradas en $(c,0)$ sobre el eje $x$).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Derivar la ecuación respecto de $x$ (recordando que $y$ es función de $x$; la derivada de la constante es cero).

$$
2(x - c) + 2\,y\,y' = 0
$$

**Paso 2:** Dividir por $2$ y despejar $(x-c)$.

$$
x - c = -\,y\,y'
$$

**Paso 3:** Reemplazar $(x-c)$ en la ecuación original para eliminar la constante $c$.

$$
(-\,y\,y')^2 + y^2 = 4
$$

**Paso 4:** El signo negativo es irrelevante por estar al cuadrado. La **ecuación diferencial** buscada es

$$
y^2\,(y')^2 + y^2 = 4
$$

</details>

</details>

## Soluciones singulares — [1:10:05](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4205s)

La ecuación diferencial de la familia de circunferencias es $y^2(y')^2+y^2=4$ y su solución general es $(x-c)^2+y^2=4$.

<details>
<summary>📝 Ejercicio 9 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4205s">1:10:05</a>: verificar la solución singular y=2</summary>

Verificar que la función $y=2$ es solución de la ecuación diferencial $y^2(y')^2+y^2=4$, y analizar de qué tipo de solución se trata.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Calcular la derivada.

$$
y = 2 \quad\Rightarrow\quad y' = 0
$$

**Paso 2:** Reemplazar en la ecuación diferencial.

$$
y^2\,(y')^2 + y^2 = 2^2\cdot 0 + 2^2 = 4
$$

**Paso 3:** Se obtiene la identidad $4=4$, por lo que $y=2$ es solución de la ecuación diferencial.

**Paso 4:** Esta solución **no** es general (no depende de una constante arbitraria) ni particular (no resulta de asignar un valor a la constante $c$ de la solución general: la recta $y=2$ no es ninguna de las circunferencias). Se la denomina **solución singular**. Geométricamente es la envolvente de la familia de soluciones, tangente a todas las circunferencias.

**Paso 5:** Análogamente, $y=-2$ (con $y'=0$) da $2^2\cdot 0 + (-2)^2 = 4$, por lo que también es solución singular.

</details>

</details>

## Trayectorias ortogonales — [1:14:51](https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4491s)

**Recordatorio geométrico:** si una recta forma un ángulo $\alpha$ con el eje $x$ y otra recta ortogonal a ella forma un ángulo $\beta$, entonces

$$
\tan\alpha = -\frac{1}{\tan\beta}
$$

Para dos curvas $y=f(x)$ e $y=g(x)$ cuyas rectas tangentes en un punto forman ángulos $\alpha$ y $\beta$, se tiene $\tan\alpha = f'(x)$ y $\tan\beta = g'(x)$. Por lo tanto, la condición de ortogonalidad entre las derivadas de dos familias de curvas cuyas gráficas se cortan a $90^\circ$ es

$$
f'(x) = -\frac{1}{g'(x)}
$$

Dos familias de curvas son **ortogonales** si sus respectivas rectas tangentes en cualquier punto de corte forman $90^\circ$. El objetivo es, dada una familia de curvas, encontrar la familia ortogonal.

<details>
<summary>📝 Ejercicio 10 — <a href="https://www.youtube.com/watch?v=ZXFsUIyYYvs&t=4844s">1:20:44</a>: trayectorias ortogonales a y = c x²</summary>

Dada la familia de parábolas

$$
y = c\,x^2
$$

hallar la familia de curvas ortogonales (comprobando que resultan elipses).

<details>
<summary>Ver resolución</summary>

**Paso 1:** Construir la ecuación diferencial de la primera familia. Como tiene una sola constante, derivar una vez respecto de $x$.

$$
y' = 2\,c\,x
$$

**Paso 2:** Combinar las dos ecuaciones para eliminar $c$. De la primera, $c=\dfrac{y}{x^2}$; reemplazar en la derivada.

$$
y' = 2\,\frac{y}{x^2}\,x = \frac{2y}{x}
$$

Esta es la ecuación diferencial de la familia 1.

**Paso 3:** Recordar que $y'=f'(x)$ y usar la relación de ortogonalidad $f'=-\dfrac{1}{g'}$. Reemplazar $y'$ por $-\dfrac{1}{y'}$ (las derivadas de la familia ortogonal).

$$
-\frac{1}{y'} = \frac{2y}{x}
$$

Esta es la ecuación diferencial de la familia 2 (ortogonal).

**Paso 4:** Resolver. Escribir $y'=\dfrac{dy}{dx}$; queda una ecuación con variables separables.

$$
-\frac{dx}{dy}\cdot\ \ldots \quad\Rightarrow\quad 2y\,dy = -x\,dx
$$

**Paso 5:** Integrar miembro a miembro.

$$
y^2 = -\frac{x^2}{2} + C
$$

**Paso 6:** Reordenar. Como la suma de cuadrados es positiva, la constante se toma positiva (se la llama $k^2$).

$$
\frac{x^2}{2} + y^2 = k^2
$$

Esta es la familia de **elipses** ortogonales a la familia de parábolas. Para cada valor de $k$ se obtiene una elipse distinta, y cualquier elipse corta a cualquier parábola siempre a $90^\circ$.

</details>

</details>

**Resumen del método de trayectorias ortogonales:**

- **Paso 1:** construir la ecuación diferencial que tiene por solución general la familia dada (derivar y eliminar la constante).
- **Paso 2:** reemplazar $y'$ por $-\dfrac{1}{y'}$ para obtener la ecuación diferencial de la familia ortogonal.
- **Paso 3:** resolver esa ecuación diferencial con alguno de los métodos vistos; su solución general es la familia de curvas ortogonales.
