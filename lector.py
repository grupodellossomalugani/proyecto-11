# Lectura de DataSet
import csv 

# La funcion open( nombre_de_archivo , modo , encoding=None) tiene 3 argumentos los cuales 
#  --  nombre_de_archivo: es el nombre del archivo
#  --  modo: puede ser 'r' cuando el fichero solo se lea
#                    'w' para solo escritura
#                    'a' abre el fichero para agregar cualquier dato
#                    'r+' abre el fichero tanto para lectura como para escritura
#                    (el argumento mode es opcional, se asume 'r' si se omite)
#  -- encoding="utf-8": es la codificacion del archivo incluye todo el alfebeto en distintos idiomas y emojis 

def dataset():
    with open("datos.csv", "r", encoding="UTF-8") as archivo:
        DATASET = list(csv.DictReader(archivo))
    return DATASET
