from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def enqueue(self, valor): #insere um novo valor no fim da fila
        nodo = No(valor)
        aux = self.inicio

        if self.inicio == None:
            self.inicio = nodo
            self.fim = nodo
        else:
            while aux.prox is not None: #vai percorrer a fila ate chegar no ultimo elemento
                aux = aux.prox
        
            aux.prox = nodo
            nodo.prox = None

        self.tamanho += 1
        self.imprimir()

    def dequeue(self): #remove o primeiro da fila
        self.inicio = self.inicio.prox

        self.tamanho -= 1
        self.imprimir()

    def imprimir(self):
        print("\n===================================")
        if self.inicio == None:
            print("Fila vazia!")
        else:
            aux = self.inicio
            while aux is not None:
                print( aux.valor )
                aux = aux.prox
            print(f"Tamanho da Fila: {self.tamanho}")

    




