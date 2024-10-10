import sys 
from PyQt5.QtWidgets import *
from Form import Form
from Carro import Carro

class FormCarro(Form):
    def __init__(self, titulo="Tela de Carro"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.lblPortas = QLabel("Portas: ")
        self.txtPortas = QLineEdit()

        self.layout.addWidget(self.lblPortas)
        self.layout.addWidget(self.txtPortas)
        
    def exibir(self):
        carro = Carro()
        carro._marca = self.txtMarca.text()
        carro.km = int(self.txtKm.text())

        QMessageBox.information(self, "Carro cadastrado", str(carro))