class CitaLaboratorio(object):
    def __init__(self):
        self.tipoExamen = ""
        self.laboratorio = ""
        self.ubicacion = ""
        self.notas = ""

    def set_tipoExamen(self, tipoExamen):
        self.tipoExamen = tipoExamen

    def set_laboratorio(self, laboratorio):
        self.laboratorio = laboratorio

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion

    def set_notas(self, notas):
        self.notas = notas

    def get_tipoExamen(self):
        return self.tipoExamen

    def get_laboratirio(self):
        return self.laboratorio

    def get_ubicacion(self):
        return self.ubicacion

    def get_notas(self):
        return self.notas

    def presentar_medicamento(self):
        cadena = "\tCitaLaboratorio: \nTipo de exámen: %s \tLaboratorio: %s \tUbicación: %s \tNotas: %s" % (
        self.get_tipoExamen(), self.get_laboratirio(), self.get_ubicacion(), self.get_notas())