import sys 
from abc import abstractmethod
from PyQt5.QtWidgets import *

class Form(QMainWindow):
    def __init__(self,titulo = "Formulario", largura = 200, altura = 300):
        super().__init__()
        self.setWindowTitle(titulo)
        self.__largura = largura
        self.__altura = altura

        self.layout = QVBoxLayout()
        self.definirLayout()

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)
        

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):
        if valor > self.__largura:
            self.__largura = valor
        else:
            print(f"Valor deve ser maior que "+str(self.__largura))    

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if valor > self.__altura:
            self.__altura = valor
        else:
            print(f"Valor deve ser maior que "+str(self.__altura))    



    def definirLayout(self):
        self.txtMarca = QLineEdit()
        self.txtKm = QLineEdit()

        self.layout.addWidget(self.txtMarca)
        self.layout.addWidget(self.txtKm)
        self.setGeometry(100, 100, self.__largura, self.__altura)

    @abstractmethod
    def exibir(self):
        pass

