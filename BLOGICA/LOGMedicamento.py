import functools

from DATA.DATMedicamento import *
from CLASES.Medicamento import *

def convertir_lista_frecuencia(medicamento):
    medicamento.frecuencia = ", ".join(medicamento.frecuencia)
    return medicamento

def convertir_tupla_consulta(id_medicamento):
    cadena = str(id_medicamento)
    caracteres = "(),"

    cadena = ''.join(x for x in cadena if x not in caracteres)
    print(cadena)
    return(cadena)

def buscar_horario_recordatorio(id):
    print('ID: ', id)
    horario = DATMedicamento.buscar_horario(id)
    horario = list(horario)
    horario_medicamento = []
    for x in horario:
        horario_medicamento.append(str(x[1]))
    return horario_medicamento


def convertir_horario(horario):
    horario_final = []
    for x in horario:
        hora = int(x.split(':')[0])
        minuto = int(x.split(':')[1])
        if(minuto >= 0 and minuto <=5):
            horario_final.append('%s:%s'% (str(hora), '00'))
        elif(minuto > 5 and minuto < 14):
            minuto = 10
            horario_final.append('%s:%s' % (str(hora), str(minuto)))
        elif (minuto > 15 and minuto < 24):
            minuto = 20
            horario_final.append('%s:%s' % (str(hora), str(minuto)))
        elif (minuto > 25 and minuto < 34):
            minuto = 30
            horario_final.append('%s:%s' % (str(hora), str(minuto)))
        elif (minuto > 35 and minuto < 44):
            minuto = 40
            horario_final.append('%s:%s' % (str(hora), str(minuto)))
        elif (minuto > 45 and minuto < 59):
            minuto = 50
            horario_final.append('%s:%s' % (str(hora), str(minuto)))
        else :
            horario_final.append('%s:%s' % (str(hora), '00'))
    print(horario_final)
    return horario_final

class LOGMedicamento():
    c_medicamento = Medicamento

    def agregar_medicamento(self, medicamento, usuario):
        convertir_lista_frecuencia(medicamento)
        DATMedicamento.agregar_medicamento(self, medicamento, usuario)

    def agregar_recordatorio(self, medicamento, usuario):
        medicamento.horario = convertir_horario(medicamento.horario)
        id_medicamento = DATMedicamento.consultar_id_medicamento(self, medicamento, usuario)
        id_medicamento = convertir_tupla_consulta(id_medicamento)
        print('IdMedicamento: ' + id_medicamento)
        DATMedicamento.agregar_recordatorio(self, medicamento, id_medicamento)

    def cargar_medicamentos(self):
        medicamentos = DATMedicamento.buscar_medicamentos(self)
        lista_medicamentos = []
        for x in medicamentos:
            id = x[0]
            horario_medicamento = buscar_horario_recordatorio(id)
            medicamento = Medicamento(id, x[1], x[2], x[3], x[4], str(x[6]), str(x[7]), horario_medicamento)
            lista_medicamentos.append(medicamento)
        if lista_medicamentos:
            return lista_medicamentos
        else:
            return None

    def buscar_medicamento(self, id):
        medicamento = DATMedicamento.buscar_medicamento(self, id)
        print(medicamento)
        medicamento = Medicamento(medicamento[0][0], medicamento[0][1], medicamento[0][6], medicamento[0][2], medicamento[0][3], medicamento[0][4], str(medicamento[0][7]), str(medicamento[0][8]), None)
        return medicamento

    # def buscar_horario_recordatorio(self, id):
    #     horario = DATMedicamento.buscar_horario(self, id)
    #     horario = list(horario)
    #     horario_medicamento = []
    #     for x in horario:
    #         horario_medicamento.append(str(x[1]))
    #     return horario_medicamento

    def actualizar_medicamento(self, medicamento):
        convertir_lista_frecuencia(medicamento)
        DATMedicamento.actualizar_medicamento(self, medicamento)

    def actualizar_recordatorio(self, medicamento):
        DATMedicamento.eliminar_recordatorio(self, medicamento)
        DATMedicamento.agregar_recordatorio(self, medicamento, medicamento.id)

    @classmethod
    def eliminar_medicamento(self, medicamento):
        DATMedicamento.eliminar_recordatorio(self, medicamento)
        DATMedicamento.eliminar_medicamento(medicamento)


