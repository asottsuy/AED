from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__ (self, nome, cpf):
        self.id = 1
        self.nome = nome
        self._cpf = cpf

    @abstractmethod
    def marcarPresenca(self):
        pass

    def matricular(self):
        self
