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

    def agregar_medicamento(self, medicamento):
        sql = "INSERT INTO medicamento (nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, idtipomedicamento) VALUES ("\
              "'%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.fecha_desde, medicamento.fecha_hasta, medicamento.tipo)

        print(sql)