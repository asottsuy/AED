from No import No

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None

    
    def adicionar(self, valor):
        nodo = No(valor)

        if self.inicio is None:
            self.inicio = nodo
            self.final = nodo
        else:
            if nodo.dado < self.inicio.dado: #verificar se o nodo e menor que o inicio
                nodo.prox = self.inicio 
                self.inicio.ant = nodo
                self.inicio = nodo
            else:
                #percorrer os dados para encontrar um lugar onde o nodo seja maior que o ant e igual ou menos que o prox
                #verificar se o aux e o ultimo da lista
                aux = self.inicio

                while aux.prox and aux.prox.dado <= valor:
                    aux = aux.prox #enquanto a condicao for falsa ele vai continuar passando pela lista

                #a lista ou esta no final ou achou o lugar onde o nodo e maior q o ant e menor q o prox
                nodo.prox = aux.prox #o novo nodo vai apontar para o que o aux apontava

                if aux.prox is not None: #se nao for o ultimo da lista
                    aux.prox.ant = nodo #o ant do proximo do aux vai apontar para o nodo
                else:
                    self.final = nodo
                    
                aux.prox = nodo
                nodo.ant = aux