from Pessoa import Pessoa

class Vendedor(Pessoa):
    def __init__(self, nomeV=None, alturaV=None, cidadeV=None, salario=None):
        super().__init__(nomeV, alturaV, cidadeV)
        self.salario = salario

    def __str__(self):
        txt = super().__str__()
        txt += "\nSalário: "+ str(self.salario)
        return txt

    def cadastrar(self):
        self = super().cadastrar()
        salario_vendedor = input("Salario do Vendedor: ")
        self.salario = float(salario_vendedor)
        return self
