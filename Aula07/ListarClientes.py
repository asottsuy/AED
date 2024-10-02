#tela de listar clientes
#fucionalidade de aparecer os clientes cadastrados
#aparecer quando for chamado o botao atualizar

import sys 
from PyQt5.QtWidgets import *
from Cliente import Cliente

class ListarClientes(QMainWindow):
    def __init__(self, listaClientes = [], telaCliente = None):
        super().__init__()
        self.clientes = listaClientes
        self.telaCliente = telaCliente
        if self.telaCliente != None:
            self.telaCliente.telaListaClientes = self

        self.setWindowTitle("Lista de Clientes Cadastrados")
        self.setGeometry(100, 300, 300, 300)
        self.layout = QVBoxLayout()

        self.btnAtualizar = QPushButton("Adicionar Cliente", self)
        self.btnAtualizar.clicked.connect(self.abrirFormulario)
        self.layout.addWidget(self.btnAtualizar)

        self.tabela = QListWidget(self)
        self.setCentralWidget(self.tabela)
        self.layout.addWidget(self.tabela)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

        for cli in self.clientes:
            self.tabela.addItem(str(cli))

        
    
    def atualizarTabela(self):
        self.tabela.clear()
        for cli in self.clientes:
            self.tabela.addItem(str(cli))

    def abrirFormulario(self):
        self.telaCliente.show()


            
