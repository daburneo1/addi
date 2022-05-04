from DATA.DATUsuario import *
from CLASES.Usuario import *

class LOGUsuario():

    def buscar_usuario(self, usuario):
        data = DATUsuario.buscar_usuario(self, usuario)
        busqueda_usuario = Usuario
        if data:
            busqueda_usuario(data[0][0], data[0][1], data[0][2], data[0][3])
            return(busqueda_usuario)
        else:
            return None

    def registrar_usuario(self, usuario):
        busqueda_usuario = self.buscar_usuario(usuario)
        print('****')
        print(type(busqueda_usuario))

        if busqueda_usuario is None:
            # DATUsuario.RegistrarUsuario(self, usuario)
            print("No encontrado")
            return 1
        else:
            print("Encontrado")
            return 0

