import streamlit as st
import csv 


# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run prueba.py " ==========

#st.title("Proyecto programacion 2 ")
#st.subheader("Airbnb, ciudad de México DF (MEX)")


DATASET = open("datos.csv", "r",encoding="UTF-8")


# La funcion open( nombre_de_archivo , modo , encoding=None) tiene 3 argumentos los cuales 
#  --  nombre_de_archivo: es el nombre del archivo
#  --  modo: puede ser 'r' cuando el fichero solo se lea
#                    'w' para solo escritura
#                    'a' abre el fichero para agregar cualquier dato
#                    'r+' abre el fichero tanto para lectura como para escritura
#                    (el argumento mode es opcional, se asume 'r' si se omite)
#  -- encoding="utf-8": es la codificacion del archivo incluye todo el alfebeto en distintos idiomas y emojis 

def f():

    # Llamada a DataSet
    with DATASET as f:
        
        # Columnas convierte cada fila en un diccionario
        Columnas = csv.DictReader(f)
        # {'Id': Value,...,'License': Value}
        
        # Acumuladores
        cantidad = 0
        suma = 0
        SinPrecio = 0 


        # Iteracion para calcular el promedio
        for fila in Columnas:
            
            # Busca las filas tal que coinciden con "Xochimilco"
            if fila["neighbourhood"] == "Xochimilco":
                
                # Evalua que el precio no sea un espacio en blanco
                if fila["price"] != "":
                    
                    # Definicion 
                    suma += float(fila["price"])
                    cantidad += 1
                
                else:
                    pass


        # Caso si hay registros de Xochimilco
        if cantidad > 0:

            # Operacion
            promedio = round(suma / cantidad, 2)
            print(f"El promedio de precio en Xochimilco es: {promedio}")
        
        # Caso si no hay registros de Xochimilco
        else:
            print("No se encontraron registros para Xochimilco.")

    return None

f()