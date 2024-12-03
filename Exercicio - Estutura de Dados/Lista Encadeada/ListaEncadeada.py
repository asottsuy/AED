from No import No

class Lista:
    
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
    
    def adicionar(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
            self.tamanho += 1
        else:
            aux = self.inicio
            while(aux.prox):
                aux = aux.prox
                
            aux.prox = nodo
            self.tamanho += 1

    def adicionarOrdemCrescente(self, valor):
        nodo = No(valor)
        if self.inicio is None or valor <= self.inicio.dado: #se o inicio for nulo ou o valor for menos q o inicio
            nodo.prox = self.inicio
            self.inicio = nodo
            self.tamanho += 1
        else:
            ant = self.inicio
            aux = self.inicio.prox
            while aux:
                if valor <= aux.dado:
                    ant.prox = nodo
                    nodo.prox = aux
                    self.tamanho += 1
                    return
                ant = aux
                aux = aux.prox
            ant.prox = nodo
            self.tamanho += 1
                
    def excluir(self, valor):
        if self.inicio is None:
            print("Lista Vazia")
            return
        if self.inicio.dado == valor:
            self.inicio = self.inicio/prox
            self.tamanho -= 1
            return
        
        aux = self.inicio
        while aux.prox:
            if aux.prox.dado == valor:
                aux.prox = aux.prox.prox
                self.tamanho -= 1
                return
            aux = aux.prox
        print("Valor nao encontrado")
    
    def imprimir(self):
        print("==========================")

        if self.inicio is None:
            print("Lista Encadeada Vazia!")

        aux = self.inicio
        while( aux ):
            print( aux.dado)
            aux = aux.prox
        print("Tamanho da Lista: " + str(self.tamanho))
            

        
                
                
                
                
