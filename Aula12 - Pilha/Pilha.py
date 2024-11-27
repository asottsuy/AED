from Livro import Livro

class Pilha:
    def __init__(self):
        self.topo = None

    def adicionarTopo(self, livro):

        if self.topo is None: #verificar se existe o topo
            self.topo = livro
            
        else: #adicionar o novo livro no topo e dizer que o livro.prox é o
            livro.prox = self.topo #dizendo que o topo anterior agora e o prox de livro
            self.topo = livro #adicionando o livro como o novo topo

        self.imprimir()
    
    def removerTopo(self):
        if self.topo is None:
            print("Pilha já está vazia!!")
        else:
            self.topo = self.topo.prox #atual topo e apagado e o que o topo anterior apontava agora e o novo topo
        self.imprimir()

    def imprimir(self):
        print("\n===================================")
        if self.topo is None:
            print("Pilha vazia!")
        else:
            aux = self.topo 
            while aux is not None: #enquanto nao for nulo
                print(f"Título: {aux.titulo}\nAutor(a): {aux.autor}\nPáginas: {aux.paginas}\n")
                aux = aux.prox



