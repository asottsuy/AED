from Torre import Torre

class Apartamento:
    def __init__(self, Torre):
        self.id = None
        self.numero = None #string
        self.torre = Torre #
        self.vaga = None
        self.prox = None

    def cadastrar(self):
        print("Insira os valores nos campos a seguir: ")
        self.id = int(input("Id do Apartamento: "))
        self.numero = input("Número do Apartamento: ")
        print("===================")
        #self.vaga = int(input("Número da vaga da garagem: "))

    def __str__(self):
        txt = f"ID: {self.id}\n"
        txt += f"Número: {self.numero}\n"
        txt += f"Torre: ({self.torre})\n"
        txt += f"Vaga de garagem: {self.vaga}"
        return txt

    def imprimir(self):
        print(f"***Info Apt {self.id}***")
        print(self)
        print("===================")