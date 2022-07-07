from datetime import datetime, timedelta

from DATA.DATIhr import *
from DATA.DATUsuario import *

class LOGIhr():
    @classmethod
    def consultar_db(self):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_actual = datetime.today()
        hora_futura = hora_actual + timedelta(minutes=5)
        recordatorios = DATIhr.consultar_recordatorios(self, fecha_actual, hora_futura.strftime('%H:%M:00'))

        return recordatorios

    @classmethod
    def confirmar_medicamento(cls, recordatorio, usuario, contador, hora_actual):
        print('confirmar')
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_programada = recordatorio.hora
        print(hora_programada)
        print(type(hora_programada))
        hora_actual = timedelta(hours = hora_actual.hour, minutes = hora_actual.minute, seconds=00)

        if hora_actual <= hora_programada:
            hora_actual = hora_programada
            DATIhr.confirmar_medicamento(fecha_actual, hora_programada, hora_actual, usuario, recordatorio)
        else:
            DATIhr.confirmar_medicamento(fecha_actual, hora_programada, hora_actual, usuario, recordatorio)
        print(hora_actual)


