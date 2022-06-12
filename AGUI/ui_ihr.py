from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtCore


class Ihr_Form(QWidget):

    def __init__(self):
        super(Ihr_Form, self).__init__()
        loadUi('./ui/ihr.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonAcceso.clicked.connect(self.acceso)
        self.pushButtonPosponer.clicked.connect(self.posponer)
        self.pushButtonConfirmar.clicked.connect(self.confirmar)
        self.pushButtonCancelar.clicked.connect(self.cancelar)

    def acceso(self):
        from AGUI.ui_login import Login_Form
        self.ui_login = Login_Form()
        self.ui_login.show()
        self.close()

    def posponer(self):
        pass

    def confirmar(self):
        pass

    def cancelar(self):
        pass