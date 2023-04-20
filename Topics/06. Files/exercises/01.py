import pathlib

path = str(pathlib.Path(__file__).parent.absolute())

entradaCorrecta = 0
while entradaCorrecta == 0:
    s = input ("¿Qué quiere buscar en el texto?: ")
    fhand = open(path + '/text.txt')
    for line in fhand:
        line = line.rstrip()
        if not s in line:
            continue
        else:
            print(line)
            entradaCorrecta = 1
    fhand.close()
    if entradaCorrecta == 0:
        print ("La palabra o frase introducida no se encuentra en el texto, vuelva a intentarlo")

