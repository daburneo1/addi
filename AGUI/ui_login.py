
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5 import QtCore
from PyQt5.uic import loadUi

from tkinter import messagebox

from AGUI.ui_registro import Register_Form as Register_Form
from BLOGICA.LOGUsuario import *
from CLASES.Usuario import *


class Login_Form(QWidget):
    log_usuario = LOGUsuario
    def __init__(self):
        super(Login_Form, self).__init__()
        loadUi('./ui/login.ui', self)

        widget = QWidget()
        layout = QVBoxLayout()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonLogin.clicked.connect(self.buscar_usuario)
        self.pushButtonRegistrarse.clicked.connect(self.register_window)

    def buscar_usuario(self):
        credenciales = Usuario(self.lineEditCedula.text(),
                            "","",
                            self.lineEditPass.text())

        c_usuario = self.log_usuario.buscar_usuario(self, credenciales)

        if(c_usuario):
            credencial_valida = self.log_usuario.validar_credenciales(self, c_usuario, credenciales)
            if credencial_valida == 1:
                self.welcome_window()
                self.set_welcome_info(c_usuario)
            else:
                messagebox.showerror(message="Contraseña incorrecta", title="Error")
        else:
            messagebox.showerror(message="La cédula ingresada no se encuentra registrada", title="Error")

    def register_window(self):
        self.ui_register = Register_Form()
        self.ui_register.show()

    def set_welcome_info(self, c_usuario):
        from AGUI.ui_bienvenida import Welcome_Form
        Welcome_Form.get_user(self, c_usuario)

    def welcome_window(self):
        from AGUI.ui_bienvenida import Welcome_Form
        self.form_welcome = QtWidgets.QMainWindow()
        self.ui_welcome = Welcome_Form()
        self.ui_welcome.show()
        self.close()