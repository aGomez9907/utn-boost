# MACHETE — Análisis Matemático II · Final

> Solo fórmulas y recetas, sin explicaciones. Orden: identificar → plantear → integrar.
> Basado en el patrón real de **24 finales** (`examenes/INDICE.md`). Unifica los machetes
> del 1P y del 2P podados a lo que cae en el final.
> **Regla del examen: 3 de 6 — UN teórico (T1 o T2) + DOS prácticos (de P1–P4).**
> Primeros 10 minutos: leer, elegir los 3, ignorar el resto.

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Herramienta |
|---|---|
| **flujo** por superficie **cerrada** / "frontera del cuerpo" / "saliente" | Gauss: $\iiint_V\operatorname{div}f\,dV$ → §1 |
| **flujo** por superficie **abierta** (paraboloide, cilindro, plano, $z=g(x,y)$) | directo: $\iint_D f\cdot N\,dA$ con $N$ de la tabla → §1; o cerrar con tapa y restar |
| flujo con $g,h\in C^1$ desconocidas en el campo | Gauss: la componente que no depende de su variable aporta 0 a la div → §1 |
| **circulación** por curva **plana cerrada** (frontera de $D$) | Green: $\iint_D(Q_x-P_y)\,dA$ → §2 |
| campo con $e^{x^2}$, $\operatorname{sen}(y^2)$, $\ln x$, $h(y)$ desconocida | no se integra directo: **Green** (las incógnitas mueren en $Q_x-P_y$) → §2 |
| circulación por **curva intersección de 2 superficies** en $\mathbb R^3$ | Stokes con superficie plana; si dan $Df$ o $\operatorname{rot}f$ y no $f$, Stokes obligado → §2 |
| circulación de $A$ a $B$ (abierta) / "por dos procedimientos" | ¿conservativo? → $\varphi(B)-\varphi(A)$; si no, parametrizar → §2 |
| hallar $g$ para que sea conservativo / solenoidal / flujo $=k\cdot$vol | $P_y=Q_x$ / $\operatorname{div}f=0$ / $\operatorname{div}f\equiv k$ → EDO en $g$ → §2, §3 |
| línea **equipotencial** por un punto | curva de nivel $\varphi=\varphi(P)$ del potencial → §2 |
| **líneas de campo** de $F=(P,Q)$ | EDO $\dfrac{dy}{dx}=\dfrac{Q}{P}$ → §3 |
| $y''+ay'+by=h(x)$ (+ tangente / PVI / límite) | característica + coef. indeterminados → §3 |
| familias **ortogonales** / hallar $a$ para que lo sean | $y'\to-1/y'$ tras eliminar la constante → §3 |
| $z=f(x,y)$ **definida implícitamente** por $F=0$ | $f_x=-F_x/F_z$, $f_y=-F_y/F_z$ → §4 |
| **plano tangente / recta normal** a superficie; "paralelo al plano…" | normal $=\nabla F$; paralelo ⇔ $\nabla F\parallel$ normal dada → §4 |
| recta tangente / **plano normal a una curva** (intersección) | $\bar T=\nabla F_1\times\nabla F_2$ → §4 |
| derivada direccional **máxima / mínima / nula**; "máximo decrecimiento" | $\pm\lVert\nabla f\rVert$ en $\pm\nabla f/\lVert\nabla f\rVert$; nula $\perp\nabla f$ → §5 |
| $h=f\circ g$ (composición con jacobianas / implícita) | $\nabla h=\nabla f(g)\cdot Dg$ → §5 |
| **aproximación lineal** / valor aproximado | $z\approx z_0+z_x\Delta x+z_y\Delta y$ → §5 |
| me dan el **Taylor** de grado 2 | leer $f,\nabla f,H$ de los coeficientes → §5 |
| **extremos** locales / en una región / punto silla | $\nabla f=0$ → Hessiano; región: interior + frontera → §6 |
| volumen / masa "densidad proporcional a la distancia a…" | $\iiint\delta\,dV$ en cilíndricas/esféricas → §7 |
| "exprese mediante **dos integrales distintas**" | proyectar sobre dos planos coordenados distintos → §7 |
| **área de superficie** / $\iint_S y\,d\sigma$ | $dS=\sqrt{1+g_x^2+g_y^2}\,dA$ → §7 |
| área$(D^*)$ sabiendo área$(D)$; integral en polares ↔ cartesianas | jacobiano → §7 |
| V/F sobre función partida en $(0,0)$ (continua / diferenciable / plano tangente) | límite por trayectorias; direccional por definición → §5, §8 |
| "enuncie / defina / demuestre" | §8: elegir el que sepas (T-A a T-D) |

---

## 1 · Flujo (cae en 23 de 24 finales)

$$
\Phi=\iint_S f\cdot\hat n\,dS=\iint_D f\big(r(u,v)\big)\cdot(r_u\times r_v)\,du\,dv
$$

(la normal SIN normalizar ya trae el $dS$)

**Normales listas:**

| Superficie | $N$ (sin normalizar) |
|---|---|
| gráfica $z=g(x,y)$ | $(-g_x,\,-g_y,\,1)$ apunta hacia $z^+$ |
| gráfica $y=g(x,z)$ / $x=g(y,z)$ | $(-g_x,\,1,\,-g_z)$ / $(1,\,-g_y,\,-g_z)$ (la variable despejada lleva el 1) |
| plano $ax+by+cz=d$ | $(a,b,c)$ |
| esfera centro $O$ | $(x,y,z)$ saliente |
| cilindro $x^2+y^2=R^2$ | $(x,y,0)$ saliente |
| cilindro corrido $(x-a)^2+y^2=R^2$ | $(x-a,\,y,\,0)$ saliente |

- Flujo por gráfica $z=g$, todo junto: $\Phi=\iint_D\big(-P\,g_x-Q\,g_y+R\big)\,dA$, con $P,Q,R$ evaluados en $z=g(x,y)$.
- La orientación la fija el enunciado ("tercera componente positiva", "saliente", "segunda componente negativa") → elegir el signo de $N$ que cumpla. **Siempre decir cuál elegiste.**

**Gauss** ($S$ cerrada, orientada saliente, $V$ el sólido, $f\in C^1$ en $V$):

$$
\iint_{\partial V}f\cdot\hat n\,dS=\iiint_V\operatorname{div}f\,dV,\qquad \operatorname{div}f=P_x+Q_y+R_z
$$

- $\operatorname{div}f=\text{cte}$ → $\Phi=\text{cte}\cdot\operatorname{Vol}(V)$. Volúmenes: esfera $\tfrac43\pi R^3$; cilindro $\pi R^2h$; cono $\tfrac13\pi R^2h$; tetraedro de interceptos $a,b,c$: $\tfrac{abc}6$.
- Componente que **no depende de su propia variable** → aporta $0$: $f=(g(y,z),\,h(x,z),\,z)$ → $\operatorname{div}=1$. Los $e^{2xz}$ en $Q$, $xe^y$ en $R$, $yz^2$ en $P$ del `2026-07-28 P1` mueren todos.
- "¿Es nulo el flujo por una esfera?" → $\iiint\operatorname{div}f\,dV$; si $\operatorname{div}\ne0$ en el interior, **no**.
- "Hallar $a$ tal que flujo $=8\cdot$vol" → $\operatorname{div}f\equiv8$ → despejar $a$. "Inventar $f$ con flujo $=3\cdot$vol" → cualquier $f$ con $\operatorname{div}\equiv3$, p. ej. $(x,y,z)$.
- **Gauss NO se aplica directo a superficie abierta** (`2026-02-10 T1a`: $x^2-2x+y^2=0$, $-1\le z\le1$ es un cilindro **sin tapas**). Receta: cerrar con tapa(s) $T$ y despejar,

$$
\Phi_S=\iiint_V\operatorname{div}f\,dV-\Phi_T\quad(\text{todo saliente})
$$

- Tapa plana $z=k$: $\hat n=(0,0,\pm1)$ → $\Phi_T=\pm\iint_D R(x,y,k)\,dA$. Al final, si la orientación pedida en $S$ no es la saliente → signo $-$ global.

**Flujo directo por cilindro corrido** (`2025-07-15 P4` ≡ `2025-12-02 P4`): $x^2+y^2=2x$ → $(x-1)^2+y^2=1$ → $r(t,z)=(1+\cos t,\ \operatorname{sen}t,\ z)$, 1er octante $t\in[0,\pi]$; techo $z\le4-(x^2+y^2)=4-2x=2-2\cos t$; $N=(\cos t,\operatorname{sen}t,0)$ saliente. Con $f=(-y,x,xz)$: $f\cdot N=\operatorname{sen}t$ → $\Phi=\int_0^\pi\operatorname{sen}t\,(2-2\cos t)\,dt=\boxed{4}$.

**Flujo por paraboloide abierto orientado $z^+$** (`2025-09-25 P2`, `2025-12-09 P2`, `2026-03-03 P4`): $z=g=c-x^2-y^2$ → $N=(2x,2y,1)$; $D$ = proyección ($z\ge0$ → $x^2+y^2\le c$; $z\ge1$ → $x^2+y^2\le c-1$); polares.

---

## 2 · Circulación: Green · Stokes · conservativo (22 de 24)

$$
\int_C f\cdot d\lambda=\int_a^b f(\lambda(t))\cdot\lambda'(t)\,dt
$$

**Parametrizaciones:** segmento $A+t(B-A)$, $t\in[0,1]$ · circunferencia $(R\cos t,R\operatorname{sen}t)$ · corrida $(a+R\cos t,\,b+R\operatorname{sen}t)$ · elipse $\frac{x^2}{a^2}+\frac{y^2}{b^2}=1$: $(a\cos t,b\operatorname{sen}t)$ · gráfica $y=g(x)$: $(t,g(t))$ · intersección de 2 superficies: el parámetro es la variable de la que dependen las otras dos.

**Antes de integrar: ¿es conservativo?** Jacobiana simétrica ($P_y=Q_x$; en 3D además $P_z=R_x$, $Q_z=R_y$ ⇔ $\operatorname{rot}f=\bar0$) + dominio simplemente conexo → $\int_C f\cdot d\lambda=\varphi(B)-\varphi(A)$; cerrada → $0$.

**Armar $\varphi$:** $\varphi=\int P\,dx+c(y,z)$ → derivar en $y$, igualar a $Q$ → $c$ → derivar en $z$, igualar a $R$. **Verificar $\nabla\varphi=f$.** Dato $\varphi(P)=k$ → ajustar la constante.

- **Línea equipotencial** por $P$: $\varphi(x,y)=\varphi(P)$. `2025-07-15 T2b`: $f=\frac{(2x,2y)}{x^2+y^2}$ → $\varphi=\ln(x^2+y^2)+C$; $\varphi(1,0)=3$ → $C=3$; equipotencial por $(1,0)$: $\ln(x^2+y^2)=0$ → $x^2+y^2=1$.
- Con agujero en el dominio ($\mathbb R^2-\{0\}$) la simetría no alcanza, pero armar $\varphi$ a mano puede funcionar igual. El campo $\frac{(-y,x)}{x^2+y^2}$ NO es conservativo en $\mathbb R^2-\{0\}$ (circulación $2\pi$ por cualquier circunferencia) pero SÍ en $y>0$ (`2025-12-09 T2b`).
- **Hallar $g$ conservativo** (`2026-07-14 P4`, `2024-12-17 P1`): $P_y=Q_x$ → EDO en $g$ (suele ser de 2º orden → §3); los datos $f(0,1)=(13,4)$ fijan $g(0)$, $g'(0)$.

**Green** ($C=\partial D$ cerrada simple, **antihorario**, $f\in C^1$ en $D$):

$$
\oint_{C^+}(P,Q)\cdot d\lambda=\iint_D\big(Q_x-P_y\big)\,dA
$$

- $Q_x-P_y=\text{cte}$ → circulación $=\text{cte}\cdot\text{área}(D)$. Sentido **negativo/horario** → signo $-$.
- Área plana: $A=\tfrac12\oint_{C^+}(x\,dy-y\,dx)=\oint_{C^+}x\,dy=-\oint_{C^+}y\,dx$ (campos con $Q_x-P_y=1$: $(0,x)$, $(-y,0)$, $\tfrac12(-y,x)$).
- **Curva abierta + Green** (`2026-05-19 T1b`, `2026-07-14 P3`, `2026-02-10 P3`): cerrar con el segmento sobre el eje, $\oint=\int_{C}+\int_{\text{seg}}$ → $\int_C=\iint_D(Q_x-P_y)\,dA-\int_{\text{seg}}$. Sobre el eje $x$ ($y=0$, $dy=0$) sólo sobrevive $\int P(x,0)\,dx$.
- **Hallar $h$ por Green** (`2026-02-24 P2`): "circulación $=4\cdot$área$(D)$ para toda $D$" ⇔ $Q_x-P_y\equiv4$ → EDO en $h$.

**Stokes** ($C=\partial S$, mano derecha: pulgar $=\hat n$, dedos $=C$):

$$
\oint_{C^+}f\cdot d\lambda=\iint_S\operatorname{rot}f\cdot\hat n\,dS,\qquad \operatorname{rot}f=(R_y-Q_z,\;P_z-R_x,\;Q_x-P_y)
$$

- Con $Df$ dada: $\operatorname{rot}f$ se lee de la jacobiana ($R_y=Df_{32}$, $Q_z=Df_{23}$, etc.). Las entradas desconocidas ($P'_x$, $Q'_y$, $R'_z$ de la diagonal) **no se usan**.
- Receta curva intersección: igualar las superficies → proyección $D$ y altura; tomar $S$ **plana** (el plano dado, o $z=z_0$) con $\hat n$ constante → $\iint_D\operatorname{rot}f\cdot N\,dA$. Términos impares ($x$, $y$, $xy$) integran $0$ sobre un disco centrado.
- Plano inclinado $x+y+z=2$ ∩ cilindro $x^2+y^2=y$ (`2025-07-15 P1` ≡ `2025-12-02 P2`): $S$ = trozo del plano, $N=(1,1,1)$, $D$: $x^2+(y-\tfrac12)^2\le\tfrac14$ (área $\tfrac\pi4$); $z=2-x-y$ dentro del rotor.
- "Circulación nula sobre toda curva cerrada en $y=k$" (`2025-02-25 T1b`): $\hat n=(0,1,0)$ → basta $(\operatorname{rot}f)_2=P_z-R_x=0$.
- **Trabajo de un campo de fuerzas** = circulación. Sobre una hélice cerrada en $z$ no (de $t=0$ a $2\pi$ sube): si $f$ es conservativo, $\varphi(B)-\varphi(A)$ (`2024-07-30 P4`).

---

## 3 · EDO (22 de 24)

**2º orden** $y''+ay'+by=h(x)$ → $y=y_H+y_p$. Característica $r^2+ar+b=0$:

| Raíces | $y_H$ |
|---|---|
| $r_1\ne r_2$ reales | $C_1e^{r_1x}+C_2e^{r_2x}$ |
| $r$ doble | $(C_1+C_2x)\,e^{rx}$ |
| $\alpha\pm\beta i$ | $e^{\alpha x}\big(C_1\cos\beta x+C_2\operatorname{sen}\beta x\big)$ |

| $h(x)$ | candidato $y_p$ |
|---|---|
| polinomio grado $n$ | polinomio COMPLETO de grado $n$ |
| $Ce^{kx}$ | $Ae^{kx}$ |
| $\cos\omega x$ y/o $\operatorname{sen}\omega x$ | $A\cos\omega x+B\operatorname{sen}\omega x$ (los dos) |
| suma | suma de candidatos |

- **Resonancia:** candidato ya en $y_H$ → $\times x$ (raíz doble → $\times x^2$). $b=0$ ⇒ $r=0$ es raíz ⇒ polinomio sube un grado ($h=8$ → $y_p=Ax$).
- Condiciones iniciales en $y_H+y_p$, nunca en $y_H$ sola. "Recta tangente $y=mx+c$ en $(0,y_0)$" ⇒ $y(0)=c$, $y'(0)=m$.
- "$\lim_{x\to+\infty}y_G$" (`2025-12-09 P4`): mirar qué términos sobreviven ($e^{-x}\to0$; $x^2e^{-x}\to0$).
- "Máximo y mínimo de $f$ en $[0,\pi]$" (`2025-07-29 P2`): resolver la EDO y después extremos de una variable.

**Resueltas del final:**

| EDO | Solución general |
|---|---|
| $y''-4y'+4y=25\operatorname{sen}x$ (`2026-07-28 P3`) | $(C_1+C_2x)e^{2x}+4\cos x+3\operatorname{sen}x$ |
| $y''+4y=8$ (`2025-07-29 P2`) | $C_1\cos2x+C_2\operatorname{sen}2x+2$ |
| $y''-y=4e^{x}$ (`2025-07-15 P2`, resonancia simple) | $C_1e^{x}+C_2e^{-x}+2xe^{x}$ |
| $y''+y'-2y=9e^{x}$ (`2025-05-20 P4`, resonancia: $r=1$) | $C_1e^{x}+C_2e^{-2x}+3xe^{x}$ |
| $y''-y'-2y=-2x-1$ (`2024-10-09 P4`) | $C_1e^{2x}+C_2e^{-x}+x$ |
| $y''+2y'+y=2e^{-x}$ (`2025-12-09 P4`, raíz doble $-1$) | $(C_1+C_2x)e^{-x}+x^2e^{-x}$ → $\lim_{x\to+\infty}y_G=0$ |
| $y''=6x$ (`2025-02-18 P1`) | $x^3+C_1x+C_2$ |

**1er orden.** Lineal $y'+P(x)y=Q(x)$: $\mu=e^{\int P}$, $y=\frac1\mu\big(\int\mu Q+C\big)$. Separable: $\int\frac{dy}{B(y)}=\int A(x)\,dx$. Exacta $M\,dx+N\,dy=0$ con $M_y=N_x$: es $d\varphi=0$ → $\varphi=C$ (§2). Si no es exacta, probar factor integrante $x^k$ (`2024-07-23 P4`: $(2y-4x^2)dx+x\,dy=0$ → $\times x$ → exacta).

- **Solución singular** (`2024-12-10 T1a`): la que no sale de la general para ningún $C$.
- **Líneas de campo** de $F=(P,Q)$: $\dfrac{dy}{dx}=\dfrac{Q}{P}$ (`2024-03-05 P2`: $F=(x-y,x+y)$; `2024-07-30 T2b`: $F=(-x,\,2y-4x^2)$ → $y'+\tfrac2x y=4x$, lineal, $y=x^2+Cx^{-2}$). Son ortogonales a las equipotenciales.

**Trayectorias ortogonales:** 1. derivar la familia y **eliminar la constante** → $y'=f(x,y)$; 2. $y'\to-1/f$; 3. resolver (siempre salió separable); ajustar con el punto.

- "Hallar $a$ para que $y=kx^3$ y $x^2+ay^2=C$ sean ortogonales" (`2026-03-03 P3`): pendientes $y'_1=3y/x$, $y'_2=-x/(ay)$ → producto $=-1$ → $a=3$. Ídem `2024-12-03 P4` con $y=kx^4$: $b=4$. Regla: $y=kx^n$ ⟂ $x^2+ny^2=C$.
- V/F `2026-05-19 T2b`: $xy=k$ ⟂ $x^2+y^2=R^2$? $y'_1=-y/x$, $y'_2=-x/y$ → producto $=1\ne-1$ → **Falso** (la ortogonal de $xy=k$ es $y^2-x^2=K$).

---

## 4 · Implícita · plano tangente · curvas en el espacio (16 de 24)

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}\qquad(F_z\ne0)
$$

- Primero el punto base: reemplazar $(x_0,y_0)$ y despejar $z_0$ (probar enteros que hagan $\ln(\cdot)=0$ o exponente $=0$). Justificación: $F(P)=0$, $F\in C^1$, $F_z(P)\ne0$.

| Superficie | Normal $\bar N$ | Plano tangente |
|---|---|---|
| implícita $F=0$ | $\nabla F(P)$ | $\nabla F(P)\cdot(X-P)=0$ |
| gráfica $z=g(x,y)$ | $(g_x,g_y,-1)$ o $(-g_x,-g_y,1)$ | $z=g(P)+g_x\Delta x+g_y\Delta y$ |
| paramétrica $\sigma(u,v)$ | $\sigma_u\times\sigma_v$ | $(\sigma_u\times\sigma_v)\cdot(X-P)=0$ |

- **Recta normal:** $X=P+t\bar N$. "¿Corta a la superficie $x+y^2=7$?" → meter $X(t)$ en la ecuación, resolver $t$.
- **Plano tangente paralelo a $ax+by+cz=d$** (`2026-07-14 P1`, `2025-12-02 P3`): $\nabla F(X_0)=\lambda(a,b,c)$ + $X_0\in S$ → sistema. Para gráfica: $(g_x,g_y,-1)\parallel(a,b,c)$.
- **Plano tangente horizontal** ⇔ $\nabla f=0$ (`2025-05-20 T1b`).
- **Superficie parametrizada, punto regular:** $\sigma_u\times\sigma_v\ne\bar0$ en el $(u,v)$ que da $P$ (`2025-02-11 T1`, `2024-05-10 T2`).

**Curva $C=S_1\cap S_2$ en $P$:** $\bar T=\nabla F_1(P)\times\nabla F_2(P)$. Recta tangente $X=P+t\bar T$; **plano normal** $\bar T\cdot(X-P)=0$. Curva $\lambda(t)$: $\bar T=\lambda'(t_0)$; **punto regular** ⇔ $\lambda'(t_0)\ne\bar0$ (`2024-10-09 T1`: $(3t^2+6t,\,2t+4,\,0)$ en $t=-2$ da $(0,0,0)$ → **no regular**); **simple** ⇔ inyectiva en el intervalo.

- "Plano tangente a $S$ ⟂ recta tangente a $C$" (`2026-05-19 T2a`) ⇔ $\nabla F\parallel\lambda'$.
- "Plano tangente a $S$ corta a la curva $C$" (`2024-12-03 P2`): parametrizar $C$ y meterla en el plano.

**B6 — el reciclado ×3** (`2024-05-10 P2` ≡ `2026-03-03 P2` ≡ `2025-07-29 T1a`): $xz+z+y+\ln(z-xy)=10$ en $(2,1)$. $z_0=3$ ($9+\ln1=9$ ✓). $F_x=z-\frac{y}{z-xy}=2$, $F_y=1-\frac{x}{z-xy}=-1$, $F_z=x+1+\frac1{z-xy}=4$ ⇒ $\nabla f(2,1)=\big(-\tfrac12,\tfrac14\big)$. Aprox. lineal: $f\approx3-\tfrac12(x-2)+\tfrac14(y-1)$. Recta normal al gráfico: $X=(2,1,3)+t\,(-\tfrac12,\tfrac14,-1)$, dirección $\propto(2,-1,4)$. V/F "paralela a $r:\{-2x-y+8=0,\ z=3\}$": dirección de $r$ es $(-1,2,0)$, no proporcional a $(2,-1,4)$ → **Falso**. *(calculado por Claude; verificalo contra `resueltos/2024-05-10_resuelto.pdf`)*

---

## 5 · Gradiente · direccional · cadena · aproximación (12 de 24)

$$
f'(A,\hat u)=\nabla f(A)\cdot\hat u\ \ (\hat u\text{ unitario}),\qquad \nabla h=\nabla f(g)\cdot Dg\ \ (h=f\circ g)
$$

| Piden | Respuesta |
|---|---|
| máxima | $\lVert\nabla f\rVert$ en $\hat u=\nabla f/\lVert\nabla f\rVert$ |
| mínima / **máximo decrecimiento** | $-\lVert\nabla f\rVert$ en $-\nabla f/\lVert\nabla f\rVert$ |
| nula | $\perp\nabla f$: en 2D $\pm(-f_y,f_x)/\lVert\nabla f\rVert$ |
| $\hat u$ "normal a la superficie $G=0$ hacia el origen" (`2025-09-25 P1`) | $\hat u=\mp\nabla G/\lVert\nabla G\rVert$, el signo que apunte hacia $O$ |

- $\nabla f$ se evalúa en el **punto imagen** $g(a,b)$, no en $(a,b)$. $g=x\cdot f$ ⇒ $\nabla g=(f+xf_x,\ xf_y)$ (`2024-10-09 P3`).
- **Gradiente ⟂ curva de nivel:** recta normal a la curva de nivel $c$ por $P$: $X=P+t\nabla f(P)$ (`2026-02-24 P4`, `2025-02-18 T2b`). Si $f=x+y\,g(x,y)$ con $g(P)=0$: $\nabla f(P)=(1,0)+y_0\nabla g(P)$.
- Si dan un vector NO unitario y dicen "según $\bar v$": convención de la cátedra $\nabla f\cdot\bar v$ sin normalizar, salvo que digan "unitario". `2024-07-30 P3` da $(1,1,-1)$: normalizar y aclararlo.
- **Por definición** en $(0,0)$ (función partida): $f'((0,0),(a,b))=\lim_{t\to0}\frac{f(ta,tb)-f(0,0)}{t}$. Continuidad: límite por trayectorias $y=mx$, $y=kx^2$ (distintos → no existe); polares para acotar.
- **Aproximación lineal:** $z\approx z_0+z_x\Delta x+z_y\Delta y$, $\Delta=$ pedido − base (con signo). Si $G=y_p-4F$ (`2026-02-10 P1`): $\nabla G=(y_p'(x),0)-4\nabla F$.
- **Taylor grado 2** en $(a,b)$: $p=f+f_x\Delta x+f_y\Delta y+\tfrac12(f_{xx}\Delta x^2+2f_{xy}\Delta x\Delta y+f_{yy}\Delta y^2)$. Leer: $f_{xx}=2\cdot$coef$(\Delta x^2)$, $f_{xy}=$coef$(\Delta x\Delta y)$. Extremo ⇔ sin términos lineales. Si dan $D(\nabla f)$ = Hessiano directamente (`2025-09-25 P3`).
- V/F "Maclaurin $3+2x^2+y^2$ ⇒ mínimo local" (`2025-07-29 T1b`): sin lineales, $H=\operatorname{diag}(4,2)$, $D>0$, $f_{xx}>0$ → **Verdadero**.

---

## 6 · Extremos (12 de 24)

1. $\nabla f=(0,0)$ → críticos. 2. $H=\begin{pmatrix}f_{xx}&f_{xy}\\f_{xy}&f_{yy}\end{pmatrix}$, $D=f_{xx}f_{yy}-f_{xy}^2$.

| $D>0,f_{xx}>0$ | $D>0,f_{xx}<0$ | $D<0$ | $D=0$ |
|---|---|---|---|
| mínimo local | máximo local | silla | analizar signo de $f-f(P)$ a mano |

- **Región cerrada** (`2026-05-19 P4`: $f=y$ en $x^2+y^2\le4$): interior ($\nabla f=0$; acá no hay) + frontera (parametrizar $(2\cos t,2\operatorname{sen}t)$ o Lagrange $\nabla f=\lambda\nabla g$) → comparar valores: máx $2$ en $(0,2)$, mín $-2$ en $(0,-2)$.
- **Sin Hessiano** (raíces/valores absolutos/potencias 4): argumento directo. $(x-y)^4+(y-1)^2\ge0=f(1,1)$ → mínimo absoluto, **estricto** (sólo se anula ahí). $9-\sqrt{4x^2+2y^4}\le9=f(0,0)$ → máximo.
- "No tiene máximos locales" (`2026-07-14 T2a`, $f=xy+x^3+y^2$): en todo crítico $f_{yy}=2>0$ → nunca máximo → **Verdadero**.
- Definiciones (plan B del teórico): ver flashcards 26.

---

## 7 · Integrales múltiples · áreas · cambio de variables (13 de 24)

| Sistema | Fórmulas | $\lvert J\rvert$ |
|---|---|---|
| Polares | $x=\rho\cos\varphi$, $y=\rho\operatorname{sen}\varphi$ | $\rho$ |
| Cilíndricas | polares + $z$ | $\rho$ |
| Esféricas | $x=\rho\operatorname{sen}\theta\cos\varphi$, $y=\rho\operatorname{sen}\theta\operatorname{sen}\varphi$, $z=\rho\cos\theta$ ($\theta$ desde $z^+$) | $\rho^2\operatorname{sen}\theta$ |

- Cambio de variables: $\iint_D f\,dx\,dy=\iint_{D^*}f(x(u,v),y(u,v))\,\lvert J\rvert\,du\,dv$. Lineal ⇒ $J$ cte ⇒ área$(D)=\lvert J\rvert\cdot$área$(D^*)$. `2025-09-25 T2b`: $(u+2v,2u+v)$, $J=-3$, área$(D)=12$ → área$(D^*)=\boxed4$.
- $\rho=2a\cos\varphi$ ↔ $x^2+y^2=2ax$ (centro $(a,0)$); $\rho=2a\operatorname{sen}\varphi$ ↔ centro $(0,a)$. $x^2+y^2\le2x$ → **completar cuadrados**.
- Cono $z=\sqrt{x^2+y^2}$ en esféricas: $\theta=\pi/4$. Cono ∩ esfera radio $R$: circunferencia $\rho=R/\sqrt2$ a $z=R/\sqrt2$.

**Volumen / masa:** $V=\iint_D(z_{\text{techo}}-z_{\text{piso}})\,dA$; $m=\iiint_V\delta\,dV$. Densidad ∝ distancia: al eje $z$ → $k\rho$; al plano $xy$ → $k|z|$; al plano $yz$ → $k|x|$; al origen → $k\rho_{\text{esf}}$. "Sólo plantear" = límites + integrando + jacobiano, sin calcular. "**Dos integrales distintas**" = proyectar sobre $xy$ y sobre $xz$ (o $yz$): cambia qué variable queda adentro.

- `2025-07-15 P3`: $(x-1)^2+y^2\le z\le5-2x$ → proyección $x^2+y^2\le4$, integrando $4-\rho^2$ → $\boxed{8\pi}$.
- V/F integral en cilíndricas (`2025-12-16 T1a`, `2026-07-14 T2b`, `2024-10-09 T2b`): chequear **techo/piso en $z$**, **rango de $\rho$** (intersección) y **el jacobiano $\rho$** dentro del integrando. `2026-07-14 T2b`: esfera radio 3 ∩ cono → $\rho$ va hasta $3/\sqrt2$, no hasta $3$ → **Falso**.

**Área de superficie / integral escalar:** $dS=\sqrt{1+g_x^2+g_y^2}\,dA$; $\iint_S h\,d\sigma=\iint_D h(x,y,g)\,dS$. Cono $z=\sqrt{x^2+y^2}$: $dS=\sqrt2\,dA$ ⇒ área $=\sqrt2\cdot$área$(D)$. Plano $z=x+y$: $dS=\sqrt3\,dA$.

- `2025-07-29 P3`: cono sobre $x^2+4y^2\le4$ (elipse, área $2\pi$) → $\boxed{2\sqrt2\,\pi}$. `2026-05-19 P2`: $\iint_S y\,d\sigma$ con $D$: $x^2+(y-2)^2\le4$ → $\sqrt2\iint_D y\,dA=\sqrt2\cdot\bar y\cdot$área$=\sqrt2\cdot2\cdot4\pi=\boxed{8\sqrt2\,\pi}$. `2025-12-02 P1`: $\sqrt3\cdot$(cuarto de elipse $x^2+\frac{y^2}4\le1$, área $\frac{2\pi}{4}$) $=\boxed{\tfrac{\sqrt3\,\pi}{2}}$.

---

## 8 · Teóricos: esqueletos (elegís UNO)

**T-A · Independencia de la trayectoria** ($f=\nabla\varphi$, $\lambda:[a,b]\to$ dominio, $\lambda(a)=A$, $\lambda(b)=B$):
1. $h(t)=\varphi(\lambda(t))$ → regla de la cadena: $h'(t)=\nabla\varphi(\lambda(t))\cdot\lambda'(t)=f(\lambda(t))\cdot\lambda'(t)$.
2. $\int_\lambda f\cdot d\lambda=\int_a^b h'(t)\,dt$.
3. Barrow: $=h(b)-h(a)=\varphi(B)-\varphi(A)$. ∎ (cerrada ⇒ $0$)

**T-B · Green + área:** enunciar (hipótesis: $f\in C^1$ en $D$, $D$ región regular, $\partial D$ cerrada simple antihoraria). Deducción del área: elegir $f$ con $Q_x-P_y=1$ → $\oint_{\partial D}f\cdot d\lambda=\iint_D1\,dA=$ área$(D)$. Dos campos: $(0,x)$ y $(-y,0)$; su promedio da $\tfrac12\oint x\,dy-y\,dx$.

**T-C · Stokes:** $f\in C^1$; $S$ simple, orientable, borde $\partial S$ curva regular simple; orientaciones coherentes (mano derecha). $\oint_{\partial S}f\cdot d\lambda=\iint_S\operatorname{rot}f\cdot\hat n\,dS$.

**T-D · Gauss:** $f\in C^1$; $\Omega$ región simple del espacio dentro del dominio; $\partial\Omega$ cerrada, orientable por partes, normales **exteriores**. $\oiint_{\partial\Omega}f\cdot\hat n\,dS=\iiint_\Omega\operatorname{div}f\,dV$. "¿Aplicable en forma directa a una superficie abierta?" → **No**: hay que cerrarla (§1).

**Otros que cayeron** (si los sabés): condición necesaria de conservativo ($P_y=Q_x$ vía Schwarz, flashcard 9); cambio de variables (flashcard 11) y jacobiano de polares $=\rho$ (flashcard 12); definir función potencial (flashcard 8); punto regular de curva / superficie (§4).

**Plan B (definiciones, sin apuntes en el repo — flashcards 25 y 26):** derivada direccional por definición (§5); "todo diferenciable es derivable" → **Verdadero** (`2026-02-24 T1a`); función partida $\frac{2x^2y}{x^2+y^2}$ / $\frac{xy^2}{x^2+y^2}$ en $(0,0)$: derivadas parciales existen y valen $0$, pero **no es diferenciable** (el cociente $\frac{f(h,k)}{\sqrt{h^2+k^2}}$ no tiende a $0$: por $h=k$ da constante $\ne0$) ⇒ no admite plano tangente (`2026-07-28 T1b`, `2025-12-16 T2b`, `2024-03-05 T2b`).

---

## 9 · Reciclados del final con resultado

| Problema (examen) | Resultado |
|---|---|
| Flujo cilindro corrido $x^2+y^2=2x$, $f=(-y,x,xz)$, 1er octante (`2025-07-15 P4`) | $4$ saliente (`2025-12-02 P4` cambia el campo: rehacer $f\cdot N$) |
| Volumen $(x-1)^2+y^2\le z\le5-2x$ (`2025-07-15 P3`) | $8\pi$ |
| área$(D^*)$ con $(u+2v,2u+v)$, área$(D)=12$ (`2025-09-25 T2b`) | $4$ |
| Implícita $xz+z+y+\ln(z-xy)=10$ en $(2,1)$ (B6) | $z_0=3$, $\nabla f=(-\tfrac12,\tfrac14)$ |
| $y''-4y'+4y=25\operatorname{sen}x$ (`2026-07-28 P3`) | $(C_1+C_2x)e^{2x}+4\cos x+3\operatorname{sen}x$ |
| Equipotencial de $\frac{(2x,2y)}{x^2+y^2}$ por $(1,0)$ (`2025-07-15 T2b`) | $x^2+y^2=1$ |
| $a$ para $y=kx^3\perp x^2+ay^2=C$ (`2026-03-03 P3`) / $y=kx^4$ (`2024-12-03 P4`) | $a=3$ / $b=4$ |
| Extremos de $f=y$ en $x^2+y^2\le4$ (`2026-05-19 P4`) | máx $2$ en $(0,2)$, mín $-2$ en $(0,-2)$ |
| Área del cono sobre $x^2+4y^2\le4$ (`2025-07-29 P3`) | $2\sqrt2\,\pi$ |
| Punto regular de $(t^3+3t^2,\,t^2+4t,\,3)$ en $(4,-4,3)$ (`2024-10-09 T1b`) | $t=-2$, $\lambda'=\bar0$ → **no** regular |

Los marcados como calculados en §4 y §7 son de Claude, no de la cátedra: **verificar contra `resueltos/` cuando exista.**

---

## 10 · OJO — errores que cuestan puntos

- **Elegir 3 y soltar 3.** Resolver los 6 es el error más caro del final: 2 horas no alcanzan.
- Green y Gauss exigen **antihorario / saliente**; "sentido negativo" o "normal con segunda componente negativa" → signo $-$. **Escribí la orientación elegida** — lo piden en casi todos los P.
- Gauss **no** sobre superficie abierta; y si el campo no está definido en un punto interior, tampoco.
- Flujo por gráfica: $(-g_x,-g_y,1)$ mira hacia arriba; si piden hacia abajo, $(g_x,g_y,-1)$.
- Si te dan $Df$ o $\operatorname{rot}f$ y no $f$: **no intentes reconstruir $f$**, es Stokes.
- Jacobiano siempre: $\rho$ / $\rho^2\operatorname{sen}\theta$. En "área$(D^*)$" va $\lvert J\rvert$.
- $x^2+y^2\le2x$, $x^2+y^2=y$, $x^2-2x+y^2=0$ → **completar cuadrados antes que nada**.
- Implícita: hallar $z_0$ primero; verificar $F_z\ne0$. $\nabla f$ de la composición se evalúa en el **punto imagen**.
- Resonancia: mirar si el candidato está en $y_H$ **antes** de derivar. Condiciones iniciales en $y_H+y_p$.
- Trayectorias ortogonales: eliminar la constante **antes** de invertir la pendiente.
- Extremos: $D<0$ es silla, no "sin información". Región cerrada ⇒ mirar la frontera siempre.
- V/F: un contraejemplo concreto vale tanto como una demostración. "Falso" sin justificar vale $0$.

---

*Generado el 2026-09-13 desde `estrategia.md`, `plan.md`, `examenes/INDICE.md` (24 finales),
`../segundo-parcial/repaso/machete.md` (fórmulas de `../segundo-parcial/apuntes/md/` 01–19) y
`../primer-parcial/repaso/machete.md`. Iterar sobre este .md; exportar con `/machete --pdf`.*
