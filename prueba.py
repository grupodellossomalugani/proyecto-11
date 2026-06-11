import streamlit as st
import csv 
import codecs

# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run prueba.py " ==========

#st.title("Proyecto programacion 2 ")
#st.subheader("Airbnb, ciudad de México DF (MEX)")

"""DATASET = open("DATASET.csv", "r",encoding="UTF-8")
for i in DATASET:
    print(i)
DATASET.close()"""


# La funcion open( nombre_de_archivo , modo , encoding=None) tiene 3 argumentos los cuales 
#  --  nombre_de_archivo: es el nombre del archivo
#  --  modo: puede ser 'r' cuando el fichero solo se lea
#                    'w' para solo escritura
#                    'a' abre el fichero para agregar cualquier dato
#                    'r+' abre el fichero tanto para lectura como para escritura
#                    (el argumento mode es opcional, se asume 'r' si se omite)
#  -- encoding="utf-8": es la codificacion del archivo incluye todo el alfebeto en distintos idiomas y emojis 

f = open("DATASET.csv",'w',encoding="utf-8")

with open("DATASET.csv",encoding="utf-8") as f:
    read_data = f.read()

f.closed
