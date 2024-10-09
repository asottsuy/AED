import sys 
from PyQt5.QtWidgets import *
from Form import Form

class FormCarro(Form):
    def __init__(self, titulo="Tela de Carro"):
        super().__init__(titulo)

    def definirLayout(self):
        super().definirLayout()
        self.txtPortas = QLineEdit()

        self.layout.addWidget(self.txtPortas)
        