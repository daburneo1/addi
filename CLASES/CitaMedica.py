class CitaMedica(object):
    def __init__(self):
        self.nombreMedico = ""
        self.especialidad = ""
        self.ubicacion = ""
        self.notas = ""

    def set_nombreMedico(self, nombreMedico):
        self.nombreMedico = nombreMedico

    def set_especialidad(self, especialidad):
        self.especialidad = especialidad

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def set_notas(self, notas):
        self.notas = notas

    def get_nombreMedico(self):
        return self.nombreMedico

    def get_especialidad(self):
        return self.especialidad

    def get_ubicacion(self):
        return self.ubicacion

    def get_notas(self):
        return self.notas

    def presentar_medicamento(self):
        cadena = "\tCitaMedica: \nNombre Medico: %s \tEspecialidad: %s \tUbicación: %s \tNotas: %s" % (
        self.get_nombreMedico(), self.get_especialidad(), self.get_ubicacion(), self.get_notas())