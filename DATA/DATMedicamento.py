import pymysql
from DATA.DATCursor import *

def buscar_horario(id):
    sql = "SELECT * FROM recordatoriomedicamento WHERE medicamento_idMedicamentos = %s" % (id)

    print(sql)
    cursor.execute(sql)
    horario = cursor.fetchall()
    return (horario)

class DATMedicamento():

    def buscar_tipo_medicamento(self):
        sql = "SELECT * FROM tipomedicamento"
        print(sql)

        cursor.execute(sql)
        data = cursor.fetchall()
        tipo_medicamento = []

        for x in data:
            tipo_medicamento.append(x)
        return tipo_medicamento

    def agregar_medicamento(self, medicamento, usuario):
        sql = "INSERT INTO medicamento (nombre, dosis, veces_dia, frecuencia, fecha_desde, fecha_hasta, idtipomedicamento, cedula) VALUES ("\
              "'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.fecha_desde, medicamento.fecha_hasta, medicamento.tipo[0], usuario.cedula)

        print(sql)

        cursor.execute(sql)
        connection.commit()

    def consultar_id_medicamento(self, medicamento, usuario):
        sql = "SELECT idMedicamentos FROM medicamento WHERE nombre = '%s' AND dosis = '%s' AND cedula = '%s'" % (
            medicamento.nombre, medicamento.dosis, usuario.cedula)
        print(sql)

        cursor.execute(sql)
        id_medicamento = cursor.fetchall()
        print(id_medicamento)
        return id_medicamento

    def agregar_recordatorio(self, medicamento, id_medicamento):
        for x in medicamento.horario:
            sql = "INSERT INTO recordatoriomedicamento (hora, medicamento_idMedicamentos ) VALUES (" \
                  "'%s', '%s')" %(x, id_medicamento)
            print(sql)

            cursor.execute(sql)
        connection.commit()

    def buscar_medicamentos(self, usuario):
        sql = "SELECT idMedicamentos, nombre, dosis, veces_dia, frecuencia, cedula, tipomedicamento, fecha_desde, fecha_hasta FROM medicamento INNER JOIN tipomedicamento ON medicamento.idtipomedicamento = tipomedicamento.idtipomedicamento WHERE cedula = %s;" % (usuario.cedula)

        print(sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        medicamentos = []

        for x in data:
            medicamentos.append(x)
        return medicamentos

    def buscar_medicamento(self, id):
        sql = "SELECT idMedicamentos, nombre, dosis, veces_dia, frecuencia, cedula, tipomedicamento, fecha_desde, fecha_hasta FROM medicamento INNER JOIN tipomedicamento ON medicamento.idtipomedicamento = tipomedicamento.idtipomedicamento WHERE idMedicamentos = %s;" % (id.text())

        print(sql)
        cursor.execute(sql)
        medicamento = cursor.fetchall()
        return medicamento

    def actualizar_medicamento(self, medicamento):
        sql = "UPDATE medicamento SET nombre = '%s', dosis = '%s', veces_dia = '%s', frecuencia = '%s', idtipomedicamento = '%s' WHERE idMedicamentos = '%s'" % (
            medicamento.nombre, medicamento.dosis, medicamento.veces_dia, medicamento.frecuencia, medicamento.tipo, medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()

    def eliminar_recordatorio(self, medicamento):
        sql = "DELETE FROM recordatoriomedicamento WHERE medicamento_idMedicamentos = %s" % (medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()

    @classmethod
    def buscar_horario(cls, id):
        sql = "SELECT * FROM recordatoriomedicamento WHERE medicamento_idMedicamentos = %s" % (id)

        print(sql)
        cursor.execute(sql)
        horario = cursor.fetchall()
        return (horario)

    @classmethod
    def eliminar_medicamento(cls, medicamento):
        sql = "DELETE FROM medicamento WHERE idMedicamentos = %s" % (medicamento.id)

        print(sql)
        cursor.execute(sql)
        cursor.fetchall()
        connection.commit()

    @classmethod
    def consultar_id_tipo_medicamento(cls, medicamento):
        sql = "SELECT idtipomedicamento FROM tipomedicamento WHERE tipoMedicamento = '%s'" % (medicamento.tipo)

        print(sql)

        cursor.execute(sql)
        id_tipo_medicamento = cursor.fetchall()
        return id_tipo_medicamento[0]