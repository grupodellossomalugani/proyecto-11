import matplotlib.pyplot as plt 
from lector import dataset
import streamlit as st

#Luca


#FUNCION DE LA PREGUNTA 4
# Cuál es el precio promedio si deseo hospedarme en la alcaldía Xochimilco?
#  Luca 


def PREGUNTA_4(alcaldias,DATOS):
    
    # Lista que guardara el promedio de los precios
    precios = []


    # Calcula el promedio por alcaldía
    for i in alcaldias:


        suma = 0
        cantidad = 0
        
        
        for j in DATOS:

            
            if j["neighbourhood"] == i:
                
                # Calcula la suma total y la cantidad de hospedajes
                if j["price"] != "":
                    suma += float(j["price"])
                    cantidad += 1

        
        # Operación
        if cantidad != 0:            
            promedio = suma / cantidad
            precios.append(promedio)
    

    # Crea una figura (Gráfico)
    fig, ax = plt.subplots()

    
    # Dibuja las gráficas sobre los ejes
    ax.plot(alcaldias,precios)
    

    # Titulo de la gráfica
    ax.set_title("Promedio de precio por alcaldía")


    # Coloca de forma vertical cada punto del eje x
    plt.xticks(rotation=90, fontsize=8)


    # Titulo de eje X
    ax.set_xlabel("Alcaldía")
    
    # Titulo de eje y
    ax.set_ylabel("Promedio")


    # Muestra la figura en streamlit
    st.pyplot(fig)


    return precios


