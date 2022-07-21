
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from AGUI.ui_cita_laboratorio import Laboratory_Form
from AGUI.ui_cita_medica import Appointment_Form
from AGUI.ui_login import Login_Form
from AGUI.ui_medicamentos import Medicine_Form
from CLASES.Usuario import Usuario

usuario = ''
class Welcome_Form(QWidget):

    def __init__(self):
        super(Welcome_Form, self).__init__()
        loadUi('./ui/bienvenida.ui', self)

        self.label_Bienvenida.setText('Bienvenido')

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonSalir.clicked.connect(self.cerrar_ventana)
        self.pushButtonRecordatorio.clicked.connect(self.medicine_window)
        self.pushButtonCitaMedica.clicked.connect(self.appointment_window)
        self.pushButtonExamenLaboratorio.clicked.connect(self.laboratory_window)

    def get_user(self, user):
        global usuario
        usuario = user
        Medicine_Form.get_user(self, user)
        Appointment_Form.get_user(self, user)
        Laboratory_Form.get_user(self, user)

    def medicine_window(self):
        self.ui_medicine = Medicine_Form()
        self.ui_medicine.show()

    def appointment_window(self):
        self.ui_appointment = Appointment_Form()
        self.ui_appointment.show()

    def laboratory_window(self):
        self.ui_laboratory = Laboratory_Form()
        self.ui_laboratory.show()

    def cerrar_ventana(self):
        self.ui_login = Login_Form()
        self.ui_login.show()
        self.close()



