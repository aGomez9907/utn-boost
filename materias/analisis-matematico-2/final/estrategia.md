# Estrategia — Final de Análisis Matemático II

> **Mesa objetivo:** 2026-09-22 / 2026-09-23 (ventana `sep` de `carrera/datos/calendario.json`).
> **Hoy:** 2026-09-09 → quedan **13 días**.
> **Objetivo declarado en `carrera/datos/objetivos.json`:** `am2-septiembre` — sacarse AM2
> de encima en este llamado.
> **Evidencia:** 24 finales reales (2024-03-05 → 2026-07-28) indexados en
> [`examenes/INDICE.md`](examenes/INDICE.md). Todo lo que sigue sale de ahí, no de intuición.

---

## 0. La regla que define TODA la estrategia

En el encabezado de los 24 finales, sin excepción:

> *Condición de aprobación (6 puntos): tres ejercicios correctamente resueltos
> (**uno de T1 o T2** y **dos de P1, P2, P3 o P4**).*

Traducción:

| Lo que hay que hacer | Lo que NO hay que hacer |
|---|---|
| **1 teórico** de los 2 → elegís el que sabés | Saber los dos teóricos |
| **2 prácticos** de los 4 → elegís los dos mejores | Resolver los cuatro |
| **3 de 6 ítems** | 6 de 6 |

Con 2 horas y sólo 3 ítems que entregar, **la habilidad decisiva es elegir rápido**. En 24
finales, siempre hubo al menos un flujo y al menos una circulación entre los P; si tenés
esos dos blindados más un teórico de la lista corta, aprobás sin tocar el resto.

**Regla de oro para el día del examen:** los primeros 10 minutos son de lectura y
descarte, no de resolución. Marcá los 2 prácticos que resolvés y el teórico que escribís,
y no vuelvas a mirar los otros tres.

---

## 1. Frecuencia real por tema (24 finales)

«Presencia» = en cuántos de los 24 exámenes aparece al menos un ítem del tema.

| Prioridad | Tema | Presencia | Dónde suele caer |
|---|---|---|---|
| 🔴 | **Flujo** (directo por parametrización, o Gauss) | **23/24 · 96%** | cualquier P; a veces T |
| 🔴 | **Circulación / trabajo** (Green, Stokes o conservativo) | **22/24 · 92%** | cualquier P; muy seguido T |
| 🔴 | **EDO** (1er o 2º orden, o trayectorias ortogonales) | **22/24 · 92%** | casi siempre un P, muchas veces P4 |
| 🔴 | **Teoremas integrales enunciados/deducidos** (Green, Stokes, Gauss, cambio de variables) | **~20/24 · 83%** | T1 o T2, item (a) |
| 🟠 | **Plano tangente / recta normal** (a superficie, a curva de nivel) | 16/24 · 67% | P o T |
| 🟠 | **Derivación implícita** | 13/24 · 54% | siempre combinada con otra cosa |
| 🟠 | **Integrales múltiples** (volumen, masa, área plana, cambio de variables) | 13/24 · 54% | P1 típicamente |
| 🟠 | **Conservativo / función potencial / líneas equipotenciales** | 13/24 · 54% | T muy seguido |
| 🟠 | **Extremos** (Hessiano, absolutos en una región, punto silla) | 12/24 · 50% | T o P |
| 🟠 | **Gradiente** (dirección de máx/mín crecimiento, ⊥ a nivel) | 12/24 · 50% | P o T |
| 🟡 | **Derivada direccional** (incl. por definición en función partida) | 10/24 · 42% | P o T |
| 🟡 | **Área de superficie** e integral de superficie escalar | 9/24 · 38% | P |
| 🟡 | **Regla de la cadena** (composición, jacobianos) | 7/24 · 29% | casi siempre como herramienta |
| 🟡 | **Curva en el espacio / punto regular** | 8/24 · 33% | T sobre todo |
| 🟡 | **Diferenciabilidad / continuidad / límite de función partida** | 8/24 · 33% | T, formato V/F |
| ⚪ | **Taylor grado 2 · aproximación lineal** | 6/24 · 25% | P |
| ⚪ | **Superficie parametrizada** | 2/24 · 8% | T |
| ⚪ | **Baricentro · longitud de curva · momento de inercia · superposición** | **0/24 · 0%** | **nunca cayeron en un final** |

### Lo que hay que leer de esta tabla

1. **El final es más "1er parcial" de lo que parece.** Casi la mitad de los ítems son de
   varias variables (implícita, plano tangente, gradiente, extremos, direccional). No
   alcanza con el temario del 2P.
2. **Flujo + circulación cubren el 96% y el 92%.** Si sólo pudieras estudiar dos cosas,
   son esas dos: te dan los 2 prácticos que necesitás casi con seguridad.
3. **Los teóricos son un menú corto y repetido.** Green, Stokes, Gauss, independencia de
   la trayectoria, cambio de variables y las definiciones (derivada direccional, función
   potencial, extremos, diferenciabilidad) cubren prácticamente todos los T1/T2 del
   dataset. Ver §4.
4. **Formato V/F:** 13 de 24 finales tienen al menos un ítem «indique si es verdadera o
   falsa, justificando». Es un formato, no un tema, pero hay que entrenarlo: un
   contraejemplo bien elegido vale lo mismo que una demostración.
5. **Podés ignorar sin culpa:** baricentro, longitud de curva, momento de inercia y
   superposición de EDO. Cero apariciones en 24 finales, aunque sí caen en parciales.

---

## 2. Brechas: qué material tenés y qué falta

| Tema | Cobertura actual | Estado |
|---|---|---|
| Integrales dobles/triples, curvas, superficies, flujo, Green, Gauss, Stokes, conservativos, EDO 2º | **19 apuntes** en `segundo-parcial/apuntes/md/` + `segundo-parcial/repaso/machete.md` (11 secciones) + 61 flashcards | ✅ completo |
| Gradiente, direccional, regla de la cadena, implícita, extremos, Taylor, plano tangente, curva en el espacio, EDO 1º, trayectorias ortogonales | **sin apuntes**, pero `primer-parcial/repaso/machete.md` (12 secciones) los cubre con recetas y reciclados verificados | 🟠 suficiente para un final, no ideal |
| Resoluciones modelo del final | **12 resoluciones** en `examenes/resueltos/` (cátedra, A. Rojas Torres, Sylvina) + respuestas oficiales del 2024-07-23 | ✅ oro puro |
| Flashcards de teoría del final | no existen | 🟠 generar con `/flashcards` (día 8) |
| Machete unificado del final | no existe (hay uno por parcial) | 🔴 **la brecha real** — generar con `/machete` (día 10) |

**Conclusión de la brecha:** no falta material de estudio, falta **integración**. Los dos
machetes existen por separado y el final los mezcla. La pieza que hay que fabricar es un
machete único con la tabla de decisión «¿qué me están pidiendo?» que abarque ambos
temarios, más las flashcards de los teóricos de §4.

**No hay que generar apuntes nuevos del 1P.** Con 13 días, escribir apuntes desde cero es
tiempo mal invertido: el machete 1P + las 12 resoluciones modelo alcanzan.

---

## 3. Banco de problemas tipo

Ordenado por retorno. Cada línea cita el examen exacto de donde sale, para que puedas
autocorregir con el original (y con la resolución cuando existe).

### 🔴 Núcleo — hacer todos, cronometrados

| # | Tipo | Practicar con | Resolución disponible |
|---|---|---|---|
| B1 | **Flujo por Gauss** (cuerpo cerrado, campo con términos que se cancelan) | `2026-07-28 P1`, `2025-07-29 P4`, `2026-05-19 P3`, `2026-07-14 P2` | 2025-07-29 ✅ · 2026-05-19 ✅ |
| B2 | **Flujo directo por superficie abierta** (paraboloide / cilindro / plano, con orientación) | `2025-09-25 P2`, `2025-12-09 P2`, `2026-03-03 P4`, `2025-12-02 P4` | 2026-02-10 ✅ (mismo estilo) |
| B3 | **Circulación por Green** (región plana, sentido, campo con `e^{x²}`-tipo que no se integra) | `2026-07-28 P2`, `2025-12-09 P3`, `2026-07-14 P3`, `2026-03-03 T1b` | — |
| B4 | **Circulación por Stokes** (curva intersección de dos superficies, con `Df` o `rot f` dados) | `2025-07-15 P1` ≡ `2025-12-02 P2`, `2025-07-29 P1`, `2026-05-19 P1`, `2026-07-14 T1b` | 2025-07-29 ✅ · 2026-05-19 ✅ |
| B5 | **EDO 2º orden** completa + condición inicial / recta tangente / límite | `2026-07-28 P3`, `2025-05-20 P4`, `2024-10-09 P4`, `2025-12-09 P4`, `2025-07-29 P2` | 2025-07-29 ✅ |
| B6 | **Implícita `xz + z + y + ln(z−xy) = 10`** — aprox. lineal + recta normal + intersección | `2026-03-03 P2`, `2024-05-10 P2`, `2025-07-29 T1a` | 2024-05-10 ✅ |
| B7 | **Conservativo:** hallar `g` / potencial / línea equipotencial | `2026-07-14 P4`, `2025-12-09 T2b`, `2025-07-15 T2b`, `2024-12-17 P1` | — |

> **B6 es el ejercicio más reciclado del dataset: cayó 3 veces en 2 años.** Hacelo primero.

### 🟠 Alta — hacer al menos uno de cada fila

| # | Tipo | Practicar con |
|---|---|---|
| B8 | **Masa / volumen** planteando límites (a veces piden *dos* integrales distintas) | `2026-03-03 P1`, `2025-12-16 P1`, `2024-12-17 P4`, `2025-02-18 P4` |
| B9 | **Plano tangente / recta normal** a superficie, y puntos donde es paralelo a un plano | `2026-07-14 P1`, `2025-12-02 P3`, `2025-12-09 P1` |
| B10 | **Derivada direccional nula / máxima / de máximo decrecimiento** con implícita o composición | `2026-07-28 P4`, `2024-10-09 P3`, `2024-12-17 P3` |
| B11 | **Trayectorias ortogonales** con parámetro a determinar | `2026-03-03 P3`, `2024-12-03 P4`, `2025-02-11 P3` |
| B12 | **Extremos:** clasificar por Hessiano, o absolutos sobre una región cerrada | `2026-05-19 P4`, `2025-02-11 P1`, `2025-05-20 T1b` |
| B13 | **Área de superficie** / integral de superficie escalar | `2026-05-19 P2`, `2025-07-29 P3`, `2025-02-18 P3` |

### ⚪ Sólo si sobra tiempo

Taylor grado 2 (`2025-09-25 P3`, `2024-12-10 P2`), superficie parametrizada
(`2025-02-11 T1b`), límite de función partida (`2024-10-09 T2a`).

---

## 4. Checklist teórico — el que decide si aprobás

**Sólo necesitás UNO de T1/T2.** Estos son los que más cayeron; con los primeros 6
escritos de memoria tenés cubierto prácticamente cualquier final del dataset.

Tenés que poder **escribirlos**, no reconocerlos.

| ✔ | Teórico | Veces | Qué exige exactamente |
|---|---|---|---|
| ☐ | **Green** — enunciar con hipótesis **y deducir la fórmula del área plana** | 5 | La deducción del área (`A = ½∮ x dy − y dx`) es la mitad de las veces. No alcanza con enunciar. |
| ☐ | **Stokes / teorema del rotor** — enunciar | 5 | Suele venir con un V/F que se resuelve viendo que `rot f · n = 0` sobre el plano de la curva. |
| ☐ | **Gauss / divergencia** — enunciar con hipótesis | 4 | Preguntan además *si es aplicable en forma directa* a una superficie **abierta**: la respuesta es no, hay que cerrarla. |
| ☐ | **Independencia de la trayectoria** — demostrar `∫_C ∇φ·ds = φ(Q) − φ(P)` | 5 | Demostración corta vía regla de la cadena sobre `φ(γ(t))` + Barrow. La piden literal. |
| ☐ | **Extremos** — definir máx/mín local, absoluto, punto silla; criterio del Hessiano | 5 | Casi siempre «defina X» + un caso concreto para clasificar. |
| ☐ | **Cambio de variables** en integrales dobles — enunciar; polares y su jacobiano | 4 | A veces piden el jacobiano deducido, a veces `Área(D*)` con `Área(D)` dada. |
| ☐ | **Derivada direccional** — definir; demostrar `f'(X₀,ǔ) = ∇f(X₀)·ǔ` | 3 | Salió en el más reciente (2026-07-28 T1a). La demostración usa diferenciabilidad. |
| ☐ | **Función potencial** — definir; condición necesaria y su demostración | 4 | Combinada con líneas equipotenciales. |
| ☐ | **Punto regular** de curva y de superficie parametrizada — definir | 4 | Definición + verificar en un caso concreto. |
| ☐ | **Gradiente ⊥ curva/superficie de nivel** — demostrar | 2 | Derivar `F(γ(u)) = cte` y aplicar regla de la cadena. |
| ☐ | **Diferenciabilidad / continuidad** — definir para `f: R² → R` | 3 | Siempre con una función partida para analizar en el origen. |
| ☐ | **Regla de la cadena** en forma matricial — enunciar | 1 | Con hipótesis. Menos frecuente, pero es la herramienta de medio examen. |

### Los V/F que se repiten

- **Función partida tipo `xy²/(x²+y²)` en el origen:** ¿es diferenciable? ¿admite plano
  tangente? — cayó 3 veces (`2024-03-05 T2b`, `2025-12-16 T2b`, `2026-07-28 T1b`). La
  respuesta siempre pasa por verificar la definición de diferenciabilidad, no por el
  gradiente.
- **«Todo campo diferenciable es derivable»** (`2026-02-24 T1a`) — verdadero, y la
  demostración es la misma de `f'(X₀,ǔ) = ∇f·ǔ`.
- **Circulación nula sobre curva cerrada** — a veces por conservativo, a veces por Stokes
  con `rot f · n = 0`. Distinguí cuál corresponde antes de escribir.

---

## 5. Cómo se convierte esto en días

Ver [`plan.md`](plan.md). El esqueleto:

1. **Días 1-2:** reactivar el 2P (flujo y circulación) con el machete que ya tenés.
2. **Días 3-4:** reactivar el 1P (implícita, gradiente, plano tangente, extremos, EDO 1º).
3. **Días 5-8:** banco de problemas 🔴 cronometrado, corrigiendo contra `resueltos/`.
4. **Día 8:** flashcards de los teóricos de §4.
5. **Días 9-10:** machete unificado + banco 🟠.
6. **Días 11-12:** simulacros cronometrados de 2 h, con la disciplina de elegir 3 de 6.
7. **Día 13:** repaso de machete y flashcards. Nada nuevo.

---

## Anexo A — Fuera del dataset

- El final del **2026-09-22/23** será, por continuidad del patrón, la primera mesa
  posterior al 2026-07-28. Los dos finales de julio 2026 (14 y 28) son los mejores
  predictores del estilo actual.
- La cátedra alterna **dos formatos de encabezado** (uno tipeado en LaTeX, otro en Word).
  Los LaTeX (`2024-10-09`, `2025-05-20`, `2026-05-19`, `2026-07-14`) tienden a ítems más
  cortos y más V/F; los Word, a ítems con más incisos. No cambia el temario.
- `2026-02-24_Final.pdf` trae en el encabezado `17/02/2026` **y** `24/02/2026`: es un
  examen reutilizado entre dos llamados. Vale como uno solo.

## Anexo B — Qué NO estudiar

Con 13 días y la regla de «3 de 6», estos temas tienen retorno negativo:

- **Baricentro, longitud de curva, momento de inercia, superposición de EDO:** 0
  apariciones en 24 finales.
- **Demostraciones largas fuera de la lista de §4** (p. ej. demostrar Green o Gauss en sí
  mismos): nunca las piden, sólo piden enunciarlos.
- **Resolver los 4 prácticos en el simulacro:** entrená explícitamente para dejar dos en
  blanco. Es parte de la técnica.

---

_Generado el 2026-09-09 · Fuentes: `examenes/INDICE.md` (24 finales),
`segundo-parcial/apuntes/md/` (19 apuntes), `primer-parcial/repaso/machete.md`,
`segundo-parcial/repaso/machete.md`, `carrera/datos/calendario.json`._
