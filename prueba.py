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

DATASET = open("DATASET.csv", "r",encoding="UTF-8")
for i in DATASET:
    print(i)
DATASET.close()


# La funcion open( nombre_de_archivo , modo , encoding=None) tiene 3 argumentos los cuales 
#  --  nombre_de_archivo: es el nombre del archivo
#  --  modo: puede ser 'r' cuando el fichero solo se lea
#                    'w' para solo escritura
#                    'a' abre el fichero para agregar cualquier dato
#                    'r+' abre el fichero tanto para lectura como para escritura
#                    (el argumento mode es opcional, se asume 'r' si se omite)
#  -- encoding="utf-8": es la codificacion del archivo incluye todo el alfebeto en distintos idiomas y emojis 




with open('DATASET.csv', 'r',encoding='UTF-8') as f:
    
    # Columnas convierte cada fila en un diccionario
    Columnas = csv.DictReader(f)
    
    # Acumuladores
    cantidad = 0
    suma = 0
    
    # Iteracion para calcular el promedio
    for fila in Columnas:
        
        # Busca las filas tal que coinciden con "Xochimilco"
        if fila["neighbourhood"] == "Xochimilco":
            
            # Definicion 
            suma += float(fila["price"])
            cantidad += 1

    # Caso si hay registros de Xochimilco
    if cantidad > 0:

        # Operacion
        promedio = suma / cantidad
        print(f"El promedio de precio en Xochimilco es: {promedio}")
    
    # Caso si no hay registros de Xochimilco
    else:
        print("No se encontraron registros para Xochimilco.")

f.close()

