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

        if medicamentos:
            return medicamentos
        else:
            return None

    def buscar_medicamento(self, id):
        medicamento = DATMedicamento.buscar_medicamento(self, id)
        print(medicamento)
        medicamento = Medicamento(medicamento[0][1], medicamento[0][6], medicamento[0][2], medicamento[0][3], medicamento[0][4], str(medicamento[0][7]), str(medicamento[0][8]), None)
        print(type(medicamento))
        return medicamento

    def buscar_horario_recordatorio(self, medicamento, id):
        horario = DATMedicamento.buscar_horario(self, id)

        horario = list(horario)
        horario_medicamento = []
        for x in horario:
            horario_medicamento.append(str(x[1]))
        medicamento.horario = horario_medicamento
        return medicamento
