"""Validación de objetivos declarados por el usuario (funcionalidad D).

Cada objetivo se contrasta contra el grafo y la proyección y devuelve un
veredicto con motivo: `alcanzable`, `ajustado` (se puede pero con condiciones)
o `inalcanzable` (y qué haría falta cambiar).
"""

from __future__ import annotations

from dataclasses import dataclass

from .finales import elegibles_para
from .grafo import Grafo
from .modelo import Cuatrimestre, DatosCarrera, ErrorDeDatos, Objetivo
from .proyeccion import Proyeccion, proyectar
from .reglas import preparacion

ALCANZABLE = "alcanzable"
AJUSTADO = "ajustado"
INALCANZABLE = "inalcanzable"


@dataclass(frozen=True)
class Veredicto:
    objetivo: Objetivo
    resultado: str  # alcanzable | ajustado | inalcanzable
    motivo: str
    que_haria_falta: tuple[str, ...] = ()

    def a_dict(self) -> dict:
        return {
            "id": self.objetivo.id,
            "tipo": self.objetivo.tipo,
            "materia": self.objetivo.materia,
            "ventana": self.objetivo.ventana,
            "cuatrimestre": self.objetivo.cuatrimestre,
            "antesDe": self.objetivo.antes_de.isoformat() if self.objetivo.antes_de else None,
            "resultado": self.resultado,
            "motivo": self.motivo,
            "queHariaFalta": list(self.que_haria_falta),
        }


# --------------------------------------------------------------------------
# Objetivo "aprobar X en la ventana Y"
# --------------------------------------------------------------------------


def _validar_aprobar(objetivo: Objetivo, datos: DatosCarrera, grafo: Grafo) -> Veredicto:
    if not objetivo.materia or not datos.existe(objetivo.materia):
        return Veredicto(objetivo, INALCANZABLE, f"la materia '{objetivo.materia}' no existe en estado.json")
    materia = datos.materia(objetivo.materia)
    estado = datos.estado_inicial()
    hoy = datos.calendario.hoy

    if materia.estado == "aprobada":
        return Veredicto(objetivo, ALCANZABLE, f"{materia.codigo} ya está aprobada")

    if datos.promocion_asumida(materia.codigo):
        return Veredicto(
            objetivo,
            ALCANZABLE,
            f"{materia.codigo} está marcada para promocionar por parciales: se aprueba al cerrar "
            "la cursada, sin final (si la promoción se cae, volvé a correr el plan sin esa marca)",
        )

    ventana = None
    if objetivo.ventana:
        ventana = datos.calendario.ventana(objetivo.ventana)
        if ventana is None:
            return Veredicto(
                objetivo,
                INALCANZABLE,
                f"la ventana '{objetivo.ventana}' no está en calendario.json",
                ("cargala en finalExamWindows con sus fechas reales",),
            )

    if materia.estado == "bloqueada":
        disp = grafo.disponibilidad(materia.codigo, estado)
        return Veredicto(
            objetivo,
            INALCANZABLE,
            f"{materia.codigo} ni siquiera se puede cursar todavía: {disp.motivo()}",
            tuple(f"resolver {c}" for c in disp.faltantes),
        )

    if ventana is None:
        return Veredicto(objetivo, ALCANZABLE, f"{materia.codigo} está {materia.estado}: puede rendir en cualquier ventana futura")

    aptas, fuera = elegibles_para(datos, estado, ventana)
    if materia.codigo not in aptas:
        motivo = next((f["motivo"] for f in fuera if f["codigo"] == materia.codigo), "no es elegible")
        return Veredicto(
            objetivo,
            INALCANZABLE,
            f"{materia.codigo} no puede rendir en '{ventana.etiqueta}': {motivo}",
        )

    # Elegible: ¿alcanza el tiempo de preparación?
    prep = preparacion(materia, ventana.desde, datos.config)
    dias_disponibles = (ventana.desde - hoy).days
    cfg = datos.config.esfuerzo
    condiciones: list[str] = []
    if dias_disponibles <= 0:
        return Veredicto(objetivo, INALCANZABLE, f"la ventana '{ventana.etiqueta}' ya pasó o es hoy")
    if prep.inicio < hoy:
        horas_dia_necesarias = prep.horas / dias_disponibles
        tope = float(datos.config.datos["objetivos"]["horas_por_dia_tope"])
        if horas_dia_necesarias > tope:
            return Veredicto(
                objetivo,
                INALCANZABLE,
                (
                    f"prepararla exigiría {horas_dia_necesarias:.1f} h/día hasta el {ventana.desde} "
                    f"(tope configurado: {tope:g} h/día)"
                ),
                (f"moverla a la próxima ventana", "bajar el esfuerzo estimado si ya la tenés avanzada"),
            )
        condiciones.append(
            f"arrancar YA con ~{horas_dia_necesarias:.1f} h/día (el plan cómodo pedía empezar el {prep.inicio})"
        )
    if condiciones:
        return Veredicto(
            objetivo,
            AJUSTADO,
            f"{materia.codigo} llega a '{ventana.etiqueta}' pero sin margen",
            tuple(condiciones),
        )
    return Veredicto(
        objetivo,
        ALCANZABLE,
        (
            f"{materia.codigo} puede rendir el {ventana.desde} arrancando la preparación el "
            f"{prep.inicio} ({prep.horas:g} h a {cfg['horas_por_dia']} h/día)"
        ),
    )


# --------------------------------------------------------------------------
# Objetivo "cursar X en el cuatrimestre Y"
# --------------------------------------------------------------------------


def _validar_cursar(
    objetivo: Objetivo, datos: DatosCarrera, grafo: Grafo, proyeccion: Proyeccion
) -> Veredicto:
    if not objetivo.materia or not datos.existe(objetivo.materia):
        return Veredicto(objetivo, INALCANZABLE, f"la materia '{objetivo.materia}' no existe en estado.json")
    materia = datos.materia(objetivo.materia)
    if materia.estado != "bloqueada":
        return Veredicto(objetivo, ALCANZABLE, f"{materia.codigo} ya está {materia.estado}")
    if not objetivo.cuatrimestre:
        disp = grafo.disponibilidad(materia.codigo, datos.estado_inicial())
        if disp.puede:
            return Veredicto(objetivo, ALCANZABLE, f"{materia.codigo} ya cumple correlativas: se puede anotar")
        return Veredicto(
            objetivo,
            AJUSTADO,
            f"{materia.codigo} todavía no cumple correlativas: {disp.motivo()}",
            tuple(f"resolver {c}" for c in disp.faltantes),
        )

    try:
        pedido = Cuatrimestre.desde_clave(objetivo.cuatrimestre)
    except ErrorDeDatos as exc:
        return Veredicto(objetivo, INALCANZABLE, str(exc))

    for periodo in proyeccion.periodos:
        if materia.codigo in periodo.cursa:
            simulado = periodo.cuatrimestre
            if (simulado.anio, simulado.numero) <= (pedido.anio, pedido.numero):
                return Veredicto(
                    objetivo,
                    ALCANZABLE,
                    f"la proyección ya la ubica en {simulado.etiqueta} (pedido: {pedido.etiqueta})",
                )
            return Veredicto(
                objetivo,
                INALCANZABLE,
                f"la proyección recién la habilita en {simulado.etiqueta}, después de {pedido.etiqueta}",
                _para_adelantar(materia.codigo, datos, grafo),
            )
    return Veredicto(
        objetivo,
        INALCANZABLE,
        f"la proyección no llega a cursar {materia.codigo} dentro del horizonte simulado",
        _para_adelantar(materia.codigo, datos, grafo),
    )


def _para_adelantar(codigo: str, datos: DatosCarrera, grafo: Grafo) -> tuple[str, ...]:
    """Qué habría que resolver antes para adelantar una materia."""
    disp = grafo.disponibilidad(codigo, datos.estado_inicial())
    pasos = []
    for faltante in disp.faltan_regularizar:
        pasos.append(f"regularizar {faltante} (hoy: {datos.materia(faltante).estado})")
    for faltante in disp.faltan_aprobar:
        pasos.append(f"aprobar {faltante} (hoy: {datos.materia(faltante).estado})")
    return tuple(pasos)


# --------------------------------------------------------------------------
# Objetivo "recibirme antes de X"
# --------------------------------------------------------------------------


def _validar_recibirse(
    objetivo: Objetivo, datos: DatosCarrera, grafo: Grafo, proyeccion: Proyeccion
) -> Veredicto:
    limite = objetivo.antes_de
    if limite is None:
        return Veredicto(objetivo, INALCANZABLE, "el objetivo 'recibirme' necesita `antesDe` (AAAA-MM-DD)")
    if not proyeccion.completa or proyeccion.graduacion is None:
        return Veredicto(
            objetivo,
            INALCANZABLE,
            "la proyección no termina la carrera dentro del horizonte simulado",
            ("revisá el horizonte.max_cuatrimestres o las correlativas cargadas",),
        )
    estimada = proyeccion.graduacion
    if estimada <= limite:
        margen = (limite - estimada).days
        resultado = ALCANZABLE if margen > 90 else AJUSTADO
        motivo = (
            f"la proyección con {proyeccion.max_materias} materias/cuatrimestre termina el "
            f"{estimada} ({margen} días antes del límite)"
        )
        condiciones = () if resultado == ALCANZABLE else ("no hay margen para recursar ni desaprobar finales",)
        return Veredicto(objetivo, resultado, motivo, condiciones)

    # No llega con el ritmo actual: ¿llega con más materias por cuatrimestre?
    tope_cfg = int(datos.config.datos["objetivos"]["max_materias_por_cuatrimestre_tope"])
    for tope in range(proyeccion.max_materias + 1, tope_cfg + 1):
        alternativa = proyectar(datos, grafo, max_materias=tope)
        if alternativa.completa and alternativa.graduacion and alternativa.graduacion <= limite:
            return Veredicto(
                objetivo,
                AJUSTADO,
                (
                    f"con {proyeccion.max_materias} materias/cuatrimestre terminás el {estimada}, "
                    f"después del límite {limite}"
                ),
                (
                    f"subir a {tope} materias por cuatrimestre (terminarías el {alternativa.graduacion})",
                ),
            )
    piso = proyeccion.piso_teorico
    return Veredicto(
        objetivo,
        INALCANZABLE,
        (
            f"ni cursando {tope_cfg} materias por cuatrimestre se llega antes del {limite}: "
            f"la cadena crítica de correlativas ({' → '.join(proyeccion.cadena_critica)}) "
            f"impone un piso de ~{piso} cuatrimestres"
        ),
        ("mover el límite de fecha", "verificar si alguna correlativa admite equivalencia/excepción"),
    )


# --------------------------------------------------------------------------
# API del módulo
# --------------------------------------------------------------------------


def validar_objetivos(
    datos: DatosCarrera,
    grafo: Grafo | None = None,
    proyeccion: Proyeccion | None = None,
    objetivos: list[Objetivo] | None = None,
) -> list[Veredicto]:
    grafo = grafo or Grafo(datos)
    proyeccion = proyeccion or proyectar(datos, grafo)
    objetivos = list(objetivos if objetivos is not None else datos.objetivos)
    veredictos = []
    for objetivo in objetivos:
        if objetivo.tipo == "aprobar":
            veredictos.append(_validar_aprobar(objetivo, datos, grafo))
        elif objetivo.tipo == "cursar":
            veredictos.append(_validar_cursar(objetivo, datos, grafo, proyeccion))
        elif objetivo.tipo == "recibirme":
            veredictos.append(_validar_recibirse(objetivo, datos, grafo, proyeccion))
        else:
            veredictos.append(
                Veredicto(
                    objetivo,
                    INALCANZABLE,
                    f"tipo de objetivo desconocido '{objetivo.tipo}' (válidos: aprobar, cursar, recibirme)",
                )
            )
    return veredictos
