## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Herramienta |
|---|---|
| familia de curvas **ortogonales** a … | §4: pasar a $y'=f(x,y)$, ortogonal $y'=-1/f$, resolver |
| resolver / verificar una **EDO** | §4: 1er orden (factor integrante / separables); $y''+py'+qy=0$ → característica (§11) |
| derivada direccional **máxima / mínima / nula** | §1: máx $=\lVert\nabla f\rVert$ dir $\nabla f$; nula $\perp\nabla f$ |
| me dan $f'(A,\hat u_1), f'(A,\hat u_2)$, piden otra | §1: sistema $2\times2$ para $\nabla f$, después proyectar |
| $h=g\circ f$ con $g$ (la de afuera) **implícita** | §2+§3: $\nabla g$ por implícita → $\nabla h=\nabla g\cdot Df$ |
| $h=f(g)$ con $\nabla f$ y jacobiana $Dg$ dados | §2: $\nabla h(a,b)=\nabla f(g(a,b))\cdot Dg(a,b)$ |
| valor **aproximado** de $z$ (aprox. lineal) | §7: $z\approx z_0+z_x\Delta x+z_y\Delta y$, $z_x,z_y$ por implícita |
| **extremos locales** de $f(x,y)$ | §5: $\nabla f=0$ → Hessiano |
| recta tangente / **plano normal a una curva** (intersección o $\lambda(t)$) | §6: $\bar T=\nabla F_1\times\nabla F_2$ (o $\lambda'$) |
| plano tangente / **recta normal a una superficie** | §8: normal $=\nabla F$ (o $\sigma_u\times\sigma_v$) |
| me dan el **polinomio de Taylor** grado 2 | §9: leer $f,\nabla f,H$ de los coeficientes |
| definir/calcular por **definición** (función partida) | §10: cociente incremental / límite por trayectorias |

---

## 1 · Gradiente y derivada direccional (cae en el 100%)

$$
\nabla f=(f_x,f_y,\dots),\qquad f'(A,\hat u)=\nabla f(A)\cdot\hat u\quad(\hat u\ \text{unitario})
$$

| Piden | Respuesta |
|---|---|
| derivada direccional **máxima** | $\lVert\nabla f(A)\rVert$, en dirección $\hat u=\dfrac{\nabla f}{\lVert\nabla f\rVert}$ |
| **mínima** | $-\lVert\nabla f(A)\rVert$, en dirección $-\dfrac{\nabla f}{\lVert\nabla f\rVert}$ |
| dirección de derivada **nula** | las $\perp\nabla f$: en 2D $\hat u=\pm\dfrac{(-f_y,\,f_x)}{\lVert\nabla f\rVert}$ |

- **OJO dirección vs. versor:** si dan un vector $\bar v$ NO unitario, la "derivada direccional según $\bar v$" de esta cátedra es $\nabla f\cdot\bar v$ (sin normalizar) salvo que aclaren "unitario".
- **Problema "con datos"** (reciclado): $\nabla f=(p,q)$ incógnita; cada dato $f'(A,\hat u_i)=c_i$ da $p\,u_{i1}+q\,u_{i2}=c_i$ → sistema $2\times2$ → despejás $(p,q)$ → después $f'(A,\hat u_3)=\nabla f\cdot\hat u_3$. Direcciones nulas: $\perp(p,q)$.

---

## 2 · Regla de la cadena / composición (94%)

$$
h(x,y)=f\big(g(x,y)\big)\ \Rightarrow\ Dh=Df(g)\cdot Dg,\qquad \nabla h=\nabla f(g)\cdot Dg
$$

- $Dg$ = matriz jacobiana de $g$ (filas = componentes de $g$, columnas = $\partial/\partial x,\partial/\partial y$).
- **Caso `h=f(g)` con datos** (reciclado ×6): te dan $\nabla f$ en el punto imagen $g(a,b)$ y la jacobiana $Dg(a,b)$ (numérica, o la calculás de la fórmula de $g$) → multiplicás → $\nabla h(a,b)$ → aplicás §1 (máxima $=\lVert\nabla h\rVert$).
- **Caso `h=g∘f` con `g` implícita** (reciclado ×5): primero $\nabla g$ por §3, después $\nabla h=\nabla g\cdot Df$ — resultado verificado en §11. (A veces viene con los nombres al revés: $h=f\circ\bar g$ con $f$ implícita — mismo esquema.)
- **Teórico "enunciar + calcular $\nabla h$"** (reciclado): $\nabla h(1,2)=\nabla f(g(1,2))\cdot Dg(1,2)$ con $Df=(uv^2,u^2v)$, $g=(2x+y^2,yx^2)$ → $g(1,2)=(6,2)$, $\nabla f(6,2)=(24,72)$, $\nabla h(1,2)=(336,168)$.

---

## 3 · Derivación implícita (88%)

$z=f(x,y)$ definida por $F(x,y,z)=0$:

$$
f_x=-\frac{F_x}{F_z},\qquad f_y=-\frac{F_y}{F_z}\qquad(F_z\ne0)
$$

- Función $z=g(u,v)$ dada por $G(u,v,z)=0$ (el caso del combo de §2): igual, $g_u=-G_u/G_z$, $g_v=-G_v/G_z$ → $\nabla g=(g_u,g_v)$.
- Primero hallá el punto base: reemplazá $(x,y)$ dados y despejá $z_0$ (probá enteros que hagan $\ln(\cdot)=\ln 1=0$ o el exponente $=0$).
- Teorema de la función implícita (para justificar): $F(P)=0$, $F\in C^1$ y $F_z(P)\ne0$ ⇒ $z=f(x,y)$ existe y es $C^1$ en un entorno.

---

## 4 · EDO de 1er orden + trayectorias ortogonales (EDO 94% · trayectorias 63%)

**Trayectorias ortogonales** — receta:

1. De la familia $F(x,y,C)=0$, derivar y **eliminar $C$** → queda $y'=f(x,y)$.
2. Familia ortogonal: reemplazar $y'\to-\dfrac{1}{f(x,y)}$.
3. Resolver esa EDO (en todos los reciclados salió separable). Ajustar la constante con el punto dado.

**EDO lineal de 1er orden** $y'+P(x)\,y=Q(x)$ — factor integrante:

$$
\mu=e^{\int P\,dx},\qquad y=\frac{1}{\mu}\Big(\int \mu\,Q\,dx+C\Big)
$$

- Variables separables: $\dfrac{dy}{dx}=A(x)B(y)\Rightarrow\displaystyle\int\frac{dy}{B(y)}=\int A(x)\,dx$.
- **Definir solución general/particular** (teórico): general (orden $n$) = familia con $n$ constantes arbitrarias esenciales; particular = la que sale de fijar esas constantes con las condiciones dadas (PVI / punto).

---

## 5 · Extremos locales por Hessiano (81%)

1. **Puntos críticos:** resolver $\nabla f=(f_x,f_y)=(0,0)$.
2. **Hessiano** en cada crítico:

$$
H=\begin{pmatrix}f_{xx}&f_{xy}\\ f_{xy}&f_{yy}\end{pmatrix},\qquad D=f_{xx}f_{yy}-f_{xy}^{2}
$$

| Caso | Conclusión |
|---|---|
| $D>0,\ f_{xx}>0$ | mínimo local |
| $D>0,\ f_{xx}<0$ | máximo local |
| $D<0$ | punto silla (no extremo) |
| $D=0$ | no decide → analizar a mano (signo de $f-f(P)$) |

- **Extremos sobre una región** (p. ej. $x^2+y^2\le4$): críticos interiores **+** frontera (parametrizar la frontera o Lagrange $\nabla f=\lambda\nabla g$) → comparar valores.

---

## 6 · Curva en el espacio: recta tangente y plano normal (63%)

Curva $C=S_1\cap S_2$ con $S_i:\,F_i=0$, en el punto $P$:

$$
\bar T=\nabla F_1(P)\times\nabla F_2(P)
$$

- **Recta tangente:** $X=P+t\,\bar T$.  **Plano normal:** $\bar T\cdot(X-P)=0$.
- Curva paramétrica $\lambda(t)$: $\bar T=\lambda'(t_0)$.
- **Intersección curva–superficie** (reciclado): meter $\lambda(t)$ en la ecuación de la superficie → resolver en $t$ → evaluar.
- **"Determinar el plano que contiene la curva":** combiná las dos ecuaciones para eliminar el término cuadrático repetido — p. ej. de $x^2+y^2=25$ y $y^2+z^2=25$ sale $x^2=z^2$ → plano $x=z$ (el signo lo elige el punto). Si una de las superficies ya ES un plano ($y=3$, $z=x+y$…), es ese.

---

## 7 · Aproximación lineal (50%)

$$
z\approx z_0+z_x(x_0,y_0)\,\Delta x+z_y(x_0,y_0)\,\Delta y,\qquad \Delta x=x-x_0,\ \Delta y=y-y_0
$$

- Punto base = el "redondo" cercano al pedido (p. ej. $(1,2)$ para $(1.03,1.98)$). $z_x,z_y$ por §3.
- Si $z=h(x,y)$ viene de una composición con datos intermedios ($u=x\sqrt y$, etc.): $z_x,z_y$ por regla de la cadena §2.

---

## 8 · Plano tangente / recta normal a superficie (44%)

| Forma de la superficie | Normal $\bar N$ | Plano tangente |
|---|---|---|
| implícita $F(x,y,z)=0$ | $\nabla F(P)$ | $\nabla F(P)\cdot(X-P)=0$ |
| gráfica $z=g(x,y)$ | $(-g_x,-g_y,1)$ | $z=g(P)+g_x\Delta x+g_y\Delta y$ |
| paramétrica $\sigma(u,v)$ | $\sigma_u\times\sigma_v$ | $(\sigma_u\times\sigma_v)\cdot(X-P)=0$ |

- **Recta normal:** $X=P+t\,\bar N$. Intersección con un plano/eje → resolver $t$.
- **Superficie parametrizada — punto regular:** $P$ regular ⇔ $\sigma_u\times\sigma_v\ne\bar0$ ahí (los tangentes son L.I.). Hallar el $(u,v)$ que da $P$ y evaluar.

---

## 9 · Polinomio de Taylor grado 2 (19%)

Alrededor de $(a,b)$:

$$
p(x,y)=f(a,b)+f_x\,\Delta x+f_y\,\Delta y+\tfrac12\big(f_{xx}\Delta x^2+2f_{xy}\Delta x\,\Delta y+f_{yy}\Delta y^2\big)
$$

**Leer los datos del $p$ dado** ($\Delta x=x-a$, $\Delta y=y-b$):

- $f(a,b)=$ término independiente. $\nabla f(a,b)=($coef. de $\Delta x$, coef. de $\Delta y)$.
- $f_{xx}=2\cdot$coef$(\Delta x^2)$; $f_{xy}=$coef$(\Delta x\,\Delta y)$; $f_{yy}=2\cdot$coef$(\Delta y^2)$.
- **Plano tangente** en $(a,b)$: usa $f(a,b)$ y $\nabla f(a,b)$. **Extremo:** solo si $\nabla f(a,b)=0$ (no hay términos lineales) → clasificar con el Hessiano leído.

---

## 10 · Teóricos: recetas de demostración (los reciclados)

**Derivadas direccionales por definición en $(0,0)$** (función partida — el T más tomado):

$$
f'\big((0,0),(a,b)\big)=\lim_{t\to0}\frac{f(ta,tb)-f(0,0)}{t}
$$

Reemplazar y ver si el límite depende de $(a,b)$ o no existe (para $f_x$: $(a,b)=(1,0)$). Después:

- **Continuidad en $(0,0)$:** ¿$\lim_{(x,y)\to(0,0)}f=f(0,0)$? Para negarlo, dos trayectorias ($y=mx$, $y=kx^2$) con límites distintos. Para afirmarlo, acotar / polares.
- **V/F "discontinua / no admite derivada en ninguna dirección":** calcular el límite (para continuidad) y la derivada direccional por definición (para la 2ª); justificar cada una.
- **Derivada direccional máxima $=\lVert\nabla f\rVert$:** $f'(A,\hat u)=\nabla f\cdot\hat u=\lVert\nabla f\rVert\cos\theta$, máximo en $\theta=0$ ($\hat u\parallel\nabla f$). Nula: $\theta=\pi/2$.
- **Diferenciable ⇒ continua:** de la definición de diferenciabilidad, $\lim_{h\to0}[f(A+h)-f(A)]=0$.
- **Regla de la cadena (enunciar):** $g$ diferenciable en $A$ y $f$ diferenciable en $g(A)$ ⇒ $h=f\circ g$ diferenciable en $A$, con $Dh(A)=Df(g(A))\cdot Dg(A)$.

---

## 11 · Reciclados con resultado verificado (autocorrección)

> Problemas que la cátedra recicla casi textuales, con su resultado verificado: si cae uno de estos, ya sabés a qué valor tenés que llegar.

**Trayectorias ortogonales** (familia ortogonal + curva por el punto):

| Familia dada | Familia ortogonal | Curva por el punto |
|---|---|---|
| $y=Ce^{2x}$ | $x+y^2=K$ | por $(1,1)$: $x+y^2=2$ |
| $y=Ce^{-x}$ | $y^2-2x=K$ | por $(1,1)$: $y^2=2x-1$ |
| $y=kx$ | $x^2+y^2=K$ | por $(3,4)$, $(3,-4)$ o $(4,-3)$: $x^2+y^2=25$ |
| $y=k/x$ | $y^2-x^2=K$ | por $(1,1)$: $y=x$ · por $(3,4)$: $y^2-x^2=7$ |
| $xy^2=C$ | $y^2-2x^2=K$ | por $(1,2)$: $y^2-2x^2=2$ · por $(1,3)$: $y^2-2x^2=7$ |
| $y=kx^3$ | $x^2+3y^2=K$ | por $(3,4)$: $x^2+3y^2=57$ · por $(1,1)$: $x^2+3y^2=4$ (y de la familia: $y=x^3$) |

**Aproximación lineal** $xz+e^{yz-2}-2=0$: punto base $(1,2,z_0{=}1)$, $z_x=z_y=-\tfrac13$ ⇒ $z\approx1-\tfrac{\Delta x+\Delta y}{3}$.

- $(1.03,1.98)$: $z\approx 0.997$ · $(1.01,1.98)$: $z\approx 1.003$.

**Taylor** $p=5+x^2+x(y-1)+4(y-1)^2$ en $(0,1)$: $\nabla f(0,1)=(0,0)$ ⇒ **es crítico**; $f_{xx}=2,\ f_{xy}=1,\ f_{yy}=8$, $D=15>0$ ⇒ **mínimo local**; plano tangente $z=5$.

**Teórico $f'_y$ con datos** (reciclado): $f'((1,1),(1,3))=f_x+3f_y=17$ y $\lim=f_x=5$ ⇒ $\boxed{f_y(1,1)=4}$.

**EDO característica** (teórico): $y=e^{mx}$ en $y''+py'+qy=0$ ⇒ $m^2+pm+q=0$ ⇒ $m=\frac{-p\pm\sqrt{p^2-4q}}{2}$ (el enunciado pide expresarlo así). Aplicado a $y''-y'-2y=0$: $m=2,-1$ ⇒ $y=C_1e^{2x}+C_2e^{-x}$.

**Combo direccional `h=g∘f`** — reciclado ×5, siempre el mismo par en $(1,1)$: $\bar f=(xy^2,\,y-x^2)$ con $g$: $z-u^2+v^2+\ln(v+z)=0$, o el espejo $\bar f=(y-x^2,\,xy^2)$ con $g$: $z+u^2-v^2+\ln(u+z)=0$. Método: $\bar f(1,1)$ → $z_0$ → $\nabla g$ por §3 → $\nabla h=\nabla g\cdot Df$. **Resultado idéntico en los 5:** $z_0=1$, $\nabla h(1,1)=(2,\tfrac32)$ ⇒ máx $\tfrac52$ en $(\tfrac45,\tfrac35)$ · mín $-\tfrac52$ en $(-\tfrac45,-\tfrac35)$ · nulas $\pm(-\tfrac35,\tfrac45)$. Checkpoint intermedio (primer sabor): $\bar f(1,1)=(1,0)$, $\nabla g(1,0)=(1,-\tfrac12)$.

---

## 12 · OJO — errores que cuestan puntos

- **Dirección vs. versor:** para la derivada direccional máxima/nula, normalizá $\nabla f$; para "según el vector $\bar v$" seguí la convención de la cátedra (§1).
- **Trayectorias ortogonales:** el $-1/y'$ va DESPUÉS de eliminar $C$; no antes.
- **Regla de la cadena:** $\nabla f$ se evalúa en el **punto imagen** $g(a,b)$, no en $(a,b)$.
- **Implícita:** verificá $F_z\ne0$ en el punto (si no, no hay $z=f(x,y)$).
- **Extremos:** $D<0$ es **silla**, no "no hay info"; $D=0$ sí obliga a análisis a mano.
- **Taylor → extremo:** solo si los términos lineales del $p$ son nulos (punto crítico); si hay término lineal, NO es extremo.
- **Plano normal a curva vs. recta tangente:** el plano normal usa $\bar T$ como normal ($\bar T\cdot(X-P)=0$); la recta tangente usa $\bar T$ como dirección.
- **Aproximación lineal:** $\Delta x,\Delta y$ son (pedido − base), con su signo.

---

*Generado el 2026-07-10, revisado el 2026-07-15 y el 2026-07-17. Fuentes: `estrategia.md`, `examenes/INDICE.md`, `examenes/resueltos/` (no hay apuntes propios del 1P). Teóricos/demostraciones completas: checklist de `estrategia.md`.*
