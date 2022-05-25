import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi

from BLOGICA.LOGMedicamento import *

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
        self.pushButtonRegistrar.clicked.connect(self.registrar)
        self.pushButtonEditar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio)

        #ancho de columna
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def cargar_tipo_medicina(self):
        tipo_medicina = LOGMedicamento.buscar_tipo_medicamento(self)
        print(tipo_medicina)

    def page_data_base(self):
        pass

    def registrar(self):
        self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        tipo_medicina = LOGMedicamento.buscar_tipo_medicamento(self)
        print(tipo_medicina[2])

        for x in tipo_medicina:
            self.comboBoxTipo.addItem(x[1])
            # self.comboBoxTipo.setCurrentIndex(-1)

    def agregar_recordatorio(self):
        nombre = self.lineEditMedicamento.text().capitalize()
        tipo = self.comboBoxTipo.currentIndex()
        frecuencia = self.obtener_frecuencia()
        dosis = self.lineEditDosis.text()
        veces_dia = self.spinBoxVecesDia.text()
        fecha_desde = self.obtener_fecha_actual()
        numero_dias = self.spinBoxDias.text()
        fecha_hasta = self.obtener_fecha_final(fecha_desde, numero_dias)

        # print(medicamento, tipo, frecuencia, dosis, veces_dia, numero_dias)
        medicamento = Medicamento(nombre, tipo, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta)
        # print(medicamento.presentar_medicamento())

        LOGMedicamento.agregar_medicamento(self, medicamento)

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

    def obtener_fecha_actual(self):
        from datetime import date
        fecha = date.today()
        return fecha

    def obtener_fecha_final(self, fecha_actual, numero_dias):
        from datetime import date, timedelta
        td = timedelta(int(numero_dias))
        fecha_final = fecha_actual + td
        return fecha_final

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






