import pymysql
from DATA.DATCursor import *
from CLASES.Usuario import *

class DATUsuario():

    def registrar_usuario(self, usuario):
        sql = "INSERT INTO Usuario (cedula, nombre, apellido, pass) VALUES (" \
              "'%s','%s','%s','%s')" %(usuario.cedula, usuario.nombre, usuario.apellido, usuario.password)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def buscar_usuario(self, credencial):
        sql = "SELECT * FROM Usuario WHERE cedula = '%s'" %(credencial.cedula)

        print(sql)

        cursor.execute(sql)
        datos = cursor.fetchall()

        if datos:
            usuario = Usuario(datos[0][0], datos[0][1], datos[0][2], datos[0][3])
            return usuario
        return None
