from datetime import datetime

from DATA.DATIhr import *
from BLOGICA.PromptManager import *

class LOGIhr():
    @classmethod
    def consultar_db(self):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_actual = datetime.today()
        hora_futura = hora_actual.replace(minute=int(hora_actual.strftime('%M')) + 5)
        if int(hora_actual.strftime('%M')) < 55:
            recordatorios = DATIhr.consultar_recordatorios(self, fecha_actual, hora_futura.strftime('%H:%M:00'))
            return recordatorios
        else:
            return None

