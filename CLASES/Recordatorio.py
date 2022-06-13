class Recordatorio(object):
    def __init__(self, id, idMedicamento, hora, nombre, dosis, frecuencia):
        self.id = id
        self.idMedicamento = idMedicamento
        self.hora = hora
        self.nombre = nombre
        self.dosis = dosis
        self.frecuencia = frecuencia

    def set_id(self, id):
        self.id = id

    def set_idMedicamento(self, idMedicamento):
        self.idMedicamento = idMedicamento

    def set_hora(self, hora):
        self.hora = hora

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_dosis(self, dosis):
        self.dosis = dosis

    def set_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia

    def get_id(self):
        return self.id

    def get_idMedicamento(self):
        return self.idMedicamento

    def get_hora(self):
        return self.hora

    def get_nombre(self):
        return self.nombre

    def get_dosis(self):
        return self.dosis

    def get_frecuencia(self):
        return self.frecuencia