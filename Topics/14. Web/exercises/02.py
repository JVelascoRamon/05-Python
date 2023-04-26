import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import requests
import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

# Pedimos al usuario que ingrese una dirección web
#url = input("Ingrese una dirección web: ")
url = 'https://www.python.org'

# Obtenemos el contenido de la página web y lo analizamos con BeautifulSoup
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Encontramos todas las etiquetas <a> que contengan un atributo "href" que comience con "http"
links = soup.find_all('a', href=lambda href: href and href.startswith('http')) # 'a' es cada uno de los enlaces que hay en un html

# Guardamos las direcciones http en el archivo urls.txt
with open(path + '/urls.txt', 'w') as f:
    for link in links:
        f.write(link.get('href') + '\n')

print ("Hecho")
