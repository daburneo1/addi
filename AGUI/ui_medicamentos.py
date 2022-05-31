import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from tkinter import messagebox

from BLOGICA.LOGMedicamento import *
from CLASES.Usuario import *

usuario = ""

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
        self.stackedWidget.setCurrentWidget(self.pageDB)
        # self.pushButtonDB.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageDB))
        self.pushButtonDB.clicked.connect(self.page_db)
        self.pushButtonActualizar.clicked.connect(self.page_db)
        # self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonRegistrar.clicked.connect(self.registrar)
        self.pushButtonEditar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio)

        #ancho de columna
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_user(self, user):
        global usuario
        usuario = user
        # print(self.usuario)

    def cargar_tipo_medicina(self):
        tipo_medicina = LOGMedicamento.buscar_tipo_medicamento(self)
        print(tipo_medicina)

    def page_db(self):
        self.stackedWidget.setCurrentWidget(self.pageDB)
        medicamentos = LOGMedicamento.cargar_medicamentos(self)
        i = len(medicamentos)
        self.tableMedicamentos.setRowCount(i)
        tablerow = 0
        for row in medicamentos:
            self.tableMedicamentos.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableMedicamentos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[6])))
            self.tableMedicamentos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableMedicamentos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableMedicamentos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[3])))
            # self.tableMedicamentos.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            tablerow+=1

    def registrar(self):
        self.stackedWidget.setCurrentWidget(self.pageRegistrar)
        self.spinBoxVecesDia.setValue(1)
        self.spinBoxVecesDia.valueChanged.connect(self.value_change)
        # self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        tipo_medicina = LOGMedicamento.buscar_tipo_medicamento(self)
        print(tipo_medicina[2])

        for x in tipo_medicina:
            self.comboBoxTipo.addItem(x[1])
            # self.comboBoxTipo.setCurrentIndex(-1)

    def agregar_recordatorio(self):
        nombre = self.lineEditMedicamento.text().capitalize()
        tipo = self.comboBoxTipo.currentIndex() + 1
        frecuencia = self.obtener_frecuencia()
        dosis = self.lineEditDosis.text()
        veces_dia = self.spinBoxVecesDia.text()
        fecha_desde = self.obtener_fecha_actual()
        numero_dias = self.spinBoxDias.text()
        fecha_hasta = self.obtener_fecha_final(fecha_desde, numero_dias)

        horario = self.obtener_horario()

        # print(medicamento, tipo, frecuencia, dosis, veces_dia, numero_dias)
        medicamento = Medicamento(nombre, tipo, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, horario)
        # print(medicamento.presentar_medicamento())
        print(usuario)
        try:
            LOGMedicamento.agregar_medicamento(self, medicamento, usuario)
            LOGMedicamento.agregar_recordatorio(self, medicamento, usuario)
            messagebox.showinfo(message="El recordatorio se ha guardado exitosamente", title="Info")
            self.vaciar_campos()
            self.stackedWidget.setCurrentWidget(self.pageDB)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

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

    def obtener_horario(self):
        value = int(self.spinBoxVecesDia.text())

        if value == 1:
            print("Veces: 1")
            hora_1 = self.timeEdit_1.text()
            horario = [hora_1]
            return horario
        elif value == 2:
            print("Veces: 2")
            hora_1 = self.timeEdit_1.text()
            hora_2 = self.timeEdit_2.text()
            horario = [hora_1, hora_2]
            return horario
        elif value == 3:
            print("Veces: 3")
            hora_1 = self.timeEdit_1.text()
            hora_2 = self.timeEdit_2.text()
            hora_3 = self.timeEdit_3.text()
            horario = [hora_1, hora_2, hora_3]
            return horario
        elif value == 4:
            print("Veces: 4")
            hora_1 = self.timeEdit_1.text()
            hora_2 = self.timeEdit_2.text()
            hora_3 = self.timeEdit_3.text()
            hora_4 = self.timeEdit_4.text()
            horario = [hora_1, hora_2, hora_3, hora_4]
            return horario

    def obtener_fecha_actual(self):
        from datetime import date
        fecha = date.today()
        return fecha

    def obtener_fecha_final(self, fecha_actual, numero_dias):
        from datetime import timedelta
        td = timedelta(int(numero_dias))
        fecha_final = fecha_actual + td
        return fecha_final

    def value_change(self):
        value = int(self.spinBoxVecesDia.text())
        if value == 1:
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_2.setVisible(False)
            self.label_time_2.setVisible(False)
            self.timeEdit_3.setVisible(False)
            self.label_time_3.setVisible(False)
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif value == 2:
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_3.setVisible(False)
            self.label_time_3.setVisible(False)
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif value == 3:
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_3.setVisible(True)
            self.label_time_3.setVisible(True)
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif value == 4:
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_3.setVisible(True)
            self.label_time_3.setVisible(True)
            self.timeEdit_4.setVisible(True)
            self.label_time_4.setVisible(True)

    def vaciar_campos(self):
        self.lineEditMedicamento.setText('')
        self.checkBoxLunes.setChecked(False)
        self.checkBoxMartes.setChecked(False)
        self.checkBoxMiercoles.setChecked(False)
        self.checkBoxJueves.setChecked(False)
        self.checkBoxViernes.setChecked(False)
        self.checkBoxSabado.setChecked(False)
        self.checkBoxDomingo.setChecked(False)
        self.lineEditDosis.setText('')
        self.spinBoxVecesDia.setValue(1)
        self.spinBoxDias.setValue(1)


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






