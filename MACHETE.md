# 🥷 Machete del sistema de estudio

Referencia rápida. Para el detalle completo mirá [CLAUDE.md](CLAUDE.md) (cómo opera Claude) y [README.md](README.md).

---

## Qué hace el sistema (3 capas)

1. **Ingesta** → material crudo (videos, PDFs, libros, fotos) se vuelve **apuntes .md** normalizados: teoría visible + ejercicios resueltos en desplegables, todo en LaTeX.
2. **Dataset de exámenes** → los parciales reales se transcriben **una vez** a un `INDICE.md` con tags por tema. Después se busca ahí (grep), nunca se releen las imágenes.
3. **Estrategia** → se cruza la frecuencia histórica de cada tema contra tus apuntes para decidir **qué dominar, qué leer por arriba y qué saltear**. De ahí salen plan, simulacros y flashcards.

> **Regla de oro:** la estrategia se arma con evidencia (frecuencias reales), no con intuición. Los apuntes salen solo de la fuente, sin inventar.

---

## Las 11 herramientas (skills)

Se invocan escribiendo `/nombre` en el chat. Todas se pueden usar en cualquier materia.

### Ingesta de material
| Comando | Qué hace |
|---|---|
| `/apunte <url-youtube>` | Un video → un apunte .md (+ HTML/PDF con `--pdf`). |
| `/apuntes-batch <urls…>` | Muchos videos → un apunte por video (un subagente c/u, sin perder calidad). |
| `/apunte-doc <ruta.pdf\|fotos>` | PDF de cátedra, diapositivas, capítulo de libro o fotos → apunte .md con el mismo formato. |

### Exámenes y análisis
| Comando | Qué hace |
|---|---|
| `/indexar-examenes` | Parciales nuevos (PDF/foto) → entradas en `examenes/INDICE.md` con tags. *Único paso que "lee" las imágenes.* |
| `/estrategia` | Genera/actualiza `estrategia.md`: frecuencias por tema, brechas, banco de problemas, checklist teórico. |
| `/que-saltear` | Genera `que-saltear.md`: poda sección por sección (🗑️ saltear / 📖 por arriba / ✅ núcleo). |

### Preparación y práctica
| Comando | Qué hace |
|---|---|
| `/plan` | (Re)calcula `plan.md`: qué estudiar cada día hasta el examen, según días restantes + tus errores. |
| `/simulacro` | Examen simulado nuevo, fiel al patrón real, con corrección desplegable. No quema los exámenes reservados "a ciegas". |
| `/flashcards` | Mazo de repaso teórico: `flashcards.md` (desplegable) + `flashcards-anki.tsv` (importable a Anki). |
| `/registrar` | Anota una sesión de práctica y tus errores; alimenta a `/plan` y `/estrategia`. |

### Organización
| Comando | Qué hace |
|---|---|
| `/nueva-materia` | Da de alta una materia nueva: crea carpetas + `MATERIA.md` desde plantilla. |

---

## Flujo típico de una evaluación nueva

```
/nueva-materia                    (una sola vez por materia)
        ↓
/apuntes-batch  ó  /apunte-doc    (generar apuntes del temario)
        ↓
/indexar-examenes                 (cargar los parciales viejos)
        ↓
/estrategia  →  /que-saltear      (qué cae, qué estudiar)
        ↓
/plan                             (cronograma de días)
        ↓
estudiar  +  /registrar           (practicar y anotar errores)
        ↓
/flashcards   (teoría)   +   /simulacro   (últimos días, con reloj)
        ↓
/plan   otra vez si algo cambió
```

---

## Reglas que protegen el sistema (los "no")

- **No se releen** los PDFs/fotos de `examenes/`: para analizar se usa el `INDICE.md`. (Ahorra tokens y es más rápido.)
- **No se inventa**: los apuntes salen solo de la fuente; lo dudoso se marca `[poco claro…]` / `[ilegible]`.
- Los archivos generados (estrategia, plan, simulacros, flashcards) **se regeneran** con su skill; no los editás a mano salvo un retoque puntual.
- Fechas siempre absolutas (AAAA-MM-DD). Todo va versionado en git.

---

## Comandos técnicos (`tools/`)

```bash
venv/bin/python tools/dump_transcript.py "<url>"        # bajar transcripción de YouTube
venv/bin/python tools/md_to_html.py <apunte.md>         # exportar a HTML (KaTeX)
venv/bin/python tools/md_to_html.py <apunte.md> --pdf   # exportar a PDF (iPad/GoodNotes)
```

- El `.env` con la key de Gemini es **legacy**: ya no hace falta (Claude genera los apuntes). Solo lo usa `tools/extract_notes.py`, que quedó de referencia.
- Rate-limit de YouTube: bajá transcripciones de a una con pausa; si te bloquea, usá `tools/fetch_transcripts.py` desde tu red de casa.

---

## Dónde está cada cosa

```
materias/<materia>/
  MATERIA.md                  ← config: evaluaciones, fechas, estructura del examen
  fuentes/                    ← PDFs de cátedra, libros, fotos (material crudo)
  <evaluacion>/               ← p. ej. segundo-parcial/
    apuntes/md|html|pdf/      ← apuntes (el .md manda; html/pdf se regeneran)
    examenes/INDICE.md        ← transcripción curada + tags de los parciales reales
    simulacros/               ← exámenes simulados generados
    estrategia.md             ← frecuencias + brechas + banco + checklist
    que-saltear.md            ← poda por apunte
    plan.md                   ← cronograma de días
    registro.md               ← tu práctica y errores
    flashcards.md + .tsv      ← mazo de repaso
```

> **Nota:** hoy tenés una sola materia (AM2), así que las skills la resuelven solas. Cuando tengas varias, o le pasás la ruta o te pregunta cuál.

---

*Machete generado el 2026-07-06. Regenerable a mano; si agregás una skill, sumala a la tabla.*
