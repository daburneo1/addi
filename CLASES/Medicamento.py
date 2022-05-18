class Medicamento(object):
    def __init__(self):
        self.nombre = ""
        self.dosis = ""
        self.frecuencia = []
        self.fecha_desde = ""
        self.fecha_hasta = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_dosis(self, dosis):
        self.dosis = dosis

    def set_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia

    def set_fecha_desde(self, fecha_desde):
        self.fecha_desde = fecha_desde

    def set_fecha_hasta(self, fecha_hasta):
        self.fecha_hasta = fecha_hasta

    def get_nombre(self):
        return self.nombre

    def get_dosis(self):
        return self.dosis

    def get_frecuencia(self):
        return self.frecuencia

    def get_fecha_desde(self):
        return self.fecha_desde

    def get_fecha_hasta(self):
        return self.fecha_hasta

    def presentar_medicamento(self):
        cadena = "\tMedicamento: \nNombre: %s \tDosis: %s \tFrecuencia: %s \tDesde: %s \tHasta: %s" %(self.get_nombre(), self.get_dosis(), self.get_frecuencia(), self.get_fecha_desde(), self.fecha_hasta)