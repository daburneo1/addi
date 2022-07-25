import math

from DATA.DATUsuario import *
from CLASES.Usuario import *


def buscar_usuario(usuario):
    usuario = DATUsuario.buscar_usuario(usuario)
    if usuario:
        return usuario
    else:
        return None

class LOGUsuario():

    c_usuario = Usuario

    def registrar_usuario(self, usuario):
        busqueda_usuario = buscar_usuario(usuario)
        if busqueda_usuario:
            obj_usuario = busqueda_usuario
            return obj_usuario
        else:
            DATUsuario.registrar_usuario(self, usuario)
            return buscar_usuario(usuario)

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

    # @classmethod
    def buscar_usuario_medicamento(self, id_medicamento):
        return DATUsuario.buscar_usuario_medicamento(self, id_medicamento)

    # @classmethod
    def buscar_usuario_cita_medica(self, id_cita_medica):
        return DATUsuario.buscar_usuario_cita_medica(self, id_cita_medica)

    def buscar_usuario_cita_laboratorio(self, id_cita_laboratorio):
        return DATUsuario.buscar_usuario_cita_laboratorio(self, id_cita_laboratorio)

