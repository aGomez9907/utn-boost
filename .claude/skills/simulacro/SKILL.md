---
name: simulacro
description: Genera un examen simulado NUEVO de una evaluación, fiel al patrón real de la cátedra. Respeta la estructura del examen (MATERIA.md) y las frecuencias por posición (examenes/INDICE.md), mezcla un problema reciclado casi textual con variantes verificadas de problemas reales, y entrega cada problema con su corrección desplegable y criterio de puntuación. Usala cuando el usuario pida un simulacro, un examen de práctica, "tomame un parcial", practicar cronometrado en los últimos días, o cuando invoque /simulacro.
---

# simulacro

Genera un examen simulado nuevo en `<base>/simulacros/`: mismo formato, misma
dificultad y mismo patrón por posición que los exámenes reales, pero con problemas
que el usuario no vio. **Regla de oro:** la composición sale de la evidencia del
`INDICE.md` (qué cae en cada posición, qué se recicla), no de intuición. Y cada
problema se **resuelve completo antes de escribirlo** — un simulacro con enunciados
irresolubles o corrección errada es peor que no practicar.

## Invocación

`/simulacro [materias/<materia>/<evaluacion>] [--enfocado] [--pdf] [notas]`

| Argumento | Efecto |
|---|---|
| ruta `materias/<m>/<e>` | Evaluación objetivo explícita. |
| `--enfocado` | Sesga la selección hacia los temas donde `registro.md` muestra errores recientes (sin romper el patrón por posición). |
| `--pdf` | Además del `.md`, exporta HTML + PDF con `tools/md_to_html.py`. |
| texto libre | Pedidos puntuales ("que P4 sea EDO", "más difícil que el anterior"). |

Si no dan la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md`: materia = la
única con `estado: cursando` en su `MATERIA.md` (si hay varias, preguntar);
evaluación = la próxima por fecha según la tabla de `MATERIA.md`. Ante ambigüedad
real, preguntar — nunca adivinar en silencio.

## Paso 0 — Levantar insumos

Con `<base> = materias/<materia>/<evaluacion>`:

1. `MATERIA.md` — estructura del examen: cuántos problemas prácticos, cuántos
   teóricos, duración, y el patrón por posición si está documentado.
2. `<base>/examenes/INDICE.md` — **obligatorio**. De acá salen: qué tema cae en cada
   posición (P1, P2, …, T1/T2), los problemas reciclados (los que se repiten casi
   idénticos entre fechas) y los formatos nuevos de los últimos 2 años. Si no
   existe, **parar** y pedir `/indexar-examenes`. Nunca leer los PDFs/imágenes de
   `examenes/`: el INDICE es la única representación textual válida.
3. `<base>/estrategia.md` — si existe, identificá los **exámenes RESERVADOS "a
   ciegas"** (banco de problemas tipo, marcados "dejalos sin mirar"). Anotá sus
   fechas: **PROHIBIDO** usar cualquier problema de esos exámenes en el simulacro,
   ni textual ni como variante — el usuario los necesita vírgenes para simulacro
   real con el examen original.
4. `<base>/simulacros/*.md` previos — leé sus enunciados para **no repetir** ni los
   mismos problemas ni las mismas variantes (cambiar solo un número respecto de un
   simulacro anterior cuenta como repetir).
5. `<base>/registro.md` — solo con `--enfocado`: temas con errores recientes.

## Paso 1 — Componer el examen

Armá exactamente la estructura de `MATERIA.md` (misma cantidad de problemas y
teóricos). Para cada posición, elegí el tema según lo que el INDICE muestra que cae
en ESA posición (si una posición rota entre 2–3 temas, elegí uno distinto al del
simulacro anterior). La mezcla de orígenes, sobre el total de problemas:

- **1 problema reciclado casi textual:** elegí uno de los problemas que el INDICE
  registra como reciclados entre varios exámenes (no reservados) y ponelo casi
  igual. Los reciclados caen de verdad; practicarlos textual es ROI puro.
- **El resto, variantes de problemas reales:** tomá problemas del INDICE (no
  reservados, no usados en simulacros previos) y cambiá números, funciones,
  regiones o condiciones de borde. La variante tiene que seguir saliendo
  **"limpia"**: resoluble a mano, sin cuentas monstruosas, en el tiempo del slot
  (duración total / cantidad de ítems, aprox.).
- **Formato nuevo reciente:** si el INDICE registra un formato que apareció por
  primera vez en los últimos 2 años (tipo de consigna nuevo, tema nuevo en una
  posición), incluí un ejemplar — es la mejor predicción de por dónde innova la
  cátedra.
- **Teóricos (T1/T2…):** elegilos de las demostraciones que realmente piden los
  exámenes (tags `#Demostracion` o equivalente en el INDICE), rotando respecto de
  simulacros previos.

Con `--enfocado`: ante dos temas candidatos para una misma posición, gana el que
tiene errores en `registro.md`. El sesgo NUNCA rompe el patrón por posición (no
poner una EDO en P1 si P1 es siempre integral múltiple).

## Paso 2 — VERIFICACIÓN OBLIGATORIA

Antes de escribir el archivo, **resolvé cada problema completo**, paso a paso, hasta
el resultado final. Si la solución da fea — números imposibles, raíces horribles,
integrales que no salen a mano, casos degenerados (región vacía, campo idénticamente
nulo, determinante cero donde no debía) — **ajustá la variante** y volvé a resolver
hasta que quede limpia. La resolución verificada es exactamente la que va en la
corrección: no redactar una corrección distinta de la cuenta que verificaste.

## Paso 3 — Escribir el simulacro

Ruta: `<base>/simulacros/AAAA-MM-DD-simulacro-NN.md`, con `AAAA-MM-DD` = hoy y
`NN` = correlativo de dos dígitos siguiendo al mayor existente en la carpeta
(`01` si está vacía).

Estructura del archivo:

1. `# Simulacro NN — <evaluación> (<materia>)` + blockquote con: duración real del
   examen, estructura (X problemas + Y teóricos) y la consigna general real de la
   cátedra si el INDICE la registra (condiciones de aprobación, "justificar todos
   los pasos", etc.).
2. Cada problema como en el examen real: `## P1)` (o la numeración que use la
   cátedra) con el enunciado **visible**, fórmulas en bloques `$$…$$` en líneas
   propias, sin sangría, con línea en blanco antes y después.
3. Debajo de cada enunciado, su corrección plegada:

   ```markdown
   <details>
   <summary><strong>Corrección P1</strong></summary>

   <details>
   <summary>Resolución completa</summary>

   **Paso 1:** …

   **Paso 2:** …

   **Resultado:**

   $$\boxed{\;…\;}$$

   </details>

   **Criterio de puntuación:** planteo correcto (X pts), desarrollo (X pts),
   resultado final (X pts). _(desglosado por ítem si el problema tiene a) y b))_

   </details>
   ```

4. Cierre `## Cómo usar este simulacro`: hacerlo **cronometrado** (la duración
   real), **sin apuntes ni corrección a la vista**; recién al terminar abrir cada
   `<details>` y corregirse con el criterio de puntuación; registrar la sesión con
   `/registrar` y anotar cada error en `registro.md` (tema, qué falló, cómo se
   corrige).
5. Pie en cursiva: fecha de generación (AAAA-MM-DD) + fuentes (`examenes/INDICE.md`,
   `estrategia.md` si se usó, y qué exámenes/fechas inspiraron cada problema —
   **sin** revelar cuáles son los reservados).

Con `--pdf`, exportar después de escribir:

```bash
venv/bin/python tools/md_to_html.py <base>/simulacros/AAAA-MM-DD-simulacro-NN.md --pdf
# fallback si no hay venv:
python tools/md_to_html.py <base>/simulacros/AAAA-MM-DD-simulacro-NN.md --pdf
```

(Para PDF los `<details>` salen expandidos — avisarle al usuario que la versión
para rendir es el `.md`/HTML con las correcciones plegadas.)

## Reglas

- Español rioplatense (voseo), enunciados con la redacción típica de la cátedra
  (imitá el estilo de los enunciados del INDICE).
- **Jamás** usar problemas de los exámenes reservados de `estrategia.md`, ni
  siquiera como variante. Si no hay estrategia.md, avisar que no hay reservas
  declaradas y sugerir correr `/estrategia` antes.
- No repetir problemas ni variantes de simulacros previos.
- Nunca leer PDFs/imágenes de `examenes/`; todo sale del `INDICE.md`.
- Sin verificación no hay simulacro: cada corrección es una resolución que hiciste
  y cerró limpia, no una promesa.
- Dificultad y extensión calibradas al examen real: si el usuario no llegaría a
  hacerlo en la duración oficial, está mal calibrado.
- Dentro de `<summary>` los enlaces van en HTML (`<a href>`), nunca Markdown.
- Después de generar, recordar el flujo: rendirlo cronometrado → `/registrar` →
  si cambia el panorama, `/plan`.
