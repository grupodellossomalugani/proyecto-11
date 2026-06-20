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


#Texto a mostrar en el dasboard 

#st.title("Airbnb Ciudad de México")
st.image("AIRBNB.png",caption="Logo de Airbnb", width=300)  # -> seria el titulo 
st.subheader("Analisis de publicaciones y alquileres por alcaldia") # -> encabezado 
st.write("Integrantes: Malugani Luca, Dell'Osso Tomas")  

# widget de interfaz de usuario se usa st.selectbox para asi poder crear el menu desplegable
alcaldia = st.selectbox(  
    "Seleccionee una alcaldia",
    lista_de_alcaldias
)

PREGUNTA_3(lista_de_alcaldias.index(alcaldia))#indexea la lista de alcaldias 

datos = PREGUNTA_1()

alcaldias = []
promedios = []

for i in range(len(datos)):
    alcaldias.append(datos[i][0])
    promedios.append(datos[i][1])

#se encarga de crear la figura vacia
fig, ax = plt.subplots()

ax.bar(alcaldias, promedios, color="#ff5a5f") #diseno del grafico vertical de barras

ax.set_title("Promedio de precio por alcaldia")  #titulo del grafico 
ax.set_xlabel("Alcaldia") #nombre en el eje x
ax.set_ylabel("Precio promedio") #nombre en el ejee y

plt.xticks(rotation=90) #rotacion de los nombres de las alcaldias 

st.pyplot(fig)#muestra el grafico en el streamlit