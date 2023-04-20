
def mirror (s): #a la función le entra una cadena
    # return s + s[::-1]
    if s =='':
        result = ''
    else:
        cadenaEspejo = []
        cadena = []
        for i in s:
            cadena = s
            cadenaEspejo = s [::-1]
        result = cadena + cadenaEspejo
    print (result)
    return result


assert(mirror("good") == "gooddoog") #assert falla si el argumento es False
assert(mirror("Python") == "PythonnohtyP")
assert(mirror("") == "")
assert(mirror("a") == "aa")