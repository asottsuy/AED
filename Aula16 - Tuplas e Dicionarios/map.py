def somar(valores):
    soma = 0
    for x in valores:
        soma += x
    return soma

values = (2,3) , (5,10,15) , [4,8]

var = map(somar, values )
print(list(var))