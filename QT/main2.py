from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('u2.ui', self)
        self.crear.clicked.connect(self.crear_cuenta)
        self.show()

    def crear_cuenta(self):
        # Aquí puedes realizar la lógica para crear la cuenta
        # (por ejemplo, verificar las contraseñas y guardar la información)

        # Muestra un mensaje en la consola de PyCharm
        print("Your account has been created successfully.")

app = QtWidgets.QApplication([])
window = Ui()
app.exec_()
