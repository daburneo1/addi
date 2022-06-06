
from PyQt5.QtWidgets import QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore

from AGUI.ui_login import Login_Form
from AGUI.ui_medicamentos import Medicine_Form
from CLASES.Usuario import Usuario


class Welcome_Form(QWidget):
    usuario = Usuario("", "", "", "")
    def __init__(self):
        super(Welcome_Form, self).__init__()
        loadUi('./ui/bienvenida.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonSalir.clicked.connect(self.cerrar_ventana)
        self.pushButtonRecordatorio.clicked.connect(self.medicine_window)

    def get_user(self, user):
        self.usuario = user
        Medicine_Form.get_user(self, user)

    def medicine_window(self):
        # self.form_medicine = QtWidgets.QMainWindow()
        self.ui_medicine = Medicine_Form()
        self.ui_medicine.show()

    def cerrar_ventana(self):
        # self.form_welcome = QtWidgets.QMainWindow()
        self.ui_login = Login_Form()
        self.ui_login.show()
        self.close()



