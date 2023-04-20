s = "Mississippi"
old = "is"
new = "IS"


"""
str = ""
cont = 0
replace = 0
controller = 0
for char in s:
    if controller == replace: #Deja actuar el bucle si no ha habido un reemplazo en la iteración anterior
        if char == old [0]:
            if len(old) == 1:
                str += new
            if len(old) == 2:
                if s [cont+1] == old [1]:
                    str += new [0]
                    str += new [1]
                    replace += 1 #Marca que ha habido un reemplazo
                else:
                    str += char
        else:
            str += char
        cont += 1
    else:
        controller += 1
        cont += 1
        
print (str)
"""

str = ""
cont = 0
index = 0
controller = 0
replace = 0
for char in s:
    index = 0
    #if controller == replace: #Deja actuar el bucle si no ha habido un reemplazo en la iteración anterior
    while index < len(old):
        if s [cont] == old [index]:
            str += new [index]
            index += 1
            cont += 1
            replace += 1 #Marca que ha habido un reemplazo
        else:
            str += char 
            break
    cont +=1
    #else:
     #   controller += index
      #  index = 0

print (str)