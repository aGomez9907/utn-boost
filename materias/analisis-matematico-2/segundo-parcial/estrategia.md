# Estrategia final AM2 — Segundo Parcial

> **Examen:** miércoles **8 de julio de 2026** · faltan **8 días**
> **Punto de partida declarado:** venís por la mitad del video de *Integrales dobles III*.
> **Fuentes analizadas:** 20 parciales reales (2014–2023) + 19 apuntes propios del segundo parcial (incluidos los 3 de Ecuaciones Diferenciales agregados el 30/06).
> Reporte generado automáticamente contrastando el patrón histórico de los parciales contra la cobertura de tus apuntes.

---

## 0. Cómo leer este documento

1. **Fase 2 — Qué toman siempre** (patrón real de 13 parciales distintos).
2. **Fase 3 — Contraste con tus apuntes**: brechas críticas, sobrecarga y mapa tema→apunte.
3. **Plan de 8 días** concreto.
4. **Banco de "problemas tipo"** con las fechas exactas donde practicarlos.
5. **Checklist teórico** para T1/T2.

**Diagnóstico en una línea:** tus apuntes cubren MUY bien el cálculo vectorial (integrales, flujo, circulación, conservativos, Green/Gauss/Stokes) **y ahora también las Ecuaciones Diferenciales** (apuntes 17-19, agregados el 30/06), con lo que se cerró la brecha más grave. Queda un solo frente teórico por consolidar: **las demostraciones de T1/T2**, que están dispersas. En paralelo, estás por invertir tiempo en dos temas (*longitud de curva* y *masa de un alambre*) que **casi no se toman** en el segundo parcial.

> **Actualización 04/07:** se sumaron 3 parciales más (**2024-07-12, 2025-07-18 y uno sin fecha**). **Refuerzan el patrón, no lo cambian:** los tres tienen **EDO** (confirma que sigue siendo tema vigente, no legado), los tres tienen **Green** como T1 —el `f=(xy²/2, 3x²y/2)` sobre `x²≤y≤x` ya es casi fijo— y aparece un **formato nuevo de T2 de cambio de variables**: dan una integral doble en polares (`∫₀^{π/2}∫₀^{2cosφ} ρ³ dρ dφ`) y piden **graficar la región y pasarla a cartesianas** (2024-07-12 y sin-fecha). También un giro de flujo/divergencia: hallar `g` para que un campo sea **solenoidal** (2025-07-18), análogo a "hallar `g` para que sea conservativo". Todo esto ya cae dentro de tus apuntes actuales.

> **Actualización 30/06:** se generaron los apuntes **17 · Ecuaciones diferenciales I** (1er orden: separables, lineal, homogénea, trayectorias ortogonales), **18 · Ecuaciones diferenciales lineales II** (2° orden homogénea: ecuación característica + los 3 casos de raíces + **superposición con demostración**) y **19 · Ecuaciones diferenciales lineales III** (no homogéneas: **coeficientes indeterminados** + variación de parámetros + **resonancia**). El P4 de EDO y la teoría T2 de superposición quedan cubiertos **sin material externo**.

---

## 1. Estructura del examen (constante 2014–2023)

Todos los segundos parciales tienen **4 problemas prácticos (P1–P4) + 2 teóricos (T1, T2)**, 2 horas. La distribución por posición es notablemente estable:

| Posición | Qué cae casi siempre |
|---|---|
| **P1** | Integral múltiple: **volumen / masa de un cuerpo / baricentro / área de una región** (triple o doble). |
| **P2** | **Circulación / trabajo** de un campo, o **campo conservativo + función potencial**. |
| **P3** | **Flujo** de un campo a través de una superficie (directo o por **divergencia/Gauss**). |
| **P4** | **EDO lineal de 2° orden**, o un segundo flujo/volumen. |
| **T1 / T2** | **Demostrar** la condición de campo conservativo, el **cambio de variables** (Jacobiano), o propiedades de **superposición de soluciones de EDO**. También Green y Divergencia. |

---

## 2. FASE 2 — Patrón real: frecuencia por tema (13 parciales distintos)

> Se analizaron 20 archivos, pero varios son el **mismo examen** en distinto formato o reediciones. Contenidos **distintos**: 13. (Ver equivalencias en el Anexo A.)

| # | Tema | Aparece en | Frecuencia | Prioridad |
|---|---|---|---|---|
| 1 | **Función potencial / campo conservativo** (práctica **o** teoría) | 13 de 13 | 🔴 **100 %** | MÁXIMA |
| 2 | **Integral múltiple** (volumen / masa de cuerpo / baricentro / área de región) | 12 de 13 | 🔴 **92 %** | MÁXIMA |
| 3 | **Flujo** de un campo (directo o por divergencia/Gauss) | 11 de 13 | 🔴 **85 %** | MÁXIMA |
| 4 | **Circulación / trabajo** de un campo (directo o por Green) | 9 de 13 | 🟠 **69 %** | ALTA |
| 5 | **EDO lineal de 2° orden** (problema P4) | 7 de 13 | 🟠 **54 %** | ALTA |
| 6 | **Superposición de soluciones de EDO** (teoría T2) | 5 de 13 | 🟠 **38 %** | ALTA |
| 7 | **Cambio de variables / Jacobiano** (teoría T1) | 5 de 13 | 🟡 **38 %** | MEDIA |
| 8 | **Teorema de la divergencia / Gauss** (enunciar/aplicar) | 5 de 13 | 🟡 **38 %** | MEDIA |
| 9 | **Área de una superficie** | 3 de 13 | 🟡 **23 %** | MEDIA-BAJA |
| 10 | **Rotor / Stokes** (explícito) | ~2 de 13 | ⚪ **15 %** | BAJA |
| 11 | **Longitud de una curva** | 1 de 13 | ⚪ **8 %** | BAJA |
| 12 | **Masa de un alambre** (integral de línea escalar) | **0 de 13** | ⚪ **0 %** | DESCARTABLE (para 2P) |

### Lectura del patrón
- **El "núcleo duro" que casi garantiza cae:** integral múltiple + flujo + conservativo/potencial. Dominando esos tres cubrís **P1, P2 y P3** en la mayoría de los exámenes.
- **La función potencial es el tema rey:** en los 13 exámenes aparece, como problema, como demostración teórica, o ambos. Si hay un solo tema que no podés fallar, es este.
- **EDO de 2° orden es el "comodín" de P4** y **superposición** el de T2: juntos aparecen en la mayoría de los exámenes, y son justamente lo que **no está en tus apuntes** (ver Fase 3).

### Problemas RECICLADOS (aparecen casi idénticos varias veces) — oro puro para practicar
- **Flujo de `f = (y², z²+x², x²)` a través de la superficie `y = x` con `x²+y²+2z² ≤ 2`** → cae en **2016-07-06, 2017-07-05, 2017-11-16 y 2022-11-24**. Cuatro veces el mismo. Si dominás este, tenés un P3 casi asegurado.
- **Circulación de `f = (yz, 2xz, xy)`** sobre intersección de paraboloides → **2016-07-06** y **2023-07-28**.
- **Flujo de `f = (x−yz, y+xz, z+2xy)`** sobre superficie esférica → **2022-12-02** y **2023-07-14**.
- **Volumen de `2x²+2y²+z² ≤ 3` con `z ≥ √(x²+y²)`** → **2016-07-06** y **2023-07-28**.
- **Cambio de variables `(x,y) = (u+2v, 2u+v)` / `(v−2u, u+v)` → área(D\*)** → **2016-07-06, 2022-12-02, 2022-12-16, 2023-07-14, 2023-07-28**.
- **Verificar conservativo + calcular potencial que vale k en un punto** → **2015-11-25, 2019-11-21, 2022-07-15, 2022-11-24** (misma mecánica, distintos números).

---

## 3. FASE 3 — Contraste con tus apuntes

Tenés **19 apuntes** del segundo parcial (los 16 de cálculo vectorial + `17`–`19` de EDO). Contrastados contra el patrón real:

### 3.1 🔴 Brechas críticas (lo que toman y NO está suficientemente cubierto)

1. **EDO lineales de 2° orden — ✅ RESUELTA (30/06).**
   - Antes: en los 16 apuntes originales `y''` → **0 apariciones**, "superposición" → **0**. Era la brecha más grave (~1 punto por parcial sin preparar).
   - EDO es **P4 en 7 de 13 parciales** (`y''+4y'=8`, `y''−6y'+9y=2x`, `y''−2y'+5y=2x`, `y''−4y'+13y=26`, `y''+y'−2y=cos x`, `y''−3y'=2−6x`…) **y** la teoría de **superposición** (T2) en otros 5.
   - **Ahora cubierto por los apuntes 18 y 19:**
     - **Homogénea con coeficientes constantes** → `18` (ecuación característica + raíces reales distintas / doble `xe^{mx}` / complejas `e^{αx}(c₁cos βx + c₂sin βx)`).
     - **No homogénea (coeficientes indeterminados y variación de parámetros) + resonancia** → `19`.
     - **Superposición (demostraciones T2)** → `18` (combinación lineal de soluciones, con demostración) y `19`.
     - `17` aporta el 1er orden (separables, lineal, homogénea, ortogonales) como base, aunque el P4 del 2° parcial es siempre de **2° orden** → priorizá `18` y `19`.

2. **Demostraciones teóricas (T1/T2) — dispersas, hay que consolidarlas.**
   - En 6.800 líneas hay solo **9** menciones a "demostr". Tus apuntes son **prácticos** (ejercicios resueltos), pero T1/T2 piden **"enunciar Y demostrar"**.
   - Lo que SÍ tenés y hay que estudiar como demostración (no solo leer):
     - **Condición necesaria de campo conservativo** → `10-campos-conservativos.md` (tiene la demostración completa) y su corolario en `16-rotor-en-el-espacio.md`.
     - **∫F·dλ = φ(B) − φ(A)** (independencia del camino) → `10-campos-conservativos.md`.
     - **Teorema de la Divergencia** → `15-divergencia.md` tiene solo la *"idea de la demostración"*: reforzá el enunciado formal (hipótesis + tesis).
     - **Teorema de Green** → `09-rotor-en-el-plano.md`.
   - **Superposición de soluciones de EDO** (que `y₁+y₂`, `y₁−y₂`, `k·yₚ` son solución) → ahora cubierto en `18-ecuaciones-diferenciales-lineales-ii.md` (con demostración) y `19`. Estudialo como demostración, no solo de lectura.

3. **Cambio de variables / Jacobiano como TEORÍA (T1).** Lo tenés aplicado en integrales dobles (03/04), pero repasá poder **enunciar el teorema** y resolver el clásico "área(D\*) sabiendo área(D)" — cae en 5 parciales.

### 3.2 🟡 Sobrecarga innecesaria (lo que estás por estudiar y casi no toman en 2P)

| Apunte | Frecuencia en 2P | Recomendación |
|---|---|---|
| `06-longitud-de-una-curva.md` | 1 de 13 (8 %) | Repaso ligero, no te detengas. |
| `07-masa-de-un-alambre.md` | **0 de 13** | **No priorizar** para el 2P (es tema más de 1er parcial). Ojo: "masa" en los parciales es siempre de **cuerpo** (triple) o de **chapa/superficie**, no de alambre. |
| Interpretaciones físicas extensas (caudal, fuentes/sumideros) en `14-flujo.md` | nunca preguntadas | Leer una vez, no memorizar. |

> **Traducción práctica:** cada hora que le saques a *masa de un alambre* y *longitud de curva* pásasela a **EDO de 2° orden** y a **repasar las demostraciones**. Es el intercambio de mayor rendimiento posible.

### 3.3 Mapa tema → apunte → prioridad

| Tema del examen | Tu apunte | Frec. | Qué hacer |
|---|---|---|---|
| Volumen / masa cuerpo / baricentro | `01`–`05` (dobles I-III, triples I-II) | 92 % | **Dominar.** Núcleo de P1. |
| Función potencial / conservativo | `10`, `11`, `16` | 100 % | **Dominar + demostración.** |
| Flujo / divergencia (Gauss) | `14-flujo`, `15-divergencia` | 85 % | **Dominar.** Núcleo de P3. |
| Circulación / trabajo / Green | `08-trabajo`, `09-rotor-en-el-plano` | 69 % | **Dominar.** |
| Área de superficie / chapa | `12-área-de-una-superficie`, `13-masa-de-una-chapa` | 23 % | Saber la fórmula y un ejemplo. |
| Rotor en el espacio / Stokes | `16-rotor-en-el-espacio` | 15 % | Repaso. |
| **EDO 2° orden (homogénea + no homogénea)** | **`18`, `19`** ✅ | 54 % | **Dominar.** Núcleo de P4. |
| EDO 1er orden + superposición (teoría) | `17`, `18` | (T2: 38 %) | `17` de base; superposición de `18`/`19` para T2. |
| Longitud de curva / masa de alambre | `06`, `07` | ≤8 % | Mínimo. |

---

## 4. Plan de 8 días (30 jun → 8 jul)

Estás arrancando, así que el plan prioriza **cobertura del núcleo duro primero** y deja los últimos días para simulacros cronometrados. Regla de oro: **por cada tema, resolvé al menos un parcial real completo de ese tema** (usá el banco de la sección 5).

| Día | Foco | Entregable del día |
|---|---|---|
| **Día 1 (mar 30/6)** | Terminar *Integrales dobles III* + repasar dobles I-II. Baricentro y momento estático. | Resolver P1 de **2017-07-05** (baricentro) y **2016-11-25** (volumen). |
| **Día 2 (1/7)** | *Integrales triples I-II*: volúmenes y **masa de cuerpo** con densidad. Cambio a cilíndricas/esféricas. | P1 de **2017-11-16** y **2022-12-02** (masa) + **2023-07-28** (volumen). |
| **Día 3 (2/7)** | **Campos conservativos + función potencial** (apuntes 10, 11). Los 2 métodos de potencial. **Estudiar la demostración de la condición necesaria.** | P2 de **2015-11-25**, **2022-07-15**, **2022-11-24**. Escribir la demostración de memoria. |
| **Día 4 (3/7)** | **Flujo + Teorema de la Divergencia** (14, 15). Directo vs. Gauss. Orientación de la superficie. | El **flujo reciclado** `f=(y²,z²+x²,x²)` (practicalo de 2017-11-16). P3 de **2022-07-15** (Gauss). |
| **Día 5 (4/7)** | **Circulación / trabajo / Green** (08, 09). Cuándo conviene Green vs. directo vs. conservativo. | P2 de **2016-07-06** y **2023-07-28**; Green de **2019-11-21**. |
| **Día 6 (5/7)** | **EDO 2° orden con tus apuntes `18` y `19`.** Homogénea (3 casos de raíces, apunte `18`) + coeficientes indeterminados / resonancia (apunte `19`). **Superposición** para T2 (demostración en `18`). | Resolver los P4 de **2016-07-06, 2019-11-21, 2022-07-15, 2022-11-24, 2023-07-28**. |
| **Día 7 (6/7)** | **Teoría T1/T2 a fondo** + área de superficie + rotor/Stokes (repaso rápido). | Escribir de memoria: condición conservativo (dem.), cambio de variables, Green, divergencia, superposición EDO. |
| **Día 8 (7/7)** | **Simulacro cronometrado (2 h)** con un parcial completo que NO hayas mirado + repasar errores. | **2022-12-16** o **2023-07-14** completo, con reloj. |
| **8/7** | **EXAMEN.** Repaso liviano de fórmulas, nada nuevo. | — |

---

## 5. Banco de "problemas tipo" (qué practicar de cada archivo)

Todos los archivos están en `examenes/` (junto a este documento) con nombre `AAAA-MM-DD_Parcial.pdf|png|jpg`.

- **Volumen (triple):** `2016-11-25`, `2019-11-21`, `2022-07-15`, `2023-07-28`.
- **Masa de cuerpo (densidad):** `2017-11-16`, `2022-12-02`, `2022-12-16`, `2023-07-14`.
- **Baricentro / área de región:** `2017-07-05`, `2023-07-14`.
- **Función potencial / conservativo:** `2015-11-25`, `2016-11-25`, `2019-11-21`, `2022-07-15`, `2022-11-24`, `2022-12-16`, `2023-07-14`.
- **Flujo (directo):** el reciclado `y=x` en `2016-07-06`, `2017-07-05`, `2017-11-16`, `2022-11-24`.
- **Flujo (divergencia / Gauss):** `2015-11-25`, `2022-07-15`, `2022-12-02`, `2023-07-28`.
- **Circulación / trabajo / Green:** `2014-11-28`, `2016-07-06`, `2019-11-21`, `2022-07-15`, `2023-07-28`.
- **EDO 2° orden:** `2016-07-06`, `2016-11-25`, `2019-11-21`, `2022-07-15`, `2022-11-24`, `2023-07-28`.
- **Área de superficie:** `2014-11-28`, `2015-11-25`, `2019-11-21` (cono).
- **Rotor / Stokes:** `2022-12-16`.

> **Simulacros "a ciegas" recomendados** (dejalos sin mirar hasta el día 7-8): `2022-12-16` y `2023-07-14`, que combinan varios temas y tienen ítems poco reciclados.

---

## 6. Checklist teórico (T1 / T2) — tenés que poder ESCRIBIRLO, no solo reconocerlo

- [ ] **Condición necesaria** para que un campo sea conservativo — enunciado (hipótesis: C¹, dominio) + **demostración**. *(en `10-campos-conservativos.md`)*
- [ ] **Condición suficiente**: dominio simplemente conexo. *(en `10`)*
- [ ] **Independencia del camino:** `∫_{A→B} F·dλ = φ(B) − φ(A)` — demostración. *(en `10`)*
- [ ] **Teorema de cambio de variables** en integrales dobles (Jacobiano) + ejercicio "área(D\*) sabiendo área(D)". *(en `03`/`04`)*
- [ ] **Cambio de variables — variante polar (2024-2025):** dada una integral en polares (ej. `∫₀^{π/2}∫₀^{2cosφ} ρ³ dρ dφ`), **graficar la región** (`ρ=2cosφ` es la circunferencia `x²+y²=2x`) y **reescribirla en cartesianas**. *(base en `03`/`04`)*
- [ ] **Teorema de Green** — enunciado + orientación positiva. *(en `09`)*
- [ ] **Teorema de la Divergencia (Gauss)** — enunciado formal (hipótesis + tesis). *(en `15`, ampliar la "idea de demostración")*
- [ ] **Teorema del rotor (Stokes)** — enunciado. *(en `16`)*
- [ ] **Superposición de soluciones de EDO**: demostrar que `y₁+y₂`, `y₁−y₂` y `k·yₚ` son solución de la ecuación correspondiente. *(en `18-ecuaciones-diferenciales-lineales-ii.md`, con demostración)*
- [ ] **Resolución de EDO 2° orden**: homogénea (ecuación característica, 3 casos) + no homogénea (coeficientes indeterminados, resonancia). *(en `18` y `19`)*

---

## Anexo A — Equivalencias entre parciales (para no practicar dos veces lo mismo)

Detectadas por contenido idéntico al renombrar:

- `2016-07-06_Parcial.png` **≡** `2022-07-22_Parcial.pdf` (el nombre original decía "mismo que 2016-07-06").
- `2022-07-15_Parcial.pdf` **≡** `2022-11-17_Parcial.pdf` (contenido idéntico).
- `2016-11-25_Parcial.pdf` fue reutilizado como el `2023-07-13` (nota del nombre original).
- `2016-11-25`, `2017-07-05`, `2017-11-16`, `2019-11-21` y `2022-11-24` existen en **doble formato** (pdf + png/jpg): son el mismo examen.

## Anexo B — Archivo que NO es un segundo parcial

- **`Parciales varios.pdf`** (se dejó **sin renombrar**): es una **compilación de PRIMEROS parciales** (Mayo/Agosto/Octubre 2019, Evaluación Integradora Oct 2020) y apuntes de teoría (Hessiano, extremos ligados). **No corresponde al dataset del segundo parcial** y no tiene una fecha única, por eso quedó con su nombre original. *(Reorganización 2026-07-05: ya fue movido a `../primer-parcial/examenes/`.)*

---

*Generado el 2026-06-30 y actualizado el mismo día con los apuntes 17-19 de Ecuaciones Diferenciales. Fuente: 20 parciales (2014–2023) + 19 apuntes propios, carpetas `examenes/` y `apuntes/md/` de esta evaluación. *(Rutas actualizadas en la reorganización del 2026-07-05.)**
