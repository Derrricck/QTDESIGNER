from PyQt5 import QtWidgets, uic, QtGui
import sys
import sympy as sp

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('u1.ui', self)
        self.aceptar.clicked.connect(self.iniciar_sesion)
        self.show()

    def iniciar_sesion(self):
        usuario = self.username.text()
        contrasena = self.contrasena.text()

        if usuario == "usuario" and contrasena == "contrasena":
            # Muestra un mensaje de éxito
            self.mostrar_mensaje("Session started successfully.")

        else:
            # Muestra un mensaje de error
            self.mostrar_mensaje("Mistake: Incorrect credentials.")
            print(self.mostrar_mensaje)

    def mostrar_mensaje(self, mensaje):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setText(mensaje)
        msg_box.setWindowTitle("Mensaje")
        msg_box.exec_()

        # Muestra un mensaje en la consola de PyCharm
        print("Session started successfully.")

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
