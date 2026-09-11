# Resoluciones oficiales 1C 2025 (K3052)

> Fuente: `2025-1C_Parcial_respuestas.pdf` (hoja OneNote de la cátedra fechada 2025-05-02) y `2025-1C_Recuperatorio_respuestas.pdf` (fechada 2025-06-23), curso K3052. Enunciados en `../INDICE.md` (secciones 2025-1C). Transcripción del método y del resultado final tal como aparecen en la hoja. La hoja usa `s` para la variable de Laplace, `j` para la unidad imaginaria y `m` o `n` indistintamente como índice.

---

## Parcial — Tema 1

### Ej1a — SEF con coeficientes reales, f(t)=π−t en 0<t<π → STF

**Método**
1. Coeficientes reales ⇒ completar como función **par**. Gráfico: triángulo con pico π en t=0. Analíticamente `f(t) = π+t si −π<t<0 ; π−t si 0<t<π`, con `T=2π`, `L=π`, `w0=1`.
2. Par ⇒ `bm = 0`; `a0/2 = π/2` (lo saca "por gráfico": área del triángulo / período).
3. `am = (2/π)∫₀^π (π−t)cos(mt) dt`, separa en dos integrales; la de `π·cos(mt)` se anula (`sen(mπ)=0`), la de `t·cos(mt)` se integra por partes: `[cos(mt)/m² + t·sen(mt)/m]₀^π`.
4. Resultado por paridad de m: `am = −(2/π)[(−1)^m/m² − 1/m²]` → si m par `am=0`; si m impar `am = 4/(πm²)`. Reindexa con `m = 2k+1`.

**Resultado final**
- `am = 4/(π m²)` (m impar), `am = 0` (m par), `bm = 0`, `a0/2 = π/2`
- `S(t) = π/2 + (4/π) Σ_{k=0}^∞ cos[(2k+1)t]/(2k+1)²`

### Ej1b — STF de f(x)=2sen(x)cos(x)

**Método**
1. Identidad trigonométrica: `2 sen x cos x = sen(2x) + sen(x−x) = sen(2x)`.
2. Alternativa mostrada ("Sino"): escribir con exponenciales `f(x) = 2·(e^{jx}−e^{−jx})/(2j) · (e^{jx}+e^{−jx})/2 = (1/2j)(e^{2jx} + 1 − 1 − e^{−2jx}) = (e^{2jx}−e^{−2jx})/(2j) = sen(2x)`.
3. La función ya ES un armónico ⇒ la STF es la propia función: un solo término no nulo (`b2 = 1`). (La hoja concluye `= sen(2x)`; la opción marcada no está escrita, pero corresponde a **c) un solo término no nulo**.)

**Resultado final**
- `f(x) = sen(2x)` ⇒ STF = un solo término (opción c).

### Ej1c — f(t)=t en 0<t<1, SEF con coeficientes imaginarios puros + simetría de media onda

**Método**
1. Coeficientes imaginarios puros ⇒ completar **impar** (`am = 0`).
2. Simetría de media onda (S.M.O.) ⇒ `f(t+T/2) = −f(t)`: espeja el tramo `t` en (0,1) bajando hacia 0 en t=2 y repite invertido a la izquierda. Período `T=4`.
3. Sólo se pide gráfico + expresión analítica; no desarrolla la serie.

**Resultado final**
- `f(t) = −t−2 si −2<t<−1 ; t si −1<t<1 ; −t+2 si 1<t<2`, extendida con `T=4`. Anotado "impar" y "S.M.O.".

### Ej2a — ∫₀^∞ t·e^{−5t}·cos(t) dt

**Método**
1. Reconoce la integral como una transformada evaluada: `∫₀^∞ t·e^{−st}cos(t) dt = L{t·cos t}(s)` con `s=5`.
2. Propiedad de multiplicación por t (derivación en s): `L{t·cos t} = −(s/(s²+1))' = −(s²+1−2s²)/(s²+1)² = (s²−1)/(s²+1)²`.
3. Evalúa en s=5.

**Resultado final**
- `L{t cos t} = (s²−1)/(s²+1)²` ; en s=5: `24/26² = 24/676`.

### Ej2b — Antitransformar Y(s)=1/(s²+1)²

**Método**
1. Factoriza `Y = F·G` con `F(s)=G(s)=1/(s²+1)` ⇒ `f(t)=g(t)=sen t`.
2. Teorema de convolución: `y(t) = ∫₀^t sen(u)·sen(t−u) du`.
3. Identidad trigonométrica producto→suma: `y(t) = ½∫₀^t [cos(t) − cos(2u−t)] du`.
4. Integra: `y(t) = ½ t·cos(t) ∓ ½[sen(2u−t)/2]₀^t` (la hoja escribe el primer término con signo `−½ t cos t`), y usa `sen t − sen(−t) = 2 sen t`.

**Resultado final**
- `y(t) = −½ t·cos(t) + ½ sen(t)` (recuadrado).

### Ej2c — Demostrar L{2^t}=1/(s−ln2)

**Método**
1. Reescribe `2^t = e^{ln 2^t} = e^{t·ln 2}`.
2. Tabla `L{e^{at}} = 1/(s−a)` con `a = ln 2`.

**Resultado final**
- `L{2^t} = L{e^{t ln 2}} = 1/(s − ln 2)`.

### Ej3a — G(s) del sistema f−Ky−By'=My'' (M=1,B=2,K=2), reposo

**Método**
1. Identifica `f(t)` = entrada, `y` = salida; reposo ⇒ `y(0)=0` (posición) y `y'(0)=0` (velocidad inicial). `G(s) = Y(s)/F(s)`.
2. Transforma miembro a miembro: `F − 2Y − 2(sY − y(0)) = s²Y − s·y(0) − y'(0)`; tacha los términos con condiciones iniciales.
3. `F = Y(s² + 2s + 2)` ⇒ despeja.

**Resultado final**
- `G(s) = 1/(s² + 2s + 2)`.

### Ej3b — Respuesta a f(t)=−e^{−t}

**Método**
1. `F(s) = −1/(s+1)`; `Y = G·F = −1/((s²+2s+2)(s+1))`.
2. Fracciones simples: `(As+B)/(s²+2s+2) + C/(s+1)`; `C` por cover-up: `C = −1/1 = −1`.
3. Identidad `(As+B)(s+1) − 1·(s²+2s+2) = −1` → cuadráticos `A−1=0 ⇒ A=1`; independientes `B−2=−1 ⇒ B=1`.
4. Completa cuadrados: `Y = (s+1)/((s+1)²+1) − 1/(s+1)` y antitransforma con desplazamiento en s.

**Resultado final**
- `y(t) = cos(t)·e^{−t} − e^{−t}` (recuadrado).

### Ej4a — Transformada Z y ROC de x(n) = (−2)^n (n par) / 4^{−n} (n impar)

**Método**
1. Escribe la serie término a término: `X(z) = (−2)^0 z^0 + 4^{−1} z^{−1} + (−2)² z^{−2} + 4^{−3} z^{−3} + …`.
2. Separa pares e impares en dos geométricas: `Σ_{k=0}^∞ (4/z²)^k + (1/(4z)) Σ_{k=0}^∞ (1/(16z²))^k`.
3. Suma cada geométrica: `1/(1−4/z²) + (1/(4z))·1/(1−1/(16z²))` y simplifica.
4. ROC de cada una: R.C.(1) `|4/z²|<1 ⇒ |z|>2`; R.C.(2) `|1/(16z²)|<1 ⇒ |16z²|>1 ⇒ |z|>1/4`. La ROC total es la intersección (dibuja dos círculos concéntricos y se queda con el exterior del mayor): "Este es el R.C."

**Resultado final**
- `X(z) = z²/(z²−4) + 4z/(16z²−1)`, ROC: `|z| > 2`.

### Ej4b — Σ_{n=0}^∞ (3^n/n!)·2^{−n} mediante Z

**Método**
1. Reconoce `Σ x(n) z^{−n}` con `z=2`: la suma es `Z{3^n/n!}` evaluada en `z=2`.
2. Tabla: `Z{a^n/n!} = e^{a/z}` ⇒ `Z{3^n/n!} = e^{3/z}`.

**Resultado final**
- `Σ = e^{3/2}`.

---

## Parcial — Tema 2

### Ej1a — SEF con coeficientes imaginarios puros, f(t)=−π−t en −π<t<0 → STF

**Método**
1. Imaginarios puros ⇒ completar **impar**: `f(t) = −π−t si −π<t<0 ; π−t si 0<t<π`, `f(t)=f(t+2π)`, `T=2π`, `L=π`, `w0=1` (diente de sierra).
2. Impar ⇒ `a0 = am = 0`.
3. `bm = (2/π)∫₀^π (π−t) sen(mt) dt = 2[−cos(mt)/m]₀^π − (2/π)[sen(mt)/m² − t·cos(mt)/m]₀^π` (partes).
4. Evalúa: `= 2[(−(−1)^m + 1)/m] − (2/π)[−π(−1)^m/m] = −2(−1)^m/m + 2/m + 2(−1)^m/m`; los términos con `(−1)^m` se cancelan.

**Resultado final**
- `bm = 2/m`
- `S(t) = 2 Σ_{m=1}^∞ sen(mt)/m`

### Ej1b — STF de 2sen(x)cos(x)

- "Ídem Tema 1": `= sen(2x)` ⇒ un solo término no nulo.

### Ej1c — f(t)=t en 0<t<1, SEF con coeficientes reales + media onda

**Método**
1. Reales ⇒ completar **par** (`bm=0`); S.M.O. ⇒ `f(t+2) = −f(t)`, `T=4`.
2. Gráfico: espeja `t` a la izquierda como `−t` en (−1,0); en (1,2) baja de −1 a 0 (`t−2`), y en (−2,−1) simétrico (`−t−2`).

**Resultado final**
- `f(t) = −t−2 si −2<t<−1 ; −t si −1<t<0 ; t si 0<t<1 ; t−2 si 1<t<2`, anotado "par" y "S.M.O.".

### Ej2a — L{sen³t}

**Método**
1. Escribe `sen³(t) = ((e^{jt}−e^{−jt})/(2j))³`, desarrolla el cubo: `= −1/(8j)·(e^{3jt} − 3e^{2jt}e^{−jt} + 3e^{jt}e^{−2jt} − e^{−3jt})`.
2. Reagrupa en senos: `= −¼[(e^{3jt}−e^{−3jt})/(2j) − 3(e^{jt}−e^{−jt})/(2j)] = −¼ sen(3t) + ¾ sen(t)`.
3. Transforma por linealidad con tabla `L{sen(at)} = a/(s²+a²)`.

**Resultado final**
- `sen³t = −¼ sen(3t) + ¾ sen t`
- `L{sen³t} = −(1/4)·3/(s²+9) + (3/4)·1/(s²+1) = −(3/4)·1/(s²+9) + (3/4)·1/(s²+1)`

### Ej2b — Antitransformar por convolución Y(s)=s²/(s²+1)²

**Método**
1. `F(s)=G(s)=s/(s²+1)` ⇒ `f=g=cos t`.
2. `y(t) = ∫₀^t cos(u)cos(t−u) du = ½∫₀^t [cos(t) + cos(2u−t)] du`.
3. `= ½ t·cos t + ½[sen(2u−t)/2]₀^t = ½ t·cos t + ¼[sen(t) − sen(−t)]`.

**Resultado final**
- `y(t) = ½ t·cos(t) + ½ sen(t)`.

### Ej3a — G(s)=10(s²−4s+k)/(s³+5s²+4s−10): K para que sea estable

**Método**
1. Factoriza el denominador por Ruffini con raíz 1: `1 5 4 −10 → 1 6 10 | 0` ⇒ `s³+5s²+4s−10 = (s−1)(s²+6s+10)`.
2. El polo en `s=1` es inestable (semiplano derecho); "Hay que eliminar el polo en s=1" ⇒ el numerador debe anularse en s=1: `1² − 4·1 + k = 0`.

**Resultado final**
- `k = 3` (recuadrado).

### Ej3b — Respuesta al escalón unitario

**Método**
1. Con k=3, Ruffini en el numerador (`1 −4 3` raíz 1 → `1 −3 | 0`) y cancela `(s−1)`: `G(s) = 10(s−3)/(s²+6s+10)`.
2. Escalón ⇒ `F(s) = 1/s`; `Y(s) = 10(s−3)/(s(s²+6s+10))`.
3. Fracciones simples `A/s + (Bs+C)/(s²+6s+10)`; `A` por cover-up: `A = −30/10 = −3`. Identidad `−3(s²+6s+10) + (Bs+C)s = 10(s−3)` → cuadráticos `−3+B=0 ⇒ B=3`; lineales `−18+C=10 ⇒ C=28`.
4. Completa cuadrados y separa para que aparezca `(s+3)`: `Y = −3/s + 3(s+3)/((s+3)²+1) + 19/((s+3)²+1)`.

**Resultado final**
- `y(t) = −3 + 3·cos(t)·e^{−3t} + 19·sen(t)·e^{−3t}` (el último exponente queda cortado en el borde de la hoja, ≈ `e^{−3t}` por el desplazamiento usado).

### Ej3c — Tipo de respuesta y valor estable

- "Rta. oscilatoria amortiguada" (polos complejos conjugados con parte real negativa: `−3 ± j`).
- Valor estable `−3` (término constante `−3/s`; equivale a `lim_{s→0} s·Y(s) = G(0)`).

### Ej4a — Σ_{n=0}^∞ cos(πn)·3^{−n} mediante Z

**Método**
1. `Σ cos(πn) 3^{−n} = Z{cos(πn)}` evaluada en `z=3`.
2. Tabla `Z{cos(Ωn)} = z(z−cosΩ)/(z²−2z cosΩ+1)` con `Ω=π`: `Z{cos(πn)} = (z²+z)/(z²+2z+1)`.
3. Evalúa en z=3: `(9+3)/(9+6+1)`.

**Resultado final**
- `Σ = 12/16` (= 3/4).

### Ej4b — x(n+1)−4x(n)=4(1−n)2^n, x(0)=3

**Método**
1. Expande el lado derecho: `4·2^n − 4n·2^n`.
2. Transforma con la propiedad de adelanto `Z{x(n+1)} = zX(z) − z·x(0)` y tablas `Z{2^n} = z/(z−2)`, `Z{n·2^n} = 2z/(z−2)²`: `zX − 3z − 4X = 4z/(z−2) − 8z/(z−2)²`.
3. Despeja: `X(z)(z−4) = 4z/(z−2) − 8z/(z−2)² + 3z` ⇒ `X(z) = [4z(z−2) − 8z + 3z(z−2)²]/((z−2)²(z−4))`.
4. Fracciones simples "dejando una z afuera" (trabaja con `X(z)/z`): `A/(z−2)² + B/(z−2) + C/(z−4) = [4(z−2) − 8 + 3(z−2)²]/((z−2)²(z−4))`. Cover-up: `A = −8/(−2) = 4`, `C = 12/4 = 3`; cuadráticos `B+3=3 ⇒ B=0`.
5. `X(z) = 4z/(z−2)² + 3z/(z−4)`; escribe `4z/(z−2)² = 2·(2z/(z−2)²)` para usar `Z{n·2^n}`.

**Resultado final**
- `x(n) = 2·n·2^n + 3·4^n`.
- La verificación de x(2) NO aparece en la hoja (calculada aparte: `x(2) = 64`, coincide con iterar la recurrencia `x(1)=16`, `x(2)=64`).

---

## Recuperatorio

### Ej1a — f(x)=2x en (0,2): completar para STF de senos y desarrollar

**Método**
1. Serie de senos ⇒ completar **impar**: `f(x) = 2x si x∈(−2,2)` ∧ `f(x)=f(x+4)`. `T=4`, `L=2`, `w0=π/2`.
2. `a0 = am = 0`. `bm = (2/2)∫₀² 2x·sen(mπx/2) dx`, por partes: `2[sen(mπx/2)/(m²π²/4) − x·cos(mπx/2)/(mπ/2)]₀²`; el término de seno se anula (tachado).
3. `cos(mπ) = (−1)^m`.

**Resultado final**
- `bm = −8(−1)^m/(mπ)`
- `S(x) = (−8/π) Σ_{m=1}^∞ ((−1)^m/m)·sen(mπx/2)`

### Ej1b — Cn de la SEF a partir de la STF

**Método**
1. Relación STF→SEF: `Cn = ½(an − bn·j)`, con `an = 0`.

**Resultado final**
- `Cn = (4/(nπ))·(−1)^n·j`

### Ej1c — Espectro |Cn| vs w0·n

- Gráfico de bastones: `|Cn| = 4/(|n|π)`, simétrico respecto de 0, nulo en n=0, decreciente en `±1w0, ±2w0, ±3w0, ±4w0` (envolvente hiperbólica punteada).

### Ej2a — ∫₀^∞ (e^{−5t}−e^{−10t})/t dt

**Método**
1. Saca factor `e^{−5t}`: `∫₀^∞ e^{−st}·(1−e^{−5t})/t dt = L{(1−e^{−5t})/t}` en `s=5`.
2. Propiedad de división por t: primero verifica que existe `lim_{t→0} (1−e^{−5t})/t = lim 5e^{−5t} = 5` (L'Hôpital).
3. `L{f/t} = ∫_s^∞ F(u) du` con `F(u) = 1/u − 1/(u+5)`: `= [ln|u| − ln|u+5|]_s^∞ = ln|u/(u+5)| |_s^∞ = 0 − ln|s/(s+5)| = ln|(s+5)/s|`.
4. Evalúa en s=5.

**Resultado final**
- `L{(1−e^{−5t})/t} = ln|(s+5)/s|` ; `∫₀^∞ (e^{−5t}−e^{−10t})/t dt = ln 2` (recuadrado).

### Ej2b — L[∫₀^t u·cos(u)·e^{t−u} du]

**Método**
1. Teorema de convolución: `L{∫₀^t f(u)g(t−u) du} = F(s)·G(s)`, identifica `f(u) = u·cos(u)`, `g(t−u) = e^{t−u}` ("pensarlo como e^t").
2. `F(s)` por multiplicación por t^n: `L{cos u} = s/(s²+1)`, derivo `(s²+1−2s²)/(s²+1)²`, cambio de signo ⇒ `F(s) = (s²−1)/(s²+1)²`.
3. `G(s) = 1/(s−1)`.
4. Multiplica y simplifica `(s²−1) = (s−1)(s+1)`.

**Resultado final**
- `F(s)·G(s) = (s²−1)/(s²+1)² · 1/(s−1) = (s+1)/(s²+1)²` (recuadrado).

### Ej3a — Polos y ceros de G(s)=2(s²+2s−3)/((s−1)(s+2)(s²+8s+17)); estabilidad

**Método**
1. Factoriza el numerador: `s²+2s−3 = (s+3)(s−1)` y cancela `(s−1)` con el denominador.
2. `G(s) = 2(s+3)/((s+2)(s²+8s+17))`; raíces del cuadrático: `−4 ± j`.
3. Diagrama polos/ceros en el plano s (cero ◯ en −3, polos × en −2 y −4±j).
4. Todos los polos con parte real negativa ⇒ estable.

**Resultado final**
- Ceros: `Z0 = −3`, `Z1 = ∞`. Polos: `P1 = −2`, `P3 = −4+j`, `P4 = −4−j`. "Sistema estable".

### Ej3b — Corte por el eje real de |G(s)|

- Gráfico cualitativo de `|G(σ)|`: tiende a ∞ en `σ=−2` (polo real), se anula en `σ=−3` (cero), tiene un lomo finito centrado en `σ=−4` (rotulado "polos complejos conjugados"), y decae hacia ±∞.

### Ej3c — Respuesta a f(t)=e^{−3t}

**Método**
1. `F(s) = 1/(s+3)`; `Y = G·F = 2/((s+2)(s²+8s+17))` (el cero en −3 cancela al polo de la entrada).
2. Fracciones simples `A/(s+2) + (Bs+C)/(s²+8s+17)`; cover-up `A = 2/5`. Identidad `(2/5)(s²+8s+17) + Bs² + Cs + 2Bs + 2C = 2` → cuadráticos `2/5 + B = 0 ⇒ B = −2/5`; independientes `(2/5)·17 + 2C = 2 ⇒ C = 1 − 17/5 = −12/5`.
3. Completa cuadrados `(s+4)²+1` y parte el numerador para que aparezca `(s+4)`: `Y = (2/5)·1/(s+2) − ((2/5)s + 8/5)/((s+4)²+1) − (4/5)/((s+4)²+1)`.

**Resultado final**
- `y(t) = (2/5)e^{−2t} − (2/5)cos(t)e^{−4t} − (4/5)sen(t)e^{−4t}` (recuadrado).

### Ej4a — V/F: la ROC de x(n)=(−2)^n (n par) / 4^{−n} (n impar) es |z|>2

**Método**
1. Expande `X(z) = (−2)^0 z^0 + 4^{−1}z^{−1} + (−2)²z^{−2} + 4^{−3}z^{−3} + …` y separa en dos geométricas: `Σ_{k}(−2/z)^{2k} + Σ_{k}(1/(4z))^{2k+1} = Σ(4/z²)^k + (1/(4z))Σ(1/(16z²))^k`.
2. "Con eso alcanza para ver el radio de convergencia": no hace falta sumar, sólo exigir razón <1 en cada geométrica: `|4/z²|<1 ⇒ |z|>2` ∧ `|1/(16z²)|<1 ⇒ |z²|>1/16 ⇒ |z|>1/4`.
3. Intersección: `|z|>2`.

**Resultado final**
- `|z| > 2` (recuadrado) → **Verdadero**.

### Ej4b — Transformada Z de la secuencia finita x(1)=1, x(2)=3, x(3)=2, x(4)=1

**Método**
1. Definición directa: suma finita `Σ x(n) z^{−n}`.
2. Lleva a común denominador `z⁴`.

**Resultado final**
- `X(z) = 1·z^{−1} + 3z^{−2} + 2z^{−3} + 1·z^{−4} = (z³ + 3z² + 2z + 1)/z⁴` (ROC implícita: todo z ≠ 0; la hoja no la escribe).

---

## Patrones transversales

- **Completar para Fourier según el tipo de coeficiente pedido:** "coeficientes reales" ⇒ extensión **par** (`bn=0`); "imaginarios puros" / "serie de senos" ⇒ extensión **impar** (`a0=an=0`). Siempre anota `T`, `L`, `w0` al costado del gráfico y escribe la función por tramos. (T1-Ej1a/c, T2-Ej1a/c, Rec-Ej1a)
- **Simetría de media onda:** `f(t+T/2) = −f(t)`; construye el gráfico espejando el tramo dado con signo cambiado y el período resulta el doble del intervalo extendido (`T=4` para t∈(0,1)). Sólo pide gráfico + fórmula por tramos, no la serie. (T1-Ej1c, T2-Ej1c)
- **Evaluar `cos(mπ)=(−1)^m`, `sen(mπ)=0` y separar por paridad de m** para reindexar con `2k+1` cuando los pares se anulan. (T1-Ej1a, T2-Ej1a, Rec-Ej1a)
- **STF→SEF:** `Cn = ½(an − j·bn)`; el espectro `|Cn|` se grafica como bastones simétricos sobre `w0·n`. (Rec-Ej1b/c)
- **Integrales impropias `∫₀^∞ … e^{−at} dt` ⇒ una Laplace evaluada en `s=a`:** reconocer el patrón, transformar con la propiedad que corresponda y recién al final sustituir `s`. Idem en Z: `Σ x(n)·c^{−n} = X(z)|_{z=c}`. (T1-Ej2a, T1-Ej4b, T2-Ej4a, Rec-Ej2a)
- **Multiplicación por t ⇒ derivar en s y cambiar signo:** `L{t·f} = −F'(s)`, aplicado a `cos` en dos exámenes: `L{t cos t} = (s²−1)/(s²+1)²`. (T1-Ej2a, Rec-Ej2b)
- **División por t ⇒ `L{f/t} = ∫_s^∞ F(u)du`**, verificando antes con L'Hôpital que exista `lim_{t→0} f/t`; el resultado sale como logaritmo `ln|(s+a)/s|`. (Rec-Ej2a)
- **Potencias de seno ⇒ exponenciales complejas:** `sen³t` se expande con el binomio en `e^{±jt}` y se reagrupa en `sen(3t)` y `sen t`; también sirve para justificar `2 sen x cos x = sen 2x`. (T1-Ej1b, T2-Ej2a)
- **Convolución para antitransformar polos dobles complejos `1/(s²+1)²`, `s²/(s²+1)²`:** partir en `F·G` con `sen`/`cos`, integrar `∫₀^t f(u)g(t−u)du` usando producto→suma; y en el sentido directo, `L{∫₀^t f(u)g(t−u)du} = F·G`. (T1-Ej2b, T2-Ej2b, Rec-Ej2b)
- **Sistemas: `G(s)=Y/F` con reposo ⇒ tachar `y(0)`, `y'(0)`;** la respuesta se obtiene siempre como `Y = G·F` y fracciones simples: la constante del polo simple por **cover-up** (anotada en color arriba de la fracción), las demás igualando coeficientes "cuadráticos / lineales / independientes"; luego **completar cuadrados** y partir el numerador en `(s+a)` + constante para leer `cos·e^{−at}` y `sen·e^{−at}`. (T1-Ej3b, T2-Ej3b, Rec-Ej3c)
- **Elegir K para estabilidad:** factorizar el denominador por **Ruffini**, detectar el polo con parte real positiva y forzar que el numerador lo cancele (`N(polo)=0`). Estabilidad se decide sólo por la parte real de los polos (diagrama polos/ceros en el plano s). (T2-Ej3a, Rec-Ej3a)
- **Escalón ⇒ `F(s)=1/s`;** el término `A/s` de la descomposición ES el valor estable; el "tipo de respuesta" se nombra por los polos: complejos conjugados con Re<0 ⇒ "oscilatoria amortiguada". (T2-Ej3b/c)
- **Z de secuencias definidas por paridad:** escribir los primeros términos, separar en dos geométricas (`z^{−2k}` y `z^{−(2k+1)}`) y pedir razón <1 en cada una; la ROC es la **intersección** (`|z|>` mayor radio). La misma secuencia cae en el parcial y en el recu. (T1-Ej4a, Rec-Ej4a)
- **Ecuaciones en diferencias:** `Z{x(n+1)} = zX − z·x(0)`, tablas `Z{a^n}=z/(z−a)`, `Z{n a^n}=az/(z−a)²`, y fracciones simples sobre `X(z)/z` ("dejo una z afuera") para que cada término vuelva a la forma de tabla. (T2-Ej4b)

---

*Generado el 2026-09-10 leyendo con visión las 20 páginas de las dos hojas de respuestas oficiales. Este archivo reemplaza a los PDFs para cualquier consulta de método: no hace falta volver a abrirlos.*
