import threading
import time

import pyttsx3
from PyQt5.QtCore import QTimer, QDateTime, QThread, QObject, pyqtSignal
from PyQt5.QtGui import QMovie

from BLOGICA.LOGIhr import *

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from BLOGICA.LOGUsuario import *


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
        self.pushButtonConfirmar.clicked.connect(self.stop)
        self.pushButtonCancelar.clicked.connect(self.cancelar)


    def ejecucion_horaria(self):
        log_ihr = LOGIhr
        log_usuario = LOGUsuario
        self._go = True
        while(self._go):
            print(f"[{time.ctime()}] >$ ", 'start')
            recordatorios = log_ihr.consultar_db()
            if recordatorios:
                recordatorio = recordatorios[0]
                usuario = log_usuario.buscar_usuario_recordatorio(self, recordatorio)
                self.ejecutar_recordatorio(recordatorio, usuario)
                print('OK')
                seconds = self.calcular_espera()
                time.sleep(seconds)
            else:
                print(f"[{time.ctime()}] >$ ", 'sleep')
                seconds = self.calcular_espera()
                time.sleep(seconds)
                print(f"[{time.ctime()}] >$ ", 'return')

    def ejecutar_recordatorio(self, recordatorio, usuario):
        ihr = Ihr_Form
        self._go = True
        self.contador = 1
        while (self._go and self.contador <= 4):
            if self.contador <= 3:
                ihr.iniciar_emocion(self, recordatorio, usuario, self.contador)
                time.sleep(5)
                self.contador += 1
            else:
                print('posponer')
                break
            # self.labelRecordatorio.setText('Hola, te recuerdo que debes tomar en este momento ' + medicine.nombre)
            # self.movie = QMovie("./Iconos/giphy.gif")
            # self.Emoji.setMovie(self.movie)
            # self.iniciar_emocion_alegria()
            # time.sleep(5)

    def iniciar_emocion(self, recordatorio, usuario, contador):
        engine = pyttsx3.init()
        engine.setProperty('voice', 'spanish-latin-am')
        if contador == 1:
            print('alegria')
            self.labelRecordatorio.setText('Hola %s, te recuerdo que tienes que tomar %s en 5 minutos' % (usuario.nombre, recordatorio.nombre))
            data = ('Hola %s, te recuerdo que tienes que tomar %s en 5 minutos' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()
        elif contador == 2:
            print('neutro')
            self.labelRecordatorio.setText('Hola %s, tienes que tomar %s en este momento' % (usuario.nombre, recordatorio.nombre))
            data = ('Hola %s, tienes que tomar %s en este momento' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()
        elif contador == 3:
            print('tristeza')
            self.labelRecordatorio.setText('%s, por favor tienes que tomar %s, ya te has pasado cinco minutos de tu horario' % (usuario.nombre, recordatorio.nombre))
            data = ('%s, por favor tienes que tomar %s, ya te has pasado cinco minutos de tu horario' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()

    def calcular_espera(self):
        hora_actual = datetime.today()
        h1 = hora_actual.time()
        print(h1.strftime('%H-%M-%S'))
        seconds = 60 - int(h1.strftime('%S'))
        print(seconds)
        return seconds

    def acceso(self):
        from AGUI.ui_login import Login_Form
        self.ui_login = Login_Form()
        self.ui_login.show()
        self.close()

    # def ejecutar_recordatorio(self, recordatorios):
    #     self._go = True
    #     s = "mustnotchange"
    #     while (self._go):
    #         print('Bucle')
    #         s = self.input_with_timeout(s, 5, recordatorios[0])
    #         print(s)
    #         if s == "mustnotchange":
    #             print(f"\n[{time.ctime()}] Recordatorio en 5 minutos.")
    #             time.sleep(5)
    #         else:
    #             print(s)
    #             print("Gracias, hasta la próxima")
    #             break

    def terminar_emocion_alegria(self):
        self.movie.stop()

    def recordatorio(self, timeout, medicine):
        a = True
        while a:
            self.pushButtonConfirmar.clicked.connect(self.stop)
            # if ans == 'ok':
            #     break

            # try:
            #     ans = inputimeout(f"[{time.ctime()}] >$ ", timeout=5)
            # except TimeoutOccurred:
            #     ans = ''
            # if ans != '':
            #     return 'ok'

    def stop(self):
        self._go = False
        # self.terminar_emocion_alegria()

    def posponer(self):
        pass

    def confirmar(self):
        pass

    def cancelar(self):
        pass