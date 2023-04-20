def replace (s, old, new):
    str = ""
    cont = 0
    replace = 0
    controller = 0
    for char in s:
        if controller == replace: #Deja actuar el bucle solo si no ha habido un reemplazo en la iteración anterior
            if char == old [0]: #Si el primer caracter coincide
                if len(old) == 1:
                    str += new
                if len(old) == 2:
                    if s [cont+1] == old [1]: #Comprueba que coinciden los dos elementos
                        str += new [0]
                        str += new [1]
                        replace += 1 #Marca que ha habido un reemplazo
                    else:
                        str += char #Si no coinciden los dos elementos, añade el caracter al str
            else:
                str += char
        else:
            controller += 1
        cont += 1 
    return str
        
assert(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
assert(replace(s, "om", "am") ==
"I love spam! Spam is my favorite food. Spam, spam, yum!")
assert(replace(s, "o", "a") ==
"I lave spam! Spam is my favarite faad. Spam, spam, yum!")