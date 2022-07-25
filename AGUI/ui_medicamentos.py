import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from tkinter import messagebox

from BLOGICA.LOGMedicamento import *
from BLOGICA.LOGUsuario import *
from CLASES.Usuario import *

medicamentos = []
global_medicamento = Medicamento('','','','','','','','')

class Medicine_Form(QWidget):
    def __init__(self):
        super(Medicine_Form, self).__init__()
        loadUi('./ui/medicamentos.ui', self)


        widget = QWidget()
        layout = QVBoxLayout()

        self.pushButtonEliminar.clicked.connect(self.eliminar_medicamento)

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
        self.pushButtonRegistrar.clicked.connect(self.page_registrar)
        # self.pushButtonEditar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        self.pushButtonEditar.clicked.connect(self.page_editar)
        self.pushButtonEliminar.clicked.connect(self.eliminar_medicamento)
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio)
        self.pushButtonActualizar_2.clicked.connect(self.actualizar_recordatorio)

        #qtable
        self.tableMedicamentos.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #ancho de columna
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def page_db(self):
        global medicamentos
        self.stackedWidget.setCurrentWidget(self.pageDB)
        medicamentos = LOGMedicamento.cargar_medicamentos(self)
        print("medicamentos")
        print(medicamentos)
        if medicamentos:
            i = len(medicamentos)
            self.tableMedicamentos.setRowCount(i)
            tablerow = 0
            for row in medicamentos:
                # print(row)
                # self.tableMedicamentos.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row.get_id())))
                usuario_nombre = LOGUsuario.buscar_usuario_medicamento(self, str(row.get_id()))
                self.tableMedicamentos.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(str(row.get_nombre())))
                self.tableMedicamentos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.get_dosis())))
                self.tableMedicamentos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.get_frecuencia())))
                self.tableMedicamentos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.get_veces_dia())))
                self.tableMedicamentos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.get_horario())))
                self.tableMedicamentos.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(usuario_nombre)))
                tablerow+=1
            self.tableMedicamentos.resizeRowsToContents()

    def page_registrar(self):
        self.label_12.setText('Nuevo medicamento')
        self.stackedWidget.setCurrentWidget(self.pageRegistrar)
        self.vaciar_campos()
        self.pushButtonGuardar.setVisible(True)
        self.pushButtonActualizar_2.setVisible(False)
        self.spinBoxVecesDia.setEnabled(True)
        self.spinBoxVecesDia.setValue(1)
        self.spinBoxVecesDia.valueChanged.connect(self.value_change)
        self.spinBoxVecesDia.setValue(1)
        self.checkBoxTodos.stateChanged.connect(self.frequency_change)
        # # self.pushButtonRegistrar.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pageRegistrar))
        # tipo_medicina = LOGMedicamento.buscar_tipo_medicamento(self)
        # print(tipo_medicina[2])
        #
        # for x in tipo_medicina:
        #     self.comboBoxTipo.addItem(x[1])
        #     # self.comboBoxTipo.setCurrentIndex(-1)

    def agregar_recordatorio(self):
        id = 0
        nombre = self.lineEditMedicamento.text().capitalize()
        frecuencia = self.obtener_frecuencia()
        dosis = self.lineEditDosis.text()
        veces_dia = self.spinBoxVecesDia.text()
        fecha_desde = self.obtener_fecha_actual()
        numero_dias = self.spinBoxDias.text()
        fecha_hasta = self.obtener_fecha_final(fecha_desde, numero_dias)
        usuario = self.lineEditUsuario.text()
        horario = self.obtener_horario()

        # print(medicamento, tipo, frecuencia, dosis, veces_dia, numero_dias)
        medicamento = Medicamento(id, nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, horario)
        # print(medicamento.presentar_medicamento())
        try:
            usuario = LOGUsuario.registrar_usuario(self, usuario)
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
        if self.checkBoxTodos.isChecked():
            frecuencia.append('Todos los días')
        else:
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

    def frequency_change(self):
        if self.checkBoxTodos.isChecked():
            print('todos')
            self.checkBoxLunes.setChecked(False)
            self.checkBoxLunes.setEnabled(False)
            self.checkBoxMartes.setChecked(False)
            self.checkBoxMartes.setEnabled(False)
            self.checkBoxMiercoles.setChecked(False)
            self.checkBoxMiercoles.setEnabled(False)
            self.checkBoxJueves.setChecked(False)
            self.checkBoxJueves.setEnabled(False)
            self.checkBoxViernes.setChecked(False)
            self.checkBoxViernes.setEnabled(False)
            self.checkBoxSabado.setChecked(False)
            self.checkBoxSabado.setEnabled(False)
            self.checkBoxDomingo.setChecked(False)
            self.checkBoxDomingo.setEnabled(False)
        else:
            print('no todos')
            self.checkBoxLunes.setChecked(False)
            self.checkBoxLunes.setEnabled(True)
            self.checkBoxMartes.setChecked(False)
            self.checkBoxMartes.setEnabled(True)
            self.checkBoxMiercoles.setChecked(False)
            self.checkBoxMiercoles.setEnabled(True)
            self.checkBoxJueves.setChecked(False)
            self.checkBoxJueves.setEnabled(True)
            self.checkBoxViernes.setChecked(False)
            self.checkBoxViernes.setEnabled(True)
            self.checkBoxSabado.setChecked(False)
            self.checkBoxSabado.setEnabled(True)
            self.checkBoxDomingo.setChecked(False)
            self.checkBoxDomingo.setEnabled(True)

    def vaciar_campos(self):
        self.lineEditUsuario.setText('')
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

    def page_editar(self):
        global global_medicamento
        print('editar')
        try:
            row = self.tableMedicamentos.currentRow()
            nombre = self.tableMedicamentos.item(row, 0).text()
            print(nombre)
            medicamento = ''
            if nombre is not None:
                for x in medicamentos:
                    print(str(x.nombre), '=', nombre)
                    if str(x.nombre) == str(nombre):
                        medicamento = x
                        global_medicamento = x

                if medicamento != '':
                    self.lineEditUsuario.setText(LOGUsuario.buscar_usuario_medicamento(self, str(medicamento.id)))
                    self.lineEditUsuario.setEnabled(False)
                    self.label_12.setText('Editar medicamento')
                    self.stackedWidget.setCurrentWidget(self.pageRegistrar)
                    self.lineEditMedicamento.setText(medicamento.nombre)
                    self.seleccionar_frecuencia(medicamento)
                    self.lineEditDosis.setText(medicamento.dosis)
                    self.mostrar_horario(medicamento)
                    self.spinBoxVecesDia.setEnabled(False)
                    self.label_7.setVisible(False)
                    self.spinBoxDias.setVisible(False)
                    self.spinBoxVecesDia.valueChanged.connect(self.value_change)
                    self.checkBoxTodos.stateChanged.connect(self.frequency_change)
                    self.pushButtonGuardar.setVisible(False)
                    self.pushButtonActualizar_2.setVisible(True)
        except:
            messagebox.showerror(message="Debe seleccionar un medicamento", title="Info")


    def seleccionar_frecuencia(self, medicamento):
        frecuencia = medicamento.frecuencia
        if 'Lunes' in frecuencia:
            self.checkBoxLunes.setChecked(True)
        if 'Martes' in frecuencia:
            self.checkBoxMartes.setChecked(True)
        if 'Miercoles' in frecuencia:
            self.checkBoxMiercoles.setChecked(True)
        if 'Jueves' in frecuencia:
            self.checkBoxJueves.setChecked(True)
        if 'Viernes' in frecuencia:
            self.checkBoxViernes.setChecked(True)
        if 'Sabado' in frecuencia:
            self.checkBoxSabado.setChecked(True)
        if 'Domingo' in frecuencia:
            self.checkBoxDomingo.setChecked(True)

    def mostrar_horario(self, medicamento):
        veces_dia = medicamento.veces_dia
        horario = medicamento.horario

        self.spinBoxVecesDia.setValue(int(veces_dia))
        print(horario)
        print(veces_dia)
        print(self.spinBoxVecesDia.text())
        if self.spinBoxVecesDia.text() == '1':
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_1.setTime(QTime(int(horario[0].split(":")[0]),int(horario[0].split(":")[1])))
            self.timeEdit_2.setVisible(False)
            self.label_time_2.setVisible(False)
            self.timeEdit_3.setVisible(False)
            self.label_time_3.setVisible(False)
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif self.spinBoxVecesDia.text() == '2':
            print("dsadasdasdasd")
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_1.setTime(QTime(int(horario[0].split(":")[0]),int(horario[0].split(":")[1])))
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_2.setTime(QTime(int(horario[1].split(":")[0]),int(horario[1].split(":")[1])))
            self.timeEdit_3.setVisible(False)
            self.label_time_3.setVisible(False)
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif self.spinBoxVecesDia.text() == '3':
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_1.setTime(QTime(int(horario[0].split(":")[0]),int(horario[0].split(":")[1])))
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_2.setTime(QTime(int(horario[1].split(":")[0]),int(horario[1].split(":")[1])))
            self.timeEdit_3.setVisible(True)
            self.label_time_3.setVisible(True)
            self.timeEdit_3.setTime(QTime(int(horario[2].split(":")[0]),int(horario[2].split(":")[1])))
            self.timeEdit_4.setVisible(False)
            self.label_time_4.setVisible(False)
        elif self.spinBoxVecesDia.text() == '4':
            self.timeEdit_1.setVisible(True)
            self.label_time_1.setVisible(True)
            self.timeEdit_1.setTime(QTime(int(horario[0].split(":")[0]),int(horario[0].split(":")[1])))
            self.timeEdit_2.setVisible(True)
            self.label_time_2.setVisible(True)
            self.timeEdit_2.setTime(QTime(int(horario[1].split(":")[0]),int(horario[1].split(":")[1])))
            self.timeEdit_3.setVisible(True)
            self.label_time_3.setVisible(True)
            self.timeEdit_3.setTime(QTime(int(horario[2].split(":")[0]),int(horario[2].split(":")[1])))
            self.timeEdit_4.setVisible(True)
            self.label_time_4.setVisible(True)
            self.timeEdit_4.setTime(QTime(int(horario[3].split(":")[0]),int(horario[3].split(":")[1])))

    def actualizar_recordatorio(self):

        print('Actualizar')

        nombre = self.lineEditMedicamento.text().capitalize()
        frecuencia = self.obtener_frecuencia()
        dosis = self.lineEditDosis.text()
        veces_dia = self.spinBoxVecesDia.text()
        horario = self.obtener_horario()
        usuario = self.lineEditUsuario.text()
        print(global_medicamento.id)
        nuevo_medicamento = Medicamento(global_medicamento.id, nombre, dosis, veces_dia, frecuencia, global_medicamento.fecha_desde, global_medicamento.fecha_hasta, horario)
        try:
            LOGMedicamento.actualizar_medicamento(self, nuevo_medicamento)
            LOGMedicamento.actualizar_recordatorio(self, nuevo_medicamento)
            messagebox.showinfo(message="El recordatorio se ha actualizado exitosamente", title="Info")
            self.vaciar_campos()
            self.stackedWidget.setCurrentWidget(self.pageDB)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

    def eliminar_medicamento(self):
        global global_medicamento
        print('editar')
        try:
            row = self.tableMedicamentos.currentRow()
            nombre = self.tableMedicamentos.item(row, 0).text()
            medicamento = ''
            if nombre is not None:
                for x in medicamentos:
                    print(str(x.nombre), '=', nombre)
                    if str(x.nombre) == str(nombre):
                        medicamento = x

                if medicamento != '':
                    opcion = messagebox.askyesno(message="Desea eliminar el medicamento seleccionado?", title="Atención")
                    if opcion == True:
                        try:
                            LOGMedicamento.eliminar_medicamento(medicamento)
                            print('medicamento eliminado')
                        except:
                            messagebox.showerror(message="No se pudo eliminar el medicamento seleccionado",
                                                 title="Error")
        except:
            messagebox.showerror(message="Debe seleccionar un medicamento", title="Info")
        print("Done")

    def actualizar_tabla(self):
        pass

    def guardar_recordatorio(self):
        pass
