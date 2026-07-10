# MACHETE MAESTRO — AM2 · Segundo parcial

> Solo fórmulas y recetas, sin explicaciones. Orden: identificar → plantear → integrar.
> Cubre los 4 problemas prácticos (P1–P4) según el patrón real de 16 parciales (`examenes/INDICE.md`).

---

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Herramienta |
|---|---|
| volumen del cuerpo | $V=\iiint_V dV$ (cilíndricas/esféricas) |
| masa del cuerpo con densidad $\delta$ | $m=\iiint_V \delta\,dV$ |
| área de la región plana | $A=\iint_D dA$, o Green: $\tfrac12\oint_{C^+}(x\,dy-y\,dx)$ |
| área de la superficie | $A=\iint_D \sqrt{1+g_x^2+g_y^2}\,dA$ |
| longitud de la curva | $L=\int_a^b \lVert\lambda'(t)\rVert\,dt$ |
| circulación / trabajo | $\int_C f\cdot d\lambda$; ¿cerrada y plana? → Green; ¿conservativo? → $\varphi(B)-\varphi(A)$ |
| función potencial | verificar $P_y=Q_x$ (jacobiana simétrica) → armar $\varphi$ |
| flujo a través de S | $\Phi=\iint_S f\cdot\hat n\,dS$; ¿S cerrada? → Gauss |
| hallar $g$ para que sea conservativo | plantear $P_y=Q_x$ → EDO en $g$ (resolver con §9) |
| hallar $g$ para que sea solenoidal | plantear $\operatorname{div}f=0$ → EDO en $g$ (§9) |
| $y''+ay'+by=h(x)$ | característica + $y_p$ por coeficientes indeterminados |
| circulación con rotor fácil / curva fea | Stokes: $\oint = \iint_S \operatorname{rot}f\cdot\hat n\,dS$ |

---

## 1 · Cambios de variables (la base de todo)

**Teorema (cambio de variables):**

$$
\iint_D f\,dx\,dy=\iint_{D^*} f\big(x(u,v),y(u,v)\big)\,|J|\,du\,dv,\qquad J=\det\frac{\partial(x,y)}{\partial(u,v)}
$$

- Truco: $J_{(x,y)\to(u,v)}=1/J_{(u,v)\to(x,y)}$ (invertís el que sea más fácil).
- Transformación lineal: $\text{área(imagen)}=|\det|\cdot\text{área(original)}$.
- **T1 reciclado ×5** (2016-07-06, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28): dan $(x,y)=T(u,v)$ y área$(D)$, piden área$(D^*)$: usar $\text{área}(D)=|J|\cdot\text{área}(D^*)$, con $J$ el jacobiano de $(u,v)\to(x,y)$.
  - Checksums: $(x,y)=(v-2u,\,u+v)$, área$(D)=9$ → $|J|=3$ → área$(D^*)=3$. Y $(x,y)=(u+3v,\,2u+2v)$, área$(D)=6$ → $|J|=4$ → área$(D^*)=3/2$.

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

**Masa:** $m=\iiint_V\delta\,dV$. Densidad "proporcional a la distancia…":

- al eje $z$ → $\delta=k\sqrt{x^2+y^2}=k\rho$ (cilíndricas)
- al plano $xy$ → $\delta=k|z|$
- al origen → $\delta=k\rho$ (esféricas)

**Baricentro:** $\bar x=\dfrac1m\iiint_V x\,\delta\,dV$ (ídem $y,z$); región plana: $\bar x=\dfrac1A\iint_D x\,dA$.

- Homogéneo → $\delta$ se cancela. Simetría → esa coordenada es $0$.

**Superficies que aparecen siempre:**

| Ecuación | Qué es |
|---|---|
| $z=x^2+y^2$ | paraboloide, vértice $O$, abre hacia arriba |
| $z=\sqrt{x^2+y^2}$ | semicono superior |
| $x^2+y^2+z^2=R^2$ | esfera |
| $x^2+y^2=R^2$ | cilindro vertical |

**Intersecciones típicas:**

- paraboloide ∩ plano $z=k$ → circunferencia $x^2+y^2=k$
- cono ∩ esfera de radio $R$ → $2z^2=R^2$: circunferencia en $z=R/\sqrt2$
- paraboloide ∩ esfera → igualar y resolver la cuadrática en $\rho^2$

**Elección de coordenadas:**

- cilindro / paraboloide / cono con tapa plana → **cilíndricas**
- esfera sola, o cono ∩ esfera → **esféricas**

**Volúmenes conocidos (para Gauss exprés):** esfera $\tfrac43\pi R^3$; cilindro $\pi R^2 h$; cono $\tfrac13\pi R^2 h$.

---

## 3 · Curvas: parametrización, longitud, circulación

| Curva | $\lambda(t)$ | $t$ |
|---|---|---|
| segmento $A\to B$ | $A+t(B-A)$ | $[0,1]$ |
| circunferencia $x^2+y^2=R^2$ | $(R\cos t,\;R\operatorname{sen}t)$ | $[0,2\pi]$ antihorario |
| elipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$ | $(a\cos t,\;b\operatorname{sen}t)$ | $[0,2\pi]$ |
| gráfica $y=g(x)$ | $(t,\;g(t))$ | $[x_0,x_1]$ |
| intersección de 2 superficies | elegir parámetro, despejar las otras 2 variables | de $A$ a $B$ |

- Longitud: $L=\int_a^b\lVert\lambda'(t)\rVert\,dt$
- Circulación / trabajo: $\int_C f\cdot d\lambda=\int_a^b f(\lambda(t))\cdot\lambda'(t)\,dt$
- Sentido: $\lambda(a)$ debe ser el punto inicial pedido; si va al revés → cambiar el signo del resultado.
- **Antes de integrar, mirar si $f$ es conservativo** → $\int_C f\cdot d\lambda=\varphi(B)-\varphi(A)$; cerrada → $0$.

---

## 4 · Teorema de Green (T1 casi fijo)

$$
\oint_{C^+}(P,Q)\cdot d\lambda=\iint_D\Big(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\Big)\,dA
$$

Hipótesis para nombrar: $C$ cerrada simple, frontera de $D$, sentido antihorario ($C^+$), $f\in C^1$ en $D$.

- Corolario área: $A=\dfrac12\oint_{C^+}(x\,dy-y\,dx)=\oint_{C^+}x\,dy=-\oint_{C^+}y\,dx$
- Curva paramétrica $\lambda(t)=(x(t),y(t))$: $A=\dfrac12\int_a^b\big(x\,y'-y\,x'\big)\,dt$ — así piden las áreas encerradas (P2 2023-07-14, P1 sin-fecha).
- Sentido horario → cambia el signo.

**El T1 más reciclado** — circulación sobre la frontera de $x^2\le y\le x$, antihorario ($\int_0^1\!\int_{x^2}^{x}\cdot\;dy\,dx$), OJO que hay dos variantes del campo:

| Variante | $Q_x-P_y$ | Resultado |
|---|---|---|
| $f=\big(\frac{xy^2}{2},\,\frac{3x^2y}{2}\big)$ — 2019‑11‑21, 2022‑07‑15, 2024‑07‑12 | $2xy$ | $1/12$ |
| $f=(xy^2,\,3x^2y)$ — sin‑fecha | $4xy$ | $1/6$ |

**Variante 2025-07-18 (T1):** $f=(y+g(x),\,2x+g(y))$ con $g$ desconocida, sobre $x^2+y^2\le2y$: las $g$ mueren en las derivadas cruzadas → $Q_x-P_y=2-1=1$ → circulación $=1\cdot\text{área}(D)=\boxed{\pi}$ (antihorario). Regla: $Q_x-P_y=\text{cte}$ → circulación $=\text{cte}\cdot\text{área}(D)$.

---

## 5 · Conservativos y función potencial (cae en el 100%)

- $f$ conservativo en $D$ ⇔ existe $\varphi$ con $\nabla\varphi=f$ ⇒ $\int_C f\cdot d\lambda=\varphi(B)-\varphi(A)$ (independiente del camino; cerrada → $0$).
- **Condición necesaria:** jacobiana simétrica. 2D: $P_y=Q_x$. 3D: $P_y=Q_x$, $P_z=R_x$, $Q_z=R_y$ (⇔ $\operatorname{rot}f=\bar 0$).
- **Condición suficiente:** simetría + $D$ simplemente conexo + $f\in C^1$.

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

- Limitación: el segmento $0\to(x,y)$ tiene que estar dentro del dominio de $f$; si $f$ no está definida en el origen (p. ej. dominio $\mathbb{R}^2-\{(0,0)\}$) → **no aplica**, usar Método 1.
- Cómodo cuando las componentes son polinomios: la integral en $t$ sale directa.

**Variante "hallar $g(x)$"** (2023-07-14, 2025-07-18, 2022-12-02): plantear $P_y=Q_x$ (o $\operatorname{div}f=0$) → **suele quedar una EDO de 2° orden en $g$** → resolverla con la receta de §9; los datos tipo $f(0,1)=(0,7)$ fijan las constantes.

- Checksum 2023-07-14: $f=(x^2-4y\,g(x),\;g'(x)-x+y)$ → $-4g=g''-1$ → $g''+4g=1$ → $g=C_1\cos 2x+C_2\operatorname{sen}2x+\tfrac14$.

**T2 reciclado ×3** (2022-12-02, 2022-12-16, 2023-07-14): $f=(2xy+2x\,g'(x^2),\;x^2)$ → $\varphi=x^2y+g(x^2)$; de $(-2,4)$ a $(2,5)$: $x^2=4$ en ambos extremos → la $g$ se cancela → $\varphi(2,5)-\varphi(-2,4)=20-16=\boxed{4}$.

---

## 6 · Superficies: $dS$, área y flujo (85%)

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

- Flujo por gráfica, todo junto: $\Phi=\iint_D\big(-P\,g_x-Q\,g_y+R\big)\,dA$
- La orientación la fija el enunciado ("componente $z$ positiva", "saliente", "según $y$ creciente") → elegir el signo de $N$ que cumpla.

**El reciclado ×4** (2017-11-16 y equivalentes): $f=(y^2,\,z^2+x^2,\,x^2)$ a través del plano $y=x$ limitado por $x^2+y^2+2z^2\le2$:

$$
r(x,z)=(x,x,z),\qquad N=(1,-1,0),\qquad \text{dominio } x^2+z^2\le1
$$

$$
f\cdot N=-z^2 \;\Rightarrow\; \Phi=\boxed{-\pi/4}
$$

(con la normal opuesta: $+\pi/4$)

---

## 7 · Divergencia y Gauss

- $\operatorname{div}f=P_x+Q_y+R_z$; **solenoidal** ⇔ $\operatorname{div}f=0$.

**Teorema de la divergencia** ($S$ cerrada, orientada saliente, $V$ el sólido encerrado, $f\in C^1$):

$$
\iint_{\partial V}f\cdot\hat n\,dS=\iiint_V\operatorname{div}f\,dV
$$

- $\operatorname{div}f=\text{cte}$ → $\Phi=\text{cte}\cdot\operatorname{Vol}(V)$ → usar los volúmenes conocidos de §2.
- Componente desconocida que **no depende de su propia variable** → aporta $0$ a la div: $f=(g(y,z),\,h(x,z),\,z)$ → $\operatorname{div}f=1$ (P3 sin-fecha); $f=(x-y-z,\,y-x-z,\,g(x,y))$ → $\operatorname{div}f=2$ (P3 2023-07-28).
- "Hallar $g$ solenoidal": $\operatorname{div}f=0$ → queda una EDO en $g$ (puede ser de 2° orden → §9). Checksum 2025-07-18: $f=(x+g'(x),\,y\,g(x),\,y^2-xz)$ → $1+g''+g-x=0$ → $g''+g=x-1$ → con $f(0,1,0)=(1,1,1)$: $g=2\cos x+x-1$.

**Superficie abierta vía Gauss** (P3 2024-07-12, P4 2025-07-18): cerrar con una tapa $T$:

$$
\Phi_S=\iiint_V\operatorname{div}f\,dV-\Phi_T \quad(\text{todo saliente})
$$

- Tapa plana $z=k$: $\hat n=(0,0,\pm1)$ → $\Phi_T=\pm\iint_D R(x,y,k)\,dA$.

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

---

## 9 · EDO lineales de 2° orden (P4 fijo desde 2022)

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

- "Recta tangente $y=mx+c$ en $x_0$" → $y(x_0)=mx_0+c$ **y** $y'(x_0)=m$.

---

## 10 · Reciclados con resultado verificado (autocorrección)

> Estos problemas se repitieron casi textuales entre parciales (según `examenes/INDICE.md`). Practicalos desde el enunciado real y chequeá acá si llegaste al resultado correcto — es tu "solucionario". Si uno cae igual en el examen, ya sabés a qué valor tenés que llegar.

**Las 10 EDOs reales de parcial (P4; a veces P1 o T2) con su solución general:**

| Examen | EDO | Solución general |
|---|---|---|
| 2015‑11‑25 | $y''+y'-2y=\cos x$ | $y=C_1e^{x}+C_2e^{-2x}+\frac{\operatorname{sen}x-3\cos x}{10}$ |
| 2016‑07‑06 | $y''+4y'=8$ | $y=C_1+C_2e^{-4x}+2x$ |
| 2016‑11‑25 | $y''+2y'=4x$ | $y=C_1+C_2e^{-2x}+x^2-x$ |
| 2019‑11‑21 | $y''-6y'+9y=2x$ | $y=(C_1+C_2x)e^{3x}+\frac{2}{9}x+\frac{4}{27}$ |
| 2022‑07‑15 | $y''-2y'+5y=2x$ | $y=e^{x}(C_1\cos 2x+C_2\operatorname{sen}2x)+\frac{2}{5}x+\frac{4}{25}$ |
| 2022‑11‑24 | $y''-4y'+13y=26$ | $y=e^{2x}(C_1\cos 3x+C_2\operatorname{sen}3x)+2$ |
| 2023‑07‑28 | $y''-3y'=2-6x$ | $y=C_1+C_2e^{3x}+x^2$ |
| 2024‑07‑12 | $y''-2y'+5y=10$ | $y=e^{x}(C_1\cos 2x+C_2\operatorname{sen}2x)+2$ |
| 2025‑07‑18 | $y''-y=4$ | $y=C_1e^{x}+C_2e^{-x}-4$ |
| sin‑fecha | $y''-6y'+9y=9x$ | $y=(C_1+C_2x)e^{3x}+x+\frac{2}{3}$ |

**Otros reciclados:**

| Problema | Resultado |
|---|---|
| Green ½: $f=(\frac{xy^2}{2},\frac{3x^2y}{2})$, frontera de $x^2\le y\le x$ | $1/12$ (antihorario) |
| Green entero: $f=(xy^2,3x^2y)$, mismo recinto (sin‑fecha) | $1/6$ |
| Green 2025: $f=(y+g(x),2x+g(y))$, frontera de $x^2+y^2\le2y$ | $\pi$ |
| Flujo: $f=(y^2,z^2+x^2,x^2)$ por $y=x$, $x^2+y^2+2z^2\le2$ | $\pm\pi/4$ según $\hat n$ |
| Flujo abierto 2025 (P4): $\operatorname{div}f=2z$, $z=4-x^2-y^2$, dato disco $7\pi$ hacia $z^+$ | $\frac{64\pi}{3}+7\pi=\frac{85\pi}{3}$ |
| Potencial con $g$: $f=(2xy+2x\,g'(x^2),x^2)$, de $(-2,4)$ a $(2,5)$ | $4$ |
| Área encerrada por $\lambda(t)=(t-t^2,\,t-t^4)$ (2023‑07‑14) | $1/30$ |
| Área encerrada por $\lambda(t)=(t-t^3,\,t-t^4)$ (sin‑fecha) | $3/140$ |
| Cambio de variables: $(x,y)=(v-2u,\,u+v)$, área$(D)=9$ | área$(D^*)=3$ |
| T2 polar: $\int_0^{\pi/2}\int_0^{2\cos\varphi}\rho^3\,d\rho\,d\varphi$ | $\frac{3\pi}{4}$ |
| Área de $z=1-x^2-y^2$, $z\ge0$ (2024‑07‑12 = apunte 12‑Ej4) | $\frac{\pi}{6}(5\sqrt5-1)$ |

---

## 11 · OJO — errores que cuestan puntos

- Green y Gauss exigen **antihorario / saliente**: al revés → signo $-$.
- Flujo por gráfica: $(-g_x,-g_y,1)$ apunta hacia **arriba**; si piden hacia abajo → usar $(g_x,g_y,-1)$.
- Gauss con tapa: si el dato del flujo de la tapa viene orientado hacia $z^+$ pero el saliente del sólido ahí apunta hacia abajo → invertile el signo antes de restar (P4 2025‑07‑18).
- Nunca olvidar el jacobiano: $\rho$ (polares/cilíndricas), $\rho^2\operatorname{sen}\theta$ (esféricas).
- Conservativo: verificar la simetría **antes** de gastar tiempo armando $\varphi$.
- Resonancia: mirar **siempre** si el candidato está en $y_H$ antes de derivar.
- Las condiciones iniciales van en $y_H+y_p$, nunca en $y_H$ sola.
- $\rho=2\cos\varphi$ completa necesita $\varphi\in[-\pi/2,\pi/2]$; con $[0,\pi/2]$ es solo la mitad superior.
- Circulación con extremos dados: el sentido lo define $A\to B$, no la parametrización "cómoda".

---

*Generado el 2026-07-07. Fuentes: apuntes 01–19 (`apuntes/md/`), `examenes/INDICE.md`, `estrategia.md`, `que-saltear.md`. Teoría y demostraciones (T1/T2): ver checklist en `estrategia.md`.*
