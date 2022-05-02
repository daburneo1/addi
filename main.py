from AGUI import ui_login
from AGUI.ui_login import *

# from AGUI import ui_registro
# from AGUI.ui_registro import *

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = ui_login.QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

    # App = QtWidgets.QApplication(sys.argv)
    # Wnd = Register_Form()
    # Wnd.show()
    # sys.exit(App.exec_())
