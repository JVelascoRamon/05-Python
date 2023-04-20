import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/0000text.txt', 'r')
fsave = open(path + '/NO0000text.txt', 'w')

frase = ""
for line in fhand:
    for char in line:
        if char.isnumeric():
            continue
        else:
            frase = frase + char
fsave.write(frase)

fsave.close()
fhand.close()