import streamlit as st
import csv 
from lector import DATASET

# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run prueba.py " ==========

st.title("Proyecto Programacion Ⅱ ")
st.subheader("Integrantes: Malugani Luca")


# La funcion open( nombre_de_archivo , modo , encoding=None) tiene 3 argumentos los cuales 
#  --  nombre_de_archivo: es el nombre del archivo
#  --  modo: puede ser 'r' cuando el fichero solo se lea
#                    'w' para solo escritura
#                    'a' abre el fichero para agregar cualquier dato
#                    'r+' abre el fichero tanto para lectura como para escritura
#                    (el argumento mode es opcional, se asume 'r' si se omite)
#  -- encoding="utf-8": es la codificacion del archivo incluye todo el alfebeto en distintos idiomas y emojis 


#FUNCION DE LA PREGUNTA 4
# Cuál es el precio promedio si deseo hospedarme en la alcaldía Xochimilco?
#  Luca 


def PREGUNTA_4():
     
        # Acumuladores
        cantidad = 0
        suma = 0


        # Iteracion para calcular el promedio
        for fila in DATASET:
            
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

PREGUNTA_4()


# funcion de la pregunta 3
# ¿Cuántos alquileres están disponibles en una alcaldía(?)
# Tomas
#
# se le ingresa la alcaldia: puede ser =
#
# 0  "Álvaro Obregón"
# 1  "Azcapotzalco"
# 2  "Benito Juárez"
# 3  "Coyoacán"
# 4  "Cuajimalpa de Morelos"
# 5  "Cuauhtémoc"
# 6  "Gustavo A. Madero"
# 7  "Iztacalco"
# 8  "Iztapalapa"
# 9  "La Magdalena Contreras"
# 10 "Miguel Hidalgo"
# 11 "Milpa Alta"
# 12 "Tláhuac"
# 13 "Tlalpan"
# 14 "Venustiano Carranza"
# 15 "Xochimilco"


lista_de_alcaldias = ["Álvaro Obregón","Azcapotzalco","Benito Juárez","Coyoacán","Cuajimalpa de Morelos","Cuauhtémoc","Gustavo A. Madero","Iztacalco","Iztapalapa","La Magdalena Contreras","Miguel Hidalgo","Milpa Alta","Tláhuac","Tlalpan","Venustiano Carranza","Xochimilco"]

def PREGUNTA_3(indice):

        alcaldia_buscada = lista_de_alcaldias[indice]

        #acumulador 
        lista_posiciones = []
        for i in DATASET:
            if i["neighbourhood"] == alcaldia_buscada:
                diccionario_posiciones = {"longitude": float(i["longitude"]), "latitude": float(i["latitude"])}
                lista_posiciones.append(diccionario_posiciones)      
        
        st.map(lista_posiciones)

        cantidad = len(lista_posiciones)
        print("la cantidad de publicaciones de",alcaldia_buscada, "es:",cantidad)
    
        return cantidad

PREGUNTA_3(2)
#PREGUNTA_3(5)
#PREGUNTA_3(14)
