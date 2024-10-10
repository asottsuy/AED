import sys 
from PyQt5.QtWidgets import *
from Form import Form
from Moto import Moto

class FormMoto(Form):
    def __init__(self, titulo="Tela de Moto"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.setGeometry(600, 100, self.largura, self.altura)
        self.lblCilindradas = QLabel("Cilindradas: ")
        self.txtCilindradas = QLineEdit()

        self.layout.addWidget(self.lblCilindradas)
        self.layout.addWidget(self.txtCilindradas)
        
    def exibir(self):
        moto = Moto()
        moto._marca = self.txtMarca.text()
        moto.km = int(self.txtKm.text())

        QMessageBox.information(self, "Carro cadastrado", str(moto))