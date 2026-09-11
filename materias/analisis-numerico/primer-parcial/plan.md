# Plan de estudio — Primer parcial · Análisis Numérico

> Examen: **martes 2026-10-06** · Hoy: jueves 2026-09-10 · **26 días restantes (13 útiles
> para AN: 2026-09-23 → 2026-10-05, con el 28/9 bloqueado)**.
> Restricciones declaradas: ninguna explícita para AN. **Supuestos** tomados de
> `carrera/datos/calendario.json` y de la memoria del repo: hasta el **2026-09-22** el
> tiempo es del final de AM2 (2-3 h/día); el **2026-09-28** es el 1P de Gestión Gerencial
> (los días 26–27 quedan livianos); el **2026-09-29** hay clase presencial de repaso del 1P
> de AN. Si algo de esto cambia, corré `/plan` de nuevo.
> Fuentes: [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> [`examenes/resueltos/RESOLUCIONES-2025.md`](examenes/resueltos/RESOLUCIONES-2025.md) ·
> `../fuentes/formulas-y-metodos-manuscrito.pdf`.

---

## La meta, en una línea

**10 ítems, se aprueba con 6, se promociona con 8.** El plan apunta a **8**: blindar
Ej1a+b (Fourier), Ej3 entero (sistemas) y Ej4 entero (Z) = 7 ítems de receta, más Ej2a/b
(Laplace) = 9. Ej1c (media onda) y Ej2c (demostración) son el colchón. No hay apuntes: se
estudia **desde las hojas resueltas**, sobre todo `RESOLUCIONES-2025.md`, que es
literalmente cómo corrige la cátedra.

## ⚠️ No entra todo… hasta el 22/9

Hasta el final de AM2 no se planifica nada de AN. Los 13 días posteriores alcanzan para
los cuatro bloques 🔴 con un día de simulacro y uno de repaso, pero **sin margen para
generar apuntes desde los videos**: si querés apuntes propios (`/apuntes-batch`), va después
del 22/9 y a costa de práctica, o no va. Lo que se sacrifica sin culpa: conjuntos de
complejos, método gráfico del módulo, fasores, sistemas de EDO, sumas de series vía
Fourier (todo ⚪ en la estrategia).

**Opcional antes del 22/9 (solo si sobra un rato, sin culpa si no):** leer una vez las 6
páginas de la hoja de fórmulas manuscrita y `RESOLUCIONES-2025.md` → "Patrones
transversales". 30 min en total. Sirve para que el D1 no arranque en frío.

---

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| jue 2026-09-10 → mar 2026-09-22 | 🚫 Final de AM2 (2026-09-22). AN: solo la lectura opcional de arriba. | — |
| **mié 2026-09-23 · D1** | 🔴 **Fourier I — la receta.** Regla par/impar según lo que piden (reales/cosenos ↔ par; imaginarios/senos ↔ impar), `T, L, ω₀`, integral por partes, `cos(nπ) = (−1)ⁿ`, reindexar en `2k+1`. Leer `RESOLUCIONES-2025.md` Ej1a T1, T2 y rec + hoja de fórmulas p.1. | **2025-1C T1 Ej1a** (π−t, par) y **2025-1C T2 Ej1a** (−π−t, impar) resueltos sin mirar y corregidos contra las respuestas oficiales. `/registrar`. |
| **jue 2026-09-24 · D2** | 🔴 **Fourier II — `Cₙ`, SEF, valor medio, media onda.** `Cₙ = ½(aₙ − j bₙ)`, `C₀ = a₀/2`; SMO: `f(t + T/2) = −f(t)`, construcción gráfica por tramos. | **2015-05-29 T1 Ej1** (el reciclado `4/k`: `k = 2`, SEF con `k = −4`), **2025-1C T1 Ej1c** y **T2 Ej1c** (SMO, gráfico + tramos), **sin-fecha K3521 T2 Ej3** (`3x`: cosenos + `Cₙ` sin integrar + ¿SMO?). `/registrar`. |
| **vie 2026-09-25 · D3** | 🔴 **Laplace I — integrales impropias y propiedades.** `∫₀^∞ f e^{−at} dt = F(a)`; `L{t f} = −F'`; `L{f/t} = ∫_s^∞ F` (chequear el límite en 0); `L{aᵗ}`. | **2025-1C T1 Ej2a** (`t e^{−5t} cos t`), **sin-fecha K3521 T1 Ej2** (`t cos 3t e^{−5t} = 4/289`), **2024-2C T1 Ej3b** (`∫ sen t / t = π/2`), y escribir de memoria la demostración de **`L(2ᵗ) = 1/(s − ln 2)`** (2025-1C T1 Ej2c). `/registrar`. |
| **sáb 2026-09-26 · D4** | 🟠 **Laplace II — convolución ida y vuelta** (`1/(s²+1)²`, `s²/(s²+1)²`, producto → suma), `sen³ t` por exponenciales, ecuación integral. *Día liviano (≈1,5 h) por GG.* | **2025-1C T1 Ej2b** (`1/(s²+1)²`), **2025-1C T2 Ej2a/b** (`sen³`, convolución con cosenos), **2024-1C T1 Ej2** (`y − ∫ y sen = t⁴`, corregir contra la resolución de cátedra en `resueltos/2024-1C_Parcial-T1_resuelto.pdf`). `/registrar`. |
| dom 2026-09-27 | ⚪ Gestión Gerencial. AN: 20 min releyendo hoja de fórmulas p.2–3. | — |
| lun 2026-09-28 | 🚫 **1P de Gestión Gerencial.** | — |
| **mar 2026-09-29 · D6** | 🔴 **Sistemas I + clase de repaso presencial.** Ruffini para factorizar el denominador, **K que cancela el polo positivo**, diagrama de polos/ceros, corte cualitativo de `\|G\|` por el eje real (∞ en polos, 0 en ceros, lomo en complejos). **Preguntar en clase: ¿se rinde con tabla de transformadas? ¿cuál?** | **2025-1C T2 Ej3a** (`k = 3`), **2025-1C rec Ej3a/b** (polos/ceros + corte), **2022-10-11 Ej5a/b** (`k = 6`, corte de `Y(s)`). Anotar en `registro.md` todo lo que el profe marcó como "seguro cae". `/registrar`. |
| **mié 2026-09-30 · D7** | 🔴 **Sistemas II — respuesta temporal completa.** `Y = G·F`, fracciones simples (cover-up para el polo simple, coeficientes para el cuadrático), completar cuadrados, partir el numerador en `(s+a)` + constante, **tipo de respuesta** por los polos y **valor estable** (`A/s`). Cronometrar 25 min por ejercicio. | **2025-1C T2 Ej3b/c** (el reciclado ×3: `y = −3 + 3cos t e^{−3t} + 19 sen t e^{−3t}`, oscilatoria amortiguada, estable en −3), **2025-1C rec Ej3c** (entrada `e^{−3t}`), **2024-1C T1 Ej5** (escalón + corte de `Y(s)` + clasificar). `/registrar`. |
| **jue 2026-10-01 · D8** | 🔴 **Sistemas III — variantes** + `G(s)` desde la EDO (reposo ⇒ tachar condiciones iniciales) + **repaso instrumental de complejos** (1 h: raíces de cuadráticas complejas, forma polar, `ln z` valor principal). | **2025-1C T1 Ej3a/b** (sistema mecánico, `G = 1/(s²+2s+2)`), **2024-2C rec Ej4** (`a` y `b` para estable + escalón), **2024-1C T2 Ej4a/b** (respuesta al impulso `δ`). `/registrar`. |
| **vie 2026-10-02 · D9** | 🔴 **Z I — sucesiones por paridad + ROC, sumas, secuencia finita.** Dos geométricas (`z^{−2k}` y `z^{−(2k+1)}`), ROC = intersección; `Σ x(n) c^{−n} = X(c)`; tablas `Z{aⁿ/n!} = e^{a/z}`, `Z{cos Ωn}`. | **2025-1C T1 Ej4a/b** (`(−2)ⁿ/4^{−n}`, ROC `\|z\|>2`; `e^{3/2}`), **2025-1C T2 Ej4a** (`Σ cos(πn) 3^{−n} = 3/4`), **2024-2C T2 Ej5a/b** (`(−2)ⁿ/4ⁿ`; `20/27`), **sin-fecha K3521 T1 Ej5**. `/registrar`. |
| **sáb 2026-10-03 · D10** | 🔴 **Z II — ecuaciones en diferencias con verificación.** Adelanto `zX − z x(0)`, fracciones simples sobre `X(z)/z`, tablas `aⁿ`, `n aⁿ`; verificar `x(2)` iterando la recurrencia. | **2025-1C T2 Ej4b** (`x = 2n 2ⁿ + 3·4ⁿ`), **2015-05-29 T1 Ej4** y **T2 Ej4** (1er orden, corregir contra las hojas del alumno), **2024-1C T1 Ej4** (2do orden, resolución de cátedra), **2024-2C rec Ej5** (`3n − 1`). `/registrar`. |
| **dom 2026-10-04 · D11** | 🔴 **Simulacro a ciegas 1 (reservado):** `examenes/2025-1C_Recuperatorio.pdf`, 4 ejercicios, cronometrado 2 h, sin apuntes ni hoja de fórmulas (o con la tabla que permita la cátedra). Corregir contra `RESOLUCIONES-2025.md` → "Recuperatorio". | Examen completo con nota estimada + errores en `registro.md` (`/registrar`). A la tarde: **`/machete`** con la hoja de fórmulas + los errores del día. |
| **lun 2026-10-05 · D12** | 🟠 **Simulacro a ciegas 2 (reservado):** `examenes/2024-2C_Parcial.docx` **Tema 2**, Ej2–Ej5 (el Ej1 de complejos se saltea), 1,5 h; corregir contra `resueltos/2024-2C_Parcial_respuestas.docx`. Si preferís algo en formato 2025, `/simulacro`. Después **repaso liviano**: machete + errores del registro. **NADA nuevo.** | Checklist teórico de `estrategia.md` §6 escrito de memoria (sobre todo `L(aᵗ)`, tabla polo → respuesta, ROC como intersección). |
| **mar 2026-10-06** | **EXAMEN.** Llevar la tabla si está permitida. | — |

---

## Circuito de mantenimiento

- Cada sesión termina con `/registrar` (qué salió ✅ / 🟡 / ❌ y el error puntual).
- Si un tema 🔴 sale ❌ dos veces, `/plan` lo reprograma antes que el material nuevo.
- Si el 29/9 el profesor cambia el panorama (formato, tabla, tema "seguro"), anotarlo en
  `registro.md` y correr `/estrategia` + `/plan`.
- `/machete` el D11; `/flashcards` solo si sobra tiempo (la teoría es corta).

---

*Generado el 2026-09-10 con: MATERIA.md (examen 2026-10-06), estrategia.md (prioridades y banco, generada hoy), registro.md (vacío, sin sesiones aún), que-saltear.md (no existe: no hay apuntes), input del usuario (ninguno; supuestos de calendario tomados de `carrera/datos/calendario.json` y de la memoria del repo sobre el final de AM2).*
