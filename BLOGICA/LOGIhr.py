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
    def mover_brazos_tristeza(cls):
        servoPIN = 13
        servoPIN2 = 19
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        GPIO.setup(servoPIN2, GPIO.OUT)
        p = GPIO.PWM(servoPIN, 60)
        p.start(2.5)
        p2 = GPIO.PWM(servoPIN2, 60)
        p2.start(2.5)

        bandera = True
        contador = 0

        while bandera:
            p.ChangeDutyCycle(6)
            p2.ChangeDutyCycle(5.5)
            time.sleep(1)

            p.ChangeDutyCycle(10)
            p2.ChangeDutyCycle(1.7)
            time.sleep(1)

            contador += 1
            if contador == 2:
                bandera = False

        p.stop()
        p2.stop()
        GPIO.cleanup()

    @classmethod
    def mover_brazos_alegria(cls):
        servoPIN = 13
        servoPIN2 = 19
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        GPIO.setup(servoPIN2, GPIO.OUT)
        p = GPIO.PWM(servoPIN, 60)
        p.start(10)
        p2 = GPIO.PWM(servoPIN2, 60)
        p2.start(5)

        bandera = True
        contador = 0

        while bandera:
            p.ChangeDutyCycle(6.2)
            p2.ChangeDutyCycle(2)
            time.sleep(.5)

            p.ChangeDutyCycle(10)
            p2.ChangeDutyCycle(5)
            time.sleep(.5)

            contador += 1
            if contador == 2:
                bandera = False

        p.stop()
        p2.stop()
        GPIO.cleanup()

    @classmethod
    def led_ojos(cls, estado):
        import board
        import neopixel

        pixel_pin = board.D18
        pixel_pin2 = board.D12

        num_pixels = 9

        ORDER = neopixel.GRB
        a = 0
        pixels = neopixel.NeoPixel(
            pixel_pin, num_pixels, brightness = 0.2, auto_write = False, pixel_order = ORDER
        )

        def wheel(self, pos):
            if pos < 0 or pos > 255:
                r = g = b = 0

            elif pos < 85:
                r = int(pos * 3)
                g = int(255 - pos * 3)
                b = 0

            elif pos < 170:
                pos -= 85
                r = int(255 - pos * 3)
                g = 0
                b = int(pos * 3)

            else:
                pos -= 170
                r = 0
                g = int(pos * 3)
                b = int(255 - pos * 3)
            return(r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)

        if estado == 1:
            pixels.fill((0, 255, 0))
            pixels.show()
            print('verde')
            time.sleep(5)
        elif estado == 2 or estado == 4:
            pixels.fill((0, 0, 0))
            pixels.show()
            print('sin luces')
            time.sleep(5)
        elif estado == 3:
            pixels.fill((0, 0, 255))
            pixels.show()
            print('azul')
            time.sleep(5)
            pixels.fill((0, 0, 0))
            pixels.show()
            print('sin luces')