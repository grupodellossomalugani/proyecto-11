import streamlit as st
from Pregunta_3 import PREGUNTA_3, lista_de_alcaldias

# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run Dashboard.py " ==========

st.title("Proyecto Programacion Ⅱ ")
st.subheader("Integrantes: Malugani Luca, Dell'Osso Tomas")

# widget de interfaz de usuario 
alcaldia = st.selectbox(
    "Seleccione una alcaldia",
    lista_de_alcaldias
)

PREGUNTA_3(lista_de_alcaldias.index(alcaldia))