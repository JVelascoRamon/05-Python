lista = [1, 24, 32, 12, 8]

mayor = 0
cont = 0
while cont < len(lista):
    if mayor < lista[cont]:
        mayor = lista[cont]
    cont += 1
print (mayor)