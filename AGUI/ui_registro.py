# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registrooMIASN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QSpinBox
from tkinter import messagebox

from CLASES.Usuario import *
from BLOGICA.LOGUsuario import *

class Register_Form(QWidget):
    clicked = QtCore.pyqtSignal()
    def __init__(self):
        super(Register_Form, self).__init__()

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resize(900, 500)
        self.setMinimumSize(QSize(900, 500))
        self.setMaximumSize(QSize(900, 500))
        self.widget = QWidget(self)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 10, 901, 491))
        self.widget.setStyleSheet(u"QPushButton{\n"
"	background-color:rgba(0, 52, 59, 1);\n"
"	color:rgba(255,255,255,200);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(0, 119, 123, 1);\n"
"	background-position:calc(100% - 10px)center;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(0, 174, 173, 1);\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 20, 631, 441))
        self.label.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 271, 481))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494, y1:0, x2:0.489, y2:1, stop:0 rgba(19, 84, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 40, 291, 31))
        self.label_3.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 79, 86)\n"
"")
        self.lineEditNombre = QLineEdit(self.widget)
        self.lineEditNombre.setObjectName(u"lineEditNombre")
        self.lineEditNombre.setGeometry(QRect(310, 150, 241, 41))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lineEditNombre.setFont(font)
        self.lineEditNombre.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.pushButtonRegistrarse = QPushButton(self.widget)
        self.pushButtonRegistrarse.setObjectName(u"pushButtonRegistrarse")
        self.pushButtonRegistrarse.setGeometry(QRect(620, 380, 171, 61))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButtonRegistrarse.setFont(font1)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(70, 30, 131, 61))
        font2 = QFont()
        font2.setPointSize(35)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 100, 221, 41))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        font3.setUnderline(False)
        font3.setWeight(75)
        font3.setStrikeOut(False)
        self.label_5.setFont(font3)
        self.label_5.setStyleSheet(u"color:rgb(222, 222, 222)")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 130, 191, 41))
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color:rgb(222, 222, 222)")
        self.lineEditApellido = QLineEdit(self.widget)
        self.lineEditApellido.setObjectName(u"lineEditApellido")
        self.lineEditApellido.setGeometry(QRect(600, 150, 241, 41))
        font4 = QFont()
        font4.setPointSize(18)
        self.lineEditApellido.setFont(font4)
        self.lineEditApellido.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.lineEditPass = QLineEdit(self.widget)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setGeometry(QRect(310, 220, 401, 31))
        self.lineEditPass.setFont(font4)
        self.lineEditPass.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.lineEditPass.setEchoMode(QLineEdit.Password)
        self.lineEditPass2 = QLineEdit(self.widget)
        self.lineEditPass2.setObjectName(u"lineEditPass2")
        self.lineEditPass2.setGeometry(QRect(310, 290, 401, 31))
        self.lineEditPass2.setFont(font4)
        self.lineEditPass2.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.lineEditPass2.setEchoMode(QLineEdit.Password)
        self.pushButtonCancelar = QPushButton(self.widget)
        self.pushButtonCancelar.setObjectName(u"pushButtonCancelar")
        self.pushButtonCancelar.setGeometry(QRect(370, 380, 171, 61))
        self.pushButtonCancelar.setFont(font1)
        self.lineEditCedula = QLineEdit(self.widget)
        self.lineEditCedula.setObjectName(u"lineEditCedula")
        self.lineEditCedula.setGeometry(QRect(310, 80, 241, 41))
        self.lineEditCedula.setFont(font)
        self.lineEditCedula.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        self.pushButtonRegistrarse.clicked.connect(self.registrarUsuario)
        self.pushButtonCancelar.clicked.connect(self.cerrarVentana)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Registrar nuevo usuario", None))
        self.lineEditNombre.setPlaceholderText(QCoreApplication.translate("Form", u"Nombre", None))
        self.pushButtonRegistrarse.setText(QCoreApplication.translate("Form", u"Registrarse", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ADDI", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Bienvenido a tu asistente", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"m\u00e9dico personalizado", None))
        self.lineEditApellido.setPlaceholderText(QCoreApplication.translate("Form", u"Apellido", None))
        self.lineEditPass.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.lineEditPass2.setPlaceholderText(QCoreApplication.translate("Form", u"Confirmar Contrase\u00f1a", None))
        self.pushButtonCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.lineEditCedula.setPlaceholderText(QCoreApplication.translate("Form", u"C\u00e9dula", None))
    # retranslateUi

    def registrarUsuario(self):
        campos_vacios = self.validarCamposVacios()
        check_password = self.validarPassword()

        usuario = Usuario(self.lineEditCedula.text(),
                          self.lineEditNombre.text(),
                          self.lineEditApellido.text(),
                          self.lineEditPass.text())

        print(usuario.presentar_usuario())
        if campos_vacios == 1 and check_password == 1:
            print(usuario.presentar_usuario())
            LOGUsuario.RegistrarUsuario(self, usuario)

    def validarCamposVacios(self):
        if not self.lineEditCedula.text():
            messagebox.showinfo(message="Debe ingresar su número de cédula", title="Advertencia")

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

    def validarPassword(self):
        if self.lineEditPass.text() == self.lineEditPass2.text():
            return 1
        else:
            messagebox.showinfo(message="Las contraseñas ingresadas no coinciden", title="Advertencia")
            return 0

    def cerrarVentana(self):
        self.close()
