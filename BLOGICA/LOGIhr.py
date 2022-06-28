from datetime import datetime, timedelta

from DATA.DATIhr import *
from DATA.DATUsuario import *
from BLOGICA.PromptManager import *

class LOGIhr():
    @classmethod
    def consultar_db(self):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_actual = datetime.today()
        hora_futura = hora_actual + timedelta(minutes=5)
        recordatorios = DATIhr.consultar_recordatorios(self, fecha_actual, hora_futura.strftime('%H:%M:00'))

        return recordatorios


