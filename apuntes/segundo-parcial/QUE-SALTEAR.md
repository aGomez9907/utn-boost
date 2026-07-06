# Qué SALTEAR de cada apunte — Segundo Parcial AM2

> Guía de poda para estudiar contra reloj (examen **8/7**). Cruza las secciones de los 19 apuntes con lo que **realmente cae** en los parciales (ver `../../parciales/segundo-parcial/INDICE-parciales.md`).
>
> **No es que el contenido sobre** — simplemente **no lo toman** en el 2° parcial. Si tenés tiempo de sobra, leelo; si no, saltealo sin culpa.
>
> **Regla mental:**
> - 🗑️ Salteable: *interpretación física*, *independencia de la parametrización*, *valor medio*, *momentos de inercia / Steiner*, *EDO de 1er orden*.
> - ✅ Cae siempre: *método de cálculo* + *orientación/sentido de recorrido* + *demostración* de (condición de potencial / Green / divergencia / superposición).

---

## ⚡ 3 apuntes casi 100% salteables para el 2P

- **06 · Longitud de una curva** → cae **1 sola vez** en 16 parciales. Quedate **solo con la fórmula** `L = ∫ₐᵇ |λ'(t)| dt`. Saltear: curva regular/simple, diferencial de longitud, independencia de parametrización, teorema de reparametrización, curva implícita.
- **07 · Masa de un alambre** → **NUNCA** cae en el 2° parcial (es tema de 1er parcial). Podés saltear el apunte **entero**.
- **17 · Ecuaciones diferenciales I** → todo es de **1er orden**, y el P4 del 2P es **siempre de 2° orden**. Saltear: variables separables, lineal de 1er orden, homogénea de 1er orden, construcción de la EDO desde la solución, soluciones singulares, trayectorias ortogonales. Leer solo (repaso): "solución general vs particular" y "condiciones iniciales".

---

## Apunte por apunte

Leyenda: 🗑️ = saltear · 📖 = leer por arriba (intuición/propiedad) · ✅ = núcleo, **sí** estudiar.

### 01 · Integrales dobles I
- 🗑️ Valor medio de una función de dos variables.
- 📖 Propiedad de linealidad · Aditividad respecto de la región (propiedades formales que usás sin demostrar).
- ✅ Definición de integral doble · Área de una región como integral doble · Integral doble como volumen.

### 02 · Integrales dobles II
- 📖 "El jacobiano como corrector de áreas" (intuición).
- ✅ Matriz jacobiana y jacobiano · Teorema de cambio de variables · Jacobiano de la inversa · Regiones tipo 1 y 2 / orden de integración (cae en T1/T2).

### 03 · Integrales dobles III
- 🗑️ **Momentos de inercia (2° orden)** · **Momento de inercia polar** · **Teorema de Steiner** (no se toman nunca).
- 📖 Momento estático respecto a un eje baricéntrico.
- ✅ Momento estático (1er orden) → Baricentro · Densidad, masa y momentos.

### 04 · Integrales triples I
- 🗑️ Valor medio de una función en una región.
- 📖 "Orden de integración indistinto" · Teoremas linealidad y aditividad · Volumen del tetraedro genérico (es un ejemplo).
- ✅ Definición · Integral triple como volumen · Cambio de variables · **Coordenadas esféricas y cilíndricas**.

### 05 · Integrales triples II
- 🗑️ **Momentos de inercia (2° orden)**.
- 📖 Momentos estáticos · Baricentro/centro de masa 3D (el baricentro de un cuerpo no lo toman; sí la masa).
- ✅ **Masa de un cuerpo y función densidad**.

### 06 · Longitud de una curva  → (ver arriba: casi todo salteable, quedate con la fórmula)

### 07 · Masa de un alambre  → (ver arriba: salteable entero para el 2P)

### 08 · Trabajo de un campo vectorial
- 📖 Interpretación física (trabajo) · Teorema de reparametrización · "Curvas gráfica de función y notación diferencial".
- ✅ Integral de campo vectorial / circulación · Cómo reducirla a integral simple · **Cómo determinar e invertir el sentido de recorrido** (lo piden siempre).

### 09 · Rotor en el plano (Green)
- 🗑️ **Interpretación física del rotor**.
- 📖 Campos irrotacionales · Región regular · Regiones por partes · Conjuntos múltiplemente conexos.
- ✅ Teorema de Green · Orientación positiva / sentido horario · **Corolario: cálculo de áreas con Green** (¡es cómo se resuelven los P1 de "área encerrada por λ(t)"! — 2023-07-14, sin-fecha).

### 10 · Campos conservativos
- 📖 "Análisis con Green y regiones agujereadas".
- ✅ Todo lo demás (definición · potencial · tres proposiciones equivalentes · **condición necesaria con demostración** · método práctico · condición suficiente) — es T1/T2 puro.

### 11 · Función potencial
- 🗑️ **Líneas de campo** · **Líneas de igual potencial (equipotenciales)** (no se toman).
- 📖 "Limitación del método 2".
- ✅ Método 1 (EDO total exacta) · Método 2 (integral de línea).

### 12 · Área de una superficie
- 🗑️ "El área no depende de la parametrización" (demostración).
- 📖 Superficies simples · Interpretación del diferencial de área.
- ✅ Fórmula del área · Caso "gráfica / definida implícitamente".

### 13 · Masa de una chapa  (baja prioridad: no aparece en los parciales)
- 🗑️ "Peso de la nieve sobre una cúpula" · Valor medio · Independencia de parametrización · Propiedades de linealidad.
- 📖 Definición de integral de campo escalar sobre superficie (por si acaso).

### 14 · Flujo
- 🗑️ **Interpretación física (flujo y caudal)** · **Fuentes y sumideros**.
- 📖 Repaso de parametrización · "Superficies orientables por partes".
- ✅ Definición de flujo · **Regla de la mano derecha** · Dependencia con la orientación · Superficie por ecuación cartesiana · Ejercicio 3 (esférica) — núcleo del P3.

### 15 · Divergencia
- 🗑️ **Teorema de Gauss para una carga puntual** (física).
- 📖 "Divergencia como campo escalar" · "Región simple del espacio".
- ✅ Divergencia y su cálculo · **Teorema de la Divergencia** · **Campos solenoidales** (¡ahora sí! el 2025-07-18 pide hallar `g` para que el campo sea solenoidal).

### 16 · Rotor en el espacio (Stokes)
- 🗑️ "Teorema de Green como caso particular de Stokes".
- 📖 Operador nabla (repaso) · Campos irrotacionales · "Circulación de conservativo sobre curvas cerradas".
- ✅ Rotor por determinante · **Teorema de Stokes** (los P2 de circulación por rotor).

### 17 · Ecuaciones diferenciales I  → (ver arriba: casi todo salteable; es de 1er orden)

### 18 · EDO lineales II
- 📖 "Verificación por reemplazo" · **"Criterio del cociente para independencia lineal"** · Dependencia/independencia.
- ✅ Ecuación característica · **Los 3 casos de raíces** (reales distintas / doble / complejas) · Superposición (combinación lineal).

### 19 · EDO lineales III
- 🗑️/opcional: **Método de variación de parámetros** y su justificación → en estos parciales el término derecho siempre es polinomio/constante/exponencial, así que **coeficientes indeterminados alcanza para todos**. Dejalo como respaldo.
- 📖 "Verificación de que y = yc + yp es solución".
- ✅ Estructura `y = yc + yp` · **Coeficientes indeterminados** · **Superposición** · **Casos de resonancia** (multiplicar por `x`/`x²`).

---

*Generado el 2026-07-04. Contraste: 19 apuntes de `apuntes/segundo-parcial` vs. 16 parciales de `parciales/segundo-parcial/INDICE-parciales.md`. La poda es para aprobar el 2° parcial; no descarta el valor conceptual del material.*
