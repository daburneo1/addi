from DATA.DATUsuario import *

class LOGUsuario():

    def RegistrarUsuario(self, usuario):
        busqueda = self.BuscarUsuario(usuario)
        DATUsuario.RegistrarUsuario(usuario)

    def BuscarUsuario(self, usuario):
        busqueda = DATUsuario.BuscarUsuario(usuario)