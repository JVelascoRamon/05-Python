import re

texto = "content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl/ContentServiceSqlOracle.java"

patron = "sakai"

resultado = re.findall(patron, texto)

if resultado:
    print("Se encontró el patrón", len(resultado), "veces")
    print (type(resultado))
else:
    print("No se encontró el patrón")






def read_lines():

    fhand = open(path +"/mbox.txt")

    lista = []

    for line in fhand:

        line = line.rstrip()

        if (len(re.findall(r'^New\sRevision:\s[0-9]+', line)) != 0):

            lista.append(line)

    return lista, len(lista)


r'^New\sRevision:\s[0-9]+'


39756.92592592593

