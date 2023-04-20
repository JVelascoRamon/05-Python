# Programa para contar las veces que aparece el patrón "New Revision: XXXXX" en un texto
import pathlib
import re #librería de regular expression

path = str(pathlib.Path(__file__).parent.absolute()) #Para darle la ruta de este mismo archivo .py

# "r" at the beginning means raw format, use it with regular expression patterns
patron = r"New Revision: \d{5}" #así busco el New Revision con 5 dígitos detrás
fhand = open(path + '/..//mbox.txt') #poner /../ hace que se vaya a una carpeta superior
cont = 0

for line in fhand:
    if re.findall(patron, line):
        cont += 1

print (cont)
print('mbox.txt had {} lines that matched {}'.format(cont , patron))