
import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from tkinter import messagebox

from PyQt5.uic import loadUi

from CLASES.Usuario import *
from BLOGICA.LOGUsuario import *

class Register_Form(QWidget):
    log_usuario = LOGUsuario()
    def __init__(self):
        super(Register_Form, self).__init__()
        loadUi('./ui/registro.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.pushButtonRegistrarse.clicked.connect(self.registrar_usuario)
        self.pushButtonCancelar.clicked.connect(self.cerrar_ventana)

    def registrar_usuario(self):
        campos_vacios = self.validar_campos_vacios()
        check_password = self.validar_password()

        usuario = Usuario(self.lineEditCedula.text(),
                          self.lineEditNombre.text(),
                          self.lineEditApellido.text(),
                          self.lineEditPass.text())

        print(usuario)
        if campos_vacios == 1 and check_password == 1:
            print(usuario)
            registro = self.log_usuario.registrar_usuario(usuario)
            if registro == 2:
                messagebox.showerror(message="El número de cédula ingresado ya se encuentra registrado en el sistema", title="Error")
            elif registro == 3:
                messagebox.showerror(message="El número de cédula ingresado no es válido", title="Error")
            elif registro == 1:
                messagebox.showinfo(message="Usuario registrado", title="Atención")
                self.cerrar_ventana()

    def validar_campos_vacios(self):
        if not self.lineEditCedula.text():
            messagebox.showinfo(message="Debe ingresar su número de cédula", title="Advertencia")
            return 0

        elif not self.lineEditNombre.text():
            messagebox.showinfo(message="Debe ingresar un nombre", title="Advertencia")
            return 0

        elif not self.lineEditApellido.text():
            messagebox.showinfo(message="Debe ingresar un apellido", title="Advertencia")
            return 0

        elif not self.lineEditPass.text():
            messagebox.showinfo(message="Por favor ingrese una contraseña", title="Advertencia")
            return 0

        elif not self.lineEditPass2.text():
            messagebox.showinfo(message="Por favor repita su contraseña", title="Advertencia")
            return 0
        else:
            return 1

    def validar_password(self):
        if self.lineEditPass.text() == self.lineEditPass2.text():
            return 1
        else:
            messagebox.showinfo(message="Las contraseñas ingresadas no coinciden", title="Advertencia")
            return 0

    def cerrar_ventana(self):
        self.close()
