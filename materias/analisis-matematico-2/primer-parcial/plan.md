# Plan de estudio — Recuperatorios 1P + 2P (mismo día, "parcial integrador")

> Examen: **2026-07-17** (rendís los dos recuperatorios el mismo viernes; si el "integrador" resultara ser UN solo examen mezclado, la preparación es idéntica: unión de los dos temarios, y este plan ya cubre eso). · Hoy: **mar 2026-07-14** · **3 días útiles** (mar 14, mié 15, jue 16).
> Restricciones declaradas (2026-07-14): **prácticos primero; teóricos SOLO si al final alcanza el tiempo** → van en bloque separado al final, no mezclados en los días.
> Sin práctica registrada esta semana (`registro.md` del 2P vacío, 1P sin registro) → se asume arranque desde cero HOY.

## ⚠️ No entra todo (triaje con 3 días)

Con 3 días para dos parciales, el plan cubre **solo el núcleo 🔴/🟠 de cada mitad + 1 simulacro**. Lo que cae o queda en mínimo:

- **1P 🟡/⚪** — plano tangente a superficie, Taylor, superficie parametrizada: NO se practican; quedan cubiertos solo por la receta del machete (§8, §9) y los resultados reciclados verificados (§11).
- **2P 🟡/⚪** — área de superficie, rotor/Stokes, longitud de curva: solo lectura del machete del 2P. Circulación (🟠 69 %) entra apenas como *(si da)* del jueves con su problema reciclado; Green queda además en el bloque teórico.
- **Teóricos** — por pedido tuyo van al final, condicionales. **Costo honesto:** son 2 de 6 ítems de cada examen (~1/3 de los puntos). Si el jueves te sobra aunque sea 1 hora, escribí de memoria el nº 1 de cada lista del bloque teórico: son los más reciclados y rinden más que un práctico extra.

## PRÁCTICOS — plan día por día

Regla de cada ejercicio: **resolver sin mirar → corregir con el resuelto de cátedra** (1P: `examenes/resueltos/`) o **con apuntes + machete** (2P). Reparto ≈ 60/40 a favor del 1P: el 2P lo rendiste el 2026-07-08 y está fresco; el 1P es el frente frío.

| Día | Foco | Entregable del día |
|---|---|---|
| **Mar 2026-07-14 (HOY)** | 🔴 **1P — los dos pilares.** (a) EDO 1er orden + trayectorias ortogonales (apunte `../segundo-parcial/apuntes/md/17-ecuaciones-diferenciales-i.md` + machete 1P §4). (b) El combo estrella: derivada direccional + regla de la cadena + implícita, en sus dos sabores. | (a) Trayectorias ortogonales **2018-07-12 P1** (`y=Ce^{2x}`) y **2023-05-31 P4** (`y=kx³`) + EDO lineal **2022-06-01 P4**. (b) Combo `h=g∘f` implícita: **2018-07-12 P3** y **2023-07-28 P2** (dirección de derivada mínima); sabor jacobiana `h=f(g)`: **2023-05-31 P1**. Los 6 tienen resuelto de cátedra. |
| **Mié 2026-07-15** | **Arranque (10-15 min): re-test de ayer** (trayectorias, otra familia). Mañana: 🟠 **1P — los comodines de P2/P3/P4.** Tarde: 🔴 **2P — núcleo A** (apuntes `01`-`05`, `10`, `11` + machete 2P). | Re-test: trayectorias ortogonales **2019-05-22 P4** (`y=C/x`). 1P: aproximación lineal **2022-10-12 P2** (`h(0.99, 4.02)`), curva en el espacio **2019-08-15 P3**, extremos por Hessiano **2023-07-28 P4** y **2019-05-22 P3** (todos con resuelto; el 2019-05-22 comparte PDF con el re-test). 2P: volumen **2016-11-25 P1** + conservativo/potencial **2022-07-15 P2** *(si da: masa **2017-11-16 P1** y potencial **2022-11-24 P2**)*. |
| **Jue 2026-07-16** | **Arranque (10-15 min): re-test del combo** del martes, sabor "derivada nula". Mañana: 🔴 **2P — núcleo B** (apuntes `14`, `15`, `18`, `19` + machete 2P). Tarde: **SIMULACRO 1P a ciegas** + corrección. Cierre: bloque teórico ↓ solo si sobra tiempo. | Re-test: combo **2019-08-15 P2** (dirección de derivada nula, con resuelto). 2P: el flujo reciclado `f=(y², z²+x², x²)` a través de `y=x` (**2017-11-16 P3**), flujo por Gauss **2022-07-15 P3**, EDO 2° orden **2019-11-21 P4** *(si da: **2016-07-06 P4** y la circulación reciclada `f=(yz, 2xz, xy)` de **2023-07-28 P2 del 2P**, que cayó 2 veces idéntica)*. Tarde: **2026-05-22 completo (los 4 prácticos), con reloj (~90 min)** — es el examen más reciente, la mejor foto de lo que te van a tomar. Corregir con machete §11 y **pasarle los resultados a Claude** (este examen no tiene resuelto de cátedra). *(Si da: los 4 prácticos de **2022-12-01**, el otro reservado, o P1+P3 del 2P **2023-07-14** a ciegas.)* |
| **Vie 2026-07-17** | **EXAMEN (1P + 2P).** | Repaso liviano SOLO con los dos machetes (`primer-parcial/exports/machete.pdf` y `segundo-parcial/repaso/machete.md`). Nada nuevo. |

## TEÓRICOS — bloque separado (SOLO si al final alcanza)

Entrás acá recién con los prácticos del día cerrados (lo natural: jueves a la noche, o huecos sueltos). El método es **escribirlos de memoria**, no releerlos. En orden de reciclaje real — si solo hay 1 hora, hacé el nº 1 de cada lista:

**1P** (checklist completo en [estrategia.md §6](estrategia.md)):
1. **Derivadas direccionales de una función partida por definición en (0,0)** — 7 de 16 exámenes, casi fijo en T2. Modelo: `resueltos/AMII 1P 2018-10-05 resuelto.pdf`; receta en machete §10.
2. **Demostrar que la derivada direccional máxima es ‖∇f‖** (+ dirección de derivada nula) — machete §10.
3. **Continuidad de una función partida en (0,0)** — modelos en resueltos 2019-10-11 y 2022-06-01.
4. **Enunciar la regla de la cadena + calcular ∇h con jacobiana** — modelo en resuelto 2022-10-12.
5. `m` tal que `y=e^{mx}` resuelva `y''−y'−2y=0` (→ `m=2, −1`, machete §11).

**2P** (checklist completo en [estrategia del 2P §6](../segundo-parcial/estrategia.md)):
1. **Condición necesaria de campo conservativo** — enunciado + demostración (apunte `10-campos-conservativos.md`).
2. **Superposición de soluciones de EDO** — demostración (apunte `18`).
3. **Cambio de variables / Jacobiano** + la variante polar 2024-2025 (graficar `ρ=2cosφ` y pasar a cartesianas) — apuntes `03`/`04`.
4. **Green y Divergencia** — enunciados formales con hipótesis (apuntes `09`, `15`).

## Qué cambió respecto del plan anterior (2026-07-10)

- **De 7 días a 3:** el plan anterior arrancaba el vie 10/7; no hubo práctica registrada, así que se recomprime todo el núcleo a mar–jue. Cae un día entero de 2P (dom 12/7) y el 2P queda en 2 medios días — se banca porque lo rendiste hace 6 días.
- **Teóricos desplazados a bloque condicional** al final (pedido tuyo del 2026-07-14); antes tenían el mié 15 dedicado.
- **Un solo simulacro garantizado** (antes eran 3): queda **2026-05-22** (el más representativo); **2022-12-01** pasa a opcional. El simulacro 2P a ciegas queda como opcional (P1+P3 de 2023-07-14).
- **Ejercicios podados por plantilla** (de 3-5 a 1-2 por plantilla), priorizando los que tienen resuelto de cátedra para corrección inmediata.
- **(2ª pasada, mismo 14/7 — auditoría pedida por el usuario):** re-test espaciado de 10-15 min al arrancar mié (trayectorias **2019-05-22 P4**) y jue (combo **2019-08-15 P2**) para no dejar los pilares "masivos" del martes sin recuperación; segundo ejercicio de extremos (**2019-05-22 P3**, 81 % ameritaba más de 1 rep); y la circulación reciclada del 2P como *(si da)* del jueves (69 % había quedado sin práctico).

## Circuito de mantenimiento

- Después de cada sesión: `/registrar` (anota qué practicaste y los errores) → si algo sale ❌, el jueves se replanifica con `/plan`.
- Machetes: ya están los dos generados; el del 1P leelo en `exports/machete.pdf` (el `.md` crudo no renderiza LaTeX).
- Si aparece el enunciado o la estructura real del "integrador", avisá: se reindexa y se recalcula.

---

*Regenerado el 2026-07-14 con: MATERIA.md (examen 2026-07-17), estrategia.md del 1P (banco y prioridades) y del 2P (banco y refresco), registro.md (sin entradas en ambos), que-saltear.md (no existe para el 1P), input del usuario (prácticos primero, teóricos solo si alcanza; menciona "parcial integrador"). Reemplaza al plan de 7 días del 2026-07-10. Ajustado el mismo día (2ª pasada) con las 3 mejoras de la auditoría: re-tests espaciados, extremos ×2 y circulación del 2P como (si da).*
