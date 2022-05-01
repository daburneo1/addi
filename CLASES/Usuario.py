class Usuario(object):
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.edad = ""
        self.user = ""
        self.password = ""

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_edad(self, edad):
        self.edad = edad

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_edad(self):
        return self.edad

    def get_user(self):
        return self.user

    def get_password(self):
        return self.password

    def presentar_usuario(self):
        cadena = "\tUsuario: \nNombre: %s \tApellido: %s \tEdad: %s \tUsuario: %s \tPassword: %s" %(self.get_nombre(), self.get_apellido(), self.get_edad(), self.get_user, self.get_password)

