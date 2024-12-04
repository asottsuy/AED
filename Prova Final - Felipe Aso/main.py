from Fila import Fila
from Apartamento import Apartamento
from Torre import Torre

filaGaragem = Fila()
torre1 = Torre()
apt1 = Apartamento(torre1)
apt2 = Apartamento(torre1)
apt3 = Apartamento(torre1)

torre1.cadastrar()
torre1.imprimir()

apt1.cadastrar()
apt2.cadastrar()
apt3.cadastrar()

apt1.imprimir()
apt2.imprimir()
apt3.imprimir()

filaGaragem.enqueue(apt1)
filaGaragem.enqueue(apt2)
filaGaragem.enqueue(apt3)

filaGaragem.dequeue()