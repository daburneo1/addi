import sys

from AGUI.ui_login import *
from AGUI.ui_registro import *
from AGUI.ui_bienvenida import *

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # Form = ui_login.QtWidgets.QWidget()
    # ui = Ui_Form()
    # ui.setupUi(Form)
    # Form.show()
    # sys.exit(app.exec_())

    # App = QtWidgets.QApplication(sys.argv)
    # Wnd = Register_Form()
    # Wnd.show()
    # sys.exit(App.exec_())

    app = QtWidgets.QApplication(sys.argv)
    login = Login_Form()
    register = Register_Form()
    welcome = Welcome_Form()

    login.pushButtonRegistrarse.clicked.connect(register.show)
    # login.pushButtonLogin.clicked.connect(welcome.show)

    login.show()
    sys.exit(app.exec_())
