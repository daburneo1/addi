# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bienvenidaBuGRRd.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QMainWindow

from AGUI.ui_medicamentos import Medicine_Form
from CLASES.Usuario import Usuario


class Welcome_Form(QMainWindow):
    clicked = QtCore.pyqtSignal()
    usuario = Usuario("", "", "", "")
    def __init__(self):
        super(Welcome_Form, self).__init__()

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
        self.label.setGeometry(QRect(330, 20, 561, 441))
        self.label.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-radius:10px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 0, 341, 481))
        self.label_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.494, y1:0, x2:0.489, y2:1, stop:0 rgba(19, 84, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-radius:10px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(120, 30, 131, 61))
        font = QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 100, 301, 51))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(222, 222, 222)")
        self.label_Bienvenida = QLabel(self.widget)
        self.label_Bienvenida.setObjectName(u"label_Bienvenida")
        self.label_Bienvenida.setGeometry(QRect(480, 40, 311, 31))
        font2 = QFont()
        font2.setPointSize(20)
        self.label_Bienvenida.setFont(font2)
        self.pushButtonRecordatorio = QPushButton(self.widget)
        self.pushButtonRecordatorio.setObjectName(u"pushButtonRecordatorio")
        self.pushButtonRecordatorio.setGeometry(QRect(380, 200, 191, 61))
        font3 = QFont()
        font3.setPointSize(14)
        self.pushButtonRecordatorio.setFont(font3)
        self.pushButtonCumplimiento = QPushButton(self.widget)
        self.pushButtonCumplimiento.setObjectName(u"pushButtonCumplimiento")
        self.pushButtonCumplimiento.setGeometry(QRect(380, 300, 191, 61))
        self.pushButtonCumplimiento.setFont(font3)
        self.pushButtonCitaMedica = QPushButton(self.widget)
        self.pushButtonCitaMedica.setObjectName(u"pushButtonCitaMedica")
        self.pushButtonCitaMedica.setGeometry(QRect(640, 200, 191, 61))
        self.pushButtonCitaMedica.setFont(font3)
        self.pushButtonExamenLaboratorio = QPushButton(self.widget)
        self.pushButtonExamenLaboratorio.setObjectName(u"pushButtonExamenLaboratorio")
        self.pushButtonExamenLaboratorio.setGeometry(QRect(640, 300, 191, 61))
        font4 = QFont()
        font4.setPointSize(12)
        self.pushButtonExamenLaboratorio.setFont(font4)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(400, 130, 141, 31))
        font5 = QFont()
        font5.setPointSize(16)
        self.label_6.setFont(font5)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(700, 130, 51, 31))
        self.label_7.setFont(font5)
        self.pushButtonSalir = QPushButton(self.widget)
        self.pushButtonSalir.setObjectName(u"pushButtonSalir")
        self.pushButtonSalir.setGeometry(QRect(560, 400, 111, 41))
        self.pushButtonSalir.setFont(font3)

        self.retranslateUi(self)

        QMetaObject.connectSlotsByName(self)

        # self.pushButtonCancelar.clicked.connect(self.cerrar_ventana)
        self.pushButtonRecordatorio.clicked.connect(self.medicine_window)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"ADDI", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Tu asistente m\u00e9dico personalizado", None))
        self.label_Bienvenida.setText(QCoreApplication.translate("Form", u"Bienvenido", None))
        self.pushButtonRecordatorio.setText(QCoreApplication.translate("Form", u"Recordatorios", None))
        self.pushButtonCumplimiento.setText(QCoreApplication.translate("Form", u"Historial", None))
        self.pushButtonCitaMedica.setText(QCoreApplication.translate("Form", u"Citas M\u00e9dicas", None))
        self.pushButtonExamenLaboratorio.setText(QCoreApplication.translate("Form", u"Ex\u00e1menes de Laboratorio", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Medicamentos", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Citas", None))
        self.pushButtonSalir.setText(QCoreApplication.translate("Form", u"Salir", None))
    # retranslateUi

    def get_user(self, user):
        self.usuario = user
        print("///////////")
        print(self.usuario)

    def medicine_window(self):
        # self.form_medicine = QtWidgets.QMainWindow()
        self.ui_medicine = Medicine_Form()
        self.ui_medicine.show()

    def cerrar_ventana(self):
        self.close()



