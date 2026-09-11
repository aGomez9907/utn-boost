# Estrategia primer parcial — Análisis Numérico

> **Examen:** martes **2026-10-06** · faltan **26 días** (hoy 2026-09-10), pero hasta el
> **2026-09-22 rendís el final de AM2** y el **2026-09-28 el 1P de Gestión Gerencial**:
> la ventana real de AN es **2026-09-23 → 2026-10-05 (13 días, con el 28/9 bloqueado)**.
> **Punto de partida declarado:** ninguno todavía (recién se armó el dataset; venís
> cursando desde el 2026-08-11 y la clase de repaso del 1P es el 2026-09-29).
> **Fuentes analizadas:** **16 hojas de examen** de **11 instancias** (2015 → 2025) sobre
> 26 archivos originales (`examenes/INDICE.md`), **14 hojas resueltas** (`examenes/resueltos/`,
> con `RESOLUCIONES-2025.md` como transcripción de las respuestas oficiales 2025) y **0
> apuntes** (`apuntes/md/` vacía; la única fuente propia es la hoja de fórmulas
> manuscrita `../fuentes/formulas-y-metodos-manuscrito.pdf`).

---

## 0. Cómo leer este documento

1. **§1 Estructura** — el formato vigente (4 ejercicios en orden fijo) y cuánto vale cada ítem.
2. **§2 Patrón real** — frecuencia por tema sobre 16 hojas, con la lectura del formato 2025 aparte.
3. **§3 Contraste con apuntes** — no hay apuntes: qué se usa en su lugar y qué brecha es real.
4. **§4 Plan inicial** de 13 días (foto de hoy; el vivo es `plan.md`).
5. **§5 Banco de problemas tipo** con hojas exactas, y los dos simulacros a ciegas.
6. **§6 Checklist teórico** (poco, pero hay).

**Diagnóstico en una línea:** el examen es **cuatro recetas fijas** (Fourier-completar,
Laplace-propiedad/convolución, sistemas-K-y-respuesta, Z-paridad/diferencias) que se
repiten **con los mismos datos** desde 2015; no hay apuntes, pero hay 14 hojas resueltas
que muestran exactamente cómo la cátedra espera cada paso. LA brecha no es de contenido
sino de **calendario**: AN compite con el final de AM2 hasta el 22/9. La sobrecarga a
evitar: números complejos como tema aparte (81 % histórico, **0 % en el formato 2025**).

---

## 1. Estructura del examen

**Formato vigente (curso K3052, 2025-1C, parcial y recuperatorio):** 4 ejercicios en orden
fijo, cada ítem a/b/c vale **1 punto**, **10 ítems**, se aprueba con **6** (promoción con 8).
Dos temas (T1/T2) con los mismos tipos de ítem. Sin ejercicio de complejos.

| Posición | Qué cae casi siempre (formato 2025, confirmado por las 3 hojas K3052) | Puntos |
|---|---|---|
| **Ej1 · Fourier** | a) función dada en medio período → **completar** (par si piden coeficientes reales / cosenos; impar si imaginarios puros / senos) y **desarrollar la STF**. b) ítem corto: justificar la STF de `2 sen x cos x` (es `sen 2x`, un solo término) o pasar de `bₙ` a `Cₙ`. c) volver a completar la función pero con **simetría de media onda** (solo gráfico + expresión por tramos) o graficar el **espectro** `\|Cₙ\|`. | 3 |
| **Ej2 · Laplace** | a) **integral impropia** resuelta como una transformada evaluada (`∫ t e^{−5t} cos t`, `∫ (e^{−5t}−e^{−10t})/t`) o una **transformada con truco** (`sen³ t` por exponenciales). b) **antitransformar `1/(s²+1)²`** o `s²/(s²+1)²` **por convolución**, o transformar una convolución dada. c) (solo T1) **demostrar** algo corto (`L(2ᵗ) = 1/(s − ln 2)`). | 2–3 |
| **Ej3 · Sistemas estables** | `G(s)` dada (o a obtener desde la EDO de un sistema mecánico): **K para que sea estable** (cancelar el polo positivo), polos y ceros, **corte de `\|G(s)\|` por el eje real**, **respuesta temporal** al escalón / `e^{−t}` / `e^{−3t}` por fracciones simples, **tipo de respuesta y valor estable**. | 2–3 |
| **Ej4 · Transformada Z** | a) `x(n)` definida por **paridad de n** → `X(z)` con dos geométricas y **ROC** (o V/F sobre la ROC). b) **ecuación en diferencias** de 1er orden con verificación de `x(2)`, o **suma de una serie numérica** evaluando `X(z)` en un punto, o Z de una **secuencia finita**. | 2 |

**Formato viejo (2015 → 2024-2C, 13 de las 16 hojas):** 5 ejercicios (2 puntos c/u o tabla
fraccionada), con un ejercicio de **números complejos** y un ítem de **multiple choice
justificado**. Los ejercicios de Fourier/Laplace/sistemas/Z son los mismos que hoy: sirven
todos para practicar; solo el ejercicio de complejos y los MC quedan como repaso rápido.

**Lo que define la estrategia:** con 10 ítems y 6 para aprobar, **no hace falta saber todo**.
Ej1a + Ej3 completo + Ej4 completo son **7 ítems que salen de recetas cerradas**; Ej2a/b
suman 2 más. Ej1c (media onda), Ej2c (demostración) y los ítems "raros" son el margen.

---

## 2. Patrón real: frecuencia por tema (16 hojas distintas)

> N = **16 hojas** (cada Tema 1 / Tema 2 es una hoja con problemas propios; ver Anexo A).
> Los porcentajes son sobre 16. La columna "2025" cuenta sobre las **3 hojas del formato
> vigente** (2025-1C T1, T2 y recuperatorio): es la que manda cuando difieren.

| # | Tema | Aparece en | % | 2025 | Prioridad |
|---|---|---|---|---|---|
| 1 | **Laplace, algún ítem** (integral impropia / ecuación integral / antitransformada / transformada) | 16 de 16 | 🔴 100 % | 3/3 | MÁXIMA |
| 2 | **Transformada Z, algún ítem** | 16 de 16 | 🔴 100 % | 3/3 | MÁXIMA |
| 3 | **Fourier: completar la función y desarrollar** (`#CompletarFuncion`) | 15 de 16 | 🔴 94 % | 3/3 | MÁXIMA |
| 4 | **Sistemas: estabilidad / elegir K** (`#Estabilidad`) | 15 de 16 | 🔴 94 % | 2/3 | MÁXIMA |
| 5 | **Sistemas: respuesta temporal** (`#RespuestaTemporal`) | 14 de 16 | 🔴 88 % | 3/3 | MÁXIMA |
| 6 | Serie trigonométrica desarrollada (`#SerieTrigonometrica`) | 14 de 16 | 🔴 88 % | 3/3 | MÁXIMA |
| 7 | Serie exponencial / `Cₙ` (`#SerieExponencial`) | 13 de 16 | 🟠 81 % | 3/3 | ALTA |
| 8 | **Números complejos como ejercicio propio** | 13 de 16 | 🟠 81 % | **0/3** | ⚪ **solo como herramienta** |
| 9 | Antitransformada por fracciones simples (`#Antitransformada`, explícita) | 11 de 16 | 🟠 69 % | 2/3 | ALTA (está dentro de todo Ej3) |
| 10 | Convolución (`#Convolucion`, directa o inversa) | 9 de 16 | 🟠 56 % | 3/3 | ALTA |
| 11 | Ecuación en diferencias (`#EcuacionDiferencia`) | 8 de 16 | 🟠 50 % | 1/3 | ALTA |
| 12 | Integral impropia por Laplace (`#IntegralPorLaplace`) | 8 de 16 | 🟠 50 % | 2/3 | ALTA |
| 13 | Multiple choice justificado (`#MultipleChoice`) | 8 de 16 | 🟠 50 % | 1/3 (solo Ej1b) | 🟡 formato viejo |
| 14 | Simetría de media onda (`#SimetriaMediaOnda`) | 7 de 16 | 🟡 44 % | 2/3 | **ALTA en 2025** |
| 15 | `X(z)` de sucesión por paridad + ROC (`#TransformadaZ #ROC`) | 7 de 16 | 🟡 44 % | 2/3 | **ALTA en 2025** |
| 16 | Corte de `\|G\|` por el eje real (`#CorteEje`) | 7 de 16 | 🟡 44 % | 1/3 | MEDIA |
| 17 | Ecuación integral / integro-diferencial (`#EcuacionIntegral`) | 7 de 16 | 🟡 44 % | 0/3 | MEDIA |
| 18 | Calcular una transformada de Laplace con truco (`#TransformadaLaplace`) | 5 de 16 | 🟡 31 % | 2/3 | MEDIA-ALTA |
| 19 | Valor medio (`#ValorMedio`) | 5 de 16 | 🟡 31 % | 0/3 | MEDIA |
| 20 | Suma de serie numérica vía Z (`#SumaSeriePorZ`) | 4 de 16 | 🟡 25 % | 2/3 | **ALTA en 2025** |
| 21 | Tipo de respuesta y valor estable (`#TipoRespuesta`) | 4 de 16 | 🟡 25 % | 1/3 | MEDIA (1 punto barato) |
| 22 | Suma de serie numérica vía Fourier (`#SumaSerieNumerica`) | 3 de 16 | ⚪ 19 % | 0/3 | BAJA |
| 23 | Polos y ceros explícitos (`#PolosCeros`) | 3 de 16 | ⚪ 19 % | 1/3 | BAJA (sale gratis del Ej3) |
| 24 | V/F justificado (`#VoF`) | 3 de 16 | ⚪ 19 % | 1/3 | BAJA |
| 25 | Espectro de amplitudes (`#Espectro`) | 2 de 16 | ⚪ 13 % | 1/3 | BAJA (5 min si sabés `Cₙ`) |
| 26 | Secuencia finita → `X(z)` (`#SecuenciaFinita`) | 2 de 16 | ⚪ 13 % | 1/3 | BAJA (regalo) |
| 27 | Módulo por método gráfico (`#ModuloGrafico`) | 2 de 16 | ⚪ 13 % | 0/3 | BAJA |
| 28 | Fasores / superposición de senoidales (`#Fasores`) | 2 de 16 | ⚪ 13 % | 0/3 | BAJA |
| 29 | `G(s)` desde la EDO del sistema (`#FuncionTransferencia`) | 1 de 16 | ⚪ 6 % | **1/3** | MEDIA (es reciente) |
| 30 | Sistema de EDO por Laplace (`#SistemaEDO`) | 1 de 16 | ⚪ 6 % | 0/3 | BAJA |
| 31 | Antitransformada Z suelta (`#AntitransformadaZ`) | 1 de 16 | ⚪ 6 % | 0/3 | BAJA (es el paso final de toda ec. en diferencias) |
| 32 | Demostración (`#Demostracion`) | 1 de 16 | ⚪ 6 % | 1/3 | MEDIA (Ej2c del T1 2025) |

### Lectura del patrón

- **Núcleo duro = las cuatro recetas del formato vigente.** Fourier-completar (94 %),
  sistemas K + respuesta (94 % / 88 %), Laplace (100 %) y Z (100 %) están en *todas* las
  hojas desde 2015. No hay temas "comodín" que roten: rota el **sub-ítem**, no el tema.
- **Tema rey: Ej3 Sistemas.** Es el ejercicio con más ítems (2–3 puntos), con la receta más
  mecánica (Ruffini → cancelar polo positivo → `Y = G·F` → fracciones simples → completar
  cuadrados) y con el `G(s)` **más reciclado del dataset** (`10(s²−4s+k)/(s³+5s²+4s−10)`, 3
  veces textual). Si dominás este ejercicio tenés 2–3 puntos casi fijos.
- **Fourier "completar" es el ítem más estable de todos** (15/16): siempre la misma decisión
  binaria (par ↔ coeficientes reales / cosenos; impar ↔ imaginarios puros / senos) más una
  integral por partes. El ítem c) de 2025 le agrega **media onda**: es 1 punto de puro
  dibujo si sabés `f(t + T/2) = −f(t)`.
- **Z en 2025 se partió en dos moldes:** la **sucesión por paridad con ROC** (2/3 hojas,
  6/16 históricas) y la **suma de serie evaluando `X(z)`** (2/3 hojas). La ecuación en
  diferencias (50 % histórico) bajó a 1/3 pero sigue siendo el ítem b) natural.
- **Complejos desaparecieron como ejercicio** (0/3 en 2025, cronograma 2026 con "repaso
  rápido" de 1 clase) pero siguen siendo **herramienta** dentro de los otros: raíces de
  polinomios para polos (`s² + 6s + 10 = 0`), exponenciales complejas para `sen³ t` y
  `cos³ t`, `ln 2` para `L(2ᵗ)`. Se estudian como repaso de 1 hora, no como tema.
- **Lo que no vale la pena:** módulo gráfico, fasores, sistemas de EDO, suma de series vía
  Fourier. Juntos no llegan a 1 punto esperado.

### Problemas reciclados (oro para practicar; detalle en `examenes/INDICE.md` → "Problemas reciclados")

- `G(s) = 10(s² − 4s + k)/(s³ + 5s² + 4s − 10)` → **sin-fecha K3521 T2, 2024-2C T1, 2025-1C T2** (3 veces; `k = 3`; respuesta al escalón `y(t) = −3 + 3cos(t)e^{−3t} + 19sen(t)e^{−3t}`, oscilatoria amortiguada, valor estable −3).
- `f(x) = 4` en `(0,2)`, `k` en `(−2,0)`, período 4 → `k = 2` (sin cosenos, valor medio 3) y SEF con `k = −4`/`0` → **2015-05-29 T1, sin-fecha-2 T1, 2024-2C T2** (3 veces).
- `y(t) − ∫₀ᵗ y(u) sen(t−u) du = t⁴` → **2022-10-11, 2024-1C T1** (textual) + 3 variantes con coseno (familia de 5 hojas).
- `x(n+1) − 4x(n) = 4(1−n)2ⁿ`, `x(0) = 3` → **sin-fecha K3521 T2, 2025-1C T2** (textual; `x(n) = 2n·2ⁿ + 3·4ⁿ`).
- `2x(n+2) − x(n+1) = 3x(n) − 1` → **2022-10-11, 2024-1C T1** (textual).
- `∫₀^∞ (e^{−5t} − e^{−10t})/t dt = ln 2` → **sin-fecha K3521 T2, 2025-1C rec** (textual).
- Antitransformar `1/(s²+1)²` → **2024-2C rec, 2025-1C T1** (textual); `s²/(s²+1)²` por convolución en 2025-1C T2.
- Sucesión por paridad (`(−2)ⁿ` / `4^{−n}` y variantes) + ROC → **6 hojas**, incluidas las 3 de 2025 (T1 directo, rec como V/F) y 2025-02-13.
- Secuencia finita `(0,1,3,2,1)` → **sin-fecha-2 T2, 2025-1C rec** (mismo gráfico).
- `G(s)` con `(s² + 8s + 17)` y polo positivo a cancelar → **4 hojas** (2022-10-11, 2024-2C rec, 2025-1C rec, sin-fecha-2 T2).

---

## 3. Contraste con tus apuntes

### 3.1 🔴 Brechas críticas

**No hay apuntes** en `apuntes/md/` (la cursada arrancó el 2026-08-11 y no se procesaron
las clases virtuales). Por definición de la skill, TODOS los temas 🔴/🟠 son brecha. Pero
la brecha real es chica, porque el material que reemplaza a los apuntes ya existe en el repo:

| Tema 🔴/🟠 | Sin apunte | Con qué se cubre (ya en el repo) | Costo si no se cubre |
|---|---|---|---|
| Fourier: completar + STF/SEF + media onda | ✗ | `resueltos/RESOLUCIONES-2025.md` (Ej1 T1/T2/rec, con la regla par/impar y la construcción de SMO paso a paso) + 5 hojas resueltas por alumnos + hoja de fórmulas pág. 1–2 | ~3 puntos por examen |
| Laplace: integral impropia, convolución, `1/(s²+1)²` | ✗ | `RESOLUCIONES-2025.md` (Ej2 ×3) + hoja de fórmulas pág. 2–3 (propiedades, división por t, convolución) | ~2 puntos |
| Sistemas: K, respuesta, tipo | ✗ | `RESOLUCIONES-2025.md` (Ej3 ×3, con Ruffini + cover-up + completar cuadrados) + `2022-10-11` y `2024-1C` resueltos por la cátedra + hoja de fórmulas pág. 4 (tabla polo → tipo de respuesta) | ~3 puntos |
| Z: paridad + ROC, diferencias, sumas | ✗ | `RESOLUCIONES-2025.md` (Ej4 ×3) + `2024-2C_Parcial_respuestas.docx` (sumas `Σ n 2^{−n}`, `Σ n² 4^{−n}`) + hoja de fórmulas pág. 5 | ~2 puntos |

**La única brecha de contenido que no se cierra con lo que hay:** las **tablas** de
transformadas (Laplace y Z) tal como las permite usar la cátedra. Hay que confirmar en la
clase del 2026-09-29 **si se rinde con tabla** y cuál. Si no, va al machete.

**Brecha de calendario (la de verdad):** entre hoy y el 2026-09-22 el tiempo es de AM2. AN
arranca en serio el 23/9 con **13 días** y el 28/9 bloqueado por Gestión Gerencial.

**Opcional, si querés apuntes de verdad:** las clases virtuales de la cátedra están
listadas en `../fuentes/clases-virtuales-links.pdf` (teórica + práctica + OneNote por
tema). Con `/apuntes-batch` sobre los 4 temas del 1P se cierran las brechas con material
propio, pero **no antes del 22/9**: no compite con AM2.

### 3.2 🟡 Sobrecarga innecesaria

| Material | Frecuencia | Recomendación |
|---|---|---|
| Números complejos como tema (potencias, raíces, conjuntos, logaritmo) | 81 % histórico, **0 % en 2025** | 1 hora de repaso instrumental (polar, raíces de cuadráticas complejas, `ln z` valor principal). No hacer los Ej1 viejos de conjuntos. |
| Multiple choice de formato viejo | 50 % histórico, 1 ítem en 2025 | Leer las opciones marcadas en el INDICE como "verdades rápidas" (ej. `L(aᵗ) = 1/(s − ln a)`); no practicarlos como ejercicios. |
| Suma de series numéricas vía Fourier (`Σ 1/(2k+1)² = π²/8`) | 19 %, 0 en 2025 | Saber la idea (evaluar `S(t)` en un punto de continuidad); un ejemplo alcanza. |
| Método gráfico del módulo, fasores, sistemas de EDO | ≤ 13 % | Saltear. |
| Apunte de cátedra `metodo-fracciones-simples.pdf` | herramienta | Leer una vez: se usa en TODOS los Ej3 y Ej4. |

> **Traducción práctica:** cada hora que no gastes en conjuntos de complejos pasala a
> **respuesta temporal con fracciones simples** (es la operación que más veces hay que
> hacer bien en el examen: Ej3b y Ej4b la necesitan).

### 3.3 Mapa tema → fuente → frecuencia → qué hacer

| Tema | Fuente en el repo (no hay apuntes) | Frec. | Qué hacer |
|---|---|---|---|
| Fourier: completar (par/impar) + STF | `RESOLUCIONES-2025.md` Ej1a T1/T2/rec; hoja fórmulas p.1 | 94 % | **Dominar.** Automatizar la decisión par/impar y la integral por partes. |
| Fourier: `Cₙ` desde `aₙ, bₙ`; SEF | `RESOLUCIONES-2025.md` rec Ej1b; 2024-2C respuestas | 81 % | **Dominar** (`Cₙ = ½(aₙ − j bₙ)`, `C₀ = a₀/2`). |
| Simetría de media onda (gráfico + tramos) | `RESOLUCIONES-2025.md` Ej1c T1/T2; 2024-1C T1/T2 resueltos | 44 % (2/3 en 2025) | **Dominar**: 1 punto de dibujo. |
| Valor medio / `k` para condición | 2015 T1, sin-fecha-2 T1 resueltos | 31 % | Saber: `a₀/2 = (1/T)∫ f`. |
| Laplace: integral impropia (`t·f`, `f/t`) | `RESOLUCIONES-2025.md` Ej2a T1 y rec; hoja fórmulas p.2 | 50 % | **Dominar** las dos propiedades + existencia del límite. |
| Laplace: convolución (ida y vuelta), `1/(s²+1)²` | `RESOLUCIONES-2025.md` Ej2b T1/T2, rec Ej2b | 56 % | **Dominar** (producto → suma de senos/cosenos). |
| Ecuación integral con convolución | 2022-10-11 y 2024-1C resueltos por cátedra; sin-fecha-2 T1/T2 | 44 % | Saber: es la misma convolución al revés. Un ejemplo. |
| Transformada con truco (`sen³`, `cos³`, `aᵗ`) | `RESOLUCIONES-2025.md` Ej2c T1, Ej2a T2; 2024-2C rec respuestas | 31 % | Saber fórmula y un ejemplo; **poder demostrar `L(aᵗ)`**. |
| Sistemas: K estable + polos/ceros | `RESOLUCIONES-2025.md` Ej3a T2 y rec; 2022-10-11 Ej5 | 94 % | **Dominar** (Ruffini + cancelar). |
| Sistemas: respuesta temporal + tipo + valor estable | `RESOLUCIONES-2025.md` Ej3b/c ×3; 2024-1C T1 Ej5; hoja fórmulas p.4 | 88 % | **Dominar + la tabla polo → respuesta.** |
| Sistemas: corte por eje real | 2025-1C rec Ej3b; 2015 T2; 2022-10-11 | 44 % | Saber dibujarlo cualitativamente (∞ en polos, 0 en ceros, lomo en complejos). |
| `G(s)` desde la EDO (sistema mecánico) | `RESOLUCIONES-2025.md` Ej3a T1 | 6 % (2025-1C T1) | Saber: transformar con reposo y despejar `Y/F`. 15 min. |
| Z: sucesión por paridad + ROC | `RESOLUCIONES-2025.md` Ej4a T1 y rec Ej4a; 2024-2C respuestas ×2 | 44 % (2/3) | **Dominar** (dos geométricas, ROC = intersección). |
| Z: ecuación en diferencias + verificación | `RESOLUCIONES-2025.md` Ej4b T2; 2015 T1/T2, 2022-10-11, 2024-1C resueltos | 50 % | **Dominar** (adelanto, `X(z)/z`, tablas `aⁿ`, `n aⁿ`). |
| Z: suma de serie evaluando `X(z)` | `RESOLUCIONES-2025.md` Ej4b T1, Ej4a T2; 2024-2C respuestas | 25 % (2/3) | Saber fórmula + tabla (`Z{aⁿ/n!} = e^{a/z}`, `Z{cos Ωn}`). |
| Z: secuencia finita | `RESOLUCIONES-2025.md` rec Ej4b | 13 % | Regalo: definición directa. |
| Complejos (herramienta) | 2022-10-11 Ej3 y 2024-1C Ej3 resueltos | 0 % en 2025 | Repaso de 1 h: raíces de cuadráticas complejas, polar, `ln z`. |

---

## 4. Plan inicial de 13 días (2026-09-23 → 2026-10-05)

> Foto de hoy. **Supuestos:** hasta el 22/9 no se toca AN (final de AM2); el 28/9 se rinde
> Gestión Gerencial (día bloqueado, y los dos anteriores livianos); el 29/9 es la clase
> presencial de repaso del 1P. El plan vivo es `plan.md` (`/plan`), que se recalcula con
> `registro.md`.

| Día | Foco | Entregable del día |
|---|---|---|
| **D1 · mié 2026-09-23** | 🔴 Fourier: la receta (par/impar, `T, L, ω₀`, integral por partes). Leer `RESOLUCIONES-2025.md` Ej1 ×3 y hoja de fórmulas p.1. | Resolver **2025-1C T1 Ej1a** y **2025-1C T2 Ej1a** sin mirar; corregir contra las respuestas oficiales. |
| **D2 · jue 2026-09-24** | 🔴 Fourier: `Cₙ`, SEF, valor medio, **media onda**. | **2015-05-29 T1 Ej1** (el reciclado `4/k`), **2025-1C T1 Ej1c** y **T2 Ej1c** (SMO), **sin-fecha K3521 T2 Ej3** (`3x`, cosenos + `Cₙ`). |
| **D3 · vie 2026-09-25** | 🔴 Laplace: propiedades `t·f`, `f/t`, integrales impropias, `L(aᵗ)` con demostración. | **2025-1C T1 Ej2a**, **2025-1C rec Ej2a** (`ln 2`), **sin-fecha K3521 T1 Ej2** (`t cos 3t e^{−5t}`), escribir la demostración de `L(2ᵗ)`. |
| **D4 · sáb 2026-09-26** | 🟠 Laplace: convolución ida y vuelta, `1/(s²+1)²`, ecuación integral. (Día liviano por GG: 1,5 h.) | **2025-1C T1 Ej2b**, **2025-1C T2 Ej2a/b** (`sen³`, convolución), **2024-1C T1 Ej2** (ecuación integral, con resolución de cátedra). |
| **D5 · dom 2026-09-27** | ⚪ Solo GG. AN: 20 min de hoja de fórmulas p.2–3 antes de dormir. | — |
| **lun 2026-09-28** | 🚫 **Parcial de Gestión Gerencial.** | — |
| **D6 · mar 2026-09-29** | 🔴 Sistemas I: **clase de repaso presencial** + Ruffini, K estable, polos/ceros, corte por eje real. Confirmar en clase **si se rinde con tabla**. | **2025-1C T2 Ej3a**, **2025-1C rec Ej3a/b**, **2022-10-11 Ej5a/b**. Anotar en `registro.md` lo que el profe dijo que "seguro cae". |
| **D7 · mié 2026-09-30** | 🔴 Sistemas II: respuesta temporal completa (fracciones simples, cover-up, completar cuadrados), tipo de respuesta y valor estable. | **2025-1C T2 Ej3b/c** (el reciclado ×3), **2025-1C rec Ej3c**, **2024-1C T1 Ej5** (con corte de `Y(s)`). Cronometrar: 25 min cada uno. |
| **D8 · jue 2026-10-01** | 🔴 Sistemas III + `G(s)` desde la EDO. Repaso instrumental de complejos (1 h). | **2025-1C T1 Ej3a/b** (sistema mecánico), **2024-2C rec Ej4** (`a, b` para estable), **2024-1C T2 Ej4a/b** (respuesta al impulso). |
| **D9 · vie 2026-10-02** | 🔴 Z I: sucesión por paridad + ROC, secuencia finita, sumas evaluando `X(z)`. | **2025-1C T1 Ej4a/b**, **2025-1C T2 Ej4a**, **2024-2C T1 Ej5b** y **T2 Ej5a/b**, **sin-fecha K3521 T1 Ej5**. |
| **D10 · sáb 2026-10-03** | 🔴 Z II: ecuaciones en diferencias con verificación (1er y 2do orden). | **2025-1C T2 Ej4b** (reciclado), **2015-05-29 T1 Ej4** y **T2 Ej4**, **2024-1C T1 Ej4** (2do orden), **2024-2C rec Ej5**. |
| **D11 · dom 2026-10-04** | 🔴 **Simulacro a ciegas 1:** `2025-1C_Recuperatorio.pdf` completo, cronometrado (≈ 2 h). Corregir contra `resueltos/2025-1C_Recuperatorio_respuestas.pdf` / `RESOLUCIONES-2025.md`. `/registrar` errores. | Examen completo + lista de errores. Después: `/machete` con la hoja de fórmulas + lo que falló. |
| **D12 · lun 2026-10-05** | 🟠 **Simulacro a ciegas 2:** `2024-2C_Parcial.docx` Tema 2 (Ej2–Ej5, saltando el de complejos) o un `/simulacro` generado. Repaso liviano del machete y de los errores del registro. **Nada nuevo.** | Checklist teórico escrito de memoria (§6). |
| **mar 2026-10-06** | **EXAMEN.** | — |

---

## 5. Banco de "problemas tipo"

Nombres cortos de hoja como en `examenes/INDICE.md` (los archivos están en `examenes/` y
`examenes/resueltos/`; las respuestas oficiales 2025 transcriptas en `RESOLUCIONES-2025.md`).

- **Fourier — completar par/impar + STF:** `2025-1C T1 Ej1a` (π−t, par), `2025-1C T2 Ej1a` (−π−t, impar), `sin-fecha K3521 T2 Ej3` (3x, cosenos), `sin-fecha-2 T2 Ej3` (x+1, senos), `2022-10-11 Ej1` (t+2, cosenos), `2024-1C T2 Ej1` (t², cosenos).
- **Fourier — `k` para valor medio / sin cosenos + SEF:** `2015-05-29 T1 Ej1`, `sin-fecha-2 T1 Ej3`, `2024-2C T2 Ej2`, `sin-fecha K3521 T1 Ej3` (|t|/k), `2015-05-29 T2 Ej1` (2t/k(t)).
- **Fourier — media onda (gráfico + tramos):** `2025-1C T1 Ej1c`, `2025-1C T2 Ej1c`, `2024-1C T1 Ej1b`, `2024-1C T2 Ej1c`, `2025-02-13 Ej2a`.
- **Fourier — `Cₙ`, SEF y espectro:** `2025-1C rec Ej1` (reservado a ciegas), `2024-2C rec Ej2` (pulso, espectro), `2024-2C T1 Ej2`.
- **Fourier — ítem corto conceptual:** `2025-1C Ej1b` (2 sen x cos x), `2015-05-29 T2 Ej2i` (cos³), `sin-fecha-2 T2 Ej1c` (x² sen x: coeficientes), `2025-02-13 Ej2b` (escalonada: valor medio, SMO, qué coeficientes).
- **Laplace — integral impropia:** `2025-1C T1 Ej2a`, `sin-fecha K3521 T1 Ej2`, `sin-fecha K3521 T2 Ej2` (= `2025-1C rec Ej2a`, reservado), `2015-05-29 T1 Ej2i` (tⁿ e^{−2t}), `2024-2C T1/T2 Ej3b` (sen t / t).
- **Laplace — transformada con truco / demostración:** `2025-1C T1 Ej2c` (L(2ᵗ)), `2025-1C T2 Ej2a` (sen³), `2024-2C rec Ej3a` (cos³), `sin-fecha-2 T1 Ej1a` (2ᵗ e^{−4t}).
- **Laplace — convolución / `1/(s²+1)²`:** `2025-1C T1 Ej2b`, `2025-1C T2 Ej2b`, `2024-2C rec Ej3b`, `2025-1C rec Ej2b` (reservado).
- **Laplace — ecuación integral:** `2022-10-11 Ej2` = `2024-1C T1 Ej2` (t⁴, resuelto por cátedra), `2024-1C T2 Ej2` (cos, =1), `sin-fecha-2 T1 Ej2`, `sin-fecha-2 T2 Ej2`.
- **Sistemas — K estable + polos/ceros + corte:** `2025-1C T2 Ej3a`, `2025-1C rec Ej3a/b` (reservado), `2022-10-11 Ej5`, `2015-05-29 T2 Ej3a`, `sin-fecha K3521 T1 Ej4a/b`, `2024-2C rec Ej4a` (a y b), `2024-1C T1 Ej5a/b/c`.
- **Sistemas — respuesta temporal + tipo + valor estable:** `2025-1C T2 Ej3b/c` (escalón, reciclado ×3), `2024-1C T1 Ej5d`, `2024-1C T2 Ej4b` (impulso), `2024-2C T2 Ej4b` (e^{−t}), `2015-05-29 T1 Ej3c` (e^{−t}), `sin-fecha K3521 T1 Ej4c` (impulso), `2025-02-13 Ej4` (eᵗ(1+2t)).
- **Sistemas — `G(s)` desde la EDO:** `2025-1C T1 Ej3`.
- **Z — sucesión por paridad + ROC:** `2025-1C T1 Ej4a`, `2024-2C T1 Ej5a`, `2024-2C T2 Ej5a`, `sin-fecha K3521 T1 Ej5`, `2025-02-13 Ej5`, `2025-1C rec Ej4a` (V/F, reservado).
- **Z — sumas evaluando `X(z)`:** `2025-1C T1 Ej4b`, `2025-1C T2 Ej4a`, `2024-2C T1 Ej5b`, `2024-2C T2 Ej5b`.
- **Z — ecuación en diferencias:** `2025-1C T2 Ej4b` (= `sin-fecha K3521 T2 Ej5`), `2015-05-29 T1 Ej4`, `2015-05-29 T2 Ej4`, `2024-2C rec Ej5`, `2022-10-11 Ej4` (= `2024-1C T1 Ej4`, 2do orden), `2024-1C T2 Ej5` (2do orden).
- **Z — antitransformada / secuencia finita:** `sin-fecha-2 T1 Ej4`, `sin-fecha-2 T2 Ej4` (= `2025-1C rec Ej4b`).

> **Simulacros "a ciegas" (no mirar hasta D11/D12; `/simulacro` no debe reciclarlos):**
> **`2025-1C_Recuperatorio.pdf`** (formato vigente completo, con respuestas oficiales) y
> **`2024-2C_Parcial.docx` Tema 2** (Ej2–Ej5; el Ej1 de complejos se saltea). Ojo: el
> `2025-1C rec Ej4b` es la misma secuencia finita que `sin-fecha-2 T2 Ej4` y el `Ej2a` es
> el mismo `ln 2` de `sin-fecha K3521 T2`: si practicás esos antes, el simulacro pierde
> un poco de sorpresa; están marcados "reservado" arriba.

---

## 6. Checklist teórico — tenés que poder ESCRIBIRLO, no solo reconocerlo

Esta cátedra casi no pide demostraciones largas: pide **justificaciones cortas** dentro de
los ítems. Todo esto sale de las hojas resueltas (no hay apunte propio).

- [ ] **`L(aᵗ) = 1/(s − ln a)`** — demostración en 2 líneas (`aᵗ = e^{t ln a}`). *(2025-1C T1 Ej2c; `RESOLUCIONES-2025.md`)*
- [ ] **Regla par/impar de Fourier:** por qué "coeficientes reales" ⇒ extensión par (`bₙ = 0`) y "imaginarios puros" / "serie de senos" ⇒ impar (`a₀ = aₙ = 0`); `Cₙ = ½(aₙ − j bₙ)`. *(todas las hojas de Fourier)*
- [ ] **Simetría de media onda:** definición `f(t + T/2) = −f(t)` y consecuencia (solo armónicos impares). Saber decir cuándo una función completada **no** la tiene. *(2025-1C Ej1c; sin-fecha-2 T2 Ej3b; 2025-02-13 Ej2b)*
- [ ] **Valor medio** `= a₀/2 = (1/T)∫_T f` y cómo se fija con `k`. *(2015 T1; 2024-2C T2)*
- [ ] **STF de `2 sen x cos x`** es un solo término (`sen 2x`); de `cos³ x` dos términos y valor medio nulo. *(2025-1C Ej1b; 2015 T2 Ej2i)*
- [ ] **Propiedades de Laplace** que se usan sin tabla: `L{t f} = −F'(s)`, `L{f/t} = ∫_s^∞ F(u) du` (**con la condición de existencia de `lim_{t→0} f/t`**), traslación en `s`, `L{f'} = sF − f(0)`, `L{f''} = s²F − s f(0) − f'(0)`. *(hoja de fórmulas p.2)*
- [ ] **Teorema de convolución** en las dos direcciones. *(2025-1C Ej2b ×3)*
- [ ] **Estabilidad:** un sistema es estable sii todos los polos tienen parte real negativa; polo en el eje imaginario ⇒ marginalmente estable. Tabla **tipo de polo → tipo de respuesta** (real negativo: exponencial decreciente; complejos con Re < 0: oscilatoria amortiguada; nulo/imaginarios puros: marginal; Re > 0: inestable). *(hoja de fórmulas p.4; 2015 T1 Ej3a)*
- [ ] **Valor estable** `= lim_{t→∞} y(t) = lim_{s→0} s·Y(s)` (TVF) = el coeficiente de `A/s` con entrada escalón. *(2025-1C T2 Ej3c)*
- [ ] **ROC de la transformada Z:** serie geométrica converge sii `|razón| < 1`; con dos series la ROC es la **intersección** (`|z| >` el mayor radio). *(2025-1C rec Ej4a como V/F)*
- [ ] **Propiedades de Z:** adelanto `Z{x(n+1)} = zX − z x(0)`, `Z{x(n+2)} = z²X − z² x(0) − z x(1)`, `Z{n x(n)} = −z X'(z)`, `Z{aⁿ} = z/(z−a)`, `Z{n aⁿ} = az/(z−a)²`, `Z{aⁿ/n!} = e^{a/z}`, `Z{cos Ωn}`. *(hoja de fórmulas p.5; `RESOLUCIONES-2025.md` Ej4)*
- [ ] **Verdades rápidas del MC viejo:** `ln` de un real negativo tiene siempre la misma parte imaginaria (`π + 2kπ`); `zⁿ = 1` tiene raíces imaginarias puras sii `4 | n`; `∫₀^∞ tⁿ e^{−at} dt = n!/a^{n+1}`; el valor principal de `jʲ` es real positivo (`e^{−π/2}`); una polinómica real de grado 5 tiene al menos una raíz real. *(2015 T1/T2, sin-fecha-2, 2025-02-13 Ej1b)*

---

## Anexo A — Equivalencias entre exámenes

- La unidad es la **hoja** (Tema 1 y Tema 2 de una misma fecha son hojas distintas con
  problemas distintos): 16 hojas de 11 instancias. Ver la lista completa en
  `examenes/INDICE.md` → "Cómo está armado el dataset".
- `examenes/duplicados/2025-1C_Recuperatorio_respuestas_copia.pdf` ≡
  `examenes/resueltos/2025-1C_Recuperatorio_respuestas.pdf` (idénticos). No cuenta.
- No hay hojas idénticas entre sí; el reciclaje es por ejercicio (§2).
- 3 hojas no tienen fecha exacta (`sin-fecha_…K3521` ≈ 2019-10-15, `sin-fecha-2_…` ≈ 2015)
  y 4 solo tienen cuatrimestre (`2024-1C`, `2024-2C`, `2025-1C`): cuentan igual, son
  exámenes reales de esta cátedra.

## Anexo B — Archivos fuera del dataset

- `../../segundo-parcial/examenes/2025-1C_*.pdf` (4 archivos): eran del **2do parcial**
  (raíces, Jacobi, interpolación, trapecios, Euler); movidos el 2026-09-10. Se indexan con
  `/indexar-examenes materias/analisis-numerico/segundo-parcial` cuando toque.
- `../fuentes/`: cronograma, links de clases virtuales, consigna del TP, hoja de fórmulas
  manuscrita y método de fracciones simples. No son exámenes; son insumos del machete.

---

*Generado el 2026-09-10 a partir de `examenes/INDICE.md` (16 hojas / 11 instancias, 2015–2025), `examenes/resueltos/RESOLUCIONES-2025.md` y `../fuentes/formulas-y-metodos-manuscrito.pdf`. Sin apuntes en `apuntes/md/`. Siguiente paso del flujo: `/plan` (ya generado como `plan.md`), y `/registrar` después de cada sesión; `/que-saltear` no aplica hasta que existan apuntes.*
