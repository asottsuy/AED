carro1 = {
    "Modelo" : "Doblo",
    "Ano" : 2005
}

#print(carro1)

carro2 = {"Modelo" : "Uno Way", "Ano" : 2015}
carro3 = {"Modelo" : "Renegade", "Ano" : 2021}

frota = carro1, carro2
print( frota )

carro2["Modelo"] = "Toro"
carro2["Cor"] = "Azul"
print( frota[1] )
