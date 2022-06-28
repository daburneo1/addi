import pymysql
from DATA.DATCursor import *
from CLASES.Usuario import *

class DATUsuario():

    def registrar_usuario(self, usuario):
        sql = "INSERT INTO usuario (cedula, nombre, apellido, pass) VALUES (" \
              "'%s','%s','%s','%s')" %(usuario.cedula, usuario.nombre, usuario.apellido, usuario.password)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def buscar_usuario(self, credencial):
        sql = "SELECT * FROM usuario WHERE cedula = '%s'" %(credencial.cedula)

        print(sql)

        cursor.execute(sql)
        datos = cursor.fetchall()
        connection.commit()

        if datos:
            usuario = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
            return usuario
        return None

    def buscar_usuario_recordatorio(self, recordatorio):
        sql = "SELECT nombre, apellido, cedula FROM usuario WHERE cedula = (SELECT cedula FROM recordatoriomedicamento INNER JOIN medicamento ON medicamento.idmedicamentos = recordatoriomedicamento.Medicamento_idMedicamentos WHERE idRecordatorio = %s);" %(recordatorio.id)

        print(sql)

        cursor.execute(sql)
        datos = cursor.fetchall()
        connection.commit()

        if datos:
            usuario = Usuario(datos[0][2], datos[0][0], datos[0][1], '')
            return usuario
        return None