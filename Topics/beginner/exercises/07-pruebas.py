"""import os

# Constants for the exercises:
WORKING_DIR = os.getcwd()
DATA_DIR = os.path.join(os.path.dirname(WORKING_DIR), 'data')
"""

import pathlib
path = str(pathlib.Path(__file__).parent.absolute())

def find_first_words (filePath):
    lista = list()
    with open(filePath, 'r') as file:
        for line in file:
            line = line.strip()  # Quitamos posibles espacios y saltos de línea 
            if line != "":
                line = line.split() #Separamos la línea en una lista en palabras
                lista.append(line[0])
            else: 
                lista.append('')
    return lista

in_file1 = path.replace('\exercises', '') + '\data\simple_file.txt'
in_file2 = path.replace('\exercises', '') + '\data\simple_file_with_empty_lines.txt'

expected_file_1 = ['First', 'Second', 'Third', 'And']
assert find_first_words(in_file1) == expected_file_1

expected_file_2 = ['The', '', 'First', 'nonsense', '', 'Then']
assert find_first_words(in_file2) == expected_file_2