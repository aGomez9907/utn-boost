# Plan de estudio — Final AM2 · examen **martes 2026-09-22**

> **Recalculado el domingo 2026-09-13.** El plan del 9/9 no arrancó (0 sesiones en
> `registro.md`). Quedan **9 días de estudio** (dom 13 → lun 21) a 2-3 h/día →
> **presupuesto ≈ 22 h**, un tercio menos que el plan original.
> **Fuentes:** [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> `repaso/machete.md` (unificado; leer desde `exports/machete.pdf`).

---

## Qué cambió respecto del plan del 9/9

No se corta la cola del plan viejo: **se comprime la cabeza**. Lo perdido eran los
cuatro días de flujo y circulación, que son los dos prácticos que aprueban. Entonces:

| Antes (13 días) | Ahora (9 días) |
|---|---|
| Flujo en 2 días, circulación en 2 días | Flujo en 1 día, circulación en 2 días |
| Un día entero de conservativos | Se elimina como bloque; entra sólo la demostración de independencia de trayectoria |
| Un día entero de flashcards, otro de machete | Los genera Claude fuera de tu tiempo; vos sólo repasás 20 min/día |
| Teoría concentrada al final | **20 min de teoría cada día desde el D4**, un teorema por día |
| Menú de 6 teóricos | Menú de **4** (cubren casi todos los T1/T2 del dataset) |
| Banco 🟠 completo | Sólo lo que el simulacro muestre que falta |

**La meta no cambió:** 2 prácticos blindados (flujo + circulación) y 1 teórico escribible.
Con 22 h entra eso y no mucho más. Está bien: es lo que aprueba.

---

## Los 4 teóricos (elegís UNO el día del examen)

| # | Teórico | Veces en 24 finales | Se practica el |
|---|---|---|---|
| T-A | **Independencia de la trayectoria** — demostrar `∫_C ∇φ·ds = φ(Q) − φ(P)` | 5 | D4 |
| T-B | **Green** — enunciar con hipótesis **y deducir la fórmula del área plana** | 5 | D5 |
| T-C | **Stokes** — enunciar con hipótesis | 5 | D6 |
| T-D | **Gauss** — enunciar con hipótesis; saber decir por qué NO se aplica directo a una superficie abierta | 4 | D6 |

Entre los cuatro cubren 19 de los 24 finales. Si un examen no trae ninguno, T2 casi
siempre es un «defina X» de extremos o derivada direccional que se resuelve con el
machete. Ese es el plan B, no se estudia aparte.

---

## Día por día

### 🔴 D1 · domingo 13/09 (hoy) — Flujo completo
Es domingo: si podés estirar a 3-4 h hoy, este es el día para hacerlo.
- [ ] Machete del final (`exports/machete.pdf`) §0 y §1 completo. **30 min, sin resolver.**
- [ ] **Gauss:** `2026-07-28 P1` → 25 min. Después `2025-07-29 P4` → 25 min y corregir con `resueltos/2025-07-29_resuelto.pdf`.
- [ ] **Abierta:** `2025-09-25 P2` (paraboloide, orientación `z⁺`) → 25 min.
- [ ] Si hay tiempo: `2025-12-09 P2` (mismo esquema; si sale en <15 min, flujo está listo).
- [ ] `/registrar`.

> Automatizá hoy la decisión: superficie **cerrada** → Gauss. **Abierta** → directo, o la
> cerrás con una tapa y restás. El `2026-02-10 T1a` pregunta exactamente esto.

### 🔴 D2 · lunes 14/09 — Circulación por Green
- [ ] Machete §2.1 a §2.3 (conservativo, Green, Green con curva abierta). **20 min.**
- [ ] `2026-07-28 P2` → 25 min. `2025-12-09 P3` (sentido **negativo**, ojo al signo) → 25 min.
- [ ] Disparador a memorizar: campo con `e^{x²}`, `sen(y²)`, `ln x` → no se integra directo, **es Green**.
- [ ] `/registrar`.

### 🔴 D3 · martes 15/09 — Circulación por Stokes
- [ ] Machete §2.4 (Stokes) y §2.5. **20 min.**
- [ ] `2025-07-15 P1` (curva intersección con `Df` dada) → 30 min.
- [ ] `2026-05-19 P1` → 30 min y corregir con `resueltos/2026-05-19_resuelto-sylvina.pdf`.
- [ ] `/registrar`.

### 🔴 D4 · miércoles 16/09 — El reciclado + primer teórico
- [ ] Machete §4 (implícita, plano tangente, curvas). **20 min.**
- [ ] **B6, el ejercicio que cayó 3 veces en 2 años:** `2026-03-03 P2` → 30 min. Corregir con `resueltos/2024-05-10_resuelto.pdf` (es el mismo enunciado).
- [ ] **T-A:** escribir de memoria la demostración de independencia de la trayectoria. En papel, sin mirar. **20 min.**
- [ ] `/registrar`.

### 🔴 D5 · jueves 17/09 — EDO + Green teórico
- [ ] Machete §3 (EDO). **15 min.**
- [ ] `2026-07-28 P3` (`y'' − 4y' + 4y = 25 sen x`: raíz doble + tanteo trigonométrico) → 30 min.
- [ ] `2025-05-20 P4` (PVI) → 20 min.
- [ ] **T-B:** enunciar Green y deducir `A = ½∮ x dy − y dx`. En papel. **20 min.**
- [ ] `/registrar`.

### 🟠 D6 · viernes 18/09 — Gradiente + Stokes y Gauss teóricos
- [ ] Machete §5 (gradiente, direccional, cadena). **15 min.**
- [ ] `2026-07-28 P4` (máximo decrecimiento con implícita) → 25 min.
- [ ] **T-C y T-D:** enunciar Stokes y Gauss con hipótesis. **20 min.**
- [ ] Flashcards, primera pasada (el mazo lo genera Claude; ver abajo). **20 min.**
- [ ] `/registrar`.

### 🔴 D7 · sábado 19/09 — Simulacro cronometrado
- [ ] `/simulacro` → **2 horas exactas con reloj.**
- [ ] 10 minutos de lectura y descarte. Elegís 1 teórico + 2 prácticos. **Los otros 3 quedan en blanco.** Si resolvés los 6, el simulacro falló.
- [ ] Corregir con la corrección desplegable. `/registrar` cada error.

### 🟠 D8 · domingo 20/09 — Tapar agujeros
- [ ] Rehacer **sólo** lo que falló el sábado.
- [ ] Si sobra tiempo, un bloque a elección según el registro: masa/volumen planteando límites (`2026-03-03 P1`) **o** extremos sobre una región (`2026-05-19 P4`). Uno, no los dos.
- [ ] Flashcards, segunda pasada. **20 min.**
- [ ] `/registrar`.

### 🟡 D9 · lunes 21/09 — Víspera: nada nuevo
- [ ] Machete completo (`exports/machete.pdf`), dos lecturas. **45 min.**
- [ ] Flashcards, sólo las flojas. **20 min.**
- [ ] Releer `estrategia.md` §0 (regla de 3 de 6).
- [ ] Mirar los enunciados de `2026-07-14` y `2026-07-28` **sin resolverlos**.
- [ ] Dormir.

---

## Lo que queda afuera (a propósito)

Conservativos como bloque de práctica, trayectorias ortogonales, área de superficie,
extremos por Hessiano, Taylor, punto regular, superficie parametrizada. Todos tienen
menos del 55% de presencia y ninguno es necesario para "2 prácticos + 1 teórico". Si el
examen trae uno de estos en dos de los cuatro P, elegís los otros dos.

## Si volvés a perder días

- **1 día perdido:** se salta D8 entero. El resto no se mueve.
- **2 días perdidos:** se salta D8 y se funde D6 en D5 (sólo los teóricos, sin `2026-07-28 P4`).
- **3 o más:** corré `/plan` de nuevo. A esa altura el plan mínimo es D1 + D2 + D4 + D7,
  y los teóricos T-A y T-B nada más.
- **Nunca se saltea:** D1 (flujo), D2 (Green), D4 (B6 + T-A), D7 (simulacro).

## Material que Claude genera fuera de tu tiempo

- ✅ `repaso/flashcards.md` (26 cartas) + `flashcards-anki.tsv` → generados el 2026-09-13; versión que renderiza: `exports/flashcards.pdf`.
- ✅ `repaso/machete.md` unificado → generado el 2026-09-13; **usar `exports/machete.pdf`** (el `.md` no renderiza LaTeX en tu visor). Si lo retocás, re-exportar con `/machete --pdf`.

---

_Plan recalculado el 2026-09-13 · 9 días · 2-3 h/día · examen martes 2026-09-22._
