import pymysql

from CLASES.Recordatorio import Recordatorio
from DATA.DATCursor import *

class DATIhr():
    # @classmethod
    def consultar_recordatorios(self, fecha_actual, hora_futura):
        sql = "SELECT idRecordatorio, idMedicamentos, hora, nombre, dosis, frecuencia " \
              "FROM recordatoriomedicamento " \
              "INNER JOIN medicamento ON medicamento.idmedicamentos = recordatoriomedicamento.Medicamento_idMedicamentos " \
              "WHERE hora = '%s' and fecha_hasta < '%s'" %(hora_futura, fecha_actual)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        recordatorios = []

        for x in data:
            recordatorio = Recordatorio(x[0], x[1], x[2], x[3], x[4], x[5])
            recordatorios.append(recordatorio)
        return recordatorios