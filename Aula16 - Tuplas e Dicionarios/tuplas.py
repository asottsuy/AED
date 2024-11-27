def calcular(x, y):
    return x+y, x-y, x*y, x/y

print(calcular(6,3))
print("======================")

for r in calcular(6,3):
    print(r)

print("======================")

soma, sub, mult, div = calcular(6,3)
print("Soma: ", soma)
print("Subtração: ", sub)
print("Multiplicação: ", mult)
print("Divisão: ", div)