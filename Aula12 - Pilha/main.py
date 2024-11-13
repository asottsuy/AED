from Pilha import Pilha
from Livro import Livro

pilha = Pilha()
livro1 = Livro("HP", "J.K Rowling", 500)
livro2 = Livro("JD", "blablabla", 200)
livro3 = Livro("Percy Jackson", "naosei", 400)

pilha.adicionarTopo(livro1)
pilha.adicionarTopo(livro2)
pilha.adicionarTopo(livro3)

pilha.removerTopo()
