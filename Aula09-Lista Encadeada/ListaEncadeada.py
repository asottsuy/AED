from No import No

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def addInicio(self, valor):
        nodo = No( valor )
        if self.inicio != None:
            nodo.prox = self.inicio
        self.inicio = nodo
        self.imprimir()

    def addFim(self, valor):
        nodo = No( valor )
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

    def removerInicio(self):
        if self.inicio == None:
            print("Nenhum dado removido!")
        else:
            self.inicio = self.inicio.prox
        self.imprimir()
    
    def removerFim(self):
        if self.inicio == None:
            print("Nenhum dado removido!")
        elif self.inicio.prox == None:
            self.inicio = None
        else:
            anterior = self.inicio
            aux = self.inicio.prox
            while aux.prox:
                anterior = aux
                aux = aux.prox
            
            anterior.prox = None
        self.imprimir()

    def remover(self, valor):
        encontrou = False
        if self.inicio == None:
            print("A lista está vazia!")
        elif self.inicio.dado == valor:
            self.inicio = self.inicio.prox
            encontrou = True
        else:
            anterior = self.inicio
            aux = self.inicio.prox
            while aux:
                if aux.dado == valor:
                    anterior.prox = aux.prox
                    encontrou = True
                    break
                anterior = aux
                aux = aux.prox

            if not encontrou:
                print("\n-----------------------------")
                print(valor + " não encontrado") 
        self.imprimir()



    def imprimir(self):
        print("\n----------------------------------")
        if self.inicio == None:
            print( "\nLista Encadeada vazia!")
        else:
            aux = self.inicio
            while aux:
                print( aux.dado )
                aux = aux.prox

