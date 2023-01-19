from PyQt5 import QtWidgets
from PyQt5.QtCore import QTime
from PyQt5.QtWidgets import QHeaderView, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from tkinter import messagebox

from BLOGICA.LOGMedicamento import *
from BLOGICA.LOGUsuario import *

medicamentos = []
global_medicamento = Medicamento('','','','','','','','')
nombreMedicamento = ''
frecuencia = 'Todos los días'
veces_dia = ''
dosis = ''
fecha_desde = ''
numero_dias = 0
fecha_hasta = ''
usuario = ''
horario = ''

class Medicine_Form(QWidget):
    def __init__(self):
        super(Medicine_Form, self).__init__()
        loadUi('./ui/medicamentos.ui', self)

        self.pushButtonEliminar.clicked.connect(self.eliminar_medicamento)
        self.pushButtonCerrar.clicked.connect(lambda: self.close())

        #eliminar barra de titulo
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        #SizeGrip
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self)
        self.grip.resize(self.gripSize, self.gripSize)

        #conexion botones
        self.stackedWidget.setCurrentWidget(self.pageDB)
        self.pushButtonDB.clicked.connect(self.page_db)
        self.pushButtonActualizar.clicked.connect(self.page_db)

        self.pushButtonRegistrar.clicked.connect(self.page_medicamento)
        self.pushButtonNext.clicked.connect(self.page_cantidad)
        self.pushButtonNext1.clicked.connect(self.page_dias)
        self.pushButtonFrecuenciaSi.clicked.connect(self.frecuencia_si)
        self.pushButtonFrecuenciaNo.clicked.connect(self.frecuencia_no)
        self.pushButtonNext2.clicked.connect(self.page_frecuencia)
        self.pushButtonNext3.clicked.connect(self.page_horarios)
        self.pushButtonNext4.clicked.connect(self.page_duracion)
        self.pushButtonContinuoSi.clicked.connect(self.continuo_si)
        self.pushButtonContinuoNo.clicked.connect(self.continuo_no)
        self.pushButtonNext5.clicked.connect(self.page_usuario)
        self.pushButtonGuardar_2.clicked.connect(self.guardar_medicamento)

        self.pushButtonEditar.clicked.connect(self.page_editar)
        self.pushButtonEliminar.clicked.connect(self.eliminar_medicamento)
        # self.pushButtonGuardar.clicked.connect(self.agregar_recordatorio)
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
                usuario_nombre = LOGUsuario.buscar_usuario_medicamento(self, str(row.get_id()))
                self.tableMedicamentos.setItem(tablerow, 0,QtWidgets.QTableWidgetItem(str(row.get_nombre())))
                self.tableMedicamentos.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row.get_dosis())))
                self.tableMedicamentos.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row.get_frecuencia())))
                self.tableMedicamentos.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row.get_veces_dia())))
                self.tableMedicamentos.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row.get_horario())))
                self.tableMedicamentos.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(usuario_nombre)))
                tablerow+=1
            self.tableMedicamentos.resizeRowsToContents()

    def page_medicamento(self):
        '''
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
        '''

        self.stackedWidget.setCurrentWidget(self.pageMedicamento)
        self.lineEditNombre.setText('')


    def page_cantidad(self):
        global nombreMedicamento
        if self.lineEditNombreMedicamento.text() != '':
            self.stackedWidget.setCurrentWidget(self.pageCantidad)
            nombreMedicamento = self.lineEditNombreMedicamento.text().capitalize()
            print(nombreMedicamento)
        else:
            messagebox.showerror(message="Debe ingresar un medicamento", title="Error")

    def page_dias(self):
        global dosis
        if self.lineEditCantidad.text() != '':
            self.frame_6.setVisible(False)
            dosis = self.lineEditCantidad.text().capitalize()
            self.stackedWidget.setCurrentWidget(self.pageDias)
        else:
            messagebox.showerror(message="Debe ingresar una cantidad (Ej. Una pastilla)", title="Error")

    def frecuencia_si(self):
        self.pushButtonNext2.setEnabled(True)
        self.frame_6.setVisible(False)

    def frecuencia_no(self):
        self.frame_6.setVisible(True)
        self.pushButtonNext2.setEnabled(True)

    def page_frecuencia(self):
        global frecuencia
        if (frecuencia != 'Todos los días'):
            if self.radioButtonUnDia.isChecked():
                frecuencia = 'Dejando un día'
            elif self.radioButtonDosDia.isChecked():
                frecuencia = 'Dejando dos días'
            elif self.radioButtonTresDia.isChecked():
                frecuencia = 'Dejando tres días'
        self.stackedWidget.setCurrentWidget(self.pageFrecuencia)

    def page_horarios(self):
        global veces_dia
        if self.radioButtonUno.isChecked():
            veces_dia = 1
            self.labelDosis1.setVisible(True)
            self.timeEditDosis1.setVisible(True)
            self.labelDosis2.setVisible(False)
            self.timeEditDosis2.setVisible(False)
            self.labelDosis3.setVisible(False)
            self.timeEditDosis3.setVisible(False)
            self.labelDosis4.setVisible(False)
            self.timeEditDosis4.setVisible(False)
        elif self.radioButtonDos.isChecked():
            veces_dia = 2
            self.labelDosis1.setVisible(True)
            self.timeEditDosis1.setVisible(True)
            self.labelDosis2.setVisible(True)
            self.timeEditDosis2.setVisible(True)
            self.labelDosis3.setVisible(False)
            self.timeEditDosis3.setVisible(False)
            self.labelDosis4.setVisible(False)
            self.timeEditDosis4.setVisible(False)
        elif self.radioButtonTres.isChecked():
            veces_dia = 3
            self.labelDosis1.setVisible(True)
            self.timeEditDosis1.setVisible(True)
            self.labelDosis2.setVisible(True)
            self.timeEditDosis2.setVisible(True)
            self.labelDosis3.setVisible(True)
            self.timeEditDosis3.setVisible(True)
            self.labelDosis4.setVisible(False)
            self.timeEditDosis4.setVisible(False)
        elif self.radioButtonCuatro.isChecked():
            veces_dia = 4
            self.labelDosis1.setVisible(True)
            self.timeEditDosis1.setVisible(True)
            self.labelDosis2.setVisible(True)
            self.timeEditDosis2.setVisible(True)
            self.labelDosis3.setVisible(True)
            self.timeEditDosis3.setVisible(True)
            self.labelDosis4.setVisible(True)
            self.timeEditDosis4.setVisible(True)

        self.stackedWidget.setCurrentWidget(self.pageHorarios)

    def page_duracion(self):
        global horario
        if veces_dia == 1:
            hora_1 = self.timeEditDosis1.text()
            horario = [hora_1]
        elif veces_dia == 2:
            hora_1 = self.timeEditDosis1.text()
            hora_2 = self.timeEditDosis2.text()
            horario = [hora_1, hora_2]
        elif veces_dia == 3:
            hora_1 = self.timeEditDosis1.text()
            hora_2 = self.timeEditDosis2.text()
            hora_3 = self.timeEditDosis3.text()
            horario = [hora_1, hora_2, hora_3]
        elif veces_dia == 4:
            hora_1 = self.timeEditDosis1.text()
            hora_2 = self.timeEditDosis2.text()
            hora_3 = self.timeEditDosis3.text()
            hora_4 = self.timeEditDosis4.text()
            horario = [hora_1, hora_2, hora_3, hora_4]

        self.labelDuracion.setVisible(False)
        self.spinBoxDuracion.setVisible(False)

        self.stackedWidget.setCurrentWidget(self.pageDuracion)

    def continuo_si(self):
        global fecha_hasta
        self.pushButtonNext5.setEnabled(True)
        self.labelDuracion.setVisible(False)
        self.spinBoxDuracion.setVisible(False)
        fecha_hasta = None

    def continuo_no(self):
        self.labelDuracion.setVisible(True)
        self.spinBoxDuracion.setVisible(True)
        self.pushButtonNext5.setEnabled(True)

    def page_usuario(self):
        global fecha_desde
        global fecha_hasta
        if fecha_hasta != None:
            numero_dias = self.spinBoxDuracion.text()
            fecha_desde = self.obtener_fecha_actual()
            fecha_hasta = self.obtener_fecha_final(fecha_desde, numero_dias)

        self.stackedWidget.setCurrentWidget(self.pageNombre)

    def guardar_medicamento(self):
        global nombreMedicamento, veces_dia, dosis, frecuencia, fecha_desde, fecha_hasta, numero_dias, usuario, horario

        usuario = self.lineEditNombre.text()
        if usuario != '':
            medicamento = Medicamento(0, nombreMedicamento, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta,
                                      horario)
            try:
                NuevoUsuario = LOGUsuario.registrar_usuario(self, usuario)
                LOGMedicamento.agregar_medicamento(self, medicamento, NuevoUsuario)
                LOGMedicamento.agregar_recordatorio(self, medicamento, NuevoUsuario)
                messagebox.showinfo(message="El recordatorio se ha guardado exitosamente", title="Info")
                self.vaciar_campos()
                self.stackedWidget.setCurrentWidget(self.pageDB)
            except Exception as e:
                print(e)
                messagebox.showerror(message="Error, no se pudo guardar el medicamento", title="Error")
        else:
            messagebox.showerror(message="Debe ingresar un nombre", title="Error")

    '''
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

        medicamento = Medicamento(id, nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, horario)
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
    '''

    def obtener_frecuencia(self):
        print('frecuencia')
        frecuencia = ''
        if self.radioButtonTodosDias1.isChecked():
            frecuencia = 'Todos los días'
        elif self.radioButtonPasandoUnDia1.isChecked():
            frecuencia = 'Dejando un día'
        elif self.radioButtonPasandoDosDias1.isChecked():
            frecuencia = 'Dejando dos días'
        elif self.radioButtonPasandoTresDias1.isChecked():
            frecuencia = 'Dejando tres días'
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
        print(frecuencia)
        if frecuencia == 'Todos los días':
            print('YES')
            self.radioButtonTodosDias1.setChecked(True)
        if frecuencia == 'Pasando un día':
            self.radioButtonPasandoUnDia1.setChecked(True)
        if frecuencia == 'Pasando dos días':
            self.radioButtonPasandoDosDias1.setChecked(True)
        if frecuencia == 'Pasando tres días':
            self.radioButtonPasandoTresDias1.setChecked(True)

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