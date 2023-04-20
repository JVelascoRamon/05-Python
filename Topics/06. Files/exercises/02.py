import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/text.txt', 'r')
fsave = open(path + '/0000text.txt', 'w')

index = 0
for line in fhand:
    numero = str(index).zfill(4)
    fsave.write(numero + " "+ line)
    index += 1

fsave.close()
fhand.close()



