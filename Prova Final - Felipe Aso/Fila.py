from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, apartamento): #insere um novo valor no fim da fila
        apt = apartamento
        aux = self.inicio

        if self.inicio == None:
            self.inicio = apt
            self.fim = apt
        else:
            while aux.prox: #vai percorrer a fila ate chegar no ultimo elemento
                aux = aux.prox
        
            aux.prox = apt
            apt.prox = None

        apt.vaga = self.tamanho + 1
        self.tamanho += 1

        self.imprimir()

    def dequeue(self): #remove o primeiro da fila
        self.inicio = self.inicio.prox
    
        self.tamanho -= 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print("Fila vazia!")
        else:
            aux = self.inicio
            while aux:
                print(f"Posição na Fila {aux.numero}: {aux.vaga}")

                aux = aux.prox
            print(f"Tamanho da Fila: {self.tamanho}")
        print("\n===================================")

    




