# Método que NÃO recebe parâmetro e tem retorno
def getPI():
    return 3.14 

# Método que NÃO recebe parâmetro e NÃO tem retorno
def imprimirPI():
    print( getPI() )

# Método que recebe parâmetro e tem retorno
def calcularAreaCirculo(raio):
    area = getPI() * ( raio * raio )
    return area

# Método que recebe parâmetro e NÃO tem retorno
def imprimirAreaCirculo(raio2):
    print( calcularAreaCirculo(raio2) )


imprimirPI()
imprimirAreaCirculo( 2 )
