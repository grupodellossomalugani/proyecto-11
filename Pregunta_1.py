import csv 
from lector import dataset
from Pregunta_3 import lista_de_alcaldias
import matplotlib.pyplot as plt
import streamlit as st

#Tomas



def AUX_PREGUNTA_1():

    # alcaldia: str
    # precio: float
    # lista_promedios: list

    # AUX_PREGUNTA_1: () -> list
    # Devuelve una lista con las 5 alcaldias con mayor
    # precio promedio de hospedaje

    #ej:
    # len(AUX_PREGUNTA_1()) == 5

    # lista vacia donde se van a guardar los promedios 
    lista_promedios = []

    DATASET = dataset()

    # for que rrecorre todas las alcaldias  
    for alcaldia in lista_de_alcaldias:

        # acumuladores 
        suma = 0
        cantidad = 0

        # Reccorre todas las filas del dataset
        for fila in DATASET:

            # si el campo neighbourhood es igual a la alcaldia que se esta buscando:
            if fila["neighbourhood"] == alcaldia:

                # y es distinto de precio vacio 
                if fila["price"] != "":
                    
                    # agrega el precio al acumulador de suma y suma una al acumulador de cantidad 
                    suma += float(fila["price"])
                    cantidad += 1
        # validacion 
        if cantidad > 0:
            
            
            # calculo del promedio
            promedio = suma / cantidad

            # guarda la alcaldia y su promedio 
            lista_promedios.append([alcaldia, promedio])

    # orden de promedio 
    for i in range(len(lista_promedios)):

        for j in range(i + 1, len(lista_promedios)):
            
            if lista_promedios[j][1] > lista_promedios[i][1]:   # cambia la posicion si se encuentra uno mayor 

                auxiliar = lista_promedios[i]
                lista_promedios[i] = lista_promedios[j]
                lista_promedios[j] = auxiliar
    # devuelve las 5 alcaldias con mayor precio 
    return lista_promedios[:5]



def PREGUNTA_1():

    #datos: list
    # alcaldias: list
    # promedios: list

    # PREGUNTA_1: () -> None
    # genera y muestra un grafico de barras con las 5 alcaldias que
    # poseen el precio promedio mas alto 

    # ejemplo
    # PREGUNTA_1() -> muestra el graf


    datos = AUX_PREGUNTA_1()

    alcaldias = []
    promedios = []

    for i in range(len(datos)):
        alcaldias.append(datos[i][0])
        promedios.append(datos[i][1])

    # se encarga de crear la figura vacia
    fig, ax = plt.subplots()

    ax.bar(alcaldias, promedios, color="#ff5a5f") # diseño del grafico vertical de barras

    ax.set_title("Promedio de precio por alcaldia")  # titulo del grafico 
    ax.set_xlabel("Alcaldia") # nombre en el eje x
    ax.set_ylabel("Precio promedio") # nombre en el ejee y

    plt.xticks(rotation=90) # rotacion de los nombres de las alcaldias 

    st.pyplot(fig)  # muestra el grafico en el streamlit

