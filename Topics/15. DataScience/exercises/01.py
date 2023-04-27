import matplotlib as mpl #Librería para representar gráficas
import matplotlib.pyplot as plt #Librería para representar gráficas
import numpy as np #Librería para utilizar funciones matemáticas
import pathlib #Librería para dar la ruta donde guardar la gráfica
import pandas as pd

path = str(pathlib.Path(__file__).parent.absolute()) #Ruta de esta carpeta
plt.style.use('classic')

ventas = list()
año = list()

#año.append (2014) #Añado a la lista el primer año
añoFinal = 2023
año.append (int ( input ('Introduzca el año inicial: '))) #Pregunto por el año inicial
#añoFinal = (int ( input ('Introduzca el año final: '))) #Pregunto por el año final
#ventas.append (10000) #Inicializo las ventas
ventas.append (int ( input ('Introduzca las ventas del año {}: '.format (año[0])))) #Pregunto por las ventas de este año

cont = 0
while año[cont] < añoFinal:
    año.append(año [cont] + 1) #Aumento el año
    ventas.append (ventas[cont] + 2000*cont) #Esto es para ahorrarme la pregunta
    #ventas.append (int ( input ('Introduzca las ventas del año {}: '.format (año[cont])))) #Pregunto por las ventas del siguiente año
    cont += 1

ventasAnuales = {'Año': año, 'Ventas': ventas} #Hago un diccionario con los años como las claves y las ventas como los valor
df = pd.DataFrame(ventasAnuales) #Esto crea un DataFrame, que es es una estructura de datos de dos dimensiones 
df.to_excel(path + '/ventas_anuales.xlsx', index=False) #Guarda el DataFrame en un archivo.csv

fig = plt.figure() #Crea la figura
plt.plot(año, ventas, '-')
fig.savefig(path + '/ventas_anuales.png') #Guardo la gráfica para que no la destruya. Le doy el camino de la carpeta donde estoy