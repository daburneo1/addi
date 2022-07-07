class CitaLaboratorio(object):
    def __init__(self, id, tipoExamen, laboratorio, ubicacion, fecha, hora, notas):
        self.id = id
        self.tipoExamen = tipoExamen
        self.laboratorio = laboratorio
        self.ubicacion = ubicacion
        self.fecha = fecha
        self.hora = hora
        self.notas = notas

    def set_id(self, id):
        self.id = id

    def set_tipoExamen(self, tipoExamen):
        self.tipoExamen = tipoExamen

    def set_laboratorio(self, laboratorio):
        self.laboratorio = laboratorio

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def set_fecha(self, fecha):
        self.fecha = fecha

    def set_hora(self, hora):
        self.hora = hora

    def set_notas(self, notas):
        self.notas = notas

    def get_id(self):
        return self.id

    def get_tipoExamen(self):
        return self.tipoExamen

    def get_laboratorio(self):
        return self.laboratorio

    def get_ubicacion(self):
        return self.ubicacion

    def get_fecha(self):
        return self.fecha

    def get_hora(self):
        return self.hora

    def get_notas(self):
        return self.notas

    def presentar_medicamento(self):
        cadena = "\tCitaLaboratorio: \nId: %s \nTipo de exámen: %s \tLaboratorio: %s \tUbicación: %s \tFecha: %s \tHora: %s \tNotas: %s" % (
        self.get_id(), self.get_tipoExamen(), self.get_laboratirio(), self.get_ubicacion(), self.get_fecha(), self.get_hora(), self.get_notas())