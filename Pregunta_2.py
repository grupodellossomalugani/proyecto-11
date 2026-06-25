#Tomas

#Cosas por hacer 
#Hacer todo el codigo + el diseno de datos y implementarlo en el dashboard 

from lector import dataset
import matplotlib.pyplot as plt
import streamlit as st

def PREGUNTA_2(alcaldia):

    DATASET = dataset()

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

    ax.set_title(
        "Distribucion de tipos de habitaciones en " + alcaldia 
    )

    st.pyplot(fig)