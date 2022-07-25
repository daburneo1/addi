import sys
import threading

from PyQt5 import QtWidgets
from AGUI.ui_ihr import Ihr_Form
from BLOGICA.LOGIhr import *
from AGUI.ui_bienvenida import *

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ihr = Ihr_Form()
    # hilo = threading.Thread(target=ejecucion_horaria)
    # hilo.start()
    # login = Login_Form()
    # register = Register_Form()
    # welcome = Welcome_Form()

    # login.pushButtonRegistrarse.clicked.connect(register.show)
    # login.pushButtonLogin.clicked.connect(welcome.show)

    ihr.show()
    sys.exit(app.exec_())
