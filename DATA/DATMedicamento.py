from DATA.DATCursor import *

def buscar_horario(id):
    sql = "SELECT * FROM recordatoriomedicamento WHERE medicamento_idMedicamentos = %s" % (id)

    print(sql)
    cursor.execute(sql)
    horario = cursor.fetchall()
    connection.commit()
    return (horario)

class DATMedicamento():

    def agregar_medicamento(self, medicamento, usuario):
        sql = "INSERT INTO medicamento (nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, idUsuario) VALUES ("\
              "'%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.fecha_desde, medicamento.fecha_hasta, usuario.idUsuario)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def consultar_id_medicamento(self, medicamento, usuario):
        sql = "SELECT idMedicamento FROM medicamento WHERE nombre = '%s' AND dosis = '%s' AND idUsuario = '%s'" % (
            medicamento.nombre, medicamento.dosis, usuario.idUsuario)
        print(sql)

        cursor.execute(sql)
        id_medicamento = cursor.fetchall()
        print(id_medicamento)
        connection.commit()
        return id_medicamento

    def agregar_recordatorio(self, medicamento, id_medicamento):
        for x in medicamento.horario:
            sql = "INSERT INTO recordatoriomedicamento (hora, medicamento_idMedicamento ) VALUES (" \
                  "'%s', '%s')" %(x, id_medicamento)
            print(sql)

            cursor.execute(sql)
        connection.commit()

    def buscar_medicamentos(self):
        sql = "SELECT idMedicamento, nombre, dosis, veces_dia, frecuencia, idUsuario, fecha_desde, fecha_hasta FROM medicamento"

        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        connection.commit()
        medicamentos = []

        for x in data:
            medicamentos.append(x)
        return medicamentos

    def buscar_medicamento(self, id):
        sql = "SELECT idMedicamentos, nombre, dosis, veces_dia, frecuencia, cedula, fecha_desde, fecha_hasta FROM medicamento WHERE idMedicamentos = %s;" % (id.text())

        print(sql)
        cursor.execute(sql)
        medicamento = cursor.fetchall()
        connection.commit()
        return medicamento

    def actualizar_medicamento(self, medicamento):
        sql = "UPDATE medicamento SET nombre = '%s', dosis = '%s', veces_dia = '%s', frecuencia = '%s' WHERE idMedicamento = '%s'" % (
            medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()

    def eliminar_recordatorio(self, medicamento):
        sql = "DELETE FROM recordatoriomedicamento WHERE medicamento_idMedicamento = %s" % (medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()

    @classmethod
    def buscar_horario(cls, id):
        sql = "SELECT * FROM recordatoriomedicamento WHERE medicamento_idMedicamento = %s" % (id)

        print(sql)
        cursor.execute(sql)
        horario = cursor.fetchall()
        connection.commit()
        return (horario)

    @classmethod
    def eliminar_medicamento(cls, medicamento):
        sql = "DELETE FROM medicamento WHERE idMedicamento = %s" % (medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()