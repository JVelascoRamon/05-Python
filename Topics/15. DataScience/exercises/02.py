import matplotlib as mpl 
import matplotlib.pyplot as plt 
import pathlib #Librería para dar la ruta donde guardar la gráfica

path = str(pathlib.Path(__file__).parent.absolute())
numbers = dict()
#numbers = {4.0: 4, 5.0: 2, 8.0: 1, 3.0: 1, 647.0: 2}

number = float (input ('Introduzca el primer número de la lista: '))
try: #Falla cuando no se introduce un número
    while 0 == 0: #Para que el bucle se ejecute siempre que se le introduzcan números
        numbers[number] = numbers.get(number, 0) + 1 #Añade al diccionario la clave nueva o le suma 1 al valor si ya existe. Por defecto devuelve 0 
        number = float (input ('Introduzca el siguiente número de la lista o escriba "salir" para salir: '))
except:
    print ("Fin de la retransmisión")

numbers = dict(sorted(numbers.items()))
values = numbers.values() #Obtener los valores del diccionario en forma de lista
labels = [str(key) for key in numbers.keys()] #Crea las etiquetas de los valores del eje x, una por cada clave del diccionario

fig = plt.figure() #Crea la figura
plt.bar(labels, values) #Crear el gráfico de barras
fig.savefig(path + '/numbers.png')