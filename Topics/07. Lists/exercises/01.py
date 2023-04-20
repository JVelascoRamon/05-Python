lista = [1, 24, 32, 12, 8]

suma = 0
suma2 =0
cont = 0
while cont < len(lista):
    suma = suma + lista[cont]
    cont += 1
print (suma)

for i in lista:
    suma2 = suma2 + i
print (suma2)