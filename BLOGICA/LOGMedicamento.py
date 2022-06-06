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

class LOGMedicamento():
    c_medicamento = Medicamento

    def buscar_tipo_medicamento(self):
        tipo_medicamento = DATMedicamento.buscar_tipo_medicamento(self)

        if tipo_medicamento:
            return tipo_medicamento
        else:
            return None

    def agregar_medicamento(self, medicamento, usuario):
        convertir_lista_frecuencia(medicamento)
        DATMedicamento.agregar_medicamento(self, medicamento, usuario)

    def agregar_recordatorio(self, medicamento, usuario):
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
            medicamento = Medicamento(id, x[1], x[6], x[2], x[3], x[4], str(x[7]), str(x[8]), horario_medicamento)
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


