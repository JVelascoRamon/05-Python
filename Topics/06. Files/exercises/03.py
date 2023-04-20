import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

fhand = open(path + '/0000text.txt', 'r')
fsave = open(path + '/NO0000text.txt', 'w')

for line in fhand:
    fsave.write(line[5:])

fsave.close()
fhand.close()
