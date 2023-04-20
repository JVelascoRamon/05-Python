# Jercicios de la web: https://www.py4e.com/html3/11-regex
# Programa para contar las veces que aparece un patrón en un texto
import pathlib
import re #librería de regular expression

path = str(pathlib.Path(__file__).parent.absolute()) #Para darle la ruta de este mismo archivo .py

# "r" at the beginning means raw format, use it with regular expression patterns
patron = r'(sakai)' 
#search_pattern = input("Introduzca el patrón que desea buscar: ")
fhand = open(path + '/..//mbox.txt') #poner /../ hace que se vaya a una carpeta superior
cont = 0
for line in fhand:
    if re.search(patron, line):
        cont += 1
    
    #cont = cont + len(re.findall(patron, line)) #Otra manera de hacerlo para contar todas las repeticiones

print (cont)
print('mbox.txt had {} lines that matched {}'.format(cont , patron))