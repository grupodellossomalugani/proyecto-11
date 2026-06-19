import streamlit as st
import matplotlib.pyplot as plt
from Pregunta_3 import PREGUNTA_3, lista_de_alcaldias
from Pregunta_1 import PREGUNTA_1


# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run Dashboard.py " ==========

#st.title("Airbnb Ciudad de México")
st.image("AIRBNB.png",caption="Logo de Airbnb", width=300)
st.subheader("Análisis de publicaciones y alquileres por alcaldía")
st.write("Integrantes: Malugani Luca, Dell'Osso Tomas")

# widget de interfaz de usuario 
alcaldia = st.selectbox(
    "Seleccione una alcaldia",
    lista_de_alcaldias
)

PREGUNTA_3(lista_de_alcaldias.index(alcaldia))

datos = PREGUNTA_1()

alcaldias = []
promedios = []

for i in range(len(datos)):
    alcaldias.append(datos[i][0])
    promedios.append(datos[i][1])

fig, ax = plt.subplots()

ax.bar(alcaldias, promedios, color="#ff5a5f")

ax.set_title("Promedio de precio por alcaldía")
ax.set_xlabel("Alcaldía")
ax.set_ylabel("Precio promedio")

plt.xticks(rotation=90)

st.pyplot(fig)