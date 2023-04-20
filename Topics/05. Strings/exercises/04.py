frase = """Si te levantas de la cama
y el cielo está nublado
sera porque esta nublado o es de noche
"""
char = 'e'
palabrasTotales = 0

import string
def analisis (s, letter):
    str = ""
    for c in s:
        if c not in string.punctuation : str += c

    lista_palabras = s.split()
    palabrasTotales = len (lista_palabras)

    palabrasContiene = 0
    for word in lista_palabras:
        contiene = False
        for i in word:
            if i == letter:
                contiene = True
        if contiene == True:
            palabrasContiene += 1
    
    porcentaje = float (100*palabrasContiene / palabrasTotales)

    print ("Your text contains", palabrasTotales , "words, of which" , palabrasContiene ,"(" , porcentaje , "%)", " contain an" , letter)

    return palabrasContiene

analisis (frase, char)
