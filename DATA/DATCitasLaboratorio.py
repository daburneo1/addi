from DATA.DATCursor import *

def buscar_citas_laboratorio(usuario):
    sql = "SELECT idCitasLaboratorio, tipoExamen, laboratorio, ubicacion, fecha, hora, notas, cedula FROM citaslaboratorio WHERE cedula = %s;" % (
        usuario.cedula)

    print(sql)
    cursor.execute(sql)
    data = cursor.fetchall()
    connection.commit()
    citas_laboratorio = []

    for x in data:
        citas_laboratorio.append(x)
    return citas_laboratorio

def agregar_cita_laboratorio(cita_laboratorio, usuario):
    sql = "INSERT INTO citaslaboratorio(tipoExamen, laboratorio, ubicacion, notas, fecha, hora, cedula) VALUES (" \
          "'%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(cita_laboratorio.tipoExamen, cita_laboratorio.laboratorio, cita_laboratorio.ubicacion, cita_laboratorio.notas, cita_laboratorio.fecha, cita_laboratorio.hora, usuario.cedula)

    print(sql)

    cursor.execute(sql)
    connection.commit()

def actualizar_cita_laboratorio(cita_laboratorio):
    sql = "UPDATE citaslaboratorio SET tipoExamen = '%s', laboratorio = '%s', ubicacion = '%s', notas = '%s', fecha = '%s', hora = '%s' WHERE idCitasMedicas = '%s'" % (
        cita_laboratorio.tipoExamen, cita_laboratorio.laboratorio, cita_laboratorio.ubicacion, cita_laboratorio.notas, cita_laboratorio.fecha,
        cita_laboratorio.hora, cita_laboratorio.id)

    print(sql)

    cursor.execute(sql)
    cursor.fetchall()
    connection.commit()

def eliminar_cita_laboratorio(cita_laboratorio):
    sql = "DELETE FROM citaslaboratorio WHERE citaslaboratorio.idCitasLaboratorio = '%s'" % (cita_laboratorio.id)

    print(sql)

    cursor.execute(sql)
    cursor.fetchall()
    connection.commit()