import sys
from datetime import datetime, date, time, timedelta

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QMainWindow, QHeaderView, QWidget, QVBoxLayout
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from tkinter import messagebox

from BLOGICA import LOGCitasMedicas, LOGCitasLaboratorio
from BLOGICA.LOGCitasMedicas import *
from CLASES.CitaLaboratorio import CitaLaboratorio
from CLASES.Usuario import *

usuario = ""
citas_laboratorio = []
global_cita_laboratorio = CitaLaboratorio('','','','','','','')

class Laboratory_Form(QWidget):
    def __init__(self):
        super(Laboratory_Form, self).__init__()
        loadUi('./ui/examen_laboratorio.ui', self)
        # now = timedelta. n
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
        self.pushButtonEliminar.clicked.connect(self.eliminar_cita_laboratorio)
        self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio_cita_laboratorio)
        self.pushButtonActualizar_2.clicked.connect(self.actualizar_recordatorio)

        #qtable
        self.tableCitasLaboratorio.setSelectionBehavior(QtWidgets.QTableView.SelectRows)

        #ancho de columna
        self.tableCitasLaboratorio.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def get_user(self, user):
        global usuario
        usuario = user
        # print(self.usuario)

    def page_db(self):
        global citas_laboratorio
        global usuario
        self.stackedWidget.setCurrentWidget(self.pageDB)
        citas_laboratorio = LOGCitasLaboratorio.cargar_citas_laboratorio(usuario)
        print("citas_laboratorio")
        print(citas_laboratorio)
        if citas_laboratorio:
            i = len(citas_laboratorio)
            self.tableCitasLaboratorio.setRowCount(i)
            tablerow = 0
            for row in citas_laboratorio:
                # print(row)
                self.tableCitasLaboratorio.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(str(row.get_tipoExamen())))
                self.tableCitasLaboratorio.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.get_laboratorio())))
                self.tableCitasLaboratorio.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.get_ubicacion())))
                self.tableCitasLaboratorio.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.get_fecha())))
                self.tableCitasLaboratorio.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.get_hora())))
                self.tableCitasLaboratorio.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row.get_notas())))
                tablerow+=1
            self.tableCitasLaboratorio.resizeRowsToContents()

    def page_registrar(self):
        self.label_12.setText('Registrar cita laboratorio')
        self.stackedWidget.setCurrentWidget(self.pageRegistrar)
        self.vaciar_campos()
        self.pushButtonGuardar.setVisible(True)
        self.pushButtonActualizar_2.setVisible(False)

    def agregar_recordatorio_cita_laboratorio(self):
        id = 0
        tipoExamen = self.lineEditTipoExamen.text().capitalize()
        laboratorio = self.lineEditLaboratorio.text().capitalize()
        ubicacion = self.lineEditUbicacion.text().capitalize()
        fecha = self.dateEdit.text()
        hora = self.timeEdit.text()
        notas = self.lineEditNotas.text().capitalize()

        cita_laboratorio = CitaLaboratorio(id, tipoExamen, laboratorio, ubicacion, fecha, hora, notas)

        try:
            LOGCitasLaboratorio.agregar_cita_laboratorio(cita_laboratorio, usuario)
            messagebox.showinfo(message="El recordatorio se ha guardado exitosamente", title="Info")
            self.vaciar_campos()
            self.stackedWidget.setCurrentWidget(self.pageDB)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

    def vaciar_campos(self):
        self.lineEditTipoExamen.setText('')
        self.lineEditLaboratorio.setText('')
        self.lineEditUbicacion.setText('')
        self.dateEdit.setDate(date.today())
        self.timeEdit.setTime(time(6,00))
        self.lineEditNotas.setText('')

    def page_editar(self):
        global global_cita_laboratorio
        print('editar')
        try:
            row = self.tableCitasLaboratorio.currentRow()
            nombre = self.tableCitasLaboratorio.item(row, 0).text()
            print(nombre)
            cita_laboratorio = ''
            if nombre is not None:
                for x in citas_laboratorio:
                    print(str(x.tipoExamen), '=', nombre)
                    if str(x.tipoExamen) == str(nombre):
                        cita_laboratorio = x
                        global_cita_laboratorio = x

            if cita_laboratorio != '':
                self.label_12.setText('Editar Cita Laboratorio')
                self.stackedWidget.setCurrentWidget(self.pageRegistrar)
                self.lineEditTipoExamen.setText(cita_laboratorio.tipoExamen)
                self.lineEditLaboratorio.setText(cita_laboratorio.laboratorio)
                self.lineEditUbicacion.setText(cita_laboratorio.ubicacion)
                self.dateEdit.setDate(cita_laboratorio.fecha)
                self.timeEdit.setTime(QTime(int(cita_laboratorio.hora.split(":")[0]), int(cita_laboratorio.hora.split(":")[1])))
                self.lineEditNotas.setText(cita_laboratorio.notas)
                self.pushButtonGuardar.setVisible(False)
                self.pushButtonActualizar_2.setVisible(True)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Debe seleccionar una cita de laboratorio", title="Info")

    def actualizar_recordatorio(self):
        print('Actualizar')
        tipoExamen = self.lineEditTipoExamen.text().capitalize()
        laboratorio = self.lineEditLaboratorio.text().capitalize()
        ubicacion = self.lineEditUbicacion.text().capitalize()
        fecha = self.dateEdit.text()
        hora = self.timeEdit.text()
        notas = self.lineEditNotas.text().capitalize()
        print(global_cita_laboratorio.id)
        nueva_cita_laboratorio = CitaLaboratorio(global_cita_laboratorio.id, tipoExamen, laboratorio, ubicacion, fecha, hora, notas)
        try:
            LOGCitasLaboratorio.actualizar_cita_laboratorio(nueva_cita_laboratorio)
            messagebox.showinfo(message="El recordatorio se ha actualizado exitosamente", title="Info")
            self.vaciar_campos()
            self.stackedWidget.setCurrentWidget(self.pageDB)
        except Exception as e:
            print(e)
            messagebox.showerror(message="Error, por favor revisar los campos ingresados", title="Error")

    def eliminar_cita_laboratorio(self):
        global global_cita_laboratorio
        print('eliminar')
        try:
            row = self.tableCitasLaboratorio.currentRow()
            nombre = self.tableCitasLaboratorio.item(row, 0).text()
            cita_laboratorio = ''
            if nombre is not None:
                for x in citas_laboratorio:
                    print(str(x.tipoExamen), '=', nombre)
                    if str(x.tipoExamen) == str(nombre):
                        cita_laboratorio = x

                if cita_laboratorio != '':
                    opcion = messagebox.askyesno(message="Desea eliminar la cita de laboratorio seleccionada?", title="Atención")
                    if opcion == True:
                        try:
                            LOGCitasLaboratorio.eliminar_cita_laboratorio(cita_laboratorio)
                            print('Cita eliminada')
                        except:
                            messagebox.showerror(message="No se pudo eliminar la cita seleccionada",
                                                 title="Error")
        except:
            messagebox.showerror(message="Debe seleccionar una cita de laboratorio", title="Info")
        print("Done")