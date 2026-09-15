# Índice de parciales — Primer Parcial · Administración Gerencial (UTN.BA)

> **Para qué sirve:** los parciales de esta materia no llegaron como hojas de examen sueltas
> sino como **compilados armados por alumnos**: un `.docx` con las preguntas de 7 hojas
> fechadas (2013–2019) **y sus respuestas**, un `.md` con 5 juegos de preguntas sin fecha y
> una foto de WhatsApp de un parcial reciente. Este archivo es la **única representación
> textual** del dataset: cada pregunta transcripta tal cual, con **tags por tema**. Para
> cualquier análisis (frecuencias, brechas, simulacros) se grepea **este archivo**, nunca se
> re-leen el docx ni la foto.
>
> **Cómo buscar** (desde `examenes/`):
> ```bash
> grep -n "#Maslow" INDICE.md                 # todas las preguntas de Maslow
> grep -n "#Mintzberg" INDICE.md              # cualquier esfera de Mintzberg
> grep -n "#LiderazgoSituacional" INDICE.md   # situacional (casi siempre con "¿es contingente?")
> grep -n "^## " INDICE.md                    # listar las 12 hojas de examen
> grep -n "RECICLADO" INDICE.md               # preguntas repetidas entre fechas
> grep -n "✅ resp" INDICE.md                 # preguntas que tienen respuesta en el compilado
> ```
> **Mantenimiento:** al agregar un parcial nuevo, sumá su sección con los mismos tags y
> actualizá las tablas del final. Si una pregunta ya está indexada, marcala `[RECICLADO]`.

## Cómo está armado el dataset

- **Unidad de conteo = hoja de examen.** En una misma fecha la cátedra toma varios
  **temas** (Tema 1 / Tema 2 / "otro tema") con preguntas distintas del mismo pool; acá
  cada tema es una sección propia porque son preguntas distintas para practicar: **12
  hojas** de **9 instancias**. Los porcentajes de `estrategia.md` se calculan sobre las 12
  hojas.
- **Hojas incompletas.** Varias hojas del compilado registran solo las preguntas que el
  alumno se acordó o quiso responder (2013: 3 de 5; recuperatorio 2015: 3 de 5; 201?-09-26:
  3 de 5; 2018 Tema A: 3; 2018 "otro tema": 4; juego C: 2). Se anota `(n de 5
  registradas)` en el encabezado. Eso **subestima** la frecuencia de todos los temas por
  igual: hay que leer las frecuencias como piso.
- **Formato del examen:** 5 preguntas teóricas a desarrollar, numeradas 1–5. Se
  transcriben como `- **Pn)** enunciado → #Tag` (P = "pregunta", no "práctico": acá no hay
  práctica). Si la pregunta tiene respuesta escrita en el compilado se marca `✅ resp.`;
  esas respuestas (y las de `../../fuentes/respuestas-finales-por-unidad.docx`) son el
  material de estudio.
- **Archivos:** `2013-2019_compilado-preguntas-respuestas.docx` (7 hojas fechadas, con
  respuestas), `sin-fecha_compilado-preguntas.md` (5 juegos de preguntas: A, B, C, D, E;
  B, D y E resultaron ser las versiones completas de los tres temas del 2014-05-06) y
  `sin-fecha_Parcial.jpg` (foto tipeada, 5 preguntas; la foto es de WhatsApp del
  2024-10-27, así que el parcial es probablemente del 2C 2024).
- **Docentes que aparecen:** Daniel Texido (2014, 201?-09-26) y Gastón Paccor (recuperatorio
  2015). Las hojas 2018 y 2019 no traen nombre.

## Leyenda de tags

**Paradigmas de dirección (unidad II):** `#Mecanicismo` `#Organicismo` `#Contingencia`

**Cultura (unidad III):** `#Cultura` (paraguas) `#ImportanciaCultura` `#CulturaFormalInformal`
`#Subculturas` `#CulturaFuerteDebil` `#GruposPrimarios` `#Pertenencia`

**Gerente (unidades IV–VI):** `#Sallenave` `#Mintzberg` (paraguas) `#MintzbergInterpersonal`
`#MintzbergInformacional` `#MintzbergDecisional` `#HabilidadesGerente` `#Negociacion`

**Liderazgo (unidad VII):** `#Liderazgo` (paraguas) `#FenomenoLiderazgo`
`#ContinuoAutocraticoDemocratico` `#TeoriaRasgos` `#TeoriasContingentes`
`#LiderazgoSituacional` `#RutaMeta`

**Motivación (unidad VIII):** `#Maslow` `#Herzberg`

**Comunicación (unidad IX):** `#FormasComunicacion` `#ClasificacionComunicacion` `#EscuchaActiva`

> Convención: `- **Pn)** enunciado → #TagPrincipal #TagSecundario`. Los paraguas
> `#Cultura`, `#Mintzberg` y `#Liderazgo` van SIEMPRE junto al tag específico, para poder
> contar el bloque entero con un solo grep. Enunciados copiados tal cual del compilado
> (errores de tipeo corregidos, redacción intacta). «≈» marca una lectura dudosa.

---

## 2013-05-07  ·  compilado docx («1er Parcial 07/05/2013»)  ·  (3 de 5 registradas)

- **P1)** Explique y detalle la Pertenencia, la Identificación y la Implicación. ✅ resp. → #Pertenencia #Cultura
- **P2)** Cuáles son las formas de comunicación. Explicar. ✅ resp. (oral, escrita, no verbal, medios electrónicos) → #FormasComunicacion
- **P3)** Explique características de la Teoría de Rasgos. Indique por qué no alcanza con esta teoría. ✅ resp. → #TeoriaRasgos #Liderazgo

## 2014-05-06  ·  compilado docx («Parcial Texido 06/05/2014») + juego D del `.md`  ·  Tema A

> El docx trae solo P2–P4 con respuesta; el juego D del `sin-fecha_compilado-preguntas.md`
> tiene exactamente esas tres preguntas con la misma redacción más P1 y P5: es la hoja
> completa.

- **P1)** Teoría situacional del liderazgo. ¿Es de contingencia? **[RECICLADO]** → #LiderazgoSituacional #TeoriasContingentes #Liderazgo
- **P2)** Clasificaciones de la comunicación. ✅ resp. (formal / informal) → #ClasificacionComunicacion
- **P3)** Culturas fuertes y débiles. Relación con paradigmas (mecanicista y organicista). ✅ resp. → #CulturaFuerteDebil #Cultura
- **P4)** Papeles de la esfera decisional según Mintzberg. ✅ resp. **[RECICLADO]** → #MintzbergDecisional #Mintzberg
- **P5)** Estrategias básicas de negociación (distributiva e integradora). **[RECICLADO]** → #Negociacion

## 2014-05-06  ·  compilado docx («Tema 2») + juego E del `.md`  ·  Tema 2

> ⚠ En el docx «Tema 2» y «Tema 1» aparecen a continuación del 06/05/2014 sin fecha propia;
> se asumen de la misma instancia. El juego E del `.md` es la hoja completa (P1 idéntica).

- **P1)** Taylorismo. En qué se basó. Cuáles eran sus principales características, etc. ✅ resp. → #Mecanicismo
- **P2)** Habilidades que tiene que tener el gerente. Explicarlas como sería en el nivel organizacional. **[RECICLADO]** → #HabilidadesGerente
- **P3)** Por qué es importante conocer la cultura de una organización. **[RECICLADO]** → #ImportanciaCultura #Cultura
- **P4)** Liderazgo. Por qué son importantes las teorías contingentes. Teoría de la Ruta-Meta. **[RECICLADO]** → #RutaMeta #TeoriasContingentes #Liderazgo
- **P5)** Describir la esfera Informacional de la teoría de Mintzberg. **[RECICLADO]** → #MintzbergInformacional #Mintzberg

## 2014-05-06  ·  compilado docx («Tema 1») + juego B del `.md`  ·  Tema 1

> El docx trae P1 y P4 con respuesta; el juego B del `.md` es la hoja completa.

- **P1)** Explicar el campo de acción y papeles básicos del gerente según Sallenave. ✅ resp. **[RECICLADO]** → #Sallenave
- **P2)** Explicar la pirámide de necesidades de Maslow, aclarando cada nivel qué es y qué sucede cuando se supera un nivel (o sea, cuando estás en un nivel y pasás al siguiente). **[RECICLADO]** → #Maslow
- **P3)** Liderazgo: explicar la teoría situacional de liderazgo, fundamentos, y si es contingente y por qué. **[RECICLADO]** → #LiderazgoSituacional #TeoriasContingentes #Liderazgo
- **P4)** Definición de cultura clásica. Explicar qué representan los grupos primarios y secundarios. ✅ resp. **[RECICLADO]** → #GruposPrimarios #Cultura
- **P5)** Explique los 3 papeles según Mintzberg que desarrolla un gerente en su rol informacional. **[RECICLADO]** → #MintzbergInformacional #Mintzberg

## 2015-11-19  ·  compilado docx («1er Parcial Recuperatorio 19-11-2015 Gastón Paccor»)  ·  (3 de 5 registradas)

- **P2)** Entre los paradigmas conocidos para la dirección de las organizaciones aparece el "Organicismo". ¿Cuáles son las críticas que se le hacen a dicho paradigma? ✅ resp. **[RECICLADO]** (gemela de la P4 del 201?-09-26 sobre mecanicismo) → #Organicismo
- **P3)** Liderazgo: continuo autocrático-democrático. ✅ resp. (autócrata / demócrata / paternalista) → #ContinuoAutocraticoDemocratico #Liderazgo
- **P4)** Motivación según Herzberg. ✅ resp. → #Herzberg

## 201?-09-26  ·  compilado docx («1er Parcial 26-09-201 Texido»)  ·  ⚠ año incompleto en el compilado  ·  (3 de 5 registradas)

> Es de un 2do cuatrimestre (septiembre) de la década de 2010, con Texido (que toma también
> en 2014). Por el orden del docx podría ser 2013 o 2015–2017; no hay más pistas.

- **P2)** Jerarquía de las necesidades y escala motivacional: describa la teoría de Maslow indicando cada una de las escalas, y explicando qué pasa con cada una de ellas cuando es satisfecha. **[RECICLADO]** → #Maslow
- **P3)** ¿Cómo se genera o se produce el fenómeno del Liderazgo? Describa brevemente los tipos elementales de Liderazgo más conocidos. ✅ resp. → #FenomenoLiderazgo #Liderazgo
- **P4)** Entre los paradigmas conocidos para la dirección de las organizaciones aparece el "Mecanicismo". ¿Cuáles son las críticas que se le hacen a dicho paradigma? ✅ resp. **[RECICLADO]** → #Mecanicismo

## 2018-05-02  ·  compilado docx («02/05/18»)  ·  Tema A  ·  (3 registradas)

- **P1)** Desarrolle sistemas culturales formales. ¿Qué son las subculturas? ✅ resp. **[RECICLADO]** → #CulturaFormalInformal #Subculturas #Cultura
- **P2)** Según Sallenave: ¿cuál es el ámbito de acción del gerente general? ✅ resp. **[RECICLADO]** → #Sallenave
- **P3)** Explique la teoría de liderazgo situacional. ✅ resp. **[RECICLADO]** → #LiderazgoSituacional #Liderazgo

## 2018-05-02  ·  compilado docx («02/05/18 Otro tema»)  ·  Tema B  ·  (4 registradas)

- **P1)** Desarrolle sistemas culturales informales. ¿Por qué surgen las subculturas? ✅ resp. **[RECICLADO]** (gemela de la P1 del Tema A) → #CulturaFormalInformal #Subculturas #Cultura
- **P2)** Según Mintzberg: ¿cuáles son los roles de la esfera de actuación decisional? ✅ resp. (la respuesta describe las tres esferas) **[RECICLADO]** → #MintzbergDecisional #Mintzberg
- **P3)** Explique la teoría de liderazgo ruta-meta. ✅ resp. (4 comportamientos) **[RECICLADO]** → #RutaMeta #Liderazgo
- **P4)** Motivación: explique la teoría de Maslow. ✅ resp. **[RECICLADO]** → #Maslow

## 2019-05-14  ·  compilado docx («14/05/19»)

- **P1)** Desarrolle la teoría de la contingencia aplicada a la dirección de las organizaciones. ✅ resp. → #Contingencia
- **P2)** Desarrolle los papeles de los gerentes, según H. Mintzberg, en su esfera de la actuación interpersonal. ✅ resp. **[RECICLADO]** → #MintzbergInterpersonal #Mintzberg
- **P3)** Describa la teoría de liderazgo situacional. ✅ resp. (dirigir / instruir / apoyar / delegar) **[RECICLADO]** → #LiderazgoSituacional #Liderazgo
- **P4)** Desarrolle los conceptos de grupo primario y secundario. ✅ resp. **[RECICLADO]** → #GruposPrimarios #Cultura
- **P5)** Detalle las distintas estrategias de negociación vistas en clase. ✅ resp. (Robbins y Coulter: distributiva / integradora; Rique: competitiva / cooperativa / integradora) **[RECICLADO]** → #Negociacion

## sin fecha (juego A)  ·  `sin-fecha_compilado-preguntas.md` («1er Parcial:»)  ·  ⚠ sin pistas de fecha

- **P1)** Características del organicismo: describa cuatro elementos pertenecientes al modelo organicista estudiados en la materia (delegación de autoridad, etc.). **[RECICLADO]** → #Organicismo
- **P2)** ¿En qué consiste la Teoría situacional? ¿Por qué se la considera una teoría contingente? **[RECICLADO]** → #LiderazgoSituacional #TeoriasContingentes #Liderazgo
- **P3)** Según Sallenave, ¿cuál es el campo de acción del gerente general? **[RECICLADO]** → #Sallenave
- **P4)** Describa la teoría de la motivación de Maslow. **[RECICLADO]** → #Maslow
- **P5)** ¿Por qué es importante conocer la cultura de la organización? **[RECICLADO]** → #ImportanciaCultura #Cultura

## sin fecha (juego C)  ·  `sin-fecha_compilado-preguntas.md`  ·  (2 de 5 registradas)  ·  ⚠ la mención a Farinstein y al «capítulo 9» sugiere un parcial reciente (mismo par de preguntas que la foto ~2024)

- **P1)** Explicar la teoría de motivación de Maslow y los "niveles". **[RECICLADO]** → #Maslow
- **P2)** Según Farinstein, ¿qué es la escucha activa? ¿Cómo se logra poner a prueba la capacidad de escucha? (Esto hace referencia a lo último del capítulo 9). **[RECICLADO]** → #EscuchaActiva

## sin fecha (foto)  ·  `sin-fecha_Parcial.jpg` (foto de hoja tipeada)  ·  ⚠ sin fecha visible; la imagen es de WhatsApp del 2024-10-27 → probablemente 2C 2024. Es la hoja más reciente del dataset.

- **P1)** Teoría de la Ruta-Meta del liderazgo: describa detalladamente las variables contingentes independientes y dependientes del modelo. **[RECICLADO]** (variante más exigente: pide los factores contingentes, no solo los 4 comportamientos) → #RutaMeta #TeoriasContingentes #Liderazgo
- **P2)** ¿De qué se trata la "escucha activa"? ¿Qué implica "poner a prueba nuestra capacidad de escucha"? **[RECICLADO]** → #EscuchaActiva
- **P3)** Habilidades que se requieren de los gerentes: describa cada una de las habilidades y relaciónelas con la escala ocupada dentro de la estructura organizacional. **[RECICLADO]** → #HabilidadesGerente
- **P4)** Desarrolle cada uno de los papeles que Mintzberg propone para la esfera interpersonal. **[RECICLADO]** → #MintzbergInterpersonal #Mintzberg
- **P5)** Según Sallenave, ¿en qué consiste el trabajo del gerente, en su rol de "organizador"? **[RECICLADO]** (variante: un solo papel en profundidad) → #Sallenave

---

## Índice inverso: tema → hojas (para búsqueda rápida)

| Tag | Aparece en |
|---|---|
| `#Liderazgo` (cualquier teoría) | 2013-05-07, 2014-05-06 (A, T2, T1), 2015-11-19, 201?-09-26, 2018-05-02 (A, B), 2019-05-14, sin-fecha A, sin-fecha foto — **11 de 12 hojas** |
| `#LiderazgoSituacional` | 2014-05-06 (A, T1), 2018-05-02 (A), 2019-05-14, sin-fecha A |
| `#RutaMeta` | 2014-05-06 (T2), 2018-05-02 (B), sin-fecha foto |
| `#TeoriasContingentes` ("¿es contingente / por qué importan?") | 2014-05-06 (A, T2, T1), sin-fecha A, sin-fecha foto |
| `#TeoriaRasgos` | 2013-05-07 |
| `#ContinuoAutocraticoDemocratico` | 2015-11-19 |
| `#FenomenoLiderazgo` | 201?-09-26 |
| `#Cultura` (cualquier pregunta) | 2013-05-07, 2014-05-06 (A, T2, T1), 2018-05-02 (A, B), 2019-05-14, sin-fecha A — **8 de 12** |
| `#ImportanciaCultura` | 2014-05-06 (T2), sin-fecha A |
| `#CulturaFormalInformal` / `#Subculturas` | 2018-05-02 (A, B) |
| `#GruposPrimarios` | 2014-05-06 (T1), 2019-05-14 |
| `#CulturaFuerteDebil` | 2014-05-06 (A) |
| `#Pertenencia` | 2013-05-07 |
| `#Mintzberg` (cualquier esfera) | 2014-05-06 (A, T2, T1), 2018-05-02 (B), 2019-05-14, sin-fecha foto — **6 de 12** |
| `#MintzbergInterpersonal` | 2019-05-14, sin-fecha foto |
| `#MintzbergInformacional` | 2014-05-06 (T2, T1) |
| `#MintzbergDecisional` | 2014-05-06 (A), 2018-05-02 (B) |
| `#Sallenave` | 2014-05-06 (T1), 2018-05-02 (A), sin-fecha A, sin-fecha foto |
| `#HabilidadesGerente` | 2014-05-06 (T2), sin-fecha foto |
| `#Negociacion` | 2014-05-06 (A), 2019-05-14 |
| `#Maslow` | 2014-05-06 (T1), 201?-09-26, 2018-05-02 (B), sin-fecha A, sin-fecha C |
| `#Herzberg` | 2015-11-19 |
| `#Mecanicismo` | 2014-05-06 (T2), 201?-09-26 |
| `#Organicismo` | 2015-11-19, sin-fecha A |
| `#Contingencia` | 2019-05-14 |
| `#EscuchaActiva` | sin-fecha C, sin-fecha foto |
| `#FormasComunicacion` | 2013-05-07 |
| `#ClasificacionComunicacion` | 2014-05-06 (A) |

## Preguntas recicladas (idénticas o casi entre hojas)

- **Liderazgo situacional, casi siempre con "¿es contingente y por qué?"** → 2014-05-06 (A y T1), 2018-05-02 (A), 2019-05-14, sin-fecha A. **(5 veces — la pregunta más repetida del dataset)**
- **Maslow: niveles y "qué pasa cuando se satisface / supera un nivel"** → 2014-05-06 (T1), 201?-09-26, 2018-05-02 (B), sin-fecha A, sin-fecha C. **(5 veces)**
- **Mintzberg: una esfera a elección de la cátedra** → interpersonal (2019-05-14, sin-fecha foto), informacional (2014-05-06 T2 y T1), decisional (2014-05-06 A, 2018-05-02 B). **(6 veces, rotando la esfera)**
- **Sallenave: campo/ámbito de acción del gerente general** → 2014-05-06 (T1), 2018-05-02 (A), sin-fecha A; variante "rol de organizador" en sin-fecha foto. **(4 veces)**
- **Ruta-meta** → 2014-05-06 (T2, junto con "por qué importan las teorías contingentes"), 2018-05-02 (B), sin-fecha foto (variables contingentes independientes y dependientes). **(3 veces)**
- **Críticas al paradigma (mecanicismo / organicismo)**, misma redacción con el paradigma cambiado → 2015-11-19 (organicismo), 201?-09-26 (mecanicismo). Variantes: taylorismo (2014-05-06 T2), cuatro elementos del organicismo (sin-fecha A).
- **Sistemas culturales formales / informales + subculturas** → 2018-05-02 (A y B, gemelas).
- **Grupos primarios y secundarios** (con o sin definición clásica de cultura) → 2014-05-06 (T1), 2019-05-14.
- **Por qué es importante conocer la cultura de la organización** → 2014-05-06 (T2), sin-fecha A.
- **Escucha activa (Farinstein) + "poner a prueba la capacidad de escucha"** → sin-fecha C, sin-fecha foto. **(las dos hojas más recientes)**
- **Habilidades del gerente relacionadas con el nivel de la estructura** → 2014-05-06 (T2), sin-fecha foto.
- **Estrategias de negociación (distributiva / integradora)** → 2014-05-06 (A), 2019-05-14.

## Equivalencias (mismo examen, no practicar dos veces)

- Juego **D** del `.md` ≡ 2014-05-06 Tema A del docx (el `.md` es la versión completa).
- Juego **E** del `.md` ≡ 2014-05-06 «Tema 2» del docx.
- Juego **B** del `.md` ≡ 2014-05-06 «Tema 1» del docx.
- 2018-05-02 Tema A y Tema B son de la misma instancia (dos temas), igual que las tres
  hojas del 2014-05-06: **12 hojas = 9 instancias**.

## Fuera de dataset

- **`SEGUNDO PARCIAL - PREGUNTAS JUNTAS.docx`** — estaba en esta carpeta pero es el
  compilado del **segundo parcial** (poder, delegación, ética, Porter, BCG, crisis; fechas
  2012-06-25 → 2018-06-13). Movido a `../../segundo-parcial/examenes/2012-2018_compilado-preguntas-respuestas.docx`, sin indexar.
- **`Respuestas Finales.docx`** — no es un parcial: respuestas de alumnos a preguntas de
  **finales**, ordenadas por unidad del libro (I–XVIII) con páginas. Movido a
  `../../fuentes/respuestas-finales-por-unidad.docx` como material de estudio.
- **`sin-fecha_compilado-preguntas.md`, juegos B, D y E** — no son hojas nuevas: son las
  versiones completas de los tres temas del 2014-05-06 (ver Equivalencias).

---

*Índice generado el 2026-09-14 a partir de la lectura del texto del docx (extraído con
Python) y de la foto (con visión) — 3 archivos, 12 hojas de examen de 9 instancias. Las
hojas del compilado son transcripciones de alumnos: pueden faltar preguntas (se anota
cuántas hay) y las fechas son las que ellos escribieron.*
