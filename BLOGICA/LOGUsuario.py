import math

from DATA.DATUsuario import *
from CLASES.Usuario import *

class LOGUsuario():

    c_usuario = Usuario

    def buscar_usuario(self, credencial):
        usuario = DATUsuario.buscar_usuario(self, credencial)
        print(credencial)
        if usuario:
            return usuario
        else:
            return None

    def validar_cedula(self, cedula):
        if len(cedula) == 10:
            return 1
        else:
            return 0

    def registrar_usuario(self, usuario):
        cedula = usuario.get_cedula()
        validar_cedula = self.validar_cedula(cedula)
        busqueda_usuario = self.buscar_usuario(usuario)


        if busqueda_usuario:
            DATUsuario.registrar_usuario(self, usuario)
            print("Usuario existente")
            return 2
        elif validar_cedula == 0:
            print("Cedula invalida")
            return 3
        else:
            DATUsuario.registrar_usuario(self, usuario)
            print('ok')
            return 1

    def validar_credenciales(self, c_usuario, credenciales):
        print(c_usuario.get_password)
        print(credenciales.get_password)
        if (c_usuario.get_password() == credenciales.get_password()):
            print('Grant')
            return 1
        else:
            return 0

    def buscar_usuario_recordatorio(self, recordatorio):
        usuario = DATUsuario.buscar_usuario_recordatorio(self, recordatorio)
        return usuario

