class CitaMedica(object):
    def __init__(self, id, nombreMedico, especialidad, ubicacion, fecha, hora, notas):
        self.id = id
        self.nombreMedico = nombreMedico
        self.especialidad = especialidad
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.hora = hora
        self.notas = notas

    def set_id(self, id):
        self.id = id

    def set_nombreMedico(self, nombreMedico):
        self.nombreMedico = nombreMedico

    def set_especialidad(self, especialidad):
        self.especialidad = especialidad

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_notas(self, notas):
        self.notas = notas

    def get_id(self):
        self.id = id

    def get_nombreMedico(self):
        return self.nombreMedico

    def get_especialidad(self):
        return self.especialidad

    def get_ubicacion(self):
        return self.ubicacion

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_notas(self):
        return self.notas

    def presentar_medicamento(self):
        cadena = "\tCitaMedica: \nId: %s  \nNombre Medico: %s \tEspecialidad: %s \tUbicación: %s \tFecha: %s \tHora: %s \tNotas: %s" % (
        self.get_id(), self.get_nombreMedico(), self.get_especialidad(), self.get_fecha, self.get_hora, self.get_ubicacion(), self.get_notas())