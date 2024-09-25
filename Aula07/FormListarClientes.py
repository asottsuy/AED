#tela de listar clientes
#fucionalidade de aparecer os clientes cadastrados
#aparecer quando for chamado o botao atualizar

import sys 
from PyQt5.QtWidgets import *
from FormCliente import FormCliente

class FormListarClientes(QMainWindow):
    def __init__(self, titulo="Lista de clientes cadastrados", listaClientes = []):
        super().__init__()
        self.listaClientes = listaClientes

        self.setWindowTitle(titulo)
        self.setGeometry(100, 300, 300, 300)
        self.layout = QVBoxLayout()
        self.construirLayout()

        self.btnAtualizar = QPushButton("Atualizar", self)
        self.btnAtualizar.clicked.connect(self.atualizar)
        self.layout.addWidget(self.btnAtualizar)

        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    
    def construirLayout(self):
        for cli in self.listaClientes:
            self.lblNome = QLabel(f"Nome: {cli.nome}")
            self.lblAltura = QLabel(f"Altura: {cli.altura}")
            self.lblCidade = QLabel(f"Cidade: {cli.cidade}")
            self.layout.addWidget(self.lblNome)
            self.layout.addWidget(self.lblAltura)
            self.layout.addWidget(self.lblAltura)
            self.layout.addWidget()
            

    def atualizar(self):
        cli = FormCliente(listaClientes=self.listaClientes)
        self.listaClientes.append(cli)
        QMessageBox.information( self, "Lista atualizada", str(cli))
