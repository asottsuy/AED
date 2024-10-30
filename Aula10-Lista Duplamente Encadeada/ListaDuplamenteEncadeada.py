from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None
        
#inserir elementos em ordem alfabética
#imprimir os elementos da lista
#imprimir os elementos na ordem inversa.

    def addOrdemAlfabetica(self, valor):
        nodo = No(valor) #instancio o No
        if self.inicio == None: #se a lista estiver vazia o nodo vai ser o inicio
            self.inicio = nodo
            self.final = nodo
        else:
            if nodo.dado < self.inicio.dado:#verificar se o nodo e menor que o inicio
                nodo.prox = self.inicio
                self.inicio.ant = nodo
                self.inicio = nodo
            else:
                aux = self.inicio
                #percorrer os dados para encontrar um lugar onde o nodo seja maior que o ant e igual ou menos que o prox
                #verificar se o aux e o ultimo da lista
                while aux.prox is not None and aux.prox.dado < valor:
                    aux = aux.prox #passa o aux para o proximo da lista
                
                nodo.prox = aux.prox #o novo nodo vai apontar para o que o aux apontava
                
                if aux.prox is not None: #se nao for o ultimo da lista
                    aux.prox.ant = nodo #o ant do proximo do aux vai apontar para o nodo
                else:
                    self.final = nodo
                aux.prox = nodo
                nodo.ant = aux

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


    def imprimirInverso(self):
        print("\n----------------------------------")
        if self.inicio == None:
            print( "\nLista Encadeada vazia!")
        else:
            aux = self.final
            while aux:
                print(aux.dado)
                aux = aux.ant