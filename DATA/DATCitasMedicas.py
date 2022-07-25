from DATA.DATCursor import *


def buscar_citas_medicas():
    sql = "SELECT idCitasMedicas, nombreMedico, especialidad, ubicacion, fecha, hora, notas, idUsuario FROM citamedica "

    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    citas_medicas = []

    for x in data:
        citas_medicas.append(x)
    return citas_medicas


def agregar_cita_medica(cita_medica, usuario):
    sql = "INSERT INTO citamedica(nombreMedico, especialidad, ubicacion, fecha, hora, notas, idUsuario) VALUES (" \
          "'%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(cita_medica.nombreMedico, cita_medica.especialidad, cita_medica.ubicacion, cita_medica.fecha, cita_medica.hora, cita_medica.notas, usuario.idUsuario)

    print(sql)

    cursor.execute(sql)
    connection.commit()


def actualizar_cita_medica(cita_medica):
    sql = "UPDATE citamedica SET nombreMedico = '%s', especialidad = '%s', ubicacion = '%s', notas = '%s', fecha = '%s', hora = '%s' WHERE idCitasMedicas = '%s'" % (
        cita_medica.nombreMedico, cita_medica.especialidad, cita_medica.ubicacion, cita_medica.notas, cita_medica.fecha, cita_medica.hora, cita_medica.id)

    print(sql)

    cursor.execute(sql)
    cursor.fetchall()
    connection.commit()


def eliminar_cita_medica(cita_medica):
    sql = "DELETE FROM citamedica WHERE citamedica.idCitasMedicas = '%s'" % (cita_medica.id)

    print(sql)

    cursor.execute(sql)
    cursor.fetchall()
    connection.commit()