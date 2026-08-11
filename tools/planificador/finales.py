"""Planificador de finales: qué rendir en cada ventana y desde cuándo prepararlo.

Funcionalidad A. Asigna materias a llamados, calcula la ventana de preparación
hacia atrás desde cada examen y detecta los choques (finales pegados, estudio
encima de un parcial, arranque tardío, regularidad al borde).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

from .grafo import Grafo
from .modelo import DatosCarrera, EstadoAcademico, Parcial, Ventana
from .reglas import (
    INTENTOS_AGOTADO,
    INTENTOS_ULTIMA_CHANCE,
    POR_VENCER,
    VENCIDA,
    EstadoIntentos,
    EstadoRegularidad,
    Preparacion,
    cuatrimestre_de,
    cupo_de_ventana,
    estado_intentos,
    estado_regularidad,
    fecha_de_examen,
    fin_cuatrimestre,
    preparacion,
)
from .scoring import Score, max_impacto
from .scoring import calcular as calcular_score

FIJADO = "fijado"  # lo fijó el usuario en el tablero (plan-manual.json)
DECLARADO = "declarado"  # lo puso el usuario en candidateSubjects
SUGERIDO = "sugerido"  # lo agrega el planificador porque entra y conviene


@dataclass(frozen=True)
class FinalPlanificado:
    codigo: str
    nombre: str
    ventana: str
    fecha: date
    llamado: int
    origen: str
    preparacion: Preparacion
    score: Score
    regularidad: EstadoRegularidad
    intentos: EstadoIntentos | None = None
    slug: str | None = None
    ventana_estimada: bool = False
    ventana_clave: str = ""

    def a_dict(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "ventana": self.ventana,
            "ventanaClave": self.ventana_clave,
            "ventanaEstimada": self.ventana_estimada,
            "fecha": self.fecha.isoformat(),
            "llamado": self.llamado,
            "origen": self.origen,
            "preparacion": self.preparacion.a_dict(),
            "score": self.score.a_dict(),
            "regularidad": self.regularidad.a_dict(),
            "intentos": self.intentos.a_dict() if self.intentos else None,
            "slug": self.slug,
        }


@dataclass(frozen=True)
class Conflicto:
    tipo: str
    severidad: str  # alta | media | baja
    involucra: tuple[str, ...]
    mensaje: str
    sugerencia: str | None = None

    def a_dict(self) -> dict:
        return {
            "tipo": self.tipo,
            "severidad": self.severidad,
            "involucra": list(self.involucra),
            "mensaje": self.mensaje,
            "sugerencia": self.sugerencia,
        }


@dataclass
class PlanFinales:
    finales: list[FinalPlanificado] = field(default_factory=list)
    conflictos: list[Conflicto] = field(default_factory=list)
    sin_ventana: list[str] = field(default_factory=list)
    descartadas: list[dict] = field(default_factory=list)
    violaciones: list[dict] = field(default_factory=list)  # pins que rompen reglas

    def a_dict(self) -> dict:
        return {
            "finales": [f.a_dict() for f in self.finales],
            "conflictos": [c.a_dict() for c in self.conflictos],
            "sinVentana": self.sin_ventana,
            "descartadas": self.descartadas,
            "violaciones": self.violaciones,
        }


# --------------------------------------------------------------------------
# Elegibilidad
# --------------------------------------------------------------------------


def elegibles_para(
    datos: DatosCarrera,
    estado: EstadoAcademico,
    ventana: Ventana,
    cierres: dict[str, date] | None = None,
) -> tuple[list[str], list[dict]]:
    """Materias que pueden rendir final en esa ventana + por qué quedaron afuera.

    Regla 2: hay que estar regularizada. Las que están `cursando` entran solo si
    la ventana cae después del cierre de la cursada (y si el parámetro
    `asumir_regulariza_cursando` está activo). `cierres` permite a la proyección
    informar la fecha real de cierre de cada cursada futura; sin él se asume el
    cierre del cuatrimestre en curso.
    """
    config = datos.config
    asumir = bool(config.finales["asumir_regulariza_cursando"])
    bloquear_vencidas = bool(config.vigencia["bloquear_por_vencimiento"])
    cuatri_actual, _ = cuatrimestre_de(datos.calendario.hoy, config)
    cierre_por_defecto = fin_cuatrimestre(cuatri_actual, config)

    aptas: list[str] = []
    fuera: list[dict] = []
    for materia in datos.materias:
        situacion = estado.estado(materia.codigo)
        if situacion == "aprobada":
            continue
        intentos = estado_intentos(materia.codigo, estado.intentos_de(materia.codigo), config)
        if intentos.situacion == INTENTOS_AGOTADO:
            fuera.append(
                {"codigo": materia.codigo, "ventana": ventana.id, "motivo": intentos.mensaje}
            )
            continue
        if situacion in ("cursando", "bloqueada") and datos.promocion_asumida(materia.codigo):
            fuera.append(
                {
                    "codigo": materia.codigo,
                    "ventana": ventana.id,
                    "motivo": "se asume promoción por parciales: no rinde final",
                }
            )
            continue
        if situacion == "regularizada":
            reg = estado_regularidad(materia, ventana.desde, config)
            if bloquear_vencidas and reg.situacion == VENCIDA:
                fuera.append(
                    {
                        "codigo": materia.codigo,
                        "ventana": ventana.id,
                        "motivo": f"regularidad vencida el {reg.vence} (bloquear_por_vencimiento=true)",
                    }
                )
                continue
            aptas.append(materia.codigo)
        elif situacion == "cursando":
            cierre = (cierres or {}).get(materia.codigo, cierre_por_defecto)
            if not asumir:
                fuera.append(
                    {"codigo": materia.codigo, "ventana": ventana.id, "motivo": "está cursando"}
                )
            elif ventana.desde < cierre:
                fuera.append(
                    {
                        "codigo": materia.codigo,
                        "ventana": ventana.id,
                        "motivo": f"la cursada cierra el {cierre}, después de esta ventana",
                    }
                )
            else:
                aptas.append(materia.codigo)
        else:
            fuera.append(
                {
                    "codigo": materia.codigo,
                    "ventana": ventana.id,
                    "motivo": f"está '{situacion}': primero hay que cursarla y regularizarla",
                }
            )
    return aptas, fuera


# --------------------------------------------------------------------------
# Asignación de finales a ventanas (primitiva compartida con la proyección)
# --------------------------------------------------------------------------


def asignar_ventana(
    datos: DatosCarrera,
    grafo: Grafo,
    estado: EstadoAcademico,
    ventana: Ventana,
    respetar_candidatas: bool = True,
    solo: list[str] | None = None,
    cierres: dict[str, date] | None = None,
    fijadas: list[str] | None = None,
    excluir: set[str] | None = None,
) -> list[FinalPlanificado]:
    """Asigna materias a los llamados de UNA ventana y avanza `estado`.

    Prioridad: pins del tablero (`fijadas`) → candidatas declaradas → mejores
    por score. En mesas especiales no se sugiere nada: solo entran pins y
    candidatas declaradas (salvo `finales.usar_mesas_especiales`). `excluir`
    saca materias fijadas a OTRA ventana. Muta `estado` (marca `aprobada`) si
    `asumir_aprueba_final` está activo.
    """
    config = datos.config
    aptas, _ = elegibles_para(datos, estado, ventana, cierres)
    if solo is not None:
        aptas = [c for c in aptas if c in solo]
    if excluir:
        aptas = [c for c in aptas if c not in excluir]
    if not aptas:
        return []

    referencia = max_impacto(datos, grafo, estado)
    puntajes = {
        c: calcular_score(c, datos, grafo, estado, ventana.desde, referencia) for c in aptas
    }

    pins = [c for c in (fijadas or []) if c in aptas]
    declaradas = (
        [c for c in ventana.candidatas if c in aptas and c not in pins]
        if respetar_candidatas
        else []
    )
    sugerir = not ventana.especial or bool(config.finales.get("usar_mesas_especiales"))
    resto = (
        sorted(
            (c for c in aptas if c not in declaradas and c not in pins),
            key=lambda c: (-puntajes[c].total, c),
        )
        if sugerir
        else []
    )
    declaradas.sort(key=lambda c: (-puntajes[c].total, c))
    orden = pins + declaradas + resto

    cupo = max(cupo_de_ventana(ventana, config), len(pins))
    planificados: list[FinalPlanificado] = []
    for indice, codigo in enumerate(orden[:cupo]):
        materia = datos.materia(codigo)
        fecha = fecha_de_examen(ventana, indice, config)
        prep = preparacion(materia, fecha, config)
        score = calcular_score(codigo, datos, grafo, estado, fecha, referencia)
        origen = FIJADO if codigo in pins else DECLARADO if codigo in declaradas else SUGERIDO
        planificados.append(
            FinalPlanificado(
                codigo=codigo,
                nombre=materia.nombre,
                ventana=ventana.etiqueta,
                fecha=fecha,
                llamado=indice + 1,
                origen=origen,
                preparacion=prep,
                score=score,
                regularidad=estado_regularidad(materia, datos.calendario.hoy, config),
                intentos=estado_intentos(codigo, estado.intentos_de(codigo), config),
                slug=materia.slug,
                ventana_estimada=ventana.estimada,
                ventana_clave=ventana.clave,
            )
        )
        if config.finales["asumir_aprueba_final"]:
            estado.marcar(codigo, "aprobada", fecha)
    return planificados


# --------------------------------------------------------------------------
# Detección de conflictos
# --------------------------------------------------------------------------


def _solapan(a_inicio: date, a_fin: date, b_inicio: date, b_fin: date) -> int:
    """Días de solapamiento entre dos intervalos cerrados (0 si no se tocan)."""
    inicio = max(a_inicio, b_inicio)
    fin = min(a_fin, b_fin)
    return max(0, (fin - inicio).days + 1)


def detectar_conflictos(
    datos: DatosCarrera, finales: list[FinalPlanificado], parciales: list[Parcial] | None = None
) -> list[Conflicto]:
    """Choques entre finales, entre preparaciones, y contra los parciales."""
    config = datos.config
    hoy = datos.calendario.hoy
    parciales = list(parciales if parciales is not None else datos.calendario.parciales)
    conflictos: list[Conflicto] = []
    ordenados = sorted(finales, key=lambda f: f.fecha)

    # 1. Dos finales demasiado pegados.
    minimo = int(config.finales["dias_minimos_entre_finales"])
    for anterior, siguiente in zip(ordenados, ordenados[1:]):
        separacion = (siguiente.fecha - anterior.fecha).days
        if separacion < minimo:
            conflictos.append(
                Conflicto(
                    tipo="finales-pegados",
                    severidad="alta" if separacion <= minimo // 2 else "media",
                    involucra=(anterior.codigo, siguiente.codigo),
                    mensaje=(
                        f"{anterior.codigo} ({anterior.fecha}) y {siguiente.codigo} "
                        f"({siguiente.fecha}) quedan a {separacion} días: menos que el mínimo de {minimo}"
                    ),
                    sugerencia=f"mové {siguiente.codigo} a otro llamado o a la ventana siguiente",
                )
            )

    # 2. Preparaciones superpuestas (dos materias a la vez).
    for i, uno in enumerate(ordenados):
        for otro in ordenados[i + 1 :]:
            dias = _solapan(
                uno.preparacion.inicio, uno.preparacion.fin, otro.preparacion.inicio, otro.preparacion.fin
            )
            if dias > 0:
                horas_dia = float(config.esfuerzo["horas_por_dia"])
                conflictos.append(
                    Conflicto(
                        tipo="preparacion-solapada",
                        severidad="alta" if dias >= 10 else "media",
                        involucra=(uno.codigo, otro.codigo),
                        mensaje=(
                            f"la preparación de {uno.codigo} y la de {otro.codigo} se pisan {dias} días: "
                            f"necesitarías ~{horas_dia * 2:g} h/día en ese tramo"
                        ),
                        sugerencia=f"empezá {uno.codigo} antes o corré {otro.codigo} de ventana",
                    )
                )

    # 3. Preparación encima de un parcial.
    antes = int(config.finales["bloqueo_parcial_dias_antes"])
    despues = int(config.finales["bloqueo_parcial_dias_despues"])
    for final in ordenados:
        for parcial in parciales:
            dias = _solapan(
                final.preparacion.inicio,
                final.preparacion.fin,
                parcial.fecha - timedelta(days=antes),
                parcial.fecha + timedelta(days=despues),
            )
            if dias > 0:
                conflictos.append(
                    Conflicto(
                        tipo="choque-con-parcial",
                        severidad="alta",
                        involucra=(final.codigo, parcial.codigo),
                        mensaje=(
                            f"preparar {final.codigo} (desde {final.preparacion.inicio}) cae encima del "
                            f"{parcial.etiqueta} del {parcial.fecha}: {dias} días compartidos"
                        ),
                        sugerencia=(
                            f"adelantá el arranque de {final.codigo} o rendilo en el llamado siguiente"
                        ),
                    )
                )

    # 4. Arranque tardío: la preparación tendría que haber empezado ayer.
    for final in ordenados:
        if final.preparacion.inicio < hoy:
            faltan = (final.fecha - hoy).days
            conflictos.append(
                Conflicto(
                    tipo="arranque-tardio",
                    severidad="alta" if faltan < final.preparacion.dias_calendario / 2 else "media",
                    involucra=(final.codigo,),
                    mensaje=(
                        f"{final.codigo} necesita ~{final.preparacion.dias_calendario} días de preparación "
                        f"y quedan {faltan} hasta el {final.fecha}"
                    ),
                    sugerencia=(
                        f"subí a ~{final.preparacion.horas / max(1, faltan):.1f} h/día o pasalo de ventana"
                    ),
                )
            )

    # 5. Regularidad vencida o por vencer.
    for final in ordenados:
        reg = final.regularidad
        if reg.situacion == VENCIDA:
            conflictos.append(
                Conflicto(
                    tipo="regularidad-vencida",
                    severidad="alta",
                    involucra=(final.codigo,),
                    mensaje=(
                        f"{final.codigo}: la regularidad habría vencido el {reg.vence} ({reg.supuesto})"
                    ),
                    sugerencia="confirmá en bedelía; si venció hay que recursar o pedir prórroga",
                )
            )
        elif reg.situacion == POR_VENCER:
            conflictos.append(
                Conflicto(
                    tipo="regularidad-por-vencer",
                    severidad="media",
                    involucra=(final.codigo,),
                    mensaje=f"{final.codigo}: la regularidad vence el {reg.vence} (en {reg.dias_restantes} días)",
                    sugerencia="es de las primeras que hay que sacarse de encima",
                )
            )

    # 6. Intentos de final al límite: presentarse sin estar seguro sale caro.
    for final in ordenados:
        intentos = final.intentos
        if intentos is None:
            continue
        if intentos.situacion == INTENTOS_ULTIMA_CHANCE:
            conflictos.append(
                Conflicto(
                    tipo="ultimo-intento",
                    severidad="alta",
                    involucra=(final.codigo,),
                    mensaje=f"{final.codigo}: {intentos.mensaje}; si lo desaprobás, se recursa",
                    sugerencia="presentate solo con simulacros aprobados (/simulacro en la materia)",
                )
            )
        elif intentos.situacion == "atencion":
            conflictos.append(
                Conflicto(
                    tipo="intentos-acumulados",
                    severidad="media",
                    involucra=(final.codigo,),
                    mensaje=f"{final.codigo}: {intentos.mensaje}",
                    sugerencia="revisá qué falló en los intentos anteriores antes de anotarte de nuevo",
                )
            )
    return conflictos


# --------------------------------------------------------------------------
# Planificador completo (funcionalidad A)
# --------------------------------------------------------------------------


def pins_por_ventana(datos: DatosCarrera) -> dict[str, list[str]]:
    """clave de ventana → materias fijadas ahí en el tablero."""
    salida: dict[str, list[str]] = {}
    for codigo, clave in datos.plan_manual.finales.items():
        salida.setdefault(clave, []).append(codigo)
    for lista in salida.values():
        lista.sort()
    return salida


def planificar(
    datos: DatosCarrera,
    grafo: Grafo | None = None,
    estado: EstadoAcademico | None = None,
    ventanas: list[Ventana] | None = None,
) -> PlanFinales:
    """Plan de finales sobre las ventanas declaradas en el calendario."""
    grafo = grafo or Grafo(datos)
    estado = (estado or datos.estado_inicial()).copia()
    hoy = datos.calendario.hoy
    if ventanas is None:
        ventanas = [v for v in datos.calendario.ventanas if v.hasta >= hoy]

    pins = pins_por_ventana(datos)
    fijadas_en_otra = {c for lista in pins.values() for c in lista}

    plan = PlanFinales()
    for ventana in sorted(ventanas, key=lambda v: v.desde):
        fijadas = pins.get(ventana.clave, [])
        _, fuera = elegibles_para(datos, estado, ventana)
        declaradas_afuera = [f for f in fuera if f["codigo"] in ventana.candidatas]
        plan.descartadas.extend(declaradas_afuera)
        for item in fuera:
            if item["codigo"] in fijadas:
                plan.violaciones.append(
                    {
                        "tipo": "final-fijado-imposible",
                        "codigo": item["codigo"],
                        "donde": ventana.clave,
                        "motivo": item["motivo"],
                    }
                )
        plan.finales.extend(
            asignar_ventana(
                datos,
                grafo,
                estado,
                ventana,
                fijadas=fijadas,
                excluir=fijadas_en_otra - set(fijadas),
            )
        )

    # Las agotadas no entran a NINGUNA mesa: dejarlo dicho una vez, con el porqué.
    for materia in datos.materias:
        if materia.estado != "regularizada":
            continue
        intentos = estado_intentos(materia.codigo, estado.intentos_de(materia.codigo), datos.config)
        if intentos.situacion == INTENTOS_AGOTADO:
            plan.descartadas.append(
                {"codigo": materia.codigo, "ventana": "todas", "motivo": intentos.mensaje}
            )

    plan.conflictos = detectar_conflictos(datos, plan.finales)
    asignados = {f.codigo for f in plan.finales}
    plan.sin_ventana = sorted(
        c
        for c in grafo.rendibles(estado, incluir_cursando=True)
        if c not in asignados
        and estado_intentos(c, estado.intentos_de(c), datos.config).situacion != INTENTOS_AGOTADO
        and not datos.promocion_asumida(c)
    )
    return plan
