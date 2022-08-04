import threading
import pyttsx3
from PyQt5.QtGui import QPixmap
import time

from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from BLOGICA.LOGIhr import *
from BLOGICA.LOGUsuario import *

# class Worker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)
#
#     def ejecucion_horaria(self):
#         global recordatorio
#         global usuario
#         self.Ihr_Form = Ihr_Form
#
#         log_ihr = LOGIhr
#         log_usuario = LOGUsuario
#         self._go = True
#         while(self._go):
#             print(f"[{time.ctime()}] >$ ", 'start')
#             recordatorios = log_ihr.consultar_db()
#             if recordatorios:
#                 recordatorio = recordatorios[0]
#                 usuario = log_usuario.buscar_usuario_recordatorio(self, recordatorio)
#                 self.Ihr_Form.ejecutar_recordatorio(recordatorio, usuario)
#                 print('OK')
#                 seconds = self.calcular_espera()
#                 time.sleep(seconds)
#             else:
#                 print(f"[{time.ctime()}] >$ ", 'sleep')
#                 seconds = self.calcular_espera()
#                 time.sleep(seconds)
#                 print(f"[{time.ctime()}] >$ ", 'return')


class Ihr_Form(QWidget):
    recordatrio = Recordatorio
    usuario = Usuario

    def __init__(self):
        super(Ihr_Form, self).__init__()
        loadUi('./ui/ihr.ui', self)

        hilo = threading.Thread(target=self.ejecucion_horaria)
        hilo.start()

        # self.thread = QThread()
        # self.worker = Worker()
        # self.worker.moveToThread(self.thread)
        # self.thread.started.connect(self.worker.ejecucion_horaria)
        # self.thread.start()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonAcceso.clicked.connect(self.acceso)
        self.pushButtonConfirmar.clicked.connect(self.confirmar)

    def ejecucion_horaria(self):
        global recordatorio
        global usuario
        self.Ihr_Form = Ihr_Form

        log_ihr = LOGIhr
        log_usuario = LOGUsuario
        self._go = True
        while (self._go):
            print(f"[{time.ctime()}] >$ ", 'start')
            recordatorios = log_ihr.consultar_db()
            if recordatorios:
                recordatorio = recordatorios[0]
                usuario = log_usuario.buscar_usuario_recordatorio(self, recordatorio)
                self.Ihr_Form.ejecutar_recordatorio(self, recordatorio, usuario)
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
        self._reminder = True
        self.contador = 1
        while (self._reminder == True and self.contador <= 4):
            if self.contador <= 3:
                self.Emoji.setVisible(True)
                ihr.iniciar_emocion(self, recordatorio, usuario, self.contador)
                time.sleep(5)
                self.contador += 1
            else:
                print('posponer')
                self.labelRecordatorio.setText('')
                self.Emoji.setVisible(False)
                break

            # self.movie = QMovie("./Iconos/giphy.gif")
            # self.Emoji.setMovie(self.movie)
            # self.iniciar_emocion_alegria()
            # time.sleep(5)

    def iniciar_emocion(self, recordatorio, usuario, contador):
        if contador == 1:
            print('alegria')
            self.labelRecordatorio.setText(
                'Hola %s, te recuerdo que tienes que tomar %s en 5 minutos' % (usuario.nombre, recordatorio.nombre))
            emoji_alegria = QPixmap('./Iconos/emoji-feliz.png')
            self.Emoji.setPixmap(emoji_alegria)
            self.Emoji.resize(20, 20)
            engine = pyttsx3.init()
            # engine.setProperty('voice', 'spanish-latin-am')
            engine.setProperty('voice', 'Spanish (Spain)')
            data = ('Hola %s, te recuerdo que tienes que tomar %s en 5 minutos' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()
            engine.stop()
            LOGIhr.mover_brazos_alegria()
        elif contador == 2:
            print('neutro')
            self.labelRecordatorio.setText('Hola %s, tienes que tomar %s en este momento' % (usuario.nombre, recordatorio.nombre))
            engine = pyttsx3.init()
            # engine.setProperty('voice', 'spanish-latin-am')
            engine.setProperty('voice', 'Spanish (Spain)')
            data = ('Hola %s, tienes que tomar %s en este momento' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()
            engine.stop()
        elif contador == 3:
            print('tristeza')
            self.labelRecordatorio.setText('%s, por favor tienes que tomar %s, ya te has pasado cinco minutos' % (
            usuario.nombre, recordatorio.nombre))
            emoji_tristeza = QPixmap('./Iconos/emoji-triste.png')
            self.Emoji.setPixmap(emoji_tristeza)
            self.Emoji.resize(20, 20)
            engine = pyttsx3.init()
            # engine.setProperty('voice', 'spanish-latin-am')
            engine.setProperty('voice', 'Spanish (Spain)')
            data = ('%s, por favor tienes que tomar %s, ya te has pasado cinco minutos' % (usuario.nombre, recordatorio.nombre))
            engine.say(data)
            engine.runAndWait()
            engine.stop()
            LOGIhr.mover_brazos_tristeza()

    def calcular_espera(self):
        hora_actual = datetime.today()
        h1 = hora_actual.time()
        print(h1.strftime('%H-%M-%S'))
        seconds = 60 - int(h1.strftime('%S'))
        print(seconds)
        return seconds

    def acceso(self):
        from AGUI.ui_bienvenida import Welcome_Form
        self.ui_welcome = Welcome_Form()
        self.ui_welcome.show()
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

    # def recordatorio(self, timeout, medicine):
    #     a = True
    #     while a:
    #         self.pushButtonConfirmar.clicked.connect(self.stop)
    #         # if ans == 'ok':
    #         #     break
    #
    #         # try:
    #         #     ans = inputimeout(f"[{time.ctime()}] >$ ", timeout=5)
    #         # except TimeoutOccurred:
    #         #     ans = ''
    #         # if ans != '':
    #         #     return 'ok'

    def confirmar(self):
        global recordatorio
        global usuario
        self._reminder = False
        self.labelRecordatorio.setText('')
        self.Emoji.setVisible(False)
        hora_actual = datetime.now().time()

        # LOGIhr.confirmar_medicamento(recordatorio, usuario, self.contador, hora_actual)
        # self.terminar_emocion_alegria()