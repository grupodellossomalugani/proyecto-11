
# Lectura de DataSet

import csv 

with open("datos.csv", "r", encoding="UTF-8") as archivo:
    DATASET = list(csv.DictReader(archivo))
