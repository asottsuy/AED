from Cidade import Cidade

class Pessoa:

    def __init__(self, nome, altura = 1.73, cidade = Cidade("Itati")):
        self.id = None
        self.__nome = nome
        self.__altura = altura
        self.cidade = cidade

    #Método acessor (getter)
    def getNome(self):
        return self.__nome

    #Método modificador (setter)
    def setNome(self, valor ):
        if len(valor) > 0:
            self.__nome = valor
        else:
            print("Valor inválido para o nome" )


    @property
    def nome(self):
        return self.__nome

    @property
    def altura(self):
        return self.__altura

    @nome.setter
    def nome(self, valor):
        if len(valor) > 0:
            self.__nome = valor
        else:
            print("Valor inválido para o nome" )

    @altura.setter
    def altura(self, valor):
        if valor > 0:
            self.__altura = valor
        else:
            print("Valor inválido para a altura" )

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