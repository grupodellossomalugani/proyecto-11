from lector import dataset
import matplotlib.pyplot as plt
import streamlit as st


#Tomas

#) Como se distribuyen los distintos tipos de habitacion  en cada alcaldia 

def PREGUNTA_2(alcaldia):

    # alcaldia: str
    #tipo_habitacion: str
    #cantidad: int
    #habitaciones: dic
    
    # PREGUNTA_2: str -> none
    # recibe por input una alcaldia y devuelve un grafico de torta que muestra
    # el porcentaje de tipos de habitacion que existen en la alcaldia

    #ejemplos:
    # PREGUNTA_2("Coyoacan") -> muestra el grafico de torta 


    DATASET = dataset() #carga del dataset

    habitaciones = {} 

    for fila in DATASET:

        if fila["neighbourhood"] == alcaldia:

            tipo = fila["room_type"]

            if tipo not in habitaciones:

                habitaciones[tipo] = 1

            else:

                habitaciones[tipo] += 1

    etiquetas = []
    cantidades = []

    for tipo in habitaciones:

        etiquetas.append(tipo)
        cantidades.append(habitaciones[tipo])
    
    fig, ax = plt.subplots()

    #colores en hex
    colores = [
    "#ff5a5f",
    "#ff7a7f",
    "#ff9aa2",
    "#ffc0cb"
    ]

    ax.pie(
        cantidades,
        labels = etiquetas,
        colors = colores,
        autopct="%1.1f%%"
    )

    #titulo
    ax.set_title(
        "Distribucion de tipos de habitaciones en " + alcaldia 
    )

    st.pyplot(fig) #muestra el grafico en el dashboard