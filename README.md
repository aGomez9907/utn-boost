# utn-boost — tu sistema de estudio para la facultad

Un sistema **multi-materia** para preparar y aprobar **parciales y finales** con el
menor desperdicio de tiempo posible. Vos le tirás el material crudo de una materia
(videos de YouTube, PDFs de cátedra, fotos de apuntes, parciales viejos) y, a través de
comandos que corrés dentro de Claude Code, lo convierte en **apuntes prolijos**, un
**dataset consultable de exámenes** y una **estrategia de estudio** basada en lo que
realmente toman.

Nació para Análisis Matemático II y hoy sirve para cualquier materia: cada una vive en
su propia carpeta bajo `materias/`, con sus apuntes, sus exámenes indexados y su
estrategia.

> **Cómo se usa, en una frase:** abrís Claude Code en la raíz del repo y escribís
> comandos tipo `/apunte`, `/estrategia`, `/plan`. Cada comando es una *skill* que hace
> una parte del trabajo. No hace falta que sepas programar.

---

## La idea en 30 segundos: 3 capas

1. **Ingesta.** El material crudo se vuelve **apuntes Markdown** normalizados: teoría a
   la vista, cada ejercicio resuelto en un desplegable, todo en LaTeX, con índice
   navegable. Estudiás de un formato único y buscable en vez de saltar entre videos de
   2 horas, diapositivas y fotos sueltas.
2. **Dataset de exámenes.** Los parciales/finales reales se transcriben **una sola vez**
   a un `INDICE.md` con cada problema taggeado por tema. Después se consulta ese texto,
   nunca se releen las imágenes.
3. **Estrategia.** Se cruza *qué tan seguido cae cada tema* (capa 2) contra *qué tan
   bien lo cubren tus apuntes* (capa 1) para decidir **qué dominar, qué leer por arriba
   y qué saltear**. De ahí salen el plan de días, el banco de problemas, las flashcards
   y los simulacros.

> **Regla de oro:** la estrategia se arma con **evidencia** (las frecuencias reales de
> los exámenes), no con intuición. Y los apuntes salen **solo de la fuente**, sin
> contenido inventado.

---

## Walkthrough: de cero a rendir una materia

Arranca una materia nueva. Este es el recorrido completo — cada paso es un comando que
escribís en el chat de Claude Code. No tenés que hacerlos todos ni en orden estricto,
pero este es el flujo que rinde.

### 0. Dar de alta la materia — `/nueva-materia`

```
/nueva-materia
```

Crea la carpeta `materias/<tu-materia>/` con su `MATERIA.md` (la ficha de configuración:
evaluaciones, fechas, estructura del examen, leyenda de tags) y las subcarpetas de la
primera evaluación. **Lo primero que hacés después:** abrir ese `MATERIA.md` y completar
las fechas de los parciales/finales y de dónde sale el material.

### 1. Convertir el material en apuntes — `/apunte`, `/apuntes-batch`, `/apunte-doc`

Según de dónde venga el material:

```
/apunte https://youtube.com/watch?v=...           # un video suelto
/apuntes-batch <url1> <url2> <url3> ...            # una playlist entera, un apunte por video
/apunte-doc materias/<materia>/fuentes/guia.pdf    # PDF de cátedra, diapositivas, capítulo de libro
/apunte-doc materias/<materia>/fuentes/foto1.jpg foto2.jpg   # fotos de tus apuntes o del pizarrón
```

**Lo que obtenés:** un `.md` por unidad en `apuntes/md/`, con teoría en secciones
visibles, cada ejercicio en un desplegable y su resolución paso a paso en otro
desplegable anidado, todo en LaTeX. En `/apuntes-batch` cada video lo procesa un
subagente aparte, así no se degrada la calidad aunque sean muchos.

> **Para el iPad/GoodNotes:** cualquiera de estas skills puede exportar a HTML y PDF con
> las fórmulas ya renderizadas (ver [Puesta en marcha técnica](#puesta-en-marcha-técnica)).

### 2. Cargar los exámenes viejos — `/indexar-examenes`

Tirás los parciales/finales reales (PDFs o fotos) en `materias/<materia>/<evaluacion>/examenes/`
y corrés:

```
/indexar-examenes
```

**Lo que obtenés:** un `examenes/INDICE.md` donde cada problema es una línea con su
enunciado resumido y sus **tags** por tema. Este es el **único paso que "mira" las
imágenes** — de ahí en más todo el análisis se hace sobre este texto. Es lo que
convierte tus parciales en un dataset consultable.

### 3. Armar la estrategia — `/estrategia` y `/que-saltear`

```
/estrategia
/que-saltear
```

`/estrategia` cruza la frecuencia de cada tema (del `INDICE.md`) contra tus apuntes y
genera `estrategia.md`: **qué temas dominar** 🔴, cuáles son de prioridad alta 🟠 / media
🟡 / baja ⚪, las **brechas** (temas que caen seguido pero tus apuntes cubren flojo), un
**banco de problemas tipo** y un **checklist teórico**.

`/que-saltear` genera `que-saltear.md`: una poda sección por sección de cada apunte,
marcando 🗑️ saltear / 📖 leer por arriba / ✅ núcleo. Es tu mapa para no perder tiempo.

### 4. El plan de días — `/plan`

```
/plan
```

**Lo que obtenés:** `plan.md`, un cronograma de acá hasta el examen que reparte qué
estudiar cada día según los días que quedan, tu avance y los errores que fuiste
registrando. Es **recalculable**: lo volvés a correr cuando cambia el panorama (te
atrasaste, apareció un examen nuevo, dominaste un tema) y se reajusta.

### 5. Estudiar y registrar — `/registrar`

Después de cada sesión de práctica, contale cómo te fue:

```
/registrar hice el P3 del 2022-07-15, salió pero dudé la orientación; el teórico de Green no me salió
```

**Lo que obtenés:** una entrada en `registro.md` y un **tablero** que lleva la cuenta de
qué practicaste, cómo te fue y la tendencia por tema. Lo que fallás sube de prioridad;
lo que te sale, baja. El próximo `/plan` y la próxima `/estrategia` lo tienen en cuenta.

### 6. Repaso y simulacros — `/flashcards` y `/simulacro`

```
/flashcards      # mazo de repaso teórico desde el checklist
/simulacro       # un examen nuevo, fiel al patrón real, con corrección
```

`/flashcards` genera `flashcards.md` (desplegables pregunta/respuesta) y un
`flashcards-anki.tsv` importable a Anki. `/simulacro` arma un examen simulado que respeta
la estructura y las frecuencias reales, con su corrección desplegable — así practicás "a
reloj" sin quemar los parciales de verdad que te reservaste para el final.

---

## Todas las skills (referencia rápida)

Se invocan escribiendo `/nombre` en el chat. Todas funcionan en cualquier materia; si no
aclarás cuál, resuelven solas (la materia con estado `cursando` y la evaluación más
próxima por fecha) y te preguntan si hay ambigüedad.

### Ingesta de material

| Comando | Qué hace |
|---|---|
| `/apunte <url>` | Un video de YouTube → un apunte `.md` (+ HTML/PDF opcional). |
| `/apuntes-batch <urls…>` | Muchos videos → un apunte por video (un subagente c/u, sin perder calidad). |
| `/apunte-doc <ruta.pdf\|fotos>` | PDF de cátedra, diapositivas, capítulo de libro o fotos → apunte `.md`. |

### Exámenes y análisis

| Comando | Qué hace |
|---|---|
| `/indexar-examenes` | Parciales/finales nuevos (PDF/foto) → entradas en `examenes/INDICE.md` con tags. *Único paso que "lee" las imágenes.* |
| `/estrategia` | Genera/actualiza `estrategia.md`: frecuencias por tema, brechas, banco de problemas, checklist teórico. |
| `/que-saltear` | Genera `que-saltear.md`: poda sección por sección (🗑️ saltear / 📖 por arriba / ✅ núcleo). |

### Preparación y práctica

| Comando | Qué hace |
|---|---|
| `/plan` | (Re)calcula `plan.md`: qué estudiar cada día hasta el examen, según días restantes + tus errores. |
| `/simulacro` | Examen simulado nuevo, fiel al patrón real, con corrección desplegable. |
| `/flashcards` | Mazo de repaso teórico: `flashcards.md` + `flashcards-anki.tsv` (importable a Anki). |
| `/registrar <lo que hiciste>` | Anota una sesión de práctica y tus errores; alimenta a `/plan` y `/estrategia`. |

### Organización

| Comando | Qué hace |
|---|---|
| `/nueva-materia` | Da de alta una materia nueva: crea carpetas + `MATERIA.md` desde plantilla. |

---

## Las reglas que hacen que funcione (los "no")

- **No se releen** los PDFs/fotos de `examenes/`: para analizar se usa siempre el
  `INDICE.md`. Ahorra tiempo y plata (leer imágenes es caro y lento).
- **No se inventa nada:** los apuntes salen únicamente de la fuente. Lo que no se
  entiende se marca `[poco claro…]` / `[ilegible]`, no se completa a ojo.
- Los archivos **generados** (`estrategia.md`, `plan.md`, simulacros, flashcards) **se
  regeneran** con su skill; no los editás a mano salvo un retoque puntual.
- **Fechas siempre absolutas** (AAAA-MM-DD) y todo **versionado en git**: el historial es
  el respaldo si algo se pisa.

---

## Cómo se organiza en el disco

```
materias/<materia>/
  MATERIA.md                  ← config: evaluaciones, fechas, estructura del examen, tags
  fuentes/                    ← material crudo: PDFs de cátedra, libros, fotos
  <evaluacion>/               ← p. ej. segundo-parcial/, final/
    apuntes/
      md/                     ← apuntes fuente (.md) — la verdad canónica
      html/  pdf/             ← exports regenerables (para leer/compartir/iPad)
      transcripts/            ← JSON de transcripciones cacheadas
    examenes/                 ← parciales reales + INDICE.md (transcripción + tags)
    simulacros/               ← exámenes simulados generados
    estrategia.md             ← frecuencias + brechas + banco + checklist
    que-saltear.md            ← poda por apunte
    plan.md                   ← cronograma de días
    registro.md               ← tu práctica y errores
    flashcards.md (+ .tsv)    ← mazo de repaso
```

En la raíz del repo: `CLAUDE.md` (las instrucciones internas que sigue Claude),
`tools/` (scripts de Python), `plantillas/` (plantillas para materias nuevas) y `venv/`
(entorno de Python para los scripts).

---

## Puesta en marcha técnica

El entorno de Python (`venv/`) solo hace falta para los scripts de `tools/`
(transcripciones y exports). Para usar las skills desde Claude Code no necesitás nada
más.

```bash
python -m venv venv
source venv/bin/activate           # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Export a HTML/PDF — `tools/md_to_html.py`

Convierte un apunte `.md` a `.html` con las fórmulas LaTeX renderizadas (markdown-it +
KaTeX). Renderiza bien los `<details>` anidados.

```bash
venv/bin/python tools/md_to_html.py materias/<materia>/<evaluacion>/apuntes/md/01-clase.md
```

**PDF para iPad / GoodNotes / compartir (`--pdf`):** el `.html` no sirve en el iPad
(WhatsApp/Files lo previsualizan sin ejecutar JS y se queda en "Renderizando…"). El flag
`--pdf` renderiza con Chrome headless local y deja la matemática horneada, así el PDF se
abre en cualquier lado sin JS ni internet. Necesita Chrome instalado (o la variable
`CHROME_PATH`); en el PDF los `<details>` salen **expandidos** (para el modo "tapá la
respuesta", usá el `.html` en la compu).

```bash
venv/bin/python tools/md_to_html.py materias/.../apuntes/md/01-clase.md --pdf
```

### Rate-limit de YouTube

Bajá las transcripciones **de a una, con pausa**. Si aparece `IpBlocked` /
`RequestBlocked` (típico en IPs de nube), usá `tools/fetch_transcripts.py` desde una IP
residencial (editando su lista `REMAINING`).

### API key de Gemini (LEGACY)

El `.env` con `GEMINI_API_KEY` solo lo usa `tools/extract_notes.py`, el pipeline original
que procesaba las transcripciones con Gemini. **Ya no se usa** — hoy Claude genera los
apuntes directamente vía las skills. El script queda como referencia de los prompts
originales; no configures la key salvo que quieras revivirlo.

---

## Versionado

Todo el material se versiona en git: apuntes, índices de exámenes, estrategias, planes y
registros. Los archivos generados se regeneran con su skill, no se editan a mano; el
historial de git es el respaldo si algo se pisa. Commiteá seguido — cada tanda de apuntes
o cada examen nuevo indexado es un buen punto para guardar.
