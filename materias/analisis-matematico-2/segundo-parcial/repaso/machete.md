# MACHETE MAESTRO — AM2 · Segundo parcial

> Fórmulas, recetas con sus pasos puente y resultados verificados para autocorregirte. Orden: identificar → plantear → integrar.
> Cubre los 4 prácticos (P1–P4) y la parte práctica de T1/T2 según el patrón real de **17 parciales** (`examenes/INDICE.md`), **incluido el 2026-07-08 — el examen que estás recuperando**.

---

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Herramienta |
|---|---|
| volumen del cuerpo | $V=\iiint_V dV$ (cilíndricas/esféricas) → §2 |
| masa del cuerpo con densidad $\delta$ | $m=\iiint_V \delta\,dV$ → §2 |
| área de la región plana | $A=\iint_D dA$, o Green: $\tfrac12\oint_{C^+}(x\,dy-y\,dx)$ → §4 |
| área de la superficie | $A=\iint_D \sqrt{1+g_x^2+g_y^2}\,dA$ → §6 |
| longitud de la curva | $L=\int_a^b \lVert\lambda'(t)\rVert\,dt$ → §3 |
| circulación / trabajo | $\int_C f\cdot d\lambda$ (§3); ¿cerrada y plana? → Green (§4); ¿conservativo? → $\varphi(B)-\varphi(A)$ (§5) |
| función potencial | verificar $P_y=Q_x$ (jacobiana simétrica) → armar $\varphi$ → §5 |
| flujo a través de S | $\Phi=\iint_S f\cdot\hat n\,dS$ (§6); ¿S cerrada? → Gauss (§7) |
| **me dan $\operatorname{rot}f$ y no me dan $f$** | Stokes sí o sí → §8 |
| área$(D^*)$ sabiendo área$(D)$ | jacobiano de la transformación → §1 |
| integral en polares: graficar / pasar a cartesianas | receta T2 polar → §1 |
| hallar $g$ para que sea conservativo | plantear $P_y=Q_x$ → EDO en $g$ (§5 + §9) |
| hallar $g$ para que sea solenoidal | plantear $\operatorname{div}f=0$ → EDO en $g$ (§7 + §9) |
| flujo = volumen del cuerpo (para todo radio) | $\operatorname{div}f\equiv1$ → EDO en $g$ → §7 |
| $y''+ay'+by=h(x)$ | característica + $y_p$ por coeficientes indeterminados → §9 |
| circulación con curva fea / rotor fácil | Stokes con superficie plana → §8 |

---

## 1 · Cambios de variables (la base de todo)

**Teorema (cambio de variables):**

$$
\iint_D f\,dx\,dy=\iint_{D^*} f\big(x(u,v),y(u,v)\big)\,|J|\,du\,dv,\qquad J=\det\frac{\partial(x,y)}{\partial(u,v)}
$$

- Truco: $J_{(x,y)\to(u,v)}=1/J_{(u,v)\to(x,y)}$ (invertís el que sea más fácil).
- Transformación lineal: $J$ es constante y $\text{área(imagen)}=|\det|\cdot\text{área(original)}$.

**El teórico reciclado ×6** (2016-07-06, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28, **2026-07-08**): dan la transformación $(x,y)=T(u,v)$ — es decir, $T$ va **de $UV$ hacia $XY$** — y el área de $D$ (en el plano $XY$); piden el área de $D^*$ (en $UV$). Como $T$ manda $D^*$ en $D$:

$$
\text{área}(D)=\lvert J\rvert\cdot\text{área}(D^*)\;\Rightarrow\;\text{área}(D^*)=\frac{\text{área}(D)}{\lvert J\rvert},\qquad J=\det\begin{pmatrix}x_u&x_v\\ y_u&y_v\end{pmatrix}
$$

| Fecha | $T(u,v)$ | $J$ | Dato | área$(D^*)$ |
|---|---|---|---|---|
| 2022-12-02 T1 · 2022-12-16 T2 | $(v-2u,\;u+v)$ | $-3$ | área$(D)=9$ | $3$ |
| 2023-07-28 T1 | $(u+3v,\;2u+2v)$ | $-4$ | área$(D)=6$ | $3/2$ |
| 2016-07-06 T1 | $(u+2v,\;2u+v)$ | $-3$ | área$(D)=6$ | $2$ |
| **2026-07-08 T2** — la MISMA $T$ de 2016 | $(u+2v,\;2u+v)$ | $-3$ | área$(D)=12$ | $4$ |

- En el resultado va **siempre $\lvert J\rvert$**: un área jamás da negativa. (Fijate que los cuatro $J$ reales son negativos — el signo se descarta.)
- Variante V/F (2023-07-14 T1): dan $\iint_{D^*}(\dots)\,du\,dv$ y afirman cuánto vale $\iint_D x\,dx\,dy$. Herramienta: la misma igualdad de arriba con $\lvert J\rvert$, reemplazando $x=x(u,v)$; compará el integrando que te dan contra el que corresponde antes de contestar.

| Sistema | Fórmulas | $\lvert J\rvert$ |
|---|---|---|
| Polares | $x=\rho\cos\varphi$, $y=\rho\operatorname{sen}\varphi$ | $\rho$ → $dA=\rho\,d\rho\,d\varphi$ |
| Cilíndricas | polares + $z=z$ | $\rho$ → $dV=\rho\,d\rho\,d\varphi\,dz$ |
| Esféricas | $x=\rho\operatorname{sen}\theta\cos\varphi$, $y=\rho\operatorname{sen}\theta\operatorname{sen}\varphi$, $z=\rho\cos\theta$ | $\rho^2\operatorname{sen}\theta$ → $dV=\rho^2\operatorname{sen}\theta\,d\rho\,d\theta\,d\varphi$ |

($\theta$ = ángulo desde el eje $z^+$, va de $0$ a $\pi$; $\varphi$ = ángulo en el plano $xy$)

**Curvas polares para reconocer al toque:**

| En polares | En cartesianas |
|---|---|
| $\rho=R$ | circunferencia centro $O$, radio $R$ |
| $\varphi=\text{cte}$ | semirrecta desde $O$ |
| $\rho=2a\cos\varphi$ | $x^2+y^2=2ax$: circunferencia centro $(a,0)$, radio $a$ |
| $\rho=2a\operatorname{sen}\varphi$ | $x^2+y^2=2ay$: circunferencia centro $(0,a)$, radio $a$ |

(el pasaje: multiplicar ambos lados por $\rho$ y usar $\rho^2=x^2+y^2$)

**Superficies en esféricas:**

| Objeto | Ecuación esférica |
|---|---|
| esfera $x^2+y^2+z^2=R^2$ | $\rho=R$ |
| cono $z=\sqrt{x^2+y^2}$ | $\theta=\pi/4$ |
| semiespacio $z\ge0$ | $\theta\in[0,\pi/2]$ |

**Receta T2 "graficar y pasar a cartesianas" (2024-07-12, sin-fecha):**

1. $\rho_{\max}=2\cos\varphi$ → circunferencia $x^2+y^2=2x$; el rango de $\varphi$ dice qué porción ($[0,\pi/2]$ = mitad superior).
2. $\rho^n\,d\rho\,d\varphi=\rho^{n-1}\cdot(\rho\,d\rho\,d\varphi)$ → integrando cartesiano $(x^2+y^2)^{(n-1)/2}$.
3. Checksum:

$$
\int_0^{\pi/2}\!\!\int_0^{2\cos\varphi}\rho^3\,d\rho\,d\varphi=\int_0^2\!\!\int_0^{\sqrt{2x-x^2}}(x^2+y^2)\,dy\,dx=\frac{3\pi}{4}
$$

---

## 2 · P1: volumen, masa, baricentro

**Receta volumen:** dibujar → proyectar sobre $xy$ →

$$
V=\iint_D\big(z_{\text{techo}}-z_{\text{piso}}\big)\,dA
$$

- La proyección $D$ es **donde techo ≥ piso** (igualalos para encontrar el borde).
- Restá techo − piso ANTES de integrar: muchas veces se cancelan términos y queda algo redondo.

**Ejemplo real completo (P1 2026-07-08):** volumen de $(x-1)^2+y^2\le z\le 5-2x$.

1. Proyección = donde techo ≥ piso: $(x-1)^2+y^2\le 5-2x$ → $x^2-2x+1+y^2\le 5-2x$ → los $-2x$ se cancelan → $x^2+y^2\le 4$.
2. Integrando = techo − piso: $5-2x-(x-1)^2-y^2=4-x^2-y^2=4-\rho^2$.
3. Polares:

$$
V=\int_0^{2\pi}\!\!\int_0^2(4-\rho^2)\,\rho\,d\rho\,d\varphi=2\pi\Big(2\rho^2-\tfrac{\rho^4}{4}\Big)\Big|_0^2=\boxed{8\pi}
$$

**Masa:** $m=\iiint_V\delta\,dV$. Densidad "proporcional a la distancia…":

- al eje $z$ → $\delta=k\sqrt{x^2+y^2}=k\rho$ (cilíndricas)
- al plano $xy$ → $\delta=k|z|$
- al origen → $\delta=k\rho$ (esféricas)

**Baricentro:** $\bar x=\dfrac1m\iiint_V x\,\delta\,dV$ (ídem $y,z$); región plana: $\bar x=\dfrac1A\iint_D x\,dA$.

- Homogéneo → $\delta$ se cancela. Simetría → esa coordenada es $0$.
- Checksum real (P1 2017-07-05): media elipse $\tfrac{x^2}4+y^2\le1$, $y\ge0$ → $A=\pi$, $\bar y=\dfrac{4}{3\pi}$, baricentro $\big(0,\tfrac{4}{3\pi}\big)$.

**Superficies que aparecen siempre:**

| Ecuación | Qué es |
|---|---|
| $z=x^2+y^2$ | paraboloide, vértice $O$, abre hacia arriba |
| $z=(x-1)^2+y^2$ | el mismo paraboloide corrido: vértice $(1,0,0)$ — completá cuadrados si viene desarrollado |
| $z=\sqrt{x^2+y^2}$ | semicono superior |
| $x^2+y^2+z^2=R^2$ | esfera |
| $x^2+y^2=R^2$ | cilindro vertical |
| $x^2+y^2=2ax$ | cilindro vertical corrido: $(x-a)^2+y^2=a^2$ |

**Intersecciones típicas** (para encontrar la proyección):

- paraboloide ∩ plano $z=k$ → circunferencia $x^2+y^2=k$
- cono ∩ esfera de radio $R$ → $2z^2=R^2$: circunferencia en $z=R/\sqrt2$
- **cuádrica ∩ cono/paraboloide** → escribí las dos en función de $\rho$ y $z$, sustituí una en la otra y resolvé la cuadrática. Ejemplo real (P1 2016-07-06 = 2023-07-28): elipsoide $2\rho^2+z^2=3$ con cono $z=\rho$ → $2z^2+z^2=3$ → $z_0=\rho_0=1$: se cortan en la circunferencia $\rho=1$ a altura $z=1$ (y esa circunferencia define la proyección $\rho\le1$).

**Elección de coordenadas:**

- cilindro / paraboloide / cono con tapa plana → **cilíndricas**
- esfera sola, o cono ∩ esfera → **esféricas**

**Volúmenes conocidos (para Gauss exprés):** esfera $\tfrac43\pi R^3$; cilindro $\pi R^2 h$; cono $\tfrac13\pi R^2 h$; tetraedro de interceptos $(a,0,0),(0,b,0),(0,0,c)$: $V=\tfrac{abc}{6}$.

---

## 3 · Curvas: parametrización, longitud, circulación

| Curva | $\lambda(t)$ | $t$ |
|---|---|---|
| segmento $A\to B$ | $A+t(B-A)$ | $[0,1]$ |
| circunferencia $x^2+y^2=R^2$ | $(R\cos t,\;R\operatorname{sen}t)$ | $[0,2\pi]$ antihorario |
| circunferencia corrida $(x-a)^2+(y-b)^2=R^2$ | $(a+R\cos t,\;b+R\operatorname{sen}t)$ | $[0,2\pi]$ |
| elipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ | $(a\cos t,\;b\operatorname{sen}t)$ | $[0,2\pi]$ |
| gráfica $y=g(x)$ | $(t,\;g(t))$ | $[x_0,x_1]$ |
| intersección de 2 superficies | el parámetro es la variable de la que dependen las otras dos; despejalas en cadena | de $A$ a $B$ |

- Longitud: $L=\int_a^b\lVert\lambda'(t)\rVert\,dt$. Checksum real (P3 2017-07-05): hélice $\lambda(t)=(2\cos t,2\operatorname{sen}t,2t)$ de $(2,0,0)$ a $(-2,0,2\pi)$: $\lVert\lambda'\rVert=\sqrt{4+4}=2\sqrt2$ cte → $L=2\sqrt2\,\pi$.
- Circulación / trabajo: $\int_C f\cdot d\lambda=\int_a^b f(\lambda(t))\cdot\lambda'(t)\,dt$
- Sentido: $\lambda(a)$ debe ser el punto inicial pedido; si va al revés → cambiar el signo del resultado.

**Ejemplo real de "intersección de 2 superficies" (P2 2016-11-25):** trabajo de $f=(xy,\,y^2,\,xz)$ sobre $z=x+y$ ∩ $x=y^2$, de $(0,0,0)$ a $(4,2,6)$.

1. Parámetro: $y=t$ (porque $x=y^2$ me da $x$, y con eso $z=x+y$ me da $z$) → $\lambda(t)=(t^2,\;t,\;t^2+t)$, $t:0\to2$ (mirá las $y$ de $A$ y $B$).
2. $\lambda'=(2t,\;1,\;2t+1)$; $f(\lambda(t))=(t^3,\;t^2,\;t^4+t^3)$.
3. $W=\displaystyle\int_0^2\big(2t^4+t^2+(t^4+t^3)(2t+1)\big)\,dt=\int_0^2(2t^5+5t^4+t^3+t^2)\,dt=\boxed{60}$

**Antes de integrar, SIEMPRE mirar si $f$ es conservativo** → $\int_C f\cdot d\lambda=\varphi(B)-\varphi(A)$; cerrada → $0$.

- El atajo que vale puntos (P3 2019-11-21): $f=(z,y,x)$ sobre $x^2+y^2=4$ ∩ $z=x$, de $(2,0,2)$ a $(-2,0,-2)$. Jacobiana simétrica ✓ → conservativo → $\varphi=xz+\tfrac{y^2}2$ → $W=\varphi(-2,0,-2)-\varphi(2,0,2)=4-4=\boxed{0}$. Cero integrales, cero parametrización.
- Si no es conservativo, igual puede simplificarse solo: en P2 2022-12-02 ($f=(xy,-y^2,z^2)$ sobre $z=9-x^2$, $z=y$, de $(3,0,0)$ a $(0,9,9)$, parámetro $x=t$) los términos de $Q$ y $R$ se cancelan entre sí y queda $\int_3^0(9t-t^3)\,dt=\boxed{-\tfrac{81}4}$.

---

## 4 · Teorema de Green (T1 casi fijo)

$$
\oint_{C^+}(P,Q)\cdot d\lambda=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA
$$

Hipótesis para nombrar: $C$ cerrada simple, frontera de $D$, sentido antihorario ($C^+$), $f\in C^1$ en $D$.

- Corolario área: $A=\dfrac12\oint_{C^+}(x\,dy-y\,dx)=\oint_{C^+}x\,dy=-\oint_{C^+}y\,dx$
- Curva paramétrica $\lambda(t)=(x(t),y(t))$: $A=\dfrac12\int_a^b\big(x\,y'-y\,x'\big)\,dt$ — así piden las áreas encerradas (P2 2023-07-14, P1 sin-fecha).
- Sentido horario → cambia el signo.

**La familia reciclada sobre $x^2\le y\le x$** (recinto parábola–recta entre $x=0$ y $x=1$; integrales listas: $\iint_D dA=\tfrac16$, $\iint_D 2x\,dA=\tfrac16$, $\iint_D 2xy\,dA=\tfrac1{12}$):

| Campo | $Q_x-P_y$ | Circulación antihoraria | Fechas |
|---|---|---|---|
| $f=\big(\tfrac{xy^2}{2},\,\tfrac{3x^2y}{2}\big)$ | $2xy$ | $1/12$ | 2019-11-21, 2022-07-15, 2024-07-12 |
| $f=(xy^2,\,3x^2y)$ | $4xy$ | $1/6$ | sin-fecha |
| $f=\big(x^2+\varphi(y-x),\,x^2-\varphi(y-x)\big)$, $\varphi\in C^1$ desconocida | $2x$ (las $\varphi$ se cancelan) | $1/6$ | 2017-11-16 |

**Función desconocida en el campo:** si $f$ trae una $g$ o $\varphi$ que no te dan y piden circulación cerrada → Green: las incógnitas **mueren en $Q_x-P_y$**. Variante 2025-07-18 (T1): $f=(y+g(x),\,2x+g(y))$ sobre la frontera de $x^2+y^2\le2y$ → $Q_x-P_y=2-1=1$ → circulación $=1\cdot\text{área}(D)=\boxed{\pi}$ (antihorario).

- Regla exprés: $Q_x-P_y=\text{cte}$ → circulación $=\text{cte}\cdot\text{área}(D)$.

---

## 5 · Conservativos y función potencial (cae en el 100%)

- $f$ conservativo en $D$ ⇔ existe $\varphi$ con $\nabla\varphi=f$ ⇒ $\int_C f\cdot d\lambda=\varphi(B)-\varphi(A)$ (independiente del camino; cerrada → $0$).
- **Condición necesaria:** jacobiana simétrica. 2D: $P_y=Q_x$. 3D: $P_y=Q_x$, $P_z=R_x$, $Q_z=R_y$ (⇔ $\operatorname{rot}f=\bar 0$).
- **Condición suficiente:** simetría + $D$ simplemente conexo + $f\in C^1$.
- Ojo fino: simplemente conexo es **suficiente, no necesario** — puede fallar y el potencial existir igual (pasó en el T1 real del 2026-07-08, abajo).

**Armar $\varphi$ — Método 1: ecuación diferencial total exacta** (apunte 11):

1. $\varphi=\int P\,dx+c(y,z)$ (la "constante" de integrar en $x$ es una función de las otras variables)
2. Derivar respecto de $y$, igualar a $Q$ → sale $c_y$ → integrar → $c(y,z)=\dots+d(z)$
3. Derivar respecto de $z$, igualar a $R$ → sale $d(z)$.
4. **Verificar $\nabla\varphi=f$** antes de seguir (recomendado explícitamente para el parcial).
5. Dato tipo $\varphi(1,2)=11$ → ajustar la constante al final.

**Armar $\varphi$ — Método 2: primitiva por integral de línea** (segmento del origen a $(x,y)$, apunte 11):

$$
\varphi(x,y)=\int_0^1 f(t\,x,\;t\,y)\cdot(x,y)\,dt + C
$$

- Limitación: el segmento $0\to(x,y)$ tiene que estar dentro del dominio de $f$; si $f$ no está definida en el origen → **no aplica**, usar Método 1.
- Cómodo cuando las componentes son polinomios: la integral en $t$ sale directa.

**El T1 real del 2026-07-08, resuelto:** ¿$f=\Big(\dfrac{2x}{x^2+y^2},\,\dfrac{2y}{x^2+y^2}\Big)$ admite potencial?

1. Simetría: $P_y=Q_x=\dfrac{-4xy}{(x^2+y^2)^2}$ ✓.
2. Dominio $\mathbb R^2-\{(0,0)\}$: NO simplemente conexo y el Método 2 no corre (el segmento arranca en el origen, donde $f$ no existe). Pero el Método 1 construye $\varphi$ igual:

$$
\varphi=\int\frac{2x}{x^2+y^2}\,dx=\ln(x^2+y^2)+c(y);\qquad \varphi_y=\frac{2y}{x^2+y^2}+c'(y)=Q\Rightarrow c'=0\Rightarrow\boxed{\varphi=\ln(x^2+y^2)+C}
$$

3. Respuesta: **sí admite** (y la verificás derivando: $\nabla\varphi=f$ ✓ en todo el dominio).

**Variante "hallar $g(x)$"** (2023-07-14, 2025-07-18, 2022-12-02): plantear $P_y=Q_x$ (o $\operatorname{div}f=0$) → **suele quedar una EDO de 2° orden en $g$** → resolverla con la receta de §9; los datos tipo $f(0,1)=(0,7)$ fijan las constantes.

- Checksum 2023-07-14 (completo): $f=(x^2-4y\,g(x),\;g'(x)-x+y)$ → $P_y=Q_x$: $-4g=g''-1$ → $g''+4g=1$ → $g=C_1\cos 2x+C_2\operatorname{sen}2x+\tfrac14$. Datos $f(0,1)=(0,7)$: 1ª componente $-4g(0)=0$ → $g(0)=0$ → $C_1=-\tfrac14$; 2ª componente $g'(0)+1=7$ → $g'(0)=6$ → $C_2=3$. $\boxed{g=3\operatorname{sen}2x-\tfrac14\cos2x+\tfrac14}$

**T2 reciclado ×3** (2022-12-02, 2022-12-16, 2023-07-14): $f=(2xy+2x\,g'(x^2),\;x^2)$, circulación de $(-2,4)$ a $(2,5)$.

1. Simetría: $P_y=2x=Q_x$ ✓ — conservativo aunque $g$ sea desconocida.
2. Armo $\varphi$ empezando por la componente fácil: $\varphi=\int Q\,dy=x^2y+c(x)$; derivo: $\varphi_x=2xy+c'(x)$, igualo a $P$ → $c'(x)=2x\,g'(x^2)$ → $c(x)=g(x^2)$ (regla de la cadena al revés). $\varphi=x^2y+g(x^2)$.
3. Los dos extremos tienen $x^2=4$ → la $g(4)$ se resta consigo misma: $\varphi(2,5)-\varphi(-2,4)=(20+g(4))-(16+g(4))=\boxed{4}$

---

## 6 · Superficies: $dS$, área y flujo (94%)

$$
dS=\lVert r_u\times r_v\rVert\,du\,dv
$$

$$
\text{gráfica } z=g(x,y):\quad dS=\sqrt{1+g_x^2+g_y^2}\,dA
$$

- Área: $A=\iint_S dS$. Esfera parametrizada: $dS=R^2\operatorname{sen}\theta\,d\theta\,d\varphi$.
- Flujo: $\Phi=\iint_S f\cdot\hat n\,dS=\iint_D f\big(r(u,v)\big)\cdot(r_u\times r_v)\,du\,dv$ — la normal SIN normalizar ya trae el $dS$.

**Normales listas para usar:**

| Superficie | $N$ (sin normalizar) |
|---|---|
| gráfica $z=g(x,y)$ | $(-g_x,\,-g_y,\,1)$ apunta hacia $z^+$ |
| plano $ax+by+cz=d$ | $(a,b,c)$ |
| esfera centro $O$ | $(x,y,z)$ saliente |
| cilindro $x^2+y^2=R^2$ | $(x,y,0)$ saliente |
| cilindro corrido $(x-a)^2+y^2=R^2$ | $(x-a,\,y,\,0)$ saliente |

- Flujo por gráfica, todo junto: $\Phi=\iint_D\big(-P\,g_x-Q\,g_y+R\big)\,dA$
- La orientación la fija el enunciado ("componente $z$ positiva", "saliente", "según $y$ creciente") → elegir el signo de $N$ que cumpla.
- Checksums de área: cono $z=\sqrt{x^2+y^2}$ bajo $z=2$ (P2 2019-11-21): $\sqrt2\cdot\text{área}(x^2+y^2\le4)=4\sqrt2\,\pi$. Y P2 2026-07-08: $z=x^2-y$ sobre $\lvert y\rvert\le x\le1$: $\sqrt{2+4x^2}$ no depende de $y$ → $\int_0^1 2x\sqrt{2+4x^2}\,dx=\sqrt6-\tfrac{\sqrt2}3$.

**El reciclado ×4** (2016-07-06, 2017-07-05, 2017-11-16, 2022-11-24): flujo de $f=(y^2,\,z^2+x^2,\,x^2)$ a través del plano $y=x$ limitado por $x^2+y^2+2z^2\le2$.

1. Parametrizo el plano con sus variables libres: $r(x,z)=(x,\,x,\,z)$ → $N=r_x\times r_z=(1,-1,0)$.
2. Dominio: meto $y=x$ en la cota → $2x^2+2z^2\le2$ → $x^2+z^2\le1$ (disco unitario).
3. $f\cdot N=y^2-(z^2+x^2)$, y con $y=x$: $x^2-z^2-x^2=-z^2$.
4. $\Phi=\displaystyle\iint_{x^2+z^2\le1}(-z^2)\,dA=-\int_0^{2\pi}\!\!\int_0^1\rho^2\operatorname{sen}^2\theta\,\rho\,d\rho\,d\theta=-\pi\cdot\tfrac14=\boxed{-\pi/4}$ (con la normal opuesta: $+\pi/4$)

**Flujo directo por cilindro corrido (P3 2026-07-08):** $f=(-y,\,x,\,xz)$ a través de $x^2+y^2=2x$ (abierta) con $z\le4-x^2-y^2$, 1er octante.

1. Completo cuadrados: $(x-1)^2+y^2=1$ → $r(t,z)=(1+\cos t,\;\operatorname{sen}t,\;z)$; 1er octante → $t\in[0,\pi]$ (para que $y\ge0$).
2. Techo sobre el cilindro: $z\le4-(x^2+y^2)=4-2x=2-2\cos t$; piso $z=0$.
3. $N=r_t\times r_z=(\cos t,\;\operatorname{sen}t,\;0)$ — es $(x-1,y,0)$, saliente. $f\cdot N=-y\cos t+x\operatorname{sen}t=\operatorname{sen}t$.
4. $\Phi=\displaystyle\int_0^\pi\operatorname{sen}t\,(2-2\cos t)\,dt=4-0=\boxed{4}$ (saliente; con la entrante, $-4$).

---

## 7 · Divergencia y Gauss

- $\operatorname{div}f=P_x+Q_y+R_z$; **solenoidal** ⇔ $\operatorname{div}f=0$.

**Teorema de la divergencia** ($S$ cerrada, orientada saliente, $V$ el sólido encerrado, $f\in C^1$):

$$
\iint_{\partial V}f\cdot\hat n\,dS=\iiint_V\operatorname{div}f\,dV
$$

- $\operatorname{div}f=\text{cte}$ → $\Phi=\text{cte}\cdot\operatorname{Vol}(V)$ → usar los volúmenes conocidos de §2. Checksums reales: 2023-07-28 P3 ($\operatorname{div}=2$, tetraedro de interceptos $6,4,3$ → $V=12$) → $\Phi=24$; 2024-07-12 P3 ($\operatorname{div}=3$, $V=\tfrac83$) → $\Phi=8$; 2015-11-25 P3 ($\operatorname{div}=6$, medio tetraedro $V=\tfrac23$) → $\Phi=4$.
- Si $\operatorname{div}$ no es constante, igual suele ser corta: 2022-07-15 P3: $\operatorname{div}=2y$ sobre el tetraedro de interceptos $2,1,3$ → $\Phi=2\,V\bar y=2\cdot1\cdot\tfrac14=\tfrac12$ (el baricentro del tetraedro está en $\tfrac b4$).
- Componente desconocida que **no depende de su propia variable** → aporta $0$ a la div: $f=(g(y,z),\,h(x,z),\,z)$ → $\operatorname{div}f=1$ (P3 sin-fecha); $f=(x-y-z,\,y-x-z,\,g(x,y))$ → $\operatorname{div}f=2$ (P3 2023-07-28).
- "Hallar $g$ solenoidal": $\operatorname{div}f=0$ → queda una EDO en $g$ (puede ser de 2° orden → §9). Checksum 2025-07-18: $f=(x+g'(x),\,y\,g(x),\,y^2-xz)$ → $1+g''+g-x=0$ → $g''+g=x-1$ → con $f(0,1,0)=(1,1,1)$: $g=2\cos x+x-1$.
- **"Flujo = volumen para todo radio"** (P4 2022-12-02): $\iiint\operatorname{div}f\,dV=\operatorname{Vol}(V)$ para toda esfera ⟺ $\operatorname{div}f\equiv1$. Con $f=(x+g'(x),\,y\,g'(x),\,-2z\,g(x))$: $1+g''+g'-2g=1$ → $g''+g'-2g=0$ → con $f(0,0,1)=(2,0,0)$ ($g(0)=0$, $g'(0)=2$): $\boxed{g=\tfrac23\big(e^{x}-e^{-2x}\big)}$

**Superficie abierta vía Gauss** (P4 2014-11-28, P3 sin-fecha, P4 2025-07-18): cerrar con una tapa $T$ y despejar:

$$
\Phi_S=\iiint_V\operatorname{div}f\,dV-\Phi_T \quad(\text{todo saliente})
$$

- Tapa plana $z=k$: $\hat n=(0,0,\pm1)$ → $\Phi_T=\pm\iint_D R(x,y,k)\,dA$.
- Al final, revisá si la orientación PEDIDA en $S$ coincide con la saliente; si no, un signo $-$ global.
- Checksum sin-fecha (P3): $f=(g(y,z),h(x,z),z)$, $S$: $z=1+x^2+y^2$ con $z\le2$, $\hat n$ hacia $z^+$. $\operatorname{div}=1$ → $\iiint=V=\tfrac\pi2$; tapa $z=2$ ($x^2+y^2\le1$, saliente $=+\hat k$): $\Phi_T=2\cdot\pi=2\pi$. En el paraboloide el saliente apunta hacia abajo (opuesto al pedido): $\Phi_{S}^{\,z^+}=\Phi_T^{\,z^+}-\iiint=2\pi-\tfrac\pi2=\boxed{\tfrac{3\pi}2}$

---

## 8 · Rotor y Stokes

$$
\operatorname{rot}f=\nabla\times f=\begin{vmatrix}\hat i&\hat j&\hat k\\ \partial_x&\partial_y&\partial_z\\ P&Q&R\end{vmatrix}=(R_y-Q_z,\;P_z-R_x,\;Q_x-P_y)
$$

- En el plano: rotor "escalar" $=Q_x-P_y$ (la 3ª componente).
- Identidades: $\operatorname{rot}(\nabla\varphi)=\bar0$; $\operatorname{div}(\operatorname{rot}f)=0$.

**Teorema de Stokes** ($C=\partial S$, orientaciones coherentes — mano derecha: pulgar $=\hat n$, dedos $=C$):

$$
\oint_{C^+}f\cdot d\lambda=\iint_S\operatorname{rot}f\cdot\hat n\,dS
$$

- Uso típico: circulación sobre curva fea → tomar $S$ **plana** con esa frontera ($\hat n$ constante) → $\iint_D\operatorname{rot}f\cdot\hat n\,dA$.

**Si te dan $\operatorname{rot}f$ y no $f$: Stokes obligado** (2022-12-16 P1, sin-fecha P2 — la curva es la intersección de dos paraboloides):

1. Igualá las dos superficies → sale $\rho_0$ y $z_0$: la curva es la circunferencia $x^2+y^2=\rho_0^2$ a altura $z_0$.
2. Tomá como $S$ el **disco plano** $z=z_0$, $x^2+y^2\le\rho_0^2$, con $\hat n=(0,0,\pm1)$ según la orientación pedida.
3. $\oint=\pm\iint_D\big(\text{3ª componente de }\operatorname{rot}f\big)\big|_{z=z_0}\,dA$ — los términos impares ($x$, $y$, $xy$) integran $0$ sobre el disco.

- Checksum 2022-12-16 P1: $\operatorname{rot}f=(x,\,x^2-2x,\,-z)$, curva $z=3-x^2-y^2$ ∩ $z=2x^2+2y^2$ → $3-\rho^2=2\rho^2$ → $\rho_0=1$, $z_0=2$ → $\oint=\iint(-2)\,dA=\boxed{-2\pi}$ con $\hat n=+\hat k$ (la otra orientación: $+2\pi$).
- Checksum sin-fecha P2: $\operatorname{rot}f=(-x^2,\,3y-x,\,4z^2-3xy)$, curva $z=3(x^2+y^2)$ ∩ $z=4-(x^2+y^2)$ → $\rho_0=1$, $z_0=3$ → $\oint=\iint(36-3xy)\,dA=36\pi-0=\boxed{36\pi}$ ($\hat n=+\hat k$).

**El reciclado ×2 de circulación por Stokes** (2016-07-06, 2023-07-28): $f=(yz,\,2xz,\,xy)$ sobre la intersección de $z=x^2+4y^2$ con $z=8-x^2-4y^2$ (en 2023: $4x^2+y^2$ y $8-4x^2-y^2$).

1. Igualo: la curva es la elipse $x^2+4y^2=4$ (resp. $4x^2+y^2=4$) a altura $z_0=4$; su interior plano tiene área $\pi\cdot2\cdot1=2\pi$ en ambas versiones.
2. $\operatorname{rot}f=(-x,\,0,\,z)$ → sobre el plano $z=4$ con $\hat n=+\hat k$: $\operatorname{rot}f\cdot\hat n=z=4$.
3. $\oint=4\cdot2\pi=\boxed{8\pi}$ (antihoraria vista desde $z^+$; al revés, $-8\pi$).

---

## 9 · EDO lineales de 2° orden (cae en 11 de 17 — P4 típico, a veces P1 o T2)

Forma $y''+ay'+by=h(x)$. Solución: $y=y_H+y_p$.

**1) Homogénea — ecuación característica** $r^2+ar+b=0$:

| Raíces | $y_H$ |
|---|---|
| $r_1\ne r_2$ reales | $C_1e^{r_1x}+C_2e^{r_2x}$ |
| $r$ doble | $(C_1+C_2x)\,e^{rx}$ |
| $\alpha\pm\beta i$ | $e^{\alpha x}\big(C_1\cos\beta x+C_2\operatorname{sen}\beta x\big)$ |

**2) Particular — coeficientes indeterminados:**

| $h(x)$ | candidato $y_p$ |
|---|---|
| polinomio de grado $n$ | polinomio COMPLETO de grado $n$ |
| $Ce^{kx}$ | $Ae^{kx}$ |
| $\cos\omega x$ y/o $\operatorname{sen}\omega x$ | $A\cos\omega x+B\operatorname{sen}\omega x$ (siempre los dos) |
| suma de varios | suma de candidatos (superposición) |

- **Resonancia:** si el candidato (o parte) ya está en $y_H$ → multiplicar por $x$ (raíz doble → por $x^2$).
- **Caso sin término en $y$** ($b=0$ ⇒ $r=0$ es raíz): con $h$ polinomio el candidato sube un grado: $h=8$ → $y_p=Ax$; $h=2-6x$ → $y_p=Ax+Bx^2$.

**3) Condiciones iniciales:** aplicar $y(x_0)$, $y'(x_0)$ en la solución **completa** $y_H+y_p$ → sistema 2×2 en $C_1,C_2$.

- "Recta tangente $y=mx+c$ en $x_0$" → $y(x_0)=mx_0+c$ **y** $y'(x_0)=m$. Así vino en los P4 de sin-fecha y del **2026-07-08** — resueltos en §10.

---

## 10 · Resultados verificados (autocorrección)

> Problemas reales de parcial con su resultado, recalculado y verificado a mano desde `examenes/INDICE.md` (2026-07-17). Practicalos desde el enunciado real y chequeá acá si llegaste. Los enunciados marcados «≈» en el índice (escaneos dudosos) quedaron afuera a propósito.

**Las 11 EDOs reales de parcial con su solución general:**

| Examen | EDO | Solución general |
|---|---|---|
| 2015-11-25 | $y''+y'-2y=\cos x$ | $y=C_1e^{x}+C_2e^{-2x}+\frac{\operatorname{sen}x-3\cos x}{10}$ |
| 2016-07-06 | $y''+4y'=8$ | $y=C_1+C_2e^{-4x}+2x$ |
| 2016-11-25 | $y''+2y'=4x$ | $y=C_1+C_2e^{-2x}+x^2-x$ |
| 2019-11-21 | $y''-6y'+9y=2x$ | $y=(C_1+C_2x)e^{3x}+\frac{2}{9}x+\frac{4}{27}$ |
| 2022-07-15 | $y''-2y'+5y=2x$ | $y=e^{x}(C_1\cos 2x+C_2\operatorname{sen}2x)+\frac{2}{5}x+\frac{4}{25}$ |
| 2022-11-24 | $y''-4y'+13y=26$ | $y=e^{2x}(C_1\cos 3x+C_2\operatorname{sen}3x)+2$ |
| 2023-07-28 | $y''-3y'=2-6x$ | $y=C_1+C_2e^{3x}+x^2$ |
| 2024-07-12 | $y''-2y'+5y=10$ | $y=e^{x}(C_1\cos 2x+C_2\operatorname{sen}2x)+2$ |
| 2025-07-18 | $y''-y=4$ | $y=C_1e^{x}+C_2e^{-x}-4$ |
| **2026-07-08** | $y''-y=x+1$ | $y=C_1e^{x}+C_2e^{-x}-x-1$ |
| sin-fecha | $y''-6y'+9y=9x$ | $y=(C_1+C_2x)e^{3x}+x+\frac{2}{3}$ |

**Las dos particulares "con recta tangente en $(0,y_0)$", resueltas** (formato que ya se repitió — §9):

- sin-fecha: tangente $y=x+2$ → $y(0)=2$, $y'(0)=1$ → $C_1=\tfrac43$, $C_2=-4$ → $y=\big(\tfrac43-4x\big)e^{3x}+x+\tfrac23$
- **2026-07-08**: tangente $x+y=2$ → $y(0)=2$, $y'(0)=-1$ → $C_1=C_2=\tfrac32$ → $y=\tfrac32\big(e^{x}+e^{-x}\big)-x-1$

**Potenciales pedidos en parciales (el tema del 100%):**

| Examen | Campo y dato | Respuesta |
|---|---|---|
| 2015-11-25 P1 | $f=(2x+y^2+1,\,2xy)$, $\varphi(0,0)=2$ | $\varphi=x^2+xy^2+x+2$ |
| 2016-11-25 P3 | $f=(2x,\,2y)$, $\varphi(0,0)=1$ | $\varphi=x^2+y^2+1$ |
| 2019-11-21 T1 | $f=(2xy+1,\,x^2+2y)$, $\varphi(1,2)=5$ | $\varphi=x^2y+x+y^2-2$ |
| 2022-07-15 P2 | $f=(6xy+2y^2+2,\,3x^2+4xy-2)$, $\varphi(1,2)=11$ | $\varphi=3x^2y+2xy^2+2x-2y-1$; piden $\varphi(1,0)=1$ |
| 2022-11-24 P2 | $f=(4xy-2,\,2x^2-2y)$, $\varphi(1,1)=0$ | $\varphi=2x^2y-2x-y^2+1$ |
| 2022-12-16 P2 | $f=(12x+2yz,\,6y+2xz,\,2xy)$; ¿qué $a$ anula $\int_{(-a,a,1)}^{(1,a,a)}$? | $\varphi=6x^2+3y^2+2xyz$ → $6+5a^2=7a^2$ → $a=\pm\sqrt3$ |
| **2026-07-08 T1** | $f=\big(\tfrac{2x}{x^2+y^2},\,\tfrac{2y}{x^2+y^2}\big)$ | $\varphi=\ln(x^2+y^2)+C$ (§5) |

**Circulación / trabajo / Green / Stokes:**

| Problema | Resultado |
|---|---|
| Green ½: $f=(\tfrac{xy^2}{2},\tfrac{3x^2y}{2})$, frontera de $x^2\le y\le x$ (2019-11-21, 2022-07-15, 2024-07-12) | $1/12$ (antihorario) |
| Green entero: $f=(xy^2,3x^2y)$, mismo recinto (sin-fecha) | $1/6$ |
| Green con $\varphi(y-x)$ desconocida, mismo recinto (2017-11-16 P2) | $1/6$ |
| Green 2025 T1: $f=(y+g(x),2x+g(y))$, frontera de $x^2+y^2\le2y$ | $\pi$ |
| Stokes con rotor dado (2022-12-16 P1) | $-2\pi$ con $\hat n=+\hat k$ |
| Stokes con rotor dado (sin-fecha P2) | $36\pi$ con $\hat n=+\hat k$ |
| Circulación $f=(yz,2xz,xy)$, paraboloides (2016-07-06 = 2023-07-28) | $\pm8\pi$ según orientación |
| Trabajo $f=(z,y,x)$, curva $x^2+y^2=4$ ∩ $z=x$ (2019-11-21 P3) | $0$ (conservativo, §3) |
| Trabajo $f=(xy,y^2,xz)$ sobre $x=y^2$, $z=x+y$ (2016-11-25 P2) | $60$ |
| Circulación $f=(xy,-y^2,z^2)$ de $(3,0,0)$ a $(0,9,9)$ (2022-12-02 P2) | $-81/4$ |
| Potencial con $g$ cancelada, de $(-2,4)$ a $(2,5)$ (T2 ×3, §5) | $4$ |

**Flujo / Gauss:**

| Problema | Resultado |
|---|---|
| Reciclado ×4: $f=(y^2,z^2+x^2,x^2)$ por $y=x$, $x^2+y^2+2z^2\le2$ | $\pm\pi/4$ según $\hat n$ |
| Gauss en tetraedro (2015-11-25 P3, $\operatorname{div}=6$) | $4$ (saliente) |
| Gauss en tetraedro (2022-07-15 P3, $\operatorname{div}=2y$) | $1/2$ (saliente) |
| Gauss en tetraedro (2023-07-28 P3, $\operatorname{div}=2$) | $24$ (saliente) |
| Gauss directo (2024-07-12 P3, $\operatorname{div}=3$, $V=8/3$) | $8$ (saliente) |
| Abierta con tapa (sin-fecha P3, $\operatorname{div}=1$) | $3\pi/2$ hacia $z^+$ |
| Flujo abierto 2025 P4: $\operatorname{div}f=2z$, $z=4-x^2-y^2$, dato disco $7\pi$ hacia $z^+$ | $\frac{64\pi}{3}+7\pi=\frac{85\pi}{3}$ |
| Cilindro corrido (2026-07-08 P3, §6) | $\pm4$ según $\hat n$ |
| Hallar $g$ solenoidal (2025-07-18 P1) | $g=2\cos x+x-1$ |
| Flujo = volumen (2022-12-02 P4) | $g=\tfrac23(e^{x}-e^{-2x})$ |
| Hallar $g$ conservativo (2023-07-14 P1) | $g=3\operatorname{sen}2x-\tfrac14\cos2x+\tfrac14$ |

**Integrales múltiples / áreas / cambio de variables:**

| Problema | Resultado |
|---|---|
| Volumen $(x-1)^2+y^2\le z\le5-2x$ (**2026-07-08 P1**, §2) | $8\pi$ |
| Volumen elipsoide ∩ cono, mitad (2016-07-06 = 2023-07-28 P1) | $\pi\,\frac{\sqrt3-1}{2}$ |
| Volumen $x^2+y^2\le2y$, $\lvert z\rvert\le2y$ (2025-07-18 P2) | $4\pi$ |
| Masa cono ∩ esfera $\rho\le\sqrt{18}$, $\delta=kz$ (2017-11-16 P1) | $\tfrac{81\pi k}{2}$ |
| Masa cilindro, altura constante $5$, $\delta=k\rho$ (2022-12-02 P1; mismo esquema girado en 2023-07-14 P3) | $\tfrac{80\pi k}{3}$ |
| Baricentro media elipse (2017-07-05 P1) | $\big(0,\tfrac{4}{3\pi}\big)$ |
| Área del cono bajo $z=2$ (2019-11-21 P2) | $4\sqrt2\,\pi$ |
| Área de $z=1-x^2-y^2$, $z\ge0$ (2024-07-12 P2 = apunte 12-Ej4) | $\frac{\pi}{6}(5\sqrt5-1)$ |
| Área de $z=x^2-y$, $\lvert y\rvert\le x\le1$ (**2026-07-08 P2**) | $\sqrt6-\tfrac{\sqrt2}{3}$ |
| Longitud de la hélice (2017-07-05 P3) | $2\sqrt2\,\pi$ |
| Área encerrada por $\lambda(t)=(t-t^2,\,t-t^4)$ (2023-07-14 P2) | $1/30$ |
| Área encerrada por $\lambda(t)=(t-t^3,\,t-t^4)$ (sin-fecha P1) | $3/140$ |
| área$(D^*)$ sabiendo área$(D)$ — las 4 variantes | tabla en §1 (resultados $3$, $3/2$, $2$ y $4$) |
| T2 polar: $\int_0^{\pi/2}\int_0^{2\cos\varphi}\rho^3\,d\rho\,d\varphi$ | $\frac{3\pi}{4}$ |

---

## 11 · OJO — errores que cuestan puntos

- Green y Gauss exigen **antihorario / saliente**: al revés → signo $-$.
- Flujo por gráfica: $(-g_x,-g_y,1)$ apunta hacia **arriba**; si piden hacia abajo → usar $(g_x,g_y,-1)$.
- Gauss con tapa: si el dato del flujo de la tapa viene orientado hacia $z^+$ pero el saliente del sólido ahí apunta hacia abajo → invertile el signo antes de restar (P4 2025-07-18).
- Nunca olvidar el jacobiano: $\rho$ (polares/cilíndricas), $\rho^2\operatorname{sen}\theta$ (esféricas).
- En "área$(D^*)$ dado área$(D)$" va $\lvert J\rvert$, nunca $J$: un área negativa es señal de que te comiste el módulo (los $J$ reales de esa familia dan $-3$ y $-4$).
- $x^2+y^2\le2x$ o $\le2y$ → **completá cuadrados antes de hacer nada**: son discos/cilindros corridos de radio 1 (cayeron en 2025-07-18 ×2 y 2026-07-08).
- Si te dan $\operatorname{rot}f$, no intentes reconstruir $f$: es Stokes con el disco plano (§8).
- Conservativo: verificar la simetría **antes** de gastar tiempo armando $\varphi$; y en curvas feas, probar conservativo **antes** de parametrizar (§3).
- Resonancia: mirar **siempre** si el candidato está en $y_H$ antes de derivar.
- Las condiciones iniciales van en $y_H+y_p$, nunca en $y_H$ sola.
- $\rho=2\cos\varphi$ completa necesita $\varphi\in[-\pi/2,\pi/2]$; con $[0,\pi/2]$ es solo la mitad superior.
- Circulación con extremos dados: el sentido lo define $A\to B$, no la parametrización "cómoda".

---

*Generado el 2026-07-07 y revisado a fondo el 2026-07-17: se incorporó el examen real del 2026-07-08 (resuelto completo: §1, §2, §5, §6, §9, §10), se agregaron las recetas que faltaban ("te dan rot f" en §8, atajos de §3) con ejemplos paso a paso, se corrigió la referencia de superficie abierta de §7 (2024-07-12 P3 es cerrada) y se recalculó a mano CADA resultado de §10 desde `examenes/INDICE.md` (los enunciados «≈» de escaneos dudosos quedaron afuera). Fuentes: apuntes 01–19 (`apuntes/md/`), `examenes/INDICE.md`, `estrategia.md`, `que-saltear.md`. Teoría y demostraciones (T1/T2): ver checklist en `estrategia.md` y `repaso/flashcards.md`.*
