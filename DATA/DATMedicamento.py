import pymysql
from DATA.DATCursor import *

class DATMedicamento():

    def buscar_tipo_medicamento(self):
        sql = "SELECT * FROM tipomedicamento"
        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        tipo_medicamento = []
        print(data[1])

        for x in data:
            tipo_medicamento.append(x)
        return tipo_medicamento

    def agregar_medicamento(self, medicamento, usuario):
        sql = "INSERT INTO medicamento (nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, idtipomedicamento, cedula) VALUES ("\
              "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.fecha_desde, medicamento.fecha_hasta, medicamento.tipo, '1104745540')

        print(sql)

        # cursor.execute(sql)
        # connection.commit()

    def consultar_id_medicamento(self, medicamento):
        sql = "SELECT idMedicamentos FROM medicamento WHERE nombre = '%s' AND dosis = '%s'" % (medicamento.nombre, medicamento.dosis)
        print(sql)

        cursor.execute(sql)
        id_medicamento = cursor.fetchall()
        print(id_medicamento)
        return id_medicamento

    def agregar_recordatorio(self, medicamento):
        for x in medicamento.horario:
            sql = "INSERT INTO recordatoriomedicamento (hora, idMedicamentos, cedulaUsuario) VALUES (" \
                  "'%s', '%s', '%s')" %(x, '0', '1104745540')
            print(sql)