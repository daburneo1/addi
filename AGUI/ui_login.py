# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginoVaSdW.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 500)
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Form.setMinimumSize(QSize(900, 500))
        Form.setMaximumSize(QSize(900, 500))
        self.widget = QWidget(Form)
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
        self.label.setGeometry(QRect(460, 20, 431, 441))
        self.label.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 461, 481))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494, y1:0, x2:0.489, y2:1, stop:0 rgba(19, 84, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(580, 60, 191, 31))
        self.label_3.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 79, 86)\n"
"")
        self.lineEditUser = QLineEdit(self.widget)
        self.lineEditUser.setObjectName(u"lineEditUser")
        self.lineEditUser.setGeometry(QRect(500, 120, 361, 31))
        font = QFont()
        font.setPointSize(18)
        self.lineEditUser.setFont(font)
        self.lineEditUser.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.lineEditPass = QLineEdit(self.widget)
        self.lineEditPass.setObjectName(u"lineEditPass")
        self.lineEditPass.setGeometry(QRect(500, 200, 361, 31))
        self.lineEditPass.setFont(font)
        self.lineEditPass.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:2px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,200);\n"
"color:rgb(0,0,0);\n"
"padding-bottom: 7px;")
        self.lineEditPass.setEchoMode(QLineEdit.Password)
        self.pushButtonLogin = QPushButton(self.widget)
        self.pushButtonLogin.setObjectName(u"pushButtonLogin")
        self.pushButtonLogin.setGeometry(QRect(500, 260, 361, 71))
        self.pushButtonLogin.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";")
        self.pushButtonRegistrarse = QPushButton(self.widget)
        self.pushButtonRegistrarse.setObjectName(u"pushButtonRegistrarse")
        self.pushButtonRegistrarse.setGeometry(QRect(500, 350, 171, 71))
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButtonRegistrarse.setFont(font1)
        self.pushButtonForgot = QPushButton(self.widget)
        self.pushButtonForgot.setObjectName(u"pushButtonForgot")
        self.pushButtonForgot.setGeometry(QRect(690, 350, 171, 71))
        font2 = QFont()
        font2.setPointSize(10)
        self.pushButtonForgot.setFont(font2)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 30, 131, 61))
        font3 = QFont()
        font3.setPointSize(35)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 100, 421, 51))
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color:rgb(222, 222, 222)")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 150, 411, 301))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.pushButtonLogin.clicked.connect(self.presentarUsuario)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Inicio de Sesi\u00f3n", None))
        self.lineEditUser.setPlaceholderText(QCoreApplication.translate("Form", u"Usuario", None))
        self.lineEditPass.setPlaceholderText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pushButtonLogin.setText(QCoreApplication.translate("Form", u"Iniciar Sesi\u00f3n", None))
        self.pushButtonRegistrarse.setText(QCoreApplication.translate("Form", u"Registrarse", None))
        self.pushButtonForgot.setText(QCoreApplication.translate("Form", u"Olvidaste tu contrase\u00f1a?", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ADDI", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Bienvenido a tu asistente m\u00e9dico personalizado", None))
        self.label_6.setText("")
    # retranslateUi

    def presentarUsuario(self):
        print(self.lineEditUser.text())
        print(self.lineEditPass.text())

# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     Form = QtWidgets.QWidget()
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show()
#     sys.exit(app.exec_())
