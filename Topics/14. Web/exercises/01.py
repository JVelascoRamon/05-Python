import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import requests
import pathlib

path = str(pathlib.Path(__file__).parent.absolute()) #Obtengo el path de esta carpeta para guardar el archivo txt con las urls

# Pedimos al usuario que ingrese una dirección web
#url = input("Ingrese una dirección web: ")
url = 'https://www.python.org'

# Obtenemos el contenido de la página web y lo analizamos con BeautifulSoup
response = requests.get(url) #Solicita una respuesta del servidor para la URL especificada. El servidor responde a esta solicitud enviando una respuesta HTTP, que puede incluir, por ejemplo, un archivo HTML, un archivo de imagen o cualquier otro tipo de recurso web.
soup = BeautifulSoup(response.content, 'html.parser') #Toma dos argumentos: el contenido de la respuesta (en este caso, response.content) y el analizador (en este caso, 'html.parser'). El analizador 'html.parser' es un analizador incorporado en Python que se utiliza para analizar documentos HTML. Con este código, se crea un objeto soup que representa el árbol DOM (modelo de objetos del documento) de la página web, y que se utilizará más adelante para extraer los enlaces de la página.

# Encontramos todas las etiquetas <a> que contengan un atributo "href" que comience con "http" 
links = soup.find_all('a', href=lambda href: href and href.startswith('http')) #se utiliza la función lambda como filtro adicional para encontrar todos los elementos <a> que tengan un atributo href que comience con 'http'. La expresión href and href.startswith('http') evalúa a True si el atributo href existe y comienza con 'http'. Por lo tanto, la función find_all() devuelve una lista de todas las etiquetas <a> que cumplan con esta condición, y esta lista se almacena en la variable links.

# Guardamos las direcciones http en el archivo urls.txt
with open(path + '/urls.txt', 'w') as f: #Crea el archivo 'urls.txt'. 'With' sirve para abrir y cerrar automáticamente
    for link in links:
        f.write(link.get('href') + '\n')

print ("Hecho")
