import sys
from datetime import datetime, date, time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from tkinter import messagebox

from BLOGICA import LOGCitasMedicas
from BLOGICA.LOGUsuario import *
from BLOGICA.LOGCitasMedicas import *
from CLASES.CitaMedica import CitaMedica
from CLASES.Usuario import *

citas_medicas = []
global_cita_medica = CitaMedica('','','','','','','')
row = -1

class Appointment_Form(QWidget):
    def __init__(self):
        super(Appointment_Form, self).__init__()
        loadUi('./ui/cita_medica.ui', self)


        widget = QWidget()
        layout = QVBoxLayout()

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
        self.pushButtonEliminar.clicked.connect(self.eliminar_cita_medica)
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio_cita_medica)
        self.pushButtonActualizar_2.clicked.connect(self.actualizar_recordatorio)

        #qtable
        self.tableCitasMedicas.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #ancho de columna
        self.tableCitasMedicas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def page_db(self):
        global citas_medicas
        self.stackedWidget.setCurrentWidget(self.pageDB)
        citas_medicas = LOGCitasMedicas.cargar_citas_medicas()
        print("citas_medicas")
        print(citas_medicas)
        if citas_medicas:
            i = len(citas_medicas)
            self.tableCitasMedicas.setRowCount(i)
            tablerow = 0
            for row in citas_medicas:
                # print(row)
                print(str(row.get_id()))
                usuario_nombre = LOGUsuario.buscar_usuario_cita_medica(self, str(row.get_id()))
                self.tableCitasMedicas.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(str(row.get_nombreMedico())))
                self.tableCitasMedicas.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.get_especialidad())))
                self.tableCitasMedicas.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.get_ubicacion())))
                self.tableCitasMedicas.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.get_fecha())))
                self.tableCitasMedicas.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.get_hora())))
                self.tableCitasMedicas.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.get_notas())))
                self.tableCitasMedicas.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(str(usuario_nombre)))
                tablerow+=1
            self.tableCitasMedicas.resizeRowsToContents()

    def page_registrar(self):
        self.label_12.setText('Nueva cita médica')
        self.stackedWidget.setCurrentWidget(self.pageRegistrar)
        self.vaciar_campos()
        self.pushButtonGuardar.setVisible(True)
        self.pushButtonActualizar_2.setVisible(False)

    def agregar_recordatorio_cita_medica(self):
        id = 0
        usuario = self.lineEditUsuario.text()
        nombre_medico = self.lineEditMedico.text().capitalize()
        especialidad = self.lineEditEspecialidad.text().capitalize()
        ubicacion = self.lineEditUbicacion.text().capitalize()
        fecha = self.dateEdit.text()
        hora = self.timeEdit.text()
        notas = self.lineEditNotas.text().capitalize()

        cita_medica = CitaMedica(id, nombre_medico, especialidad, ubicacion, fecha, hora, notas)

        try:
            usuario = LOGUsuario.registrar_usuario(self, usuario)
            LOGCitasMedicas.agregar_cita_medica(cita_medica, usuario)
            messagebox.showinfo(message="El recordatorio se ha guardado exitosamente", title="Info")
            self.vaciar_campos()
            self.stackedWidget.setCurrentWidget(self.pageDB)
            row = -1
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

    def vaciar_campos(self):
        self.lineEditUsuario.setText('')
        self.lineEditMedico.setText('')
        self.lineEditEspecialidad.setText('')
        self.lineEditUbicacion.setText('')
        self.dateEdit.setDate(date.today())
        self.timeEdit.setTime(time(8,00))
        self.lineEditNotas.setText('')

    def page_editar(self):
        global global_cita_medica
        print('editar')
        try:
            row = self.tableCitasMedicas.currentRow()
            nombre = self.tableCitasMedicas.item(row, 0).text()
            cita_medica = ''
            if nombre is not None:
                for x in citas_medicas:
                    print(str(x.nombreMedico), '=', nombre)
                    if str(x.nombreMedico) == str(nombre):
                        cita_medica = x
                        global_cita_medica = x

            if cita_medica != '':
                self.lineEditUsuario.setText(LOGUsuario.buscar_usuario_cita_medica(self, str(cita_medica.id)))
                self.lineEditUsuario.setEnabled(False)
                self.label_12.setText('Editar Cita Médica')
                self.stackedWidget.setCurrentWidget(self.pageRegistrar)
                self.lineEditMedico.setText(cita_medica.nombreMedico)
                self.lineEditEspecialidad.setText(cita_medica.especialidad)
                self.lineEditUbicacion.setText(cita_medica.ubicacion)
                self.dateEdit.setDate(cita_medica.fecha)
                # self.timeEdit.setTime(QTime(cita_medica.hora))
                self.timeEdit.setTime(QTime(int(cita_medica.hora.split(":")[0]), int(cita_medica.hora.split(":")[1])))
                self.lineEditNotas.setText(cita_medica.notas)
                self.pushButtonGuardar.setVisible(False)
                self.pushButtonActualizar_2.setVisible(True)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Debe seleccionar una cita médica", title="Info")

    def actualizar_recordatorio(self):
        print('Actualizar')
        nombre_medico = self.lineEditMedico.text().capitalize()
        especialidad = self.lineEditEspecialidad.text().capitalize()
        ubicacion = self.lineEditUbicacion.text().capitalize()
        fecha = self.dateEdit.text()
        hora = self.timeEdit.text()
        notas = self.lineEditNotas.text().capitalize()
        print(global_cita_medica.id)
        nueva_cita_medica = CitaMedica(global_cita_medica.id, nombre_medico, especialidad, ubicacion, fecha, hora, notas)
        try:
            LOGCitasMedicas.actualizar_cita_medica(nueva_cita_medica)
            messagebox.showinfo(message="El recordatorio se ha actualizado exitosamente", title="Info")
            self.vaciar_campos()
            row = -1
            self.stackedWidget.setCurrentWidget(self.pageDB)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

    def eliminar_cita_medica(self):
        global global_cita_medica
        print('eliminar')
        try:
            row = self.tableCitasMedicas.currentRow()
            nombre = self.tableCitasMedicas.item(row, 0).text()
            cita_medica = ''
            if nombre is not None:
                for x in citas_medicas:
                    print(str(x.nombreMedico), '=', nombre)
                    if str(x.nombreMedico) == str(nombre):
                        cita_medica = x

                if cita_medica != '':
                    opcion = messagebox.askyesno(message="Desea eliminar la cita médica seleccionada?", title="Atención")
                    if opcion == True:
                        try:
                            LOGCitasMedicas.eliminar_cita_medica(cita_medica)
                            print('Cita eliminada')
                            row = -1
                        except:
                            messagebox.showerror(message="No se pudo eliminar la cita seleccionada",
                                                 title="Error")
        except:
            messagebox.showerror(message="Debe seleccionar una cita médica", title="Info")
        print("Done")