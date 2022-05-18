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
        self.pushButtonDB.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageDB))
        self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonEditar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio)

        #ancho de columna
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def page_data_base(self):
        pass

    def agregar_recordatorio(self):
        medicamento = self.lineEditMedicamento.text().capitalize()
        # tipo = self.comboBoxTipo.text()
        frecuencia = self.obtener_frecuencia()
        dosis = self.lineEditDosis.text()
        veces_dia = self.spinBoxVecesDia.text()
        numero_dias = self.spinBoxDias.text()

        print(medicamento, frecuencia, dosis, veces_dia, numero_dias)

    def obtener_frecuencia(self):
        print('frecuencia')
        frecuencia = []
        if self.checkBoxLunes.isChecked():
            frecuencia.append('Lunes')
        if self.checkBoxMartes.isChecked():
            frecuencia.append('Martes')
        if self.checkBoxMiercoles.isChecked():
            frecuencia.append('Miercoles')
        if self.checkBoxJueves.isChecked():
            frecuencia.append('Jueves')
        if self.checkBoxViernes.isChecked():
            frecuencia.append('Viernes')
        if self.checkBoxSabado.isChecked():
            frecuencia.append('Sabado')
        if self.checkBoxDomingo.isChecked():
            frecuencia.append('Domingo')
        return frecuencia

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






