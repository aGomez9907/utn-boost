---
name: que-saltear
description: Genera o regenera que-saltear.md, la guía de poda sección por sección de los apuntes de una evaluación. Cruza cada sección de cada apunte contra lo que realmente cae en los exámenes (según estrategia.md y examenes/INDICE.md) y clasifica todo en 🗑️ saltear / 📖 leer por arriba / ✅ núcleo. Úsala cuando el usuario quiera saber qué partes de los apuntes puede saltear, qué estudiar a fondo, cómo podar el material para estudiar contra reloj, después de regenerar la estrategia, o cuando invoque /que-saltear.
---

# que-saltear

Genera `materias/<materia>/<evaluacion>/que-saltear.md`: la **guía de poda** de los
apuntes. Para cada apunte de `apuntes/md/`, clasifica CADA sección en saltear / leer
por arriba / núcleo, cruzándola contra la evidencia de los exámenes reales. El
objetivo es que el usuario abra un apunte y sepa al instante qué partes ignorar sin
culpa y qué partes dominar.

Es una **vista derivada**: se calcula a partir de `estrategia.md` + `examenes/INDICE.md`
+ los apuntes. Se reescribe entera en cada corrida; no se edita a mano.

## Entrada / argumentos

Invocación: `/que-saltear [materias/<materia>/<evaluacion>]`

| Argumento | Efecto | Default |
|---|---|---|
| `materias/<m>/<e>` | Ruta explícita de la evaluación a podar. | resolución de contexto |

Si el usuario no da la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`:

1. Materia: la única con `estado: cursando` en su `MATERIA.md`. Si hay varias, preguntá.
2. Evaluación: la próxima por fecha según la tabla de evaluaciones de `MATERIA.md`.
3. Ante ambigüedad real, preguntá. Nunca adivines en silencio.

## Requisitos previos (bloqueantes)

Dentro de `materias/<m>/<e>/` tienen que existir:

- `estrategia.md` — frecuencias por tema, prioridades 🔴🟠🟡⚪, banco de problemas
  tipo y checklist teórico. Si falta → **pará** y pedile al usuario correr `/estrategia`.
- `examenes/INDICE.md` — el dataset de exámenes con tags. Si falta → **pará** y
  pedile correr `/indexar-examenes`.
- `apuntes/md/*.md` — los apuntes fuente. Si no hay ninguno, no hay nada que podar: avisá.

Leé también `MATERIA.md` (fecha de la evaluación, estructura del examen, leyenda de
tags) y la `estrategia.md` COMPLETA antes de clasificar nada.

## Pasos

1. **Resolver contexto** (ver arriba) y leer `MATERIA.md`, `estrategia.md` y
   `examenes/INDICE.md`. De la estrategia sacá: qué temas caen y con qué frecuencia,
   qué demostraciones/enunciados pide el checklist teórico, y qué quedó ⚪ descartable.

2. **Relevar las secciones de todos los apuntes:**

   ```bash
   grep -n "^##\|^###" materias/<m>/<e>/apuntes/md/*.md
   ```

   Eso da el esqueleto: cada línea es una sección a clasificar. No hace falta leer
   los apuntes enteros.

3. **Clasificar CADA sección de CADA apunte** cruzándola contra la evidencia:
   - 🗑️ **Saltear** — el tema/subtema no cae nunca (o casi nunca) en esta evaluación:
     interpretaciones físicas, demostraciones que el checklist no pide, propiedades
     que jamás se evaluaron, curiosidades, temas que pertenecen a OTRA evaluación.
   - 📖 **Leer por arriba** — propiedades que se usan sin demostrar, intuiciones que
     ayudan a entender el método, repasos, casos límite que conviene tener vistos.
   - ✅ **Núcleo** — métodos de cálculo que resuelven los problemas tipo, enunciados
     y demostraciones que figuran en el checklist teórico, todo lo que la estrategia
     marcó 🔴/🟠.

   Cuando el **título de la sección no alcance** para decidir (ambiguo, genérico),
   leé esa parte del apunte (con `Read` + offset sobre la línea que dio el grep)
   antes de clasificar. No adivines por el título.

4. **Detectar los apuntes casi 100% salteables:** los que cubren temas que no caen
   (o cayeron 1 vez en N exámenes, o son de otra evaluación). Para cada uno, anotá la
   **justificación de frecuencia** concreta (p. ej. "cae 1 sola vez en 16 parciales",
   "NUNCA cae en esta evaluación") y, si aplica, el mínimo rescatable ("quedate solo
   con la fórmula X").

5. **Destilar la "regla mental":** 2-4 patrones generales que resumen la poda, del
   estilo "🗑️ salteable: interpretaciones físicas, X, Y · ✅ cae siempre: método de
   cálculo + demostración de Z". Es lo primero que se lee del documento.

6. **Escribir `materias/<m>/<e>/que-saltear.md`** (sobreescribir entero) con la
   estructura de abajo. Confirmá la ruta escrita.

## Estructura del documento generado

```markdown
# Qué SALTEAR de cada apunte — <Evaluación> <Materia>

> Guía de poda para estudiar contra reloj (examen **<fecha>**). Cruza las secciones
> de los <N> apuntes con lo que **realmente cae** (ver `examenes/INDICE.md`).
>
> **No es que el contenido sobre** — simplemente **no lo toman** en esta evaluación.
>
> **Regla mental:**
> - 🗑️ Salteable: <patrones generales>.
> - ✅ Cae siempre: <patrones generales>.

---

## ⚡ <K> apuntes casi 100% salteables

- **NN · Título** → <justificación de frecuencia>. <mínimo rescatable si lo hay>.
  Saltear: <lista de secciones>.

---

## Apunte por apunte

Leyenda: 🗑️ = saltear · 📖 = leer por arriba (intuición/propiedad) · ✅ = núcleo, **sí** estudiar.

### NN · Título del apunte
- 🗑️ Sección A · Sección B <(motivo breve si no es obvio)>.
- 📖 Sección C (por qué alcanza con leerla por arriba).
- ✅ Sección D · **Sección E** (nota de evidencia: qué problema/teórico la usa,
  con fecha de examen si es un dato fuerte).

---

*Generado el AAAA-MM-DD. Contraste: <N> apuntes de `apuntes/md/` vs. <M> exámenes de
`examenes/INDICE.md`. La poda es para aprobar <esta evaluación>; no descarta el valor
conceptual del material.*
```

Detalles del formato:

- Los apuntes casi 100% salteables aparecen igual en "Apunte por apunte", pero con
  una línea de remisión: `### NN · Título → (ver arriba: …)`.
- Las secciones núcleo con evidencia fuerte llevan la referencia entre paréntesis
  (fecha del examen o problema tipo que las usa): eso es lo que hace creíble la poda.
- Todo apunte de `apuntes/md/` tiene que aparecer; ninguna sección queda sin clasificar.

## Reglas

- **Evidencia, no intuición:** cada 🗑️ y cada ✅ se justifica con `estrategia.md` /
  `INDICE.md` (frecuencias, checklist, banco). No re-leas los PDFs/imágenes de
  `examenes/` — solo el índice.
- **Regenerable:** reescribí el archivo entero en cada corrida; no hagas ediciones
  incrementales ni preserves texto viejo.
- **Dependencia declarada:** si `estrategia.md` cambia (examen nuevo indexado,
  `/estrategia` re-corrida), este archivo queda desactualizado y hay que regenerarlo
  con esta skill. Lo mismo si se agregan apuntes nuevos.
- En caso de duda entre 🗑️ y 📖, elegí 📖 (leer por arriba es barato; saltear algo
  que cae es caro). En caso de duda entre 📖 y ✅, mirá el checklist teórico y el
  banco de problemas: si aparece ahí, es ✅.
- Fechas siempre absolutas (AAAA-MM-DD) y pie con fecha de generación + fuentes.
- Español rioplatense (voseo), tono directo, igual que el resto del repo.

## Notas

- Escala de la poda: 🗑️ / 📖 / ✅ (esta skill). No confundir con la escala de
  prioridades de `estrategia.md` (🔴🟠🟡⚪): la estrategia prioriza TEMAS; esta skill
  poda SECCIONES de apuntes. El mapeo aproximado es ⚪→🗑️, 🟡→📖, 🔴/🟠→✅, pero se
  decide sección por sección, no tema por tema.
- Resultado de referencia (calidad esperada, ejemplo real):
  `materias/analisis-matematico-2/segundo-parcial/que-saltear.md`.
- No hace falta ningún script de `tools/` para esta skill; si en algún paso usás uno,
  corrélo con `venv/bin/python tools/<script>.py` (fallback `python tools/<script>.py`).
