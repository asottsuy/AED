from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cidade = Cidade("Itati")):
        self.id = None
        self.nome = nome
        self.altura = altura
        self.cidade = cidade

    def __str__(self):
        txt = "Nome: " + self.nome
        txt += "\nAltura: " + str(self.altura)
        txt += "\nCidade: " + str(self.cidade)
        return txt

    def cadastrar(self):
        self.nome = input("Digite o seu nome: ")
        self.altura = float(input("Digite a sua altura: "))
        self.cidade = Cidade( input("Qual a sua cidade que reside: ") )
        return self