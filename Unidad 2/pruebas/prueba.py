import csv
archivo = open('prueba.csv')
reader = csv.reader(archivo, delimiter = ';')
for fila in reader:
    print(fila)
archivo.close()