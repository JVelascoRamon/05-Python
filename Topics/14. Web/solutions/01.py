import urllib.request, urllib.parse, urllib.error
import re
import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

web = input('Entrer a web: ')

url_pattern = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'

try:
    with urllib.request.urlopen(web) as response:
        charset = response.info().get_content_charset() # Establece el idioma de comunicación entre mi ordenador y 
        html = response.read().decode(charset) #Lee lo que hay en la veriable response y lo decodifica en el idioma charset, lo que convierte el contenido de la respuesta en una cadena de texto legible. La cadena de texto decodificada se almacena en la variable "html".

        urls = re.findall(url_pattern, html)
        with open(path + '/urls.txt', 'w') as fsave:
            for url in urls:
                fsave.write(url)
                fsave.write('\n')
            #fsave.write('\n'.join(urls))  #compact version
except ValueError:
    print('The web address entered is not correct')