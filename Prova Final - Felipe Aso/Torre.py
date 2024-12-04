class Torre:
    def __init__(self):
        self.id = None
        self.nome = None
        self.endereco = None

    def cadastrar(self):
        print("Insira os valores nos campos a seguir: ")
        self.id = int(input("Id da Torre: "))
        self.nome = input("Nome da Torre: ")
        self.endereco = input("Endereço da Torre: ")
        print("===================")

    def __str__(self):
        txt = f"ID: {self.id}\n"
        txt += f"Nome: {self.nome}\n"
        txt += f"Endereço: {self.endereco}"
        return txt

    def imprimir(self):
        print(f"***Info Torre {self.id}***")
        print(self)
        print("===================")