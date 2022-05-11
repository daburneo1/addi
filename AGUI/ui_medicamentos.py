import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi

class Medicine_Form(QWidget):
    def __init__(self):
        super(Medicine_Form, self).__init__()
        loadUi('./ui/medicamentos.ui', self)

        widget = QWidget()
        layout = QVBoxLayout()

        # widget.setLayout(layout)
        # self.setCentralWidget(widget)

        self.pushButtonEliminar.clicked.connect(self.eliminar_medicamento)
        self.pushButtonMenu.clicked.connect(self.menu)


        self.pushButtonActualizar.clicked.connect(self.actualizar_tabla)
        self.pushButtonGuardar.clicked.connect(self.guardar_recordatorio)
        self.pushButtonCerrar.clicked.connect(lambda: self.close())

        #eliminar barra de titulo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #coneccion botones
        self.pushButtonDB.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_data_base))
        self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_agregar_recordatorio))
        self.pushButtonEditar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_editar_recordatorio))

        #ancho de columna
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def page_data_base(self):
        pass

    def page_agregar_recordatorio(self):
        pass

    def page_editar_recordatorio(self):
        pass

    def eliminar_medicamento(self):
        pass

    def menu(self):
        pass

    def actualizar_tabla(self):
        pass

    def guardar_recordatorio(self):
        pass






