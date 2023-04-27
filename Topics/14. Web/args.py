#ARGUMENTOS VARIOS
def sumar(*args): #Al poner el asteriscos estamos diciendo que el método 'sumar' puede tener tantos argumentos como se quiera (argumentos acorde con el código)
    resultado = 0
    for n in args:
        resultado += n
    return resultado

suma = sumar(2,3,3) #Le da 3 parámetros a la función sumar
print (suma)

def area(**kwargs):
    return kwargs['widht'] * kwargs['height']

valores = dict()
valores['widht'] = 10
valores['height'] = 15
print(area(**valores))
