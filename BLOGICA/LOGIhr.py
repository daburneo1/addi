from datetime import datetime, timedelta
import RPi.GPIO as GPIO
import time


from DATA.DATIhr import *

def angle_to_percent (angle):
    if angle > 180 or angle < 0:
        return False

    start = 4
    end = 12.5
    ratio = (end - start)/180

    angle_as_percent = angle * ratio

    return start + angle_as_percent

class LOGIhr():
    @classmethod
    def consultar_db(self):
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_actual = datetime.today()
        hora_futura = hora_actual + timedelta(minutes=5)
        recordatorios = DATIhr.consultar_recordatorios(self, fecha_actual, hora_futura.strftime('%H:%M:00'))

        return recordatorios

    @classmethod
    def confirmar_medicamento(cls, recordatorio, usuario, contador, hora_actual):
        print('confirmar')
        fecha_actual = datetime.today().strftime('%Y-%m-%d')
        hora_programada = recordatorio.hora
        print(hora_programada)
        print(type(hora_programada))
        hora_actual = timedelta(hours = hora_actual.hour, minutes = hora_actual.minute, seconds=00)

        if hora_actual <= hora_programada:
            hora_actual = hora_programada
            DATIhr.confirmar_medicamento(fecha_actual, hora_programada, hora_actual, usuario, recordatorio)
        else:
            DATIhr.confirmar_medicamento(fecha_actual, hora_programada, hora_actual, usuario, recordatorio)
        print(hora_actual)

    @classmethod
    def mover_brazos(cls, emocion):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)

        pwm_gpio = 29
        pwm_gpio2 = 31
        frequence = 50

        GPIO.setup(pwm_gpio, GPIO.OUT)
        GPIO.setup(pwm_gpio2, GPIO.OUT)

        pwm = GPIO.PWM(pwm_gpio, frequence)
        pwm2 = GPIO.PWM(pwm_gpio2, frequence)

        pwm.start(angle_to_percent(0))
        pwm2.start(angle_to_percent(0))
        time.sleep(1)

        pwm.start(angle_to_percent(90))
        pwm2.start(angle_to_percent(90))
        time.sleep(1)

        pwm.start(angle_to_percent(180))
        pwm2.start(angle_to_percent(180))
        time.sleep(1)

        pwm.stop()
        pwm2.stop()
        GPIO.cleanup()