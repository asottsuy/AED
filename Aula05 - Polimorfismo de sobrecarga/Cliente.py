from Pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nomeC=None, alturaC=None, cidadeC=None, limite = 10.000):
        super().__init__(nomeC, alturaC, cidadeC)
        self.limite = limite

    def __str__(self):
        txt = super().__str__()
        txt += "\nLimite: "+ str(self.limite)
        return txt

    def cadastrar(self): #cadastro de cliente deve ter como parametro o limite tambem
        self = super().cadastrar()
        return self
        