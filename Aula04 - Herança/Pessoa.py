from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cid = Cidade("Itati")):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = cid

    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nAltura: " + str(self.altura)
        txt += "\nCidade: " + self.cidade.nome
        return txt
