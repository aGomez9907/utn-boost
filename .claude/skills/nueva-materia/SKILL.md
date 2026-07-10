---
name: nueva-materia
description: Scaffolding completo de una materia nueva en el sistema de estudio. Crea el árbol de carpetas (fuentes/, una carpeta por evaluación con apuntes/examenes/simulacros), genera MATERIA.md y un registro.md por evaluación desde las plantillas, y deja todo listo para ingestar material. Úsala cuando el usuario diga que empieza a cursar una materia nueva, quiera dar de alta / agregar / inicializar una materia en el repo, o cuando invoque /nueva-materia.
---

# nueva-materia

Da de alta una materia nueva en `materias/`: carpetas, `MATERIA.md` (la config que todas
las demás skills leen primero) y un `registro.md` por evaluación. No genera contenido de
estudio — para eso están `/apunte`, `/apuntes-batch`, `/apunte-doc` e `/indexar-examenes`
después. El objetivo es que al terminar, cualquier skill del sistema pueda trabajar sobre
la materia sin configuración extra.

## Entrada / argumentos

Invocación: `/nueva-materia [datos de la materia en texto libre]`

| Argumento | Efecto | Default |
|---|---|---|
| Texto libre | Parsear de ahí todo lo que se pueda (nombre, slug, evaluaciones, fechas, fuentes). | — |
| _(sin argumentos)_ | Recolectar todo preguntando (paso 1). | — |

## Datos necesarios

Antes de crear nada tenés que tener estos datos. Lo que no venga en el argumento se
pregunta con **AskUserQuestion, de a UNA tanda por vez** (nunca un interrogatorio de diez
preguntas sueltas ni una sola pregunta gigante). Tandas sugeridas:

1. **Identidad**: nombre completo, alias corto (p. ej. _"Análisis Matemático II" / "AM2"_,
   como ejemplo), y slug `kebab-case` (proponelo vos desde el nombre — minúsculas, sin
   acentos ni "ñ", guiones — y pedí confirmación). Estado: casi siempre `cursando`.
2. **Evaluaciones**: cuáles son (parciales, final, recuperatorios…) y sus **fechas
   absolutas AAAA-MM-DD**, las que se sepan. Las que no se saben quedan `_(a definir)_`.
   Cada evaluación tiene su slug `kebab-case` (p. ej. `primer-parcial`, `final`).
3. **Estructura del examen y fuentes**: si se conoce, cuántos problemas prácticos y
   teóricos tiene cada examen y su duración; y las fuentes principales — canal/playlist
   de YouTube, PDFs de cátedra, libros, exámenes viejos que ya tenga.

No bloquees el alta por datos faltantes: con nombre, slug y al menos una evaluación
alcanza. Todo lo demás puede quedar `_(completar)_`.

## Pasos

### 1. Recolectar datos
- Parseá el argumento (si lo hay) y completá los huecos con AskUserQuestion según las
  tandas de arriba. Solo preguntá lo que falte.
- Verificá que `materias/<slug>/` **no exista ya**. Si existe, avisá y preguntá si el
  usuario quiere completar lo que falte (modo reparación: crear solo carpetas/archivos
  ausentes, sin pisar nada) o abortar.
- **Estado `cursando`**: la resolución de contexto de `CLAUDE.md` asume UNA sola materia
  con `estado: cursando`. Si ya hay otra materia cursando (grepeá `estado` en los
  `MATERIA.md` existentes), avisá que van a convivir varias y que las skills van a
  preguntar cuál usar cuando no se dé la ruta explícita.

### 2. Crear el árbol de carpetas
- `materias/<slug>/fuentes/` con un `.gitkeep`.
- Por **cada evaluación** declarada:

```
materias/<slug>/<eval>/
  apuntes/
    md/           ← .gitkeep
    html/         ← .gitkeep
    pdf/          ← .gitkeep
    transcripts/  ← .gitkeep
  examenes/       ← .gitkeep
  simulacros/     ← .gitkeep
  repaso/         ← .gitkeep  (flashcards + machete)
  exports/        ← .gitkeep  (html/pdf regenerables de los docs de la evaluación)
```

- El `.gitkeep` va en cada hoja vacía para que git conserve la estructura. Crealo todo
  con `mkdir -p` + `touch` en un solo comando por evaluación.

### 3. Generar `MATERIA.md`
- Partí de `plantillas/MATERIA.md`: leéla y completala con los datos recolectados. Lo
  que no se sepa queda literal `_(completar)_` (o `_(a definir)_` en fechas), nunca
  inventado ni borrado de la plantilla.
- Si la plantilla no existiera todavía, generá el archivo con estas secciones (es el
  contrato que las demás skills esperan): título `# <Nombre completo> (<alias>)`;
  metadatos en lista (`Slug`, `Estado`, `Año/cuatrimestre`, `Carrera/facultad`);
  `## Evaluaciones` (tabla Evaluación | Carpeta | Fecha | Estado, marcando la próxima);
  `## Estructura del examen`; `## Temario por evaluación`; `## Fuentes`;
  `## Leyenda de tags (para examenes/INDICE.md)`; `## Estado del material` (tabla
  Evaluación | Apuntes | INDICE | Estrategia | Poda | Plan | Registro | Flashcards |
  Machete | Simulacros, todo en `—`/pendiente al arrancar).
- **Leyenda de tags: arranca VACÍA**, con esta nota (o equivalente): _"Se define al
  indexar los primeros exámenes: `/indexar-examenes` la va construyendo con tags
  `#CamelCase` a medida que aparecen los temas reales."_ No inventes tags a priori: la
  leyenda sale de la evidencia (los exámenes), no de la intuición.

### 4. Generar `registro.md` por evaluación
- Por cada evaluación, creá `materias/<slug>/<eval>/registro.md` desde
  `plantillas/registro.md`, completando materia/evaluación/fecha y dejando el resto
  (tablero, sesiones) vacío tal como lo trae la plantilla.
- Si la plantilla no existiera, creá un registro mínimo: `# Registro — <evaluación>
  (<materia>)`, un tablero de errores por tema (tabla vacía) y una sección
  `## Sesiones` vacía. `/registrar` lo va llenando.
- Los demás archivos generables (`estrategia.md`, `que-saltear.md`, `plan.md`,
  `repaso/flashcards.md`, `repaso/machete.md`, `INDICE.md`) **NO se crean acá**: los
  generan sus skills cuando haya material. No dejes esqueletos vacíos que después
  confundan.

### 5. Cierre
- Mostrá el árbol creado (`find materias/<slug> -type f -o -type d | sort` o similar,
  formateado como árbol).
- Sugerí los **próximos pasos según las fuentes declaradas**:
  - Videos de YouTube (canal/playlist) → `/apuntes-batch` con la lista de links
    (o `/apunte` para uno solo).
  - PDFs de cátedra / libros / fotos → copiarlos a `materias/<slug>/fuentes/` y correr
    `/apunte-doc`.
  - Exámenes viejos ya disponibles → ponerlos en `<eval>/examenes/` y correr
    `/indexar-examenes` (eso además construye la leyenda de tags).
  - Y recordá el flujo completo: apuntes → índice → `/estrategia` → `/que-saltear` →
    `/plan`.
- Commiteá con mensaje en español describiendo el alta (p. ej.
  `Alta de <materia>: estructura, MATERIA.md y registros`), salvo que el usuario pida
  no commitear.

## Reglas

- **Español rioplatense** (voseo) en todo lo generado, como el resto del repo.
- **Fechas absolutas** (AAAA-MM-DD) en `MATERIA.md` y en los registros. Fecha
  desconocida = `_(a definir)_`, nunca una fecha inventada.
- **Slugs `kebab-case`** para materia y evaluaciones: minúsculas, sin acentos, guiones.
- **No inventar contenido**: ni tags, ni temario, ni estructura de examen que el usuario
  no haya dado. Hueco = `_(completar)_`.
- No pises archivos existentes: si algo ya está, se completa lo que falta o se pregunta.
- Esta skill normalmente no necesita scripts, pero si hiciera falta alguno del repo,
  corrélo con `venv/bin/python tools/<script>.py` (fallback `python tools/<script>.py`).

## Notas

- La **resolución de contexto** de `CLAUDE.md` (materia = la única `cursando`,
  evaluación = la próxima por fecha) es lo que hace que las demás skills funcionen sin
  ruta explícita: por eso importa dejar bien puestos `estado:` y las fechas de la tabla
  de evaluaciones.
- `materias/analisis-matematico-2/MATERIA.md` sirve como **ejemplo real** de una materia
  ya poblada (es solo un ejemplo: no copies su contenido, solo su forma).
- Si más adelante aparece una evaluación nueva (recuperatorio, final con fecha), se puede
  volver a invocar `/nueva-materia` en modo reparación para crear solo esa carpeta y su
  `registro.md`, y actualizar la tabla de `MATERIA.md`.
