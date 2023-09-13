import csv

with open("archivos\\tabla1.csv")as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row) 