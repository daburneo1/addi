from DATA.DATMedicamento import *
from CLASES.Medicamento import *

class LOGMedicamento():
    c_medicamento = Medicamento

    def buscar_tipo_medicamento(self):
        tipo_medicamento = DATMedicamento.buscar_tipo_medicamento(self)
        # print(tipo_medicamento)

        if tipo_medicamento:
            return tipo_medicamento
        else:
            return None

    def agregar_medicamento(self, medicamento):
        DATMedicamento.agregar_medicamento(self, medicamento)