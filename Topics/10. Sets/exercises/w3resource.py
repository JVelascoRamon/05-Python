conjunto = set([0, 1, 2, 3, 4])

salida = True
x = set([input("Introduzca un nuevo elemento:")])
conjunto.update(x)

for i in conjunto:
    print (i)