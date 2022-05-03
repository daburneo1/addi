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
        sql = "INSERT INTO Usuario (nombre, apellido, edad, user, pass) VALUES (" \
              "'%s','%s','%s','%s','%s')" %(usuario.nombre, usuario.apellido, usuario.edad, usuario.user, usuario.password)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def BuscarUsuario(self, usuario):

