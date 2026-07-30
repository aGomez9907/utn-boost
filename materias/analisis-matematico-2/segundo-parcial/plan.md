# Plan de estudio — Recuperatorio 2º Parcial (2ª instancia) AM2

> Examen: **2026-07-31** (viernes) · Hoy: lun 2026-07-27 · **4 días completos** de
> preparación (lun 27, mar 28, mié 29, jue 30) — Física II salió de la agenda
> (no se rinde el final del 29/7), así que es **full AM2**.
> Restricciones: ninguna. Sin registro del recuperatorio del 2026-07-17 (ni enunciado
> ni errores) → el plan pondera por frecuencia histórica + candidatos a reciclaje.
> **Si aparece el enunciado del 17/7 o me contás qué falló, se recalcula más fino.**

**Reglas fijas de la semana:**
- Cada día arranca con **10 min de re-test**: rehacer (de memoria, sin mirar) lo que
  falló el día anterior según `registro.md`.
- Todo se resuelve **sin mirar el machete** y se corrige DESPUÉS con él (§N citados
  abajo) o con `examenes/INDICE.md`. Errores → `/registrar` (o contámelos y los anoto).

## Qué queda afuera (a propósito)

- ⚪ **Longitud de curva, masa de alambre, momento de inercia** (≤8 % histórico): no
  entran ni como lectura.
- **Stokes** solo en su forma rentable — "te dan rot f y no f" — como vistazo de 15 min
  con los checksums de §8 (viene creciendo en 2024–2026, no amerita más).
- Con 4 días completos, todo el resto del temario 🔴🟠🟡 tiene práctica activa.

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| **Lun 2026-07-27 (HOY)** | 🔴 **Simulacro-diagnóstico: el examen real del 8/7 completo, con reloj (2 h).** Son los candidatos #1 a variante en el recu, y lo que falle acá reordena los próximos días. | Los 6 ítems del **2026-07-08** sin mirar nada: P1 volumen `(x−1)²+y² ≤ z ≤ 5−2x` (§2) · P2 área de la superficie `z+y=x²` (§6) · P3 flujo por el cilindro corrido abierto (§6) · P4 EDO `y''−y=x+1` con dato recta tangente (§9+§10) · T1 potencial de `(2x/(x²+y²), 2y/(x²+y²))` (§5) · T2 jacobiano con área(D)=12 (§1). Corregir con el machete y anotar TODO error en `registro.md`. |
| **Mar 2026-07-28** | 🔴 **Flujo por todas las vías** (el P3 de casi todos los exámenes) **+ volumen reciclado.** | (a) El reciclado ×4: flujo de `f=(y², z²+x², x²)` por `y=x`, `x²+y²+2z²≤2` — **P3 del 2017-11-16** (§6, con los puentes). (b) Gauss cerrado: **P3 del 2024-07-12** (prisma, §7). (c) Superficie abierta + tapa: **P3 del sin-fecha** (`z=1+x²+y²`, `z≤2`, con `g,h` desconocidas que mueren en la div — receta y checksum en §7). (d) «Hallar `g`» con div dada: **P4 del 2022-12-02** («flujo por la esfera = volumen» ⇒ div ≡ 1; checksum en §7). (e) Volumen reciclado ×2: `2x²+2y²+z²≤3`, `z≥√(x²+y²)` — **P1 del 2023-07-28** (§2, elipsoide∩cono). *Si da:* **P1 del 2024-07-12** (paraboloide/cono, corregir el planteo con §2). Teórico del día (de memoria): **enunciado formal de Gauss** (hipótesis + tesis). |
| **Mié 2026-07-29** | 🔴 **Conservativo/potencial (el tema del 100 %) + Green/circulación + los dos formatos de T2.** | (a) El T2 reciclado ×3: potencial de `f=(2xy+2x·g'(x²), x²)` — **T2 del 2022-12-02** (§5; también cayó en el 2022-12-16 y el 2023-07-14). (b) **P2 del 2022-11-24**: potencial que vale k en un punto (§5, los 2 métodos). (c) «Hallar `g` para que sea conservativo»: **P1 del 2023-07-14** (`f=(x²−4y·g(x), g'(x)−x+y)` ⇒ `g''+4g=1`; checksum en §5). (d) El T1 casi fijo: Green con `f=(xy²/2, 3x²y/2)` sobre `x²≤y≤x` — **T1 del 2024-07-12** (§4 → 1/12) y su variante `(xy², 3x²y)` — **T1 del sin-fecha** (§4 → 1/6). (e) La circulación 3D reciclada: `f=(yz, 2xz, xy)` — **P2 del 2023-07-28** (§8 vía Stokes, ±8π). (f) T2 formato nuevo: integral polar → graficar región + pasar a cartesianas — **T2 del 2024-07-12** (§1). Teóricos del día (de memoria): **Green · cambio de variables · condición necesaria de conservativo (demostración completa)**. |
| **Jue 2026-07-30** | 🔴 Mañana: **EDO en batch + demostración de superposición + re-test general.** Tarde: **SIMULACRO a ciegas cronometrado.** Noche: parche. | Mañana: **P4 del 2024-07-12** (`y''−2y'+5y=10` con PVI), **P4 del sin-fecha** (`y''−6y'+9y=9x` con tangente `y=x+2`, §10), y **P4 del 2015-11-25** (`y''+y'−2y=cos x` con PVI) — las tres del tirón, corrigiendo con la tabla de §10. **Superposición: demostración escrita de memoria** (apunte `18`). Re-test de todos los ❌ acumulados del registro. Vistazo 15 min: §8 (rot dado ⇒ Stokes: **P1 del 2022-12-16** y **P2 del sin-fecha**) y §6 (área de superficie: **P2 del 2019-11-21**, el cono → 4√2π, y el P2 del 2026-07-08 ya hecho el lunes). Tarde: **2025-07-18 completo, 2 h con reloj, a ciegas** → corregir con `INDICE.md` + machete → errores a `registro.md`. Noche: parche SOLO de lo que falló. |
| **Vie 2026-07-31** | **EXAMEN.** | Repaso liviano únicamente con `exports/machete.pdf` + los errores anotados en la semana. NADA nuevo. |

**Sobre el simulacro del jueves:** `2025-07-18` es el examen más reciente que nunca se
te asignó en ningún plan (quedó intacto) y es de la misma época/formato que el recu.
Aviso honesto: algún resultado final suyo figura entre los checksums del machete, y
tras esta semana no queda ningún parcial completo sin usar (el único intacto,
`2014-11-28`, es un escaneo con transcripción aproximada «≈», no sirve de simulacro) —
si querés estreno absoluto, pedí `/simulacro` y se genera un `simulacro-02` nuevo.

## Qué cambió respecto del plan anterior (2026-07-27, primera versión de hoy)

- **Cae la restricción de Física II** (no se rinde el final del 29/7): lun–mié pasan
  de bloques de 45–60 min a **días completos**, y el miércoles deja de estar bloqueado.
- La reparación del examen del 8/7 se **concentra HOY como simulacro-diagnóstico con
  reloj** (antes estaba partida en dos medios días) — lo que falle hoy reordena la semana.
- Entran **frentes completos** que antes quedaban en "solo machete": flujo por todas
  las vías (martes), conservativo + Green + T2s (miércoles), EDO en batch (jueves).
- Los **teóricos dejan de ser condicionales**: cada día cierra con 1–3 escritos de
  memoria (Gauss → Green/cambio de variables/conservativo → superposición).
- El simulacro a ciegas `2025-07-18` sigue fijo el jueves a la tarde.

## Circuito de mantenimiento

- Después de cada bloque: `/registrar` (o contá qué salió y se anota). Lo que dé ❌
  se re-testea al día siguiente y entra al parche del jueves; el viernes no se toca
  nada nuevo.
- **Lo que más mejoraría este plan:** el enunciado del recuperatorio del
  **2026-07-17** (foto/PDF) para indexarlo — es la mejor pista de lo que va a tomar
  la misma cátedra dos semanas después — y saber qué te salió mal ese día.

---

*Regenerado el 2026-07-27 con: MATERIA.md (examen 2026-07-31), `estrategia.md` del
2026-06-30 (prioridades y frecuencias; previa al 8/7, el patrón sigue vigente),
`examenes/INDICE.md` (reciclados + examen real 2026-07-08), `registro.md` (sin
entradas), `que-saltear.md` (sí), `repaso/machete.md` (referencias §N). Input del
usuario: "no voy a rendir el final de Física II — meterle full a AM2". Reemplaza la
versión de esta mañana (que repartía la semana con Física II). Corregido el mismo día:
cada ejercicio cita ahora su parcial de origen exacto (pedido del usuario).*
