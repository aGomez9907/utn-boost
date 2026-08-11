"""Proyección de cursada multi-año (funcionalidad C).

Simula cuatrimestre por cuatrimestre: qué se cursa (o recursa), qué se
regulariza o promociona y qué finales se rinden en cada mesa, hasta que no
queda nada pendiente. De ahí salen la fecha estimada de graduación y los
escenarios ("¿y si curso 3?").

La simulación respeta los *pins* del tablero (`carrera/datos/plan-manual.json`):
cursadas fijadas a un cuatrimestre, finales fijados a una mesa y promociones
asumidas. Un pin que rompe una regla no se descarta en silencio: se ejecuta lo
que se puede y se reporta en `violaciones`.

Supuestos (todos parametrizables, ver config.json):
  · se aprueba la cursada de todo lo que se cursa (`cursada.asumir_aprueba_cursada`);
  · se aprueba el final en el primer intento (`finales.asumir_aprueba_final`);
  · lo marcado como promoción aprueba por parciales, sin final;
  · no se inscribe a materias nuevas en un cuatrimestre ya empezado;
  · las anuales arrancan en el cuatrimestre `cursada.anual_empieza_en_cuatrimestre`;
  · una materia con los intentos de final agotados se RECURSA (vuelve a ocupar cupo).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from .finales import FinalPlanificado, asignar_ventana, detectar_conflictos, elegibles_para, pins_por_ventana
from .grafo import Grafo
from .modelo import Cuatrimestre, DatosCarrera, ErrorDeDatos, EstadoAcademico, Ventana
from .reglas import (
    INTENTOS_AGOTADO,
    cuatrimestre_de,
    estado_intentos,
    fin_cuatrimestre,
    inicio_cuatrimestre,
    ventanas_efectivas,
)


@dataclass
class Periodo:
    """Un cuatrimestre de la proyección."""

    cuatrimestre: Cuatrimestre
    inicio: date
    fin: date
    cursa: tuple[str, ...] = ()
    nuevas: tuple[str, ...] = ()
    continua: tuple[str, ...] = ()
    fijadas: tuple[str, ...] = ()  # subset de nuevas que vino de un pin del tablero
    recursa: tuple[str, ...] = ()  # subset de nuevas que son recursadas (intentos agotados)
    regulariza: tuple[str, ...] = ()
    promociona: tuple[str, ...] = ()  # cursadas que cierran aprobando por parciales
    finales: list[FinalPlanificado] = field(default_factory=list)
    cupo: int = 0
    inscripcion_abierta: bool = True

    @property
    def vacio(self) -> bool:
        return not (self.cursa or self.finales or self.regulariza or self.promociona)

    def a_dict(self) -> dict:
        return {
            "cuatrimestre": self.cuatrimestre.clave,
            "etiqueta": self.cuatrimestre.etiqueta,
            "inicio": self.inicio.isoformat(),
            "fin": self.fin.isoformat(),
            "cursa": list(self.cursa),
            "nuevas": list(self.nuevas),
            "continua": list(self.continua),
            "fijadas": list(self.fijadas),
            "recursa": list(self.recursa),
            "regulariza": list(self.regulariza),
            "promociona": list(self.promociona),
            "finales": [f.a_dict() for f in self.finales],
            "cupo": self.cupo,
            "inscripcionAbierta": self.inscripcion_abierta,
        }


@dataclass
class Proyeccion:
    max_materias: int
    periodos: list[Periodo] = field(default_factory=list)
    graduacion: date | None = None
    cuatrimestres_restantes: int = 0
    piso_teorico: int = 0
    cadena_critica: tuple[str, ...] = ()
    completa: bool = True
    pendientes: tuple[str, ...] = ()
    supuestos: tuple[str, ...] = ()
    violaciones: list[dict] = field(default_factory=list)

    @property
    def finales(self) -> list[FinalPlanificado]:
        return [f for p in self.periodos for f in p.finales]

    def a_dict(self) -> dict:
        return {
            "maxMateriasPorCuatrimestre": self.max_materias,
            "graduacion": self.graduacion.isoformat() if self.graduacion else None,
            "cuatrimestresRestantes": self.cuatrimestres_restantes,
            "pisoTeoricoCuatrimestres": self.piso_teorico,
            "cadenaCritica": list(self.cadena_critica),
            "completa": self.completa,
            "pendientes": list(self.pendientes),
            "supuestos": list(self.supuestos),
            "violaciones": self.violaciones,
            "periodos": [p.a_dict() for p in self.periodos],
        }


# --------------------------------------------------------------------------
# Selección de materias por cuatrimestre
# --------------------------------------------------------------------------


def _cadena_critica(grafo: Grafo, estado: EstadoAcademico) -> list[str]:
    """La cadena de correlativas pendiente más larga del plan."""
    mejor: list[str] = []
    for codigo in grafo.codigos():
        if estado.al_menos(codigo, "aprobada"):
            continue
        cadena = grafo.cadena_mas_larga(codigo, estado)
        if len(cadena) > len(mejor):
            mejor = cadena
    return mejor


def seleccionar_materias(
    datos: DatosCarrera,
    grafo: Grafo,
    estado: EstadoAcademico,
    cuatri: Cuatrimestre,
    cupo: int,
    en_curso: set[str],
    vetadas: set[str] | None = None,
    recursables: list[str] | None = None,
) -> list[str]:
    """Elige qué cursar este cuatrimestre: lo que más destraba, primero.

    Orden: anuales disponibles (si no arrancan ahora esperan un año entero) →
    materias de la cadena crítica → recursadas pendientes → mayor impacto aguas
    abajo → nivel más bajo. `vetadas` (pins a otros cuatrimestres) no se tocan.
    """
    if cupo <= 0:
        return []
    config = datos.config
    arranque_anual = int(config.cursada["anual_empieza_en_cuatrimestre"])
    critica = set(_cadena_critica(grafo, estado))
    niveles = grafo.niveles_topologicos()
    vetadas = vetadas or set()

    candidatas = [c for c in grafo.cursables(estado) if c not in en_curso and c not in vetadas]
    candidatas += [c for c in (recursables or []) if c not in en_curso and c not in vetadas]
    disponibles = []
    for codigo in candidatas:
        materia = datos.materia(codigo)
        if materia.es_anual and cuatri.numero != arranque_anual:
            continue  # una anual solo puede arrancar en su cuatrimestre
        disponibles.append(codigo)

    def clave(codigo: str) -> tuple:
        materia = datos.materia(codigo)
        impacto = grafo.impacto(codigo, estado)
        return (
            0 if materia.es_anual else 1,
            0 if codigo in critica else 1,
            -impacto.puntaje,
            niveles.get(codigo, 0),
            materia.nivel,
            codigo,
        )

    return sorted(disponibles, key=clave)[:cupo]


# --------------------------------------------------------------------------
# Simulación
# --------------------------------------------------------------------------


def _pins_cursada(datos: DatosCarrera) -> dict[str, list[str]]:
    """clave de cuatrimestre → materias fijadas ahí en el tablero."""
    salida: dict[str, list[str]] = {}
    for codigo, clave in datos.plan_manual.cursadas.items():
        try:
            Cuatrimestre.desde_clave(clave)
        except ErrorDeDatos:
            continue  # se reporta como violación en proyectar()
        salida.setdefault(Cuatrimestre.desde_clave(clave).clave, []).append(codigo)
    for lista in salida.values():
        lista.sort()
    return salida


def proyectar(
    datos: DatosCarrera,
    grafo: Grafo | None = None,
    estado: EstadoAcademico | None = None,
    max_materias: int | None = None,
    usar_pins: bool = True,
) -> Proyeccion:
    """Corre la simulación completa hasta graduarse (o hasta el horizonte)."""
    config = datos.config
    grafo = grafo or Grafo(datos)
    estado = (estado or datos.estado_inicial()).copia()
    hoy = datos.calendario.hoy
    manual = datos.plan_manual if usar_pins else datos.plan_manual.__class__()
    tope = max_materias or manual.max_materias or config.max_materias_por_cuatrimestre
    limite = int(config.horizonte["max_cuatrimestres"])

    cuatri, _ = cuatrimestre_de(hoy, config)
    horizonte = date(cuatri.anio + limite // 2 + 2, 12, 31)
    ventanas = [v for v in ventanas_efectivas(datos.calendario, config, horizonte) if v.hasta >= hoy]

    pins_cursada = _pins_cursada(datos) if usar_pins else {}
    pins_final = pins_por_ventana(datos) if usar_pins else {}
    codigos_pin_cursada = {c for lista in pins_cursada.values() for c in lista}
    codigos_pin_final = {c for lista in pins_final.values() for c in lista}
    claves_ventana_vistas: set[str] = set()

    def promociona(codigo: str) -> bool:
        return datos.promocion_asumida(codigo) or (
            usar_pins and codigo in manual.promociones
        )

    # codigo → (inicio de la cursada, fecha de cierre, es_recursada)
    en_curso: dict[str, tuple[date, date, bool]] = {}
    for codigo in estado.codigos_en("cursando"):
        materia = datos.materia(codigo)
        cierre = fin_cuatrimestre(cuatri.siguiente() if materia.es_anual else cuatri, config)
        en_curso[codigo] = (inicio_cuatrimestre(cuatri, config), cierre, False)

    proyeccion = Proyeccion(max_materias=tope)
    cadena = _cadena_critica(grafo, estado)
    proyeccion.piso_teorico = len(cadena)
    proyeccion.cadena_critica = tuple(cadena)

    # Pins con clave rota (no parsea como cuatrimestre).
    for codigo, clave in (manual.cursadas if usar_pins else {}).items():
        try:
            Cuatrimestre.desde_clave(clave)
        except ErrorDeDatos:
            proyeccion.violaciones.append(
                {
                    "tipo": "pin-invalido",
                    "codigo": codigo,
                    "donde": clave,
                    "motivo": f"'{clave}' no es un cuatrimestre válido (usá '1C-2027')",
                }
            )

    actual = cuatri
    for _ in range(limite):
        inicio = inicio_cuatrimestre(actual, config)
        fin = fin_cuatrimestre(actual, config)
        siguiente_inicio = inicio_cuatrimestre(actual.siguiente(), config)
        periodo = Periodo(
            cuatrimestre=actual,
            inicio=inicio,
            fin=fin,
            cupo=tope,
            inscripcion_abierta=inicio >= hoy,
        )

        # 1. Materias que vienen de antes (anuales) y ocupan cupo.
        continua = sorted(c for c, (ini, cierre, _) in en_curso.items() if ini < inicio <= cierre)
        periodo.continua = tuple(continua)

        # 2. Inscripción: primero los pins de este cuatrimestre, después el resto.
        nuevas: list[str] = []
        fijadas: list[str] = []
        recursa: list[str] = []
        if periodo.inscripcion_abierta:
            activas = {c for c, (ini, cierre, _) in en_curso.items() if ini <= inicio <= cierre}

            def anotar(codigo: str, es_pin: bool) -> None:
                materia = datos.materia(codigo)
                es_recursada = estado.al_menos(codigo, "regularizada")
                cierre = fin_cuatrimestre(actual.siguiente() if materia.es_anual else actual, config)
                en_curso[codigo] = (inicio, cierre, es_recursada)
                nuevas.append(codigo)
                if es_pin:
                    fijadas.append(codigo)
                if es_recursada:
                    recursa.append(codigo)
                else:
                    estado.marcar(codigo, "cursando", inicio)

            for codigo in pins_cursada.get(actual.clave, []):
                if estado.al_menos(codigo, "aprobada"):
                    proyeccion.violaciones.append(
                        {
                            "tipo": "pin-redundante",
                            "codigo": codigo,
                            "donde": actual.clave,
                            "motivo": "para ese cuatrimestre la materia ya estaría aprobada",
                        }
                    )
                    continue
                if codigo in activas or codigo in en_curso:
                    continue
                agotada = (
                    estado.estado(codigo) == "regularizada"
                    and estado_intentos(codigo, estado.intentos_de(codigo), config).situacion
                    == INTENTOS_AGOTADO
                )
                if estado.estado(codigo) == "bloqueada":
                    disp = grafo.disponibilidad(codigo, estado)
                    if not disp.puede:
                        proyeccion.violaciones.append(
                            {
                                "tipo": "cursada-fijada-sin-correlativas",
                                "codigo": codigo,
                                "donde": actual.clave,
                                "motivo": disp.motivo(),
                            }
                        )
                elif estado.estado(codigo) == "regularizada" and not agotada:
                    proyeccion.violaciones.append(
                        {
                            "tipo": "pin-redundante",
                            "codigo": codigo,
                            "donde": actual.clave,
                            "motivo": "ya está regularizada: no hace falta recursarla (le falta el final)",
                        }
                    )
                    continue
                materia = datos.materia(codigo)
                if materia.es_anual and actual.numero != int(config.cursada["anual_empieza_en_cuatrimestre"]):
                    proyeccion.violaciones.append(
                        {
                            "tipo": "anual-fuera-de-arranque",
                            "codigo": codigo,
                            "donde": actual.clave,
                            "motivo": f"es anual: arranca en {config.cursada['anual_empieza_en_cuatrimestre']}C",
                        }
                    )
                anotar(codigo, es_pin=True)

            if len(activas) + len(nuevas) > tope:
                proyeccion.violaciones.append(
                    {
                        "tipo": "cupo-excedido",
                        "codigo": ", ".join(fijadas),
                        "donde": actual.clave,
                        "motivo": f"los pins llevan la carga a {len(activas) + len(nuevas)} materias (tope {tope})",
                    }
                )

            recursables = [
                c
                for c in estado.codigos_en("regularizada")
                if estado_intentos(c, estado.intentos_de(c), config).situacion == INTENTOS_AGOTADO
            ]
            for codigo in seleccionar_materias(
                datos,
                grafo,
                estado,
                actual,
                tope - len(activas) - len(nuevas),
                set(en_curso),
                vetadas=codigos_pin_cursada - set(nuevas),
                recursables=recursables,
            ):
                anotar(codigo, es_pin=False)

        periodo.nuevas = tuple(nuevas)
        periodo.fijadas = tuple(fijadas)
        periodo.recursa = tuple(sorted(recursa))
        periodo.cursa = tuple(
            sorted(c for c, (ini, cierre, _) in en_curso.items() if ini <= inicio <= cierre)
        )

        cierres = {c: cierre for c, (_, cierre, _) in en_curso.items()}

        def cerrar_cursadas(hasta: date) -> None:
            """Cierra cursadas terminadas: promoción → aprobada; si no → regularizada."""
            for codigo, (_, cierre, es_recursada) in list(en_curso.items()):
                if cierre > hasta:
                    continue
                if es_recursada:
                    estado.intentos[codigo] = 0  # regularidad nueva, intentos de nuevo
                if promociona(codigo):
                    estado.marcar(codigo, "aprobada", cierre)
                    periodo.promociona = periodo.promociona + (codigo,)
                else:
                    estado.marcar(codigo, "regularizada", cierre)
                    periodo.regulariza = periodo.regulariza + (codigo,)
                del en_curso[codigo]

        # 3. Mesas de finales que caen en este período.
        for ventana in [v for v in ventanas if inicio <= v.desde < siguiente_inicio]:
            cerrar_cursadas(ventana.desde)
            claves_ventana_vistas.add(ventana.clave)
            fijadas_aca = pins_final.get(ventana.clave, [])
            if fijadas_aca:
                _, fuera = elegibles_para(datos, estado, ventana, cierres)
                for item in fuera:
                    if item["codigo"] in fijadas_aca:
                        proyeccion.violaciones.append(
                            {
                                "tipo": "final-fijado-imposible",
                                "codigo": item["codigo"],
                                "donde": ventana.clave,
                                "motivo": item["motivo"],
                            }
                        )
            periodo.finales.extend(
                asignar_ventana(
                    datos,
                    grafo,
                    estado,
                    ventana,
                    cierres=cierres,
                    fijadas=fijadas_aca,
                    excluir=codigos_pin_final - set(fijadas_aca),
                )
            )
        cerrar_cursadas(siguiente_inicio)
        periodo.regulariza = tuple(sorted(periodo.regulariza))
        periodo.promociona = tuple(sorted(periodo.promociona))

        if not periodo.vacio:
            proyeccion.periodos.append(periodo)

        pendientes = [c for c in grafo.codigos() if not estado.al_menos(c, "aprobada")]
        if not pendientes:
            break
        actual = actual.siguiente()

    for clave in set(pins_final) - claves_ventana_vistas:
        proyeccion.violaciones.append(
            {
                "tipo": "mesa-desconocida",
                "codigo": ", ".join(pins_final[clave]),
                "donde": clave,
                "motivo": "esa mesa no existe en el calendario ni en la plantilla (¿ya pasó o está mal escrita?)",
            }
        )

    pendientes = tuple(sorted(c for c in grafo.codigos() if not estado.al_menos(c, "aprobada")))
    proyeccion.pendientes = pendientes
    proyeccion.completa = not pendientes
    fechas_aprobacion = list(estado.aprobada_desde.values())
    proyeccion.graduacion = max(fechas_aprobacion) if fechas_aprobacion and proyeccion.completa else None
    proyeccion.cuatrimestres_restantes = len(proyeccion.periodos)

    promovidas = sorted(c for c in grafo.codigos() if promociona(c) and not datos.materia(c).al_menos("aprobada"))
    supuestos = [
        f"máximo {tope} materias por cuatrimestre",
        "se aprueba la cursada de todo lo que se cursa",
        "se aprueba cada final en el primer intento",
        "no hay inscripción a materias nuevas en un cuatrimestre ya empezado",
        f"las anuales arrancan en {config.cursada['anual_empieza_en_cuatrimestre']}C",
    ]
    if promovidas:
        supuestos.append("promocionan por parciales (sin final): " + ", ".join(promovidas))
    if usar_pins and not manual.vacio:
        supuestos.append(
            f"se respetan {len(manual.cursadas)} cursada(s) y {len(manual.finales)} final(es) fijados en el tablero"
        )
    proyeccion.supuestos = tuple(supuestos)
    return proyeccion


# --------------------------------------------------------------------------
# Escenarios
# --------------------------------------------------------------------------


@dataclass
class Escenario:
    max_materias: int
    graduacion: date | None
    cuatrimestres: int
    completa: bool
    ultimo_periodo: str | None = None

    def a_dict(self) -> dict:
        return {
            "maxMateriasPorCuatrimestre": self.max_materias,
            "graduacion": self.graduacion.isoformat() if self.graduacion else None,
            "cuatrimestres": self.cuatrimestres,
            "completa": self.completa,
            "ultimoPeriodo": self.ultimo_periodo,
        }


def escenarios(
    datos: DatosCarrera, valores: list[int] | None = None, grafo: Grafo | None = None
) -> list[Escenario]:
    """Corre la proyección con distintos topes de materias por cuatrimestre."""
    grafo = grafo or Grafo(datos)
    valores = valores or list(datos.config.horizonte["escenarios_materias_por_cuatrimestre"])
    salida = []
    for tope in sorted(set(int(v) for v in valores)):
        proy = proyectar(datos, grafo, max_materias=tope)
        salida.append(
            Escenario(
                max_materias=tope,
                graduacion=proy.graduacion,
                cuatrimestres=proy.cuatrimestres_restantes,
                completa=proy.completa,
                ultimo_periodo=proy.periodos[-1].cuatrimestre.etiqueta if proy.periodos else None,
            )
        )
    return salida


def conflictos_de_proyeccion(datos: DatosCarrera, proyeccion: Proyeccion) -> list:
    """Conflictos de la tanda de finales más próxima (el resto es demasiado hipotético)."""
    if not proyeccion.periodos:
        return []
    return detectar_conflictos(datos, proyeccion.periodos[0].finales)


def ventanas_del_horizonte(datos: DatosCarrera, anios: int = 3) -> list[Ventana]:
    """Ventanas (declaradas + estimadas) de los próximos `anios` años."""
    hoy = datos.calendario.hoy
    return [
        v
        for v in ventanas_efectivas(datos.calendario, datos.config, date(hoy.year + anios, 12, 31))
        if v.hasta >= hoy
    ]
