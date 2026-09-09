# Plan de estudio — Final AM2 · examen **martes 2026-09-22**

> **Hoy:** miércoles 2026-09-09 · **13 días de estudio** (mié 9 → lun 21).
> **Disponibilidad declarada:** 2-3 h/día → **presupuesto ≈ 33 h**.
> **Fuentes:** [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> `../primer-parcial/repaso/machete.md` · `../segundo-parcial/repaso/machete.md`.
> **Este archivo se recalcula:** si te atrasás, si un día no podés o si `registro.md`
> muestra que un tema no entra, corré `/plan` de nuevo y se rearma con lo que quede.

---

## La meta, en una línea

**No es saber AM2. Es tener 2 prácticos blindados + 1 teórico escribible.** Todo el plan
está podado a eso: el 96% de los finales trae un flujo y el 92% una circulación, así que
esos dos son los prácticos elegidos, y la teoría se ataca por el menú corto de 6.

Con 2-3 h/día no entra el banco completo. **Lo que se sacrifica está marcado ⚪ y es
descartable sin culpa.** Lo que no se negocia son los bloques 🔴.

---

## Semana 1 — reconstruir las dos mitades (mié 9 → mar 15)

### 🔴 D1 · miércoles 09/09 — Flujo, la mitad más rentable
- [ ] Leer `../segundo-parcial/repaso/machete.md` §6 (superficies, `dS`, área y flujo) y §7 (divergencia y Gauss). **40 min, sin resolver nada.**
- [ ] **B1 — flujo por Gauss:** `2026-07-28 P1` y `2025-07-29 P4`. Cronometrados, 25 min cada uno.
- [ ] Corregir `2025-07-29 P4` contra `resueltos/2025-07-29_resuelto.pdf`.
- [ ] `/registrar` lo que salió y lo que no.

> **Criterio de decisión que tenés que automatizar hoy:** superficie **cerrada** → Gauss.
> Superficie **abierta** → o parametrizás directo, o la cerrás con una tapa y restás. El
> `2026-02-10 T1a` pregunta exactamente esto.

### 🔴 D2 · jueves 10/09 — Flujo directo por superficie abierta
- [ ] **B2:** `2025-09-25 P2`, `2025-12-09 P2`, `2026-03-03 P4`. 25 min cada uno.
- [ ] Los tres son el mismo esquema (paraboloide abierto, orientación `z⁺`). Si el tercero
      te sale en menos de 15 min, B2 está listo y pasás a `2025-12-02 P4` (cilindro).
- [ ] `/registrar`.

### 🔴 D3 · viernes 11/09 — Circulación: Green
- [ ] Machete 2P §4 (Green). **25 min.**
- [ ] **B3:** `2026-07-28 P2`, `2025-12-09 P3` (¡sentido **negativo**!), `2026-07-14 P3`.
- [ ] Ojo con el disparador: campo con `e^{x²}`, `sen(y²)`, `ln x` → **no se integra
      directo, es Green sí o sí**. Es la señal que pone la cátedra.
- [ ] `/registrar`.

### 🔴 D4 · sábado 12/09 — Circulación: Stokes (día largo, aprovechá el finde)
- [ ] Machete 2P §8 (rotor y Stokes). **25 min.**
- [ ] **B4:** `2025-07-15 P1`, después `2025-12-02 P2` (es el mismo con otro jacobiano —
      confirmá que lo reconocés), `2026-05-19 P1`.
- [ ] Corregir `2026-05-19 P1` contra `resueltos/2026-05-19_resuelto-sylvina.pdf`.
- [ ] Si queda tiempo: `2025-07-29 P1` (con `rot F` ya dado — es el caso fácil).
- [ ] `/registrar`.

### 🟠 D5 · domingo 13/09 — Conservativos y potencial (cierra el bloque 2P)
- [ ] Machete 2P §5. **25 min.**
- [ ] **B7:** `2026-07-14 P4` (hallar `g` para que sea conservativo), `2025-12-09 T2b`
      (línea equipotencial), `2024-12-17 P1`.
- [ ] **Teórico del día:** escribir de memoria la demostración de **independencia de la
      trayectoria** (`∫_C ∇φ·ds = φ(Q) − φ(P)`). Cayó 5 veces. 20 min, en papel, sin mirar.
- [ ] `/registrar`.

### 🔴 D6 · lunes 14/09 — Cambio de mitad: implícita y plano tangente
- [ ] `../primer-parcial/repaso/machete.md` §3 (implícita) y §8 (plano tangente). **30 min.**
- [ ] **B6 — el ejercicio más reciclado del dataset (3 veces en 2 años):**
      `2026-03-03 P2`, y después `2024-05-10 P2` para confirmar que es el mismo.
- [ ] Corregir contra `resueltos/2024-05-10_resuelto.pdf`.
- [ ] `/registrar`.

### 🔴 D7 · martes 15/09 — Gradiente y derivada direccional
- [ ] Machete 1P §1 (gradiente y direccional) y §2 (regla de la cadena). **30 min.**
- [ ] **B10:** `2026-07-28 P4` (máximo decrecimiento con implícita), `2024-10-09 P3`
      (direcciones de derivada nula).
- [ ] **Teórico del día:** demostrar `f'(X₀,ǔ) = ∇f(X₀)·ǔ`. Es el T1a del final más
      reciente (2026-07-28). 20 min, en papel.
- [ ] `/registrar`.

---

## Semana 2 — teoría, integración y simulacros (mié 16 → lun 21)

### 🔴 D8 · miércoles 16/09 — EDO (el tercer pilar, 92%)
- [ ] Machete 2P §9 (EDO 2º orden) + machete 1P §4 (EDO 1er orden y trayectorias). **30 min.**
- [ ] **B5:** `2026-07-28 P3` (`y'' − 4y' + 4y = 25 sen x` — raíz doble + tanteo
      trigonométrico, el caso que más se traba), `2025-05-20 P4`, `2025-12-09 P4` (límite
      de la solución general).
- [ ] **B11 rápido:** `2026-03-03 P3` (trayectorias ortogonales con parámetro). 15 min.
- [ ] `/registrar`.

### 🔴 D9 · jueves 17/09 — Flashcards de teoría
- [ ] Correr `/flashcards` sobre el checklist teórico de `estrategia.md` §4.
- [ ] Primera pasada del mazo. Objetivo: los **6 primeros** (Green + área plana, Stokes,
      Gauss, independencia de trayectoria, extremos/Hessiano, cambio de variables) los
      escribís sin dudar.
- [ ] `/registrar`.

### 🟠 D10 · viernes 18/09 — Machete unificado
- [ ] Correr `/machete` para el final: **un solo documento** que mezcle ambos temarios,
      encabezado por la tabla de decisión «¿qué me están pidiendo?».
      Es la brecha real identificada en `estrategia.md` §2.
- [ ] Mientras se arma, repasar flashcards (segunda pasada).
- [ ] `/registrar`.

### 🔴 D11 · sábado 19/09 — **Simulacro 1**, cronometrado (día largo)
- [ ] `/simulacro` → resolver **2 horas exactas, con reloj**.
- [ ] **La disciplina que estás entrenando:** 10 min de lectura y descarte, elegís 1
      teórico + 2 prácticos, **dejás los otros 3 en blanco**. Si resolvés los 6, el
      simulacro falló.
- [ ] Corregir con la corrección desplegable. `/registrar` cada error.

### 🟠 D12 · domingo 20/09 — Tapar los agujeros del simulacro
- [ ] Rehacer **sólo** los ítems que fallaron el sábado.
- [ ] De lo que quede del banco 🟠, elegir según el registro: `B8` (masa/volumen
      planteando límites), `B9` (plano tangente / paralelo a un plano), `B12` (extremos
      absolutos sobre una región), `B13` (área de superficie).
- [ ] Tercera pasada de flashcards.
- [ ] `/registrar`.

### 🟡 D13 · lunes 21/09 — Víspera: nada nuevo
- [ ] Leer el machete unificado entero, dos veces. **45 min.**
- [ ] Flashcards, pasada final, sólo las marcadas como flojas. **30 min.**
- [ ] Releer `estrategia.md` §0 (la regla de 3 de 6) y §4 (los 6 teóricos).
- [ ] Mirar los enunciados de `2026-07-14` y `2026-07-28` **sin resolverlos**: son los dos
      predictores más cercanos del estilo actual.
- [ ] Dormir. **No estudiar tema nuevo hoy** — a esta altura sólo genera ruido.

---

## Si te atrasás

Orden de sacrificio, de lo primero que se tira a lo último:

1. ⚪ Banco de baja prioridad del D12 (Taylor, superficie parametrizada, límites).
2. ⚪ El bloque 🟠 de conservativos del D5 — pero **no** la demostración de independencia
   de la trayectoria, esa se queda.
3. 🟡 La segunda pasada de flashcards del D10.
4. 🟠 El machete unificado del D10: si no hay tiempo, usá los dos machetes por separado.
5. **Nunca se sacrifica:** D1-D4 (flujo y circulación), D6 (B6, el reciclado), D8 (EDO),
   D11 (el simulacro cronometrado).

Si perdés 2 días o más, corré `/plan` de nuevo en vez de improvisar: recalcula la poda con
los días que queden.

## Qué mirar cada día antes de arrancar

```bash
cd materias/analisis-matematico-2/final
grep -n "#Flujo\|#Circulacion" examenes/INDICE.md   # el enunciado exacto del día
tail -30 registro.md                                 # qué fallaste la última vez
```

---

_Plan generado el 2026-09-09 · 13 días · 2-3 h/día · examen martes 2026-09-22.
Recalculable con `/plan`._
