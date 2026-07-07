import streamlit as st
from lector import dataset
import matplotlib.pyplot as plt
from Pregunta_1 import PREGUNTA_1
from Pregunta_2 import PREGUNTA_2
from Pregunta_3 import PREGUNTA_3, lista_de_alcaldias
from Pregunta_4 import Grafico_Pregunta4
from Pregunta_5 import Grafico_Pregunta5
from Pregunta_6 import Grafico_Pregunta6

# LIBRERIAS Q SE PUEDEN USAR StreamLight.io, MatPlotLib, csv y Pytest 

# streamlit = crea paginas web interactivas traduciendo todo lo que se hace en python en (HTML, CSS y JavaScript)

# MatPlotLib = crea graficos para mostrar datos 

# csv = permite leer y escribir datos en archivos CSV (valores Separados por Comas)

# Pytest = para crear casos de pruebas

# Para ejecutar el codigo " python3 -m streamlit run Dashboard.py " ==========



#Texto a mostrar en el dasboard 

#st.title("Airbnb Ciudad de México")
st.image("AIRBNB.png", width=300)  # -> seria el titulo 
#st.subheader("Analisis de publicaciones y alquileres por alcaldia") # -> encabezado 
#st.write("Integrantes: Malugani Luca, Dell'Osso Tomas")  


st.markdown(
    "<h1 style='text-align: center; font-weight: bold;'>Análisis de publicaciones y alquileres por alcaldía</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Integrantes: Malugani Luca, Dell'Osso Tomas</p>",
    unsafe_allow_html=True
)

#para que se muestre bien el streamlit
st.set_page_config(
    page_title="Dashboard Airbnb",
    layout="wide"
)

AlcaldiasTotales = [
    "Álvaro Obregón",
    "Azcapotzalco",
    "Benito Juárez",
    "Coyoacán",
    "Cuajimalpa de Morelos",
    "Cuauhtémoc",
    "Gustavo A. Madero",
    "Iztacalco",
    "Iztapalapa",
    "La Magdalena Contreras",
    "Miguel Hidalgo",
    "Milpa Alta",
    "Tláhuac",
    "Tlalpan",
    "Venustiano Carranza",
    "Xochimilco"
]

# para poder mostrar columnas 

col1, col2, col3 = st.columns(3) #==============================================================================

with col1:
    st.subheader("Cuales son las 5 alcaldias que tienen el precio mas caro ?")
    PREGUNTA_1()

with col2:
    st.subheader("Como se distribuyen los distintos tipos de habitacion en cada alcaldia ")
    alcaldia = st.selectbox(
        "Seleccione una Alcaldia",
        lista_de_alcaldias
    )

    PREGUNTA_2(alcaldia)  

col4, col5,col6 = st.columns(3) #=============================================================================

with col3:
    st.subheader("¿Cuántos alquileres están disponibles en una alcaldía")

    alcaldia = st.selectbox(  
        "Seleccionee una alcaldia",
        lista_de_alcaldias
        )
        
    PREGUNTA_3(AlcaldiasTotales.index(alcaldia))   

with col4: 
    st.subheader("Cuál es el precio promedio de hospedaje por alcaldía?")
    Grafico_Pregunta4(lista_de_alcaldias, dataset())

#==============================================================================

with col5: 
    st.subheader("Cuáles son los hospedajes que puedo encontrar por un precio menor a x en la alcaldía")

    alcaldia = st.selectbox("Seleccione una alcaldía", lista_de_alcaldias)
    precio = st.number_input(
        "Ingrese un precio maximo para filtrar",
        min_value=0.0,
        max_value=100000.0,
        value=0.0,step=100.0,
        placeholder="Ingresar"
        )
    
    # Llamado a la funcion
    Grafico_Pregunta5(alcaldia,precio,dataset())

with col6:
    st.subheader("Cuáles son los hospedajes que están a menos de 0.5km de la Catedral Metropolitana ")

    Grafico_Pregunta6(dataset())    





