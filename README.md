# AM2-transcripts

Extrae apuntes de **Análisis Matemático II** desde videos de YouTube: descarga la
transcripción (incluso autogenerada), la procesa con Gemini y guarda un apunte en
Markdown listo para estudiar (definiciones, teoremas y fórmulas en LaTeX).

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración

Pegá tu API key de Gemini en un archivo `.env` (Google AI Studio:
<https://aistudio.google.com/apikey>):

```bash
cp .env.example .env
# editá .env y completá GEMINI_API_KEY=...
```

> El `.env` está en `.gitignore`, así que tu clave no se sube a git.

## Uso

```bash
python extract_notes.py "https://www.youtube.com/watch?v=XXXXXXXXXXX"
```

El apunte queda en `./apuntes/titulo-del-video.md`, encabezado por un **Índice
navegable**: cada tema enlaza al minuto exacto del video (`...&t=123s`), así saltás
directo en vez de mirar la clase entera de forma lineal.

### Opciones

| Flag         | Descripción                                          | Default    |
| ------------ | ---------------------------------------------------- | ---------- |
| `--out-dir`  | Carpeta donde guardar el `.md`                       | `apuntes`  |
| `--lang`     | Idiomas preferidos de la transcripción, en orden     | `es es-419 en` |
| `--no-index` | No generar el índice con enlaces a los timestamps    | (índice activado) |
| `--practice` | Generar además `…-practica.md` aparte con los ejercicios | (desactivado) |
| `--consolidated` | Un único `.md` (una sola pasada): teoría visible + ejercicios desplegables | (desactivado) |

### Consolidado (`--consolidated`)

Genera **un solo archivo** en **una sola llamada** a Gemini: la teoría queda visible
arriba, y abajo cada ejercicio va en un bloque desplegable (`<details>`) con su
resolución en otro bloque desplegable anidado, para que primero leas el enunciado,
lo intentes, y recién después abras la solución. Mitad de costo que `--practice` y un
único `.md`.

```bash
python extract_notes.py "https://youtu.be/XXXXXXXXXXX" --consolidated
```

### Práctica (`--practice`)

Hace una **segunda pasada** sobre la misma transcripción y extrae *solo los ejercicios
que el profesor resuelve* (no inventa ejercicios). Cada uno sale con su enunciado y la
resolución dentro de un bloque colapsable (`<details>`), para que la intentes vos antes
de espiar. Como la transcripción es solo audio, los pasos que quedaron en el pizarrón se
marcan `[paso en el pizarrón, ver video]` — ahí mirás tu screenshot o el minuto enlazado.

```bash
python extract_notes.py "https://youtu.be/XXXXXXXXXXX" --practice
```

Ejemplo:

```bash
python extract_notes.py "https://youtu.be/XXXXXXXXXXX" --out-dir apuntes/parciales --lang es en
```

## Exportar a HTML con LaTeX renderizado

`md_to_html.py` convierte los apuntes `.md` a `.html` con las fórmulas renderizadas.
No necesita pandoc ni paquetes de pip: usa markdown-it + KaTeX desde CDN.

```bash
python md_to_html.py apuntes/clase.md        # un archivo
python md_to_html.py apuntes                 # todos los .md de la carpeta
python md_to_html.py apuntes/*.md --out-dir html
```

Renderiza bien los `<details>` (anidados incluidos) y el LaTeX (`$…$`, `$$…$$`,
matrices, etc.). Como el render ocurre en el navegador, hace falta conexión a internet
la primera vez que abrís el `.html`.

### PDF para iPad / GoodNotes / compartir (`--pdf`)

El `.html` **no** sirve para abrir en el iPad (WhatsApp/Files lo previsualizan sin
ejecutar JS, así que se queda en "Renderizando…"). Para eso generá un **PDF**: se
renderiza acá en la Mac con Chrome headless y queda estático (math horneada), así se
abre en cualquier lado sin JS ni internet.

```bash
python md_to_html.py apuntes/clase.md --pdf
```

En el PDF los `<details>` salen **expandidos** (no se pueden desplegar en un PDF), o sea
muestra todo: teoría, enunciados y resoluciones. Necesita Chrome (o seteá `CHROME_PATH`).
El `.html` interactivo seguilo usando en la compu para el modo "tapá la respuesta".

## Modelo

Usa `gemini-2.5-pro` (constante `MODEL` en `extract_notes.py`). Para lotes grandes
y más baratos, cambialo por `gemini-2.5-flash`.
