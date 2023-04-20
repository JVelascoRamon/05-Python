def count_letters(s):#función cuenta letras.
    letter_count = {} #Creamos el diccionario donde guardar las letras
    for char in s: #Por cada caracter en la string.
        char_lower = char.lower() #Convertimos a minúscula
        if char_lower.isalnum():#Comprobamos si es letra.
            if char_lower in letter_count:#Comprobamos si ya está en el diccionario.
                letter_count[char_lower] += 1 #Si está en el diccionario añadimos +1 al contador, 
            else:
                letter_count[char_lower] = 1 #Si no está, creamos el contador empezando por 1.
    return letter_count #Devolvemos la cuenta, cuidado con la identación, si lo metemos en el bucle for, parará trás hacerlo 1 vez, dando error.

s = input("Enter a string: ") #Pedimos al usuario una string.
letter_count = count_letters(s) #Llamamos la función y almacenamos el resultado en letter_count 
sorted_keys = sorted(letter_count.keys()) #Ordena en orden alfabético las claves del diccionario.
for key in sorted_keys: #iteramos en las claves ordenadas.
    print(f"{key:5} {letter_count[key]:5}") #Imprimimos con formato "Key: "número"

keys_list = list(letter_count.keys()) #Hago una lista de claves con la variable de letter_count.keys.
keys_list.sort() #Ordeno con .sort()
print(keys_list) # Imprimo.


keys_list = (letter_count.keys())
keys_list = list(letter_count.keys())