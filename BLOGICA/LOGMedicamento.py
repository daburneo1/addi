from DATA.DATMedicamento import *
from CLASES.Medicamento import *

def convertir_lista_frecuencia(medicamento):
    medicamento.frecuencia = ", ".join(medicamento.frecuencia)
    return medicamento

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
        # id_medicamento = DATMedicamento.consultar_id_medicamento(self, medicamento)
        # print('IdMedicamento: '+ id_medicamento)
        # DATMedicamento.agregar_recordatorio(self, medicamento)