from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome="", cpf="", matricula = ""):
        super().__init__(nome, cpf)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, valor):
        self.__matricula = valor

    def matricular(self):
        super().matricular()
        self.nome = input("Digite o seu nome: ")
        self._cpf = input("Digite seu CPF: ")
        self.__matricula = input("Digite sua matrícula: ")

    def marcarPresenca(self):
        super().marcarPresenca()

    def __str__(self):
        txt = "ID: "+str(self.id)+"\n"
        txt += "Nome: "+self.nome+"\n"
        txt += "CPF: "+self._cpf+"\n"
        txt += "Matrícula: "+self.__matricula
        return txt

