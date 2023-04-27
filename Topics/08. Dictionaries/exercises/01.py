s = 'ThiS is a String with Upper and lower case Letters' 
s = s.lower()
diccionario = dict()

cadena = []
for char in s:
    if char.isalnum(): 
        cadena.append(char)
cadena.sort()

for char in cadena:  #Contar los elementos y añadir los nuevos al diccionario
    diccionario[char] = diccionario.get(char, 0) + 1
    
for key, value in diccionario.items():
    print(key, value)