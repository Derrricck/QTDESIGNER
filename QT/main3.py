from PyQt5 import QtWidgets, uic
import sys
import sympy as sp

x = sp.symbols('x')

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('u3.ui', self)
        self.aceptar.clicked.connect(self.factoreo)
        self.show()

    def factoreo(self):
        expresion = self.operacion.text()
        factores = sp.factor(expresion)
        self.imprimir_resultado(factores)

    def imprimir_resultado(self, resultado):
        self.resultado.setText(str(resultado))

app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
