# Estrategia — Primer Parcial AM2 (recuperatorio)

> **Examen:** viernes **17 de julio de 2026** · faltan **7 días** · se rinde **el mismo día que el recuperatorio del 2P**.
> **Punto de partida declarado:** arrancás de cero en el 1P (no hay apuntes propios todavía), pero con los exámenes ya indexados y 11 resoluciones de cátedra disponibles.
> **Fuentes analizadas:** 16 exámenes reales de contenido distinto (2017–2026) + 2 simulacros de cátedra, indexados en `examenes/INDICE.md`. **Apuntes propios del 1P: 0** (ver Fase 3). Reporte generado contrastando el patrón histórico contra la cobertura de apuntes.

---

## 0. Cómo leer este documento

1. **Fase 2 — Qué toman siempre** (patrón real de 16 parciales distintos).
2. **Fase 3 — Contraste con tus apuntes**: la gran brecha (no hay apuntes) y qué la tapa.
3. **Plan de 7 días** compartido con el recu del 2P.
4. **Banco de "problemas tipo"** con las fechas exactas donde practicar.
5. **Checklist teórico** para T1/T2.

**Diagnóstico en una línea:** el 1P de esta cátedra es **extremadamente repetitivo** — con dominar ~6 plantillas de problema y ~4 teóricos cubrís casi cualquier examen. La única brecha real es que **no tenés apuntes propios del 1P**, pero eso se compensa con: (a) el tema más frecuente —**EDO de 1er orden + trayectorias ortogonales**— ya está en el apunte **`17-ecuaciones-diferenciales-i.md` del 2P**, reusable tal cual; y (b) **11 exámenes resueltos por la cátedra** que funcionan como "teoría por ejemplo". El riesgo no es el temario (es acotado y conocido): es el **tiempo compartido con el 2P** el mismo día.

> **Nota sobre los dos exámenes el 17/7:** esta estrategia es del 1P. El 2P ya está preparado (apuntes, estrategia, flashcards, machete y simulacro). El plan de abajo reserva los últimos días para refrescar el 2P; el reparto fino día a día entre ambos lo recalcula `/plan`.

---

## 1. Estructura del examen (constante 2017–2026)

Todos los primeros parciales tienen **4 problemas prácticos (P1–P4) + 2 teóricos (T1, T2)**. A diferencia del 2P, el orden por posición **no es rígido** (los temas rotan de posición), pero las *tendencias* son claras:

| Posición | Qué suele caer |
|---|---|
| **P1** | **Trayectorias ortogonales** (EDO 1er orden), o **EDO** suelta, o **derivada direccional** con datos. |
| **P2** | **Derivada direccional** (`h=g∘f`) / **aproximación lineal** (con `z` implícita) / **curva intersección**. |
| **P3** | **Curva en el espacio** (recta tangente / plano normal) / **derivada direccional con jacobiana** / aproximación lineal. |
| **P4** | **Trayectorias ortogonales** / **extremos** (Hessiano) / **plano tangente implícito** / curva. |
| **T1** | Teórico de **continuidad de función partida**, o **V/F** (discontinua / no admite derivada), o **regla de la cadena** (enunciar + `∇h`), o **EDO** (definir sol. general + resolver). |
| **T2** | **Derivadas direccionales de una función partida por definición** (el más reciclado), o **extremos**, o **EDO** (`y=e^{mx}`), o `f'_y` a partir de datos. |

> Lectura: casi todo problema práctico es una **combinación** de derivada direccional + regla de la cadena + derivación implícita. Ese "combo" es la firma del 1P.

---

## 2. FASE 2 — Patrón real: frecuencia por tema (16 parciales distintos)

> N = 16 exámenes reales de contenido distinto (se descuentan las equivalencias 2022-07-22≡2019-08-15 y 2022-10-05≡2019-10-11; ver Anexo A). Los 2 simulacros de cátedra **refuerzan** el patrón, no lo cambian. Cada número se puede rehacer con `grep` sobre `examenes/INDICE.md`.

| # | Tema | Aparece en | Frecuencia | Prioridad |
|---|---|---|---|---|
| 1 | **Derivada direccional + gradiente** (máx / mín / nula, con datos o por definición) | 16 de 16 | 🔴 **100 %** | MÁXIMA |
| 2 | **Regla de la cadena / composición** (`h=g∘f`, jacobiana) | 15 de 16 | 🔴 **94 %** | MÁXIMA |
| 3 | **EDO** (1er orden lineal/PVI, `y=e^{mx}`, trayectorias ortogonales) | 15 de 16 | 🔴 **94 %** | MÁXIMA |
| 4 | **Derivación implícita** (`z` definida implícitamente, T. función implícita) | 14 de 16 | 🔴 **88 %** | MÁXIMA |
| 5 | **Extremos** (Hessiano; libres o sobre región) | 13 de 16 | 🟠 **81 %** | ALTA |
| 6 | **Trayectorias ortogonales** (subconjunto de EDO — P1/P4) | 10 de 16 | 🟠 **63 %** | ALTA |
| 7 | **Curva en el espacio** (recta tangente / plano normal a intersección o `λ(t)`) | 10 de 16 | 🟠 **63 %** | ALTA |
| 8 | **Aproximación lineal** (diferencial, casi siempre con `z` implícita) | 8 de 16 | 🟠 **50 %** | ALTA |
| 9 | **Plano tangente / recta normal a superficie** (explícita, implícita, paramétrica) | 7 de 16 | 🟡 **44 %** | MEDIA |
| 10 | **Continuidad** de función partida (teórico) | 6 de 16 | 🟡 **38 %** | MEDIA |
| 11 | **Taylor** de grado 2 (→ plano tangente / extremo / aproximación) | 3 de 16 | ⚪ **19 %** | BAJA |
| 12 | **Superficie parametrizada** (punto regular, plano tangente paramétrico) | 3 de 16 | ⚪ **19 %** | BAJA |
| 13 | **Derivadas parciales** (por definición, teórico explícito) | 2 de 16 | ⚪ **13 %** | BAJA |
| 14 | **Diferenciabilidad ⇒ continuidad** (demostración teórica) | 1 de 16 | ⚪ **6 %** | BAJA |

### Lectura del patrón
- **El "núcleo duro" (🔴) es un solo combo:** derivada direccional + regla de la cadena + derivación implícita. Los tres viajan juntos en el problema estrella del 1P (`h=g∘f` con `g` implícita → dirección de derivada máxima/mínima/nula). Si dominás ese combo, tenés **1–2 problemas prácticos casi asegurados**.
- **El "tema rey" es la derivada direccional:** 16 de 16. No hay parcial sin ella (práctica o teoría). Es lo que no podés fallar.
- **EDO es el otro pilar (94 %)**, casi siempre como **trayectorias ortogonales** en P1/P4 (63 %) o como teórico. Es el tema más "mecánico" y de mayor ROI: se aprende una receta y cae seguro.
- **Extremos por Hessiano (81 %)** es el tercer pilar, muy repetido con polinomios cuadrático-cúbicos.
- **Comodines de posición:** curva en el espacio (63 %) y aproximación lineal (50 %) rotan entre P2/P3.

### Problemas RECICLADOS (aparecen casi idénticos varias veces) — oro puro para practicar
- **Trayectorias ortogonales + curva por un punto** → **2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-08-11, 2022-10-12, 2022-12-01, 2022-12-16, 2023-05-31, 2023-07-28** (y el simulacro 2024-05-17). **El problema más reciclado del 1P.** Cambia la familia (`y=Ce^{2x}`, `y=C/x`, `xy²=C`, `y=kx`, `y=kx³`) pero la receta es idéntica.
- **`h=g∘f` con `g` implícita → derivada direccional máx/mín/nula** (`f⃗=(xy²,y−x²)`, `g: z−u²+v²+ln(v+z)=0`) → **2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2023-07-28**. Cinco veces la misma mecánica.
- **`h=f(g)` con `∇f` o jacobiana dados → derivada direccional máxima** → **2022-05-20, 2022-06-01, 2022-12-01, 2022-12-16, 2023-05-31, 2026-05-22**. La versión "moderna" (2022+), seis veces.
- **Aproximación lineal con `z` implícita** → `xz+e^{yz−2}−2=0` en **2022-05-20 y 2026-05-22**; `z=u·x·v²…` en **2022-08-11 (h(1.01,3.98)) y 2022-10-12 (h(0.99,4.02))**.
- **Curva intersección → recta tangente / plano normal** → **2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-08-11, 2022-10-12, 2022-12-01, 2023-05-31, 2023-07-28, 2026-05-22**. Diez veces (el caso `x=√(25−y²) ∧ y²+z²=25 en (3,4,3)` se repite exacto).
- **Taylor grado 2 → plano tangente + extremo**, mismo `p(x,y)=5+x²+x(y−1)+4(y−1)²` → **2019-10-11** (y simulacros 2022-10-05, 2024-05-17).

### Teóricos RECICLADOS
- **Derivadas direccionales de función partida por definición en (0,0)** (`y²/x`, `y/x`, `y/x²`, `x³/y`, `x²/y`) → **2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2022-06-01, 2022-12-16, 2023-07-28**. **El teórico más tomado — casi fijo en T2.**
- **Continuidad de función partida en (0,0)** (`y/(x−y)`, `x³/(x²+y)`) → **2017-09-29, 2019-10-11, 2022-06-01**.
- **V/F: campo partido discontinuo / no admite derivada** (`x²/(x²+y⁴)`, `y²/(x⁴+y²)`) → **2022-12-01, 2023-05-31** (y simulacro 2024-05-17).
- **Enunciar regla de la cadena + calcular `∇h` con jacobiana** → **2022-08-11, 2022-10-12**.
- **`m` tal que `y=e^{mx}` es solución de `y''+py'+qy=0`** → **2022-05-20, 2022-12-16**.
- **`f'((1,1),(1,3))=17` y `lím[…]=5` → `f'_y(1,1)`** → **2023-05-31** (y simulacro 2024-05-17).

---

## 3. FASE 3 — Contraste con tus apuntes

**Tenés 0 apuntes propios del primer parcial.** En condiciones normales eso convertiría a TODOS los temas 🔴/🟠 en brechas críticas. Pero hay dos cosas que tapan casi toda la brecha:

### 3.1 🔴 La brecha (no hay apuntes) y qué la cubre

1. **EDO 1er orden + trayectorias ortogonales — ✅ CUBIERTO por el 2P.**
   El tema #3/#6 del ranking (94 %/63 %) ya está resuelto: el apunte **`../segundo-parcial/apuntes/md/17-ecuaciones-diferenciales-i.md`** cubre separables, lineal de 1er orden, homogénea y **trayectorias ortogonales**. Es exactamente lo que cae en P1/P4 del 1P. **Reusalo tal cual.** (El `y=e^{mx}` de los teóricos se apoya en el apunte `18` del 2P.)

2. **Todo el resto (derivada direccional, regla de la cadena, implícita, extremos, curva en el espacio, aproximación lineal, plano tangente, Taylor) — sin apunte propio, pero con clave de respuestas.**
   No hay teoría escrita tuya, PERO hay **11 exámenes resueltos por la cátedra** en `examenes/resueltos/` (2018-07-12, 2018-10-05, 2019-05-22, 2019-08-15, 2019-10-11, 2022-06-01, 2022-10-05, 2022-10-12, 2022-12-16, 2023-05-31, 2023-07-28) + tu propia resolución del 2022-08-11 (nota 7). Como los problemas son **los mismos reciclados**, esos resueltos son, en la práctica, la teoría-por-ejemplo de cada plantilla. **Estrategia:** aprendé cada plantilla resolviendo su versión de cátedra, no leyendo teoría abstracta.

> **Traducción práctica:** no gastes los 7 días escribiendo apuntes desde cero. Gastalos **resolviendo las 6 plantillas** hasta automatizarlas, usando los resueltos como corrección. Si querés apuntes formales del 1P para el futuro, es un proyecto post-recu (`/apunte-doc` sobre los resueltos).

### 3.2 Mapa tema → recurso → prioridad

| Tema del examen | Recurso disponible | Frec. | Qué hacer |
|---|---|---|---|
| Derivada direccional + gradiente | resueltos (casi todos) | 100 % | **Dominar.** Es el eje. |
| Regla de la cadena / composición | resueltos 2022-08-11, 2022-10-12 (con teórico) | 94 % | **Dominar + saber enunciar el teorema.** |
| EDO / trayectorias ortogonales | **apunte `17` del 2P** ✅ + resueltos | 94 % | **Dominar.** Receta cerrada, ROI máximo. |
| Derivación implícita | resueltos (va con el combo) | 88 % | **Dominar.** |
| Extremos (Hessiano) | resueltos 2023-07-28, etc. | 81 % | **Dominar.** |
| Curva en el espacio | resueltos 2018-07-12, 2019-05-22, 2023-05-31 | 63 % | **Dominar.** |
| Aproximación lineal | resueltos 2022-10-12, 2023-05-31 | 50 % | **Dominar** (mecánica corta). |
| Plano tangente / recta normal superficie | resueltos 2019-10-11 | 44 % | Saber la receta + un ejemplo. |
| Continuidad (teórico) | resueltos 2019-10-11, 2022-06-01 | 38 % | Saber escribirlo. |
| Taylor grado 2 | resuelto 2019-10-11 | 19 % | Un ejemplo. |
| Superficie parametrizada | resuelto 2019-10-11 (P2) | 19 % | Fórmula de punto regular. |

---

## 4. Plan de 7 días (vie 10/7 → vie 17/7) — compartido con el recu del 2P

Prioriza **cubrir el núcleo del 1P primero** (es el frente nuevo) y deja los últimos días para simulacros de ambos. Regla de oro: **por cada plantilla, resolvé al menos un examen real de esa plantilla** y corregí con el resuelto de cátedra.

| Día | Foco | Entregable del día |
|---|---|---|
| **Día 1 (vie 10/7)** | **EDO 1er orden + trayectorias ortogonales** (apunte `17` del 2P). Las 5 familias. | Resolver P1/P4 de **2018-07-12** (`y=Ce^{2x}`), **2019-05-22** (`y=C/x`), **2023-05-31** (`y=kx³`) + una EDO lineal (**2022-06-01 P4**). |
| **Día 2 (sáb 11/7)** | **El combo estrella:** derivada direccional + regla de la cadena + implícita. Los dos sabores (`h=g∘f` implícita / `h=f(g)` con jacobiana). | Resolver **2018-07-12 P3**, **2019-08-15 P2** (nula), **2023-07-28 P2** (mín) + **2023-05-31 P1**, **2022-05-20 P3** (jacobiana). |
| **Día 3 (dom 12/7)** | **Aproximación lineal** (con `z` implícita) + **curva en el espacio** (recta tangente / plano normal). | **2022-10-12 P2** y **2026-05-22 P2** (aprox.) + **2019-08-15 P3**, **2023-07-28 P3** (curva). |
| **Día 4 (lun 13/7)** | **Extremos por Hessiano** + **plano tangente / recta normal a superficie** + **Taylor** (repaso). | Extremos de **2023-07-28 P4** y **2019-05-22 P3**; recta normal **2017-05-05 P2**; Taylor **2019-10-11 P4**. |
| **Día 5 (mar 14/7)** | **Teoría del 1P a fondo** (ver checklist §6). Escribir de memoria. + **1er simulacro 1P**. | Escribir: direccionales de función partida, continuidad, V/F, regla de la cadena, `y=e^{mx}`. Simulacro **2022-12-01** cronometrado. |
| **Día 6 (mié 15/7)** | **Refresco del 2P** (su `repaso/machete.md` + `repaso/flashcards.md`) + **simulacro 2P** ya generado (sin quemarlo antes). | Simulacro 2P completo con reloj + repaso de sus demostraciones. |
| **Día 7 (jue 16/7)** | **Simulacro 1P a ciegas** (2 h) con el examen más representativo + repaso de errores de ambos parciales. Machetes listos. | **2026-05-22** completo, con reloj. Ajustar machetes. |
| **vie 17/7** | **EXAMEN (los dos).** Repaso liviano de fórmulas, nada nuevo. | — |

> Este es el plan **inicial**. El vivo (reparto fino 1P/2P, ajuste por errores de `registro.md`) lo recalcula `/plan` en `plan.md`.

---

## 5. Banco de "problemas tipo" (qué practicar de cada archivo)

Todos en `examenes/` con nombre `AAAA-MM-DD_Parcial.pdf|PNG`, con su resolución en `examenes/resueltos/` cuando existe.

- **Trayectorias ortogonales:** `2018-07-12`, `2018-10-05`, `2019-05-22`, `2019-08-15`, `2022-12-16`, `2023-05-31`, `2023-07-28`.
- **Combo direccional + cadena + implícita (`h=g∘f`):** `2018-07-12`, `2018-10-05`, `2019-08-15`, `2023-07-28`.
- **Direccional con jacobiana (`h=f(g)`):** `2022-05-20`, `2022-06-01`, `2022-12-16`, `2023-05-31`.
- **Aproximación lineal (implícita):** `2022-08-11`, `2022-10-12`, `2022-12-16`, `2026-05-22`.
- **Curva en el espacio (tangente / plano normal):** `2018-07-12`, `2019-05-22`, `2019-08-15`, `2022-12-01`, `2023-07-28`.
- **Extremos (Hessiano):** `2017-05-05`, `2019-05-22`, `2019-08-15`, `2022-12-16`, `2023-07-28`.
- **Plano tangente / recta normal superficie:** `2017-05-05`, `2019-10-11`, `2022-05-20`, `2022-06-01`.
- **Taylor grado 2:** `2019-10-11` (y simulacros `2022-10-05`, `2024-05-17`).
- **Teórico direccionales de función partida:** `2018-10-05`, `2019-05-22`, `2022-06-01`, `2022-12-16`, `2023-07-28`.

> **Simulacros "a ciegas" recomendados** (NO los mires hasta el día 5 y 7): **`2022-12-01`** (combina direccional-jacobiana + Taylor + curva + trayectorias, poco reciclado) y **`2026-05-22`** (el más reciente — la mejor foto de lo que te van a tomar). Que `/simulacro` **no los queme**.

---

## 6. Checklist teórico (T1 / T2) — tenés que poder ESCRIBIRLO, no solo reconocerlo

- [ ] **Derivadas direccionales de una función partida por definición en (0,0)** (`y²/x`, `y/x`, `y/x²`, `x²/y`): plantear el límite del cociente incremental por dirección genérica. *(el T más tomado — sin apunte; modelo en `resueltos/AMII 1P 2018-10-05 resuelto.pdf`)*
- [ ] **Continuidad de una función partida en (0,0):** definición + análisis por trayectorias / acotación. *(sin apunte; modelo en `resueltos/…2019-10-11`, `…2022-06-01`)*
- [ ] **V/F justificar:** un campo partido es discontinuo en (0,0) / no admite derivada en ninguna dirección. *(sin apunte; modelo en `resueltos/…2023-05-31`)*
- [ ] **Enunciar el teorema de la regla de la cadena** (funciones vectoriales) + calcular `∇h(a,b)` con la jacobiana `Df` dada. *(sin apunte; modelo en `resueltos/…2022-10-12`)*
- [ ] **Demostrar que la derivada direccional máxima es `‖∇f‖`** (+ direcciones de derivada nula). *(sin apunte)*
- [ ] **Demostrar que diferenciable ⇒ continua.** *(sin apunte)*
- [ ] **Definir derivada parcial** + calcularla por definición en una función partida. *(sin apunte; modelo en `resueltos/…2018-07-12`)*
- [ ] **EDO:** definir solución general y particular + resolver una EDO lineal de 1er orden. *(apoyo en `../segundo-parcial/apuntes/md/17-ecuaciones-diferenciales-i.md`)*
- [ ] **`m` tal que `y=e^{mx}` es solución de `y''+py'+qy=0`** y aplicarlo a `y''−y'−2y=0`. *(apoyo en apunte `18` del 2P)*
- [ ] **Definir superficie parametrizada y punto regular** (`σ_u × σ_v ≠ 0`). *(sin apunte; modelo en `2026-05-22 T2`)*
- [ ] **A partir de `f'((1,1),(1,3))` y un límite, calcular `f'_y`** (relación gradiente–derivada direccional). *(sin apunte; modelo en `resueltos/…2023-05-31`)*

---

## Anexo A — Equivalencias entre exámenes (para no practicar dos veces lo mismo)

- `2022-07-22` **≡** `2019-08-15` (mismo examen reutilizado).
- `2022-10-05` (simulacro) **≡** `2019-10-11`.
- `2018-07-12_Parcial.pdf` ≡ `duplicados/2018-07-12_captura.PNG`.
- `2022-08-11_Parcial.pdf` ≡ `duplicados/2022-08-11_foto.jpg` ≡ `resueltos/AMII 1P 2022-08-11 resuelto-lucho.pdf` (tu resolución, nota 7).

## Anexo B — Fuera del dataset

- **`_fuera-dataset_2doParcial-2017-07-06.PNG`** — es un **segundo parcial** mal archivado (rótulo "SEGUNDO PARCIAL"). No se computa en las frecuencias del 1P.
- **Simulacros de cátedra** (`2024-05-17`, `2022-10-05`): se indexan y sirven para practicar, pero no cuentan en los porcentajes (están armados con problemas reciclados de exámenes reales).

---

*Generado el 2026-07-10. Fuente: `examenes/INDICE.md` (16 exámenes reales + 2 simulacros) y `examenes/resueltos/` (11 resoluciones de cátedra). Apuntes propios del 1P: 0 — la teoría se apoya en los resueltos y en el apunte `17` de EDO del segundo parcial. Próximos pasos sugeridos: `/que-saltear` (poda) y `/plan` (plan vivo combinado 1P+2P).*
