#tela de listar clientes
#fucionalidade de aparecer os clientes cadastrados
#aparecer quando for chamado o botao atualizar

import sys 
from PyQt5.QtWidgets import *
from Cidade import Cidade
from Pessoa import Pessoa

class ListarClientes(QMainWindow):
    def __init__(self, titulo="Lista de clientes cadastrados", listaClientes = []):
        super().__init__()
        self.listaClientes = listaClientes

        self.setWindowTitle(titulo)
        self.setGeometry(100, 300, 300, 300)

        self.listaCli = QListWidget()
        self.setCentralWidget(self.listaCli)

        self.btnAtualizar = QPushButton("Atualizar", self)
        self.btnAtualizar.clicked.connect(self.atualizar)
        layout = QVBoxLayout()
        layout.addWidget(self.listaCli)
        layout.addWidget(self.btnAtualizar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        
    
    def atualizar(self):
        self.listaCli.clear()
        for cli in self.listaClientes:
            self.listaCli.addItem(str(cli))


            
