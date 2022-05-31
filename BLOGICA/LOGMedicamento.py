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


