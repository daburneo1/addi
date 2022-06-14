from datetime import datetime

from DATA.DATIhr import *
from BLOGICA.PromptManager import *

class LOGIhr():
    @classmethod
    def consultar_db(self):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_actual = datetime.today()
        hora_futura = hora_actual.replace(minute=int(hora_actual.strftime('%M'))+5)
        # OJO, cambiar por las variables definidas

        # recordatorios = DATIhr.consultar_recordatorios(self, fecha_actual, hora_futura.strftime('%H:%M:00'))

        recordatorios = DATIhr.consultar_recordatorios(self, '2022-06-20', '20:00:00')

        if recordatorios:
            # for recordatorio in recordatorios:
            s = "mustnotchange"
            while(True):
                s = self.input_with_timeout(s, 5, recordatorios[0])
                if s == "mustnotchange":
                    print(f"\n[{time.ctime()}] Recordatorio en 5 minutos.")
                    time.sleep(5)
                else:
                    print("Gracias, hasta la próxima")
                    break
        print('Fin')

    def input_with_timeout(default, timeout, medicine):
        print('Hola, te recuerdo que debes tomar en este momento ' + medicine.nombre)
        print('Presiona Enter para confirmar')
        pm = PromptManager(timeout)
        ans = pm.start()
        if isinstance(ans, str):
            return ans
        else:
            return default