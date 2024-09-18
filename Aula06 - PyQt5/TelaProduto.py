import sys 
from PyQt5.QtWidgets import *
from Produto import Produto

class TelaProduto(QMainWindow):
    def __init__(self, titulo="Tela de Produto"):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setGeometry(100, 100, 300, 150)
        self.layout = QVBoxLayout()
        self.construirLayout()

        self.btnSalvar = QPushButton("Salvar", self)
        self.btnSalvar.clicked.connect(self.salvar)
        self.layout.addWidget(self.btnSalvar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)


    def salvar(self):
        prod = Produto(None)
        prod.nome = self.txtNome.text()
        preco = self.txtPreco.text()
        prod.preco = 0.0
        if len(preco) > 0:
            prod.preco = preco.replace(",",".")

        
        QMessageBox.information( self, "Produto Salvo", str(prod))


    def construirLayout(self):
        self.lblNome = QLabel("Nome: ")
        self.lblPreco = QLabel("Preço: ")
        self.txtNome = QLineEdit(self)
        self.txtPreco = QLineEdit(self)

        self.layout.addWidget(self.lblNome)
        self.layout.addWidget(self.txtNome)
        self.layout.addWidget(self.lblPreco)
        self.layout.addWidget(self.txtPreco)






