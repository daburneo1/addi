import sys
import threading

from AGUI.ui_ihr import Ihr_Form
from AGUI.ui_login import *
from AGUI.ui_registro import *
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
