import sys
from PyQt5.QtWidgets import QApplication
from TelaProduto import TelaProduto
from TelaPerecivel import TelaPerecivel

from FormCidade import FormCidade

from FormCliente import FormCliente
from FormListarClientes import FormListarClientes

cidades = []
clientes = []

app = QApplication( sys.argv )

telaCid = FormCidade(listaCidades=cidades)
telaCid.show()

telaCli = FormCliente( listaClientes=clientes ,listaCidades=cidades)
telaCli.show()

telaListaCli = FormListarClientes(listaClientes=clientes)
telaListaCli.show()
sys.exit(app.exec_())




#telaProduto = TelaProduto()
#telaProduto.show()

#telaPerecivel = TelaPerecivel()
#telaPerecivel.show()
