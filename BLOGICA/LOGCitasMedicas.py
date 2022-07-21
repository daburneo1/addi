from DATA import DATCitasMedicas
from CLASES.CitaMedica import *

def cargar_citas_medicas(usuario):
    citas_medicas = DATCitasMedicas.buscar_citas_medicas(usuario)
    lista_citas_medicas = []
    for x in citas_medicas:
        id = x[0]
        cita_medica = CitaMedica(id, x[1], x[2], x[3], x[4], x[5], x[6])
        lista_citas_medicas.append(cita_medica)
    if lista_citas_medicas:
        return lista_citas_medicas
    else:
        return None


def agregar_cita_medica(cita_medica, usuario):
    cita_medica.fecha = cita_medica.fecha.replace('/','-')
    print(cita_medica.fecha)
    DATCitasMedicas.agregar_cita_medica(cita_medica, usuario)


def actualizar_cita_medica(nueva_cita_medica):
    nueva_cita_medica.fecha.replace('/', '-')
    DATCitasMedicas.actualizar_cita_medica(nueva_cita_medica)


def eliminar_cita_medica(cita_medica):
    DATCitasMedicas.eliminar_cita_medica(cita_medica)