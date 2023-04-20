# Programa para hacer la media de los números del patrón el patrón "New Revision: XXXXX" en un texto
import pathlib
import re #librería de regular expression

path = str(pathlib.Path(__file__).parent.absolute())

patron = r"New Revision: \d{5}" #así busco el New Revision con 5 dígitos detrás
patronNumeros = "\D" # Expresión regular que busca cualquier cosa que no sea un dígito
#patronNumeros = "[^0-9]"  # Expresión regular que busca cualquier cosa que no sea un número (este caracter '^' niega lo que le sigue)
#patronNumeros = r"[^\d{5}]" # Expresión regular que busca cualquier cosa que no sea un número de 5 dígitos

fhand = open(path + '/..//mbox.txt') 
cont = 0
suma = 0

for line in fhand:
    if re.findall(patron, line):
        numero = (re.sub(patronNumeros, "", line)) #Declaro la variable XXX, que será la cadena de line sin letras
        numero = int (numero) #Cast de cadena a entero
        suma += numero 
        cont += 1
average = int (suma / cont)

print ('\nLa suma total es:', suma)
print ("The average is: {}\n".format(average))