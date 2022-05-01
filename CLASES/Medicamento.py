class Medicamento(object):
    def __init__(self):
        self.nombre = ""
        self.cantidad = 0.0
        self.tipo = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_tipo(self):
        return self.tipo

    def presentar_medicamento(self):
        cadena = "\tMedicamento: \nNombre: %s \tCantidad: %s \tTipo: %s" %(self.get_nombre(), self.get_cantidad(), self.get_tipo())