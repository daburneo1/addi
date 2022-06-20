import threading

from BLOGICA.LOGIhr import *

from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class Ihr_Form(QWidget):

    def __init__(self):
        super(Ihr_Form, self).__init__()
        loadUi('./ui/ihr.ui', self)

        hilo = threading.Thread(target=self.ejecucion_horaria)
        hilo.start()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonAcceso.clicked.connect(self.acceso)
        self.pushButtonPosponer.clicked.connect(self.posponer)
        self.pushButtonConfirmar.clicked.connect(self.confirmar)
        self.pushButtonCancelar.clicked.connect(self.cancelar)

    def ejecucion_horaria(self):
        log_ihr = LOGIhr
        while(True):
            print(f"[{time.ctime()}] >$ ", 'start')
            recordatorios = log_ihr.consultar_db()
            if recordatorios:
                self.ejecutar_recordatorio(recordatorios)
                seconds = self.calcular_espera()
                time.sleep(seconds)
            else:
                print(f"[{time.ctime()}] >$ ", 'sleep')
                time.sleep(60)
                print(f"[{time.ctime()}] >$ ", 'return')

    def acceso(self):
        from AGUI.ui_login import Login_Form
        self.ui_login = Login_Form()
        self.ui_login.show()
        self.close()

    def ejecutar_recordatorio(self, recordatorios):
        s = "mustnotchange"
        while (True):
            s = self.input_with_timeout(s, 5, recordatorios[0])
            print(s)
            if s == "mustnotchange":
                print(f"\n[{time.ctime()}] Recordatorio en 5 minutos.")
                time.sleep(5)
            else:
                print(s)
                print("Gracias, hasta la próxima")
                break

    def input_with_timeout(self, default, timeout, medicine):
        print('Hola, te recuerdo que debes tomar en este momento ' + medicine.nombre)
        print('Presiona Enter para confirmar')
        pm = PromptManager(timeout)
        ans = pm.start()
        if isinstance(ans, str):
            return ans
        else:
            return default

    def calcular_espera(self):
        print()
        hora_actual = datetime.today()
        h1 = hora_actual.time()
        print(h1.strftime('%H-%M-%S'))
        seconds = 60 - int(h1.strftime('%S'))
        print(seconds)
        return seconds

    def posponer(self):
        pass

    def confirmar(self):
        pass

    def cancelar(self):
        pass