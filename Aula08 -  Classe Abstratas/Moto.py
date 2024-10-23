from Veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca = None, cilindradas = 0):
        super().__init__(marca)
        self.cilindradas = cilindradas

    def cadastrar(self):
        self._marca = input("Digite a marca: ")
        self.km = int(input("Digite a kilometragem: ")) #nao precisa do __km, pelo fato de ter metodos getters e setters
        self.nCilindradas = int(input("Quantidade de cilindradas: "))

    def __str__(self):
        txt = "\nCilindradas: " + str(self.nCilindradas)
        return super().__str__() + txt