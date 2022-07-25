from CLASES.Recordatorio import Recordatorio
from DATA.DATCursor import *

class DATIhr():
    def consultar_recordatorios(self, fecha_actual, hora_futura):
        sql = "SELECT idRecordatorio, idMedicamento, hora, nombre, dosis, frecuencia " \
              "FROM recordatoriomedicamento " \
              "INNER JOIN medicamento ON medicamento.idMedicamento = recordatoriomedicamento.medicamento_idMedicamento " \
              "WHERE hora = '%s' and fecha_hasta > '%s'" %(hora_futura, fecha_actual)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        recordatorios = []

        for x in data:
            recordatorio = Recordatorio(x[0], x[1], x[2], x[3], x[4], x[5])
            recordatorios.append(recordatorio)
        return recordatorios

    @classmethod
    def confirmar_medicamento(cls, fecha_actual, hora_programada, hora_actual, usuario, recordatorio):
        # sql = "INSERT INTO confirmaciones (fecha, horaProgramada, horaConfirmacion, cedula, idMedicamentos) VALUES (" \
        #       "'%s', '%s', '%s', '%s', '%s')" %(fecha_actual, hora_programada, hora_actual, usuario.cedula, recordatorio.idMedicamento)

        sql = "INSERT INTO confirmaciones (horaProgramada, horaConfirmacion, cedula, idMedicamentos) VALUES (" \
              "'%s', '%s', '%s', '%s')" % (
              hora_programada, hora_actual, usuario.cedula, recordatorio.idMedicamento)

        print(sql)

        cursor.execute(sql)
        connection.commit()

