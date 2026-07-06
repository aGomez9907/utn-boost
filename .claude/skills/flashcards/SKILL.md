---
name: flashcards
description: Genera el mazo de repaso teórico de una evaluación, flashcards.md (estudio en Markdown con respuestas desplegables) + flashcards-anki.tsv (import directo en Anki). Convierte el checklist teórico de estrategia.md, las secciones núcleo de que-saltear.md y los apuntes en cartas de enunciado, demostración, fórmula y método. Usala cuando el usuario pida flashcards, tarjetas de repaso, un mazo de Anki, repasar teoría de memoria antes del examen, o cuando invoque /flashcards.
---

# flashcards

Genera el **mazo de repaso teórico** de una evaluación en dos formatos:

- `materias/<materia>/<evaluacion>/flashcards.md` — para estudiar en el repo: cartas
  con la respuesta oculta en `<details>` desplegables.
- `materias/<materia>/<evaluacion>/flashcards-anki.tsv` — para importar en Anki y
  repasar con repetición espaciada.

La fuente de verdad de QUÉ preguntar es la evidencia de los exámenes (checklist de
`estrategia.md`); la fuente de verdad de QUÉ responder son los apuntes. **El contenido
de cada carta se EXTRAE de `apuntes/md/`** (enunciados, hipótesis, fórmulas, pasos de
demostración tal como están ahí), nunca de memoria del modelo.

## Entrada / argumentos

Invocación: `/flashcards [materias/<materia>/<evaluacion>]`

| Argumento | Efecto | Default |
|---|---|---|
| `materias/<m>/<e>` | Ruta explícita de la evaluación. | resolución de contexto |

Si el usuario no da la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`:

1. Materia: la única con `estado: cursando` en su `MATERIA.md`. Si hay varias, preguntá.
2. Evaluación: la próxima por fecha según la tabla de evaluaciones de `MATERIA.md`.
3. Ante ambigüedad real, preguntá. Nunca adivines en silencio.

## Requisitos previos (bloqueantes)

Dentro de `materias/<m>/<e>/` tienen que existir:

- `estrategia.md` — en particular su **checklist teórico** (sección "Checklist
  teórico"): es la fuente #1 de cartas. Si falta → **pará** y pedí correr `/estrategia`.
- `apuntes/md/*.md` — de ahí sale el contenido de las respuestas. Sin apuntes no hay
  mazo: avisá.

Opcional pero recomendado: `que-saltear.md` (sus secciones ✅ núcleo suman cartas de
fórmula/método que el checklist no lista explícitamente).

## Tipos de carta

| Tipo | Tag | Frente (ejemplo de formato) | Dorso |
|---|---|---|---|
| Enunciado | `[enunciado]` | "Enunciá el teorema X (hipótesis y tesis)." | Hipótesis y tesis textuales del apunte. |
| Demostración | `[demostración]` | "Demostrá X." | Pasos clave **numerados** (1., 2., …) extraídos de la demostración del apunte + referencia al apunte. |
| Fórmula | `[fórmula]` | "¿Fórmula de X?" | La fórmula tal como figura en el apunte, con qué es cada símbolo si el apunte lo aclara. |
| Método / decisión | `[método]` | "¿Cuándo conviene X vs Y?" / "¿Pasos del método X?" | El criterio de decisión o los pasos numerados del método, según el apunte. |

## Pasos

1. **Resolver contexto** y leer `MATERIA.md`, el checklist teórico de `estrategia.md`
   y, si existe, `que-saltear.md`. Del checklist sacá la lista de ítems que los
   exámenes piden enunciar/demostrar (con el apunte de referencia que el checklist
   indica en cursiva); de la poda, las secciones ✅ con fórmulas y métodos núcleo.

2. **Planificar el mazo:** para cada ítem del checklist, decidí qué cartas salen
   (un teorema que piden "enunciar y demostrar" genera DOS cartas: una `[enunciado]`
   y una `[demostración]`). Sumá cartas `[fórmula]` y `[método]` desde las secciones
   ✅ de la poda y el banco de problemas tipo (decisiones del estilo "¿cuándo conviene
   X vs Y?"). Agrupá por tema, en el **orden de prioridad de la estrategia**
   (🔴 primero, después 🟠, etc.).

3. **Extraer el contenido de cada respuesta desde los apuntes.** Localizá la sección
   fuente con `grep -n` sobre `apuntes/md/*.md` y leé ESA parte (Read + offset).
   Copiá hipótesis, tesis, fórmulas y pasos como están en el apunte (podés condensar
   pasos de demostración a los hitos clave, pero sin cambiarlos ni completar huecos).
   Si el apunte solo tiene "idea de demostración" o el checklist marca que la
   demostración falta, la carta lo dice explícitamente ("el apunte solo da la idea:
   …") — no rellenes con una demostración inventada.

4. **Escribir `flashcards.md`** con la estructura de abajo (o aplicar la regeneración
   incremental si ya existe — ver más abajo).

5. **Escribir `flashcards-anki.tsv`** con las mismas cartas en formato Anki (ver
   formato). Verificá que la cantidad de líneas del TSV coincida con la cantidad de
   cartas del md.

6. **Confirmar** las dos rutas escritas, cuántas cartas hay por tipo, y recordar cómo
   importar en Anki (instrucciones de la sección del TSV).

## Estructura de `flashcards.md`

```markdown
# Flashcards — <Evaluación> <Materia>

> Mazo de repaso teórico (<N> cartas). Fuente de preguntas: checklist de
> `estrategia.md`; fuente de respuestas: `apuntes/md/`. Versión Anki:
> `flashcards-anki.tsv`.

## <Tema 1 — prioridad 🔴>

### 1. [enunciado] Teorema X
**P:** Enunciá el teorema X (hipótesis y tesis).
<details><summary>Ver respuesta</summary>

**Hipótesis:** … **Tesis:** …

$$…$$

*Fuente: `apuntes/md/NN-slug.md` § Sección.*
</details>

### 2. [demostración] Teorema X
**P:** Demostrá el teorema X.
<details><summary>Ver respuesta</summary>

**Paso 1:** … **Paso 2:** … **Paso 3:** …

*Fuente: `apuntes/md/NN-slug.md` § Sección.*
</details>

---

*Generado el AAAA-MM-DD desde `estrategia.md` (checklist), `que-saltear.md` (✅) y
`apuntes/md/`.*
```

Detalles: numeración corrida a lo largo de TODO el mazo (no se reinicia por tema);
cada carta lleva su tag de tipo y su apunte fuente; fórmulas en `$$…$$` en líneas
propias sin sangría (convención del repo); dentro de `<summary>` nada de Markdown.

## Formato de `flashcards-anki.tsv`

- Una carta por línea: `frente<TAB>dorso`. **Sin encabezado.** Mismo orden y misma
  numeración que el md (podés prefijar el frente con `N. [tipo]`).
- HTML plano: saltos de línea con `<br>`, pasos como `1. … <br> 2. …`. Nada de
  Markdown (`**`, `$$`) en el TSV.
- Matemática en **MathJax**: inline `\( … \)`, en bloque `\[ … \]`. Anki NO
  renderiza `$...$` por default — convertí todo LaTeX del apunte a esa notación.
- Sin tabs ni saltos de línea literales dentro de un campo (romperían el formato).

**Cómo importarlo en Anki** (dejalo dicho al usuario al confirmar): File → Import →
elegir `flashcards-anki.tsv` → tipo de nota Basic, separador de campos **Tab**,
"Allow HTML in fields" activado → elegir el mazo destino → Import.

## Regeneración incremental (si el mazo ya existe)

**NO reescribir de cero.** Leer `flashcards.md` existente y:

1. Detectar qué cartas ya existen (por tema + frente) y qué ítems nuevos aparecieron
   en el checklist / la poda desde la última corrida.
2. Agregar SOLO las cartas nuevas al final de su tema (o en un tema nuevo al final),
   continuando la numeración existente — **no renumerar ni tocar cartas viejas**
   (romperías el historial de repaso en Anki).
3. Anotar al pie: `> **Actualización AAAA-MM-DD:** agregadas cartas N–M (<temas>).`
4. Agregar las mismas cartas nuevas al FINAL de `flashcards-anki.tsv` (Anki deduplica
   por frente al reimportar; las viejas no se duplican).

## Reglas

- **Extraer, no recordar:** toda respuesta sale textual (o condensada) de
  `apuntes/md/`. Si algo no está en los apuntes, la carta lo declara como faltante;
  no se completa de memoria del modelo.
- Cobertura mínima: TODO ítem del checklist teórico de `estrategia.md` tiene al menos
  una carta. Las secciones ✅ de `que-saltear.md` aportan las de fórmula/método.
- No generar cartas de temas ⚪/🗑️: el mazo hereda la poda, no la contradice.
- Nunca leer PDFs/imágenes de `examenes/`; si hace falta evidencia, grepear
  `examenes/INDICE.md`.
- Fechas absolutas (AAAA-MM-DD); pie con fecha de generación y fuentes.
- Español rioplatense (voseo), preguntas directas tipo consigna de examen
  ("Enunciá…", "Demostrá…"), igual que el resto del repo.
- Scripts (si hicieran falta): `venv/bin/python tools/<script>.py`, con fallback
  `python tools/<script>.py`.
- Si `estrategia.md` o `que-saltear.md` se regeneran, el mazo puede quedar corto:
  re-correr esta skill agrega las cartas que falten (incremental).
