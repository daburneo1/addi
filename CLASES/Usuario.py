class Usuario(object):
    def __init__(self, cedula, nombre, apellido, password):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.password = password

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_cedula(self, cedula):
        self.cedula = cedula

    def set_password(self, password):
        self.password = password

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_cedula(self):
        return self.cedula

    def get_password(self):
        return self.password

    def presentar_usuario(self):
        return "\tUsuario: \nCedula: %s \tNombre: %s \tApellido: %s \tPassword: %s" %(self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_password)

