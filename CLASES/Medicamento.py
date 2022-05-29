class Medicamento(object):
    def __init__(self, nombre, tipo, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, horario):
        self.nombre = nombre
        self.tipo = tipo
        self.dosis = dosis
        self.veces_dia = veces_dia
        self.frecuencia = frecuencia
        self.fecha_desde = fecha_desde
        self.fecha_hasta = fecha_hasta
        self.horario = horario

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_dosis(self, dosis):
        self.dosis = dosis

    def set_veces_dia(self, veces_dia):
        self.veces_dia = veces_dia

    def set_frecuencia(self, frecuencia):
        self.frecuencia = frecuencia

    def set_fecha_desde(self, fecha_desde):
        self.fecha_desde = fecha_desde

    def set_fecha_hasta(self, fecha_hasta):
        self.fecha_hasta = fecha_hasta

    def set_horario(self, horario):
        self.horario = horario

    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_dosis(self):
        return self.dosis

    def get_veces_dia(self):
        return self.veces_dia

    def get_frecuencia(self):
        return self.frecuencia

    def get_fecha_desde(self):
        return self.fecha_desde

    def get_fecha_hasta(self):
        return self.fecha_hasta

    def get_horario(self):
        return self.horario

    def presentar_medicamento(self):
        cadena = "\tMedicamento: \nNombre: %s \tTipo: %s \tDosis: %s \tVeces por dia: %s \tFrecuencia: %s \tDesde: %s \tHasta: %s \tHorario: %s" %(self.get_nombre(), self.get_tipo(), self.get_dosis(), self.veces_dia(), self.get_frecuencia(), self.get_fecha_desde(), self.fecha_hasta, self.horario)