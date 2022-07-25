from DATA.DATCursor import *
from CLASES.Usuario import *

class DATUsuario():

    def registrar_usuario(self, usuario):
        sql = "INSERT INTO usuario (nombre) VALUES (" \
              "'%s')" %(usuario)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    @classmethod
    def buscar_usuario(cls, nombre_usuario):
        sql = "SELECT idUsuario, nombre FROM usuario WHERE nombre = '%s'" %(nombre_usuario)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        if data:
            usuario = Usuario(data[0][0], data[0][1])
            return usuario
        return None

    def buscar_usuario_recordatorio(self, recordatorio):
        sql = "SELECT idUsuario, nombre FROM usuario WHERE idUsuario = (SELECT idUsuario FROM recordatoriomedicamento INNER JOIN medicamento ON medicamento.idmedicamento = recordatoriomedicamento.Medicamento_idMedicamento WHERE idRecordatorio = %s);" %(recordatorio.id)

        print(sql)

        cursor.execute(sql)
        datos = cursor.fetchall()
        connection.commit()

        if datos:
            usuario = Usuario(datos[0][0], datos[0][1])
            return usuario
        return None

    # @classmethod
    def buscar_usuario_medicamento(self, id_medicamento):
        sql = "SELECT usuario.nombre FROM usuario INNER JOIN medicamento ON medicamento.idUsuario = usuario.idUsuario WHERE idMedicamento = '%s'" %(id_medicamento)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()

        if data:
            nombre_usuario = data[0][0]
            return nombre_usuario
        return None

    def buscar_usuario_cita_medica(self, id_cita_medica):
        sql = "SELECT usuario.nombre FROM usuario INNER JOIN citamedica ON citamedica.idUsuario = usuario.idUsuario WHERE idCitasMedicas = '%s'" % (
            id_cita_medica)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()

        if data:
            nombre_usuario = data[0][0]
            return nombre_usuario
        return None

    def buscar_usuario_cita_laboratorio(self, id_cita_laboratorio):
        sql = "SELECT usuario.nombre FROM usuario INNER JOIN citaslaboratorio ON citaslaboratorio.idUsuario = usuario.idUsuario WHERE idCitasLaboratorio = '%s'" % (
            id_cita_laboratorio)

        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()

        if data:
            nombre_usuario = data[0][0]
            return nombre_usuario
        return None