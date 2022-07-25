class Usuario(object):

    def __init__(self, idUsuario, nombre):
        self.idUsuario = idUsuario
        self.nombre = nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_idUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def get_nombre(self):
        return self.nombre

    def get_idUsuario(self):
        return self.idUsuario

    def __str__(self):
        return "\tUsuario: \nidUsuario: %s \tNombre: %s" % (
        self.get_idUsuario(), self.get_nombre())
    # def presentar_usuario(self):
    #     return "\tUsuario: \nCedula: %s \tNombre: %s \tApellido: %s \tPassword: %s" %(self.get_cedula(), self.get_nombre(), self.get_apellido(), self.get_password)
    #
