from CLASES.CitaLaboratorio import CitaLaboratorio
from DATA import DATCitasLaboratorio


def cargar_citas_laboratorio():
    citas_laboratorio = DATCitasLaboratorio.buscar_citas_laboratorio()
    lista_citas_laboratorio = []
    for x in citas_laboratorio:
        id = x[0]
        cita_laboratorio = CitaLaboratorio(id, x[1], x[2], x[3], str(x[4]), x[5], x[6])
        lista_citas_laboratorio.append(cita_laboratorio)
    if lista_citas_laboratorio:
        return lista_citas_laboratorio
    else:
        return None


def agregar_cita_laboratorio(cita_laboratorio, usuario):
    cita_laboratorio.fecha = cita_laboratorio.fecha.replace('/', '-')
    DATCitasLaboratorio.agregar_cita_laboratorio(cita_laboratorio, usuario)


def actualizar_cita_laboratorio(cita_laboratorio):
    cita_laboratorio.fecha = cita_laboratorio.fecha.replace('/', '-')
    DATCitasLaboratorio.actualizar_cita_laboratorio(cita_laboratorio)


def eliminar_cita_laboratorio(cita_laboratorio):
    DATCitasLaboratorio.eliminar_cita_laboratorio(cita_laboratorio)