import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="addi"
)

cursor = connection.cursor()

class DATUsuario():

    def RegistrarUsuario(self, usuario):
        sql = "INSERT INTO Usuario (cedula, nombre, apellido, pass) VALUES (" \
              "'%s','%s','%s','%s')" %(usuario.cedula, usuario.nombre, usuario.apellido, usuario.password)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def BuscarUsuario(self, usuario):
        sql = "SELECT * FROM Usuario WHERE cedula = '%s'" %(usuario.cedula)

        print(sql)

        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()

        for i in datos:
            print(i)
