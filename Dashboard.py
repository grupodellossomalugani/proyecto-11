import streamlit as st
from lector import dataset
import matplotlib.pyplot as plt
from Pregunta_3 import PREGUNTA_3, lista_de_alcaldias
from Pregunta_1 import PREGUNTA_1
from Pregunta_4 import PREGUNTA_4
from Pregunta_6 import PREGUNTA_6
from Pregunta_5 import PREGUNTA_5

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


def main():
    
    DATASET = dataset()


    # Lista con todas las alcaldias
    AlcaldiasTotales = ["Álvaro Obregón","Azcapotzalco","Benito Juárez","Coyoacán","Cuajimalpa de Morelos","Cuauhtémoc","Gustavo A. Madero","Iztacalco","Iztapalapa","La Magdalena Contreras","Miguel Hidalgo","Milpa Alta","Tláhuac","Tlalpan","Venustiano Carranza","Xochimilco"]
    
    
    # Diccionario con preguntas
    dict_Preguntas = {"¿Cuales son las 5 alcaldias que tienen el precio mas alto?": 1, "¿Si quiero hospedarme en la alcaldía(??) cual es el precio(??) segun los diferentes tipos de habitación(??)?": 2, "¿Cuántos alquileres están disponibles en una alcaldía(??)?": 3,
                       "¿Cuál es el precio promedio de hospedaje por alcaldía?": 4, "¿Cuáles son los hospedajes que puedo encontrar por un precio menor a (??) en la alcaldía(??)?": 5, "¿Cuáles son los hospedajes que están a menos de 0.5km de la Catedral Metropolitana?": 6}
    
    
    # Seleccion de pregunta 
    Pregunta = st.selectbox("Seleccione su pregunta", dict_Preguntas)
    
    # Dependiendo la pregunta del usuario se llama a tal funcion 
    Pregunta = dict_Preguntas[Pregunta]


    if Pregunta == 1:
        PREGUNTA_1()
    
    elif Pregunta == 2:
        ...

    elif Pregunta == 3:

        alcaldia = st.selectbox(  
        "Seleccionee una alcaldia",
        lista_de_alcaldias
        )
        
        PREGUNTA_3(AlcaldiasTotales.index(alcaldia))
    
    elif Pregunta == 4:

        PREGUNTA_4(lista_de_alcaldias, DATASET)
    
    elif Pregunta == 5:
        
        # Pide los paramatros al usuario
        alcaldia = st.selectbox("Seleccione una alcaldía", lista_de_alcaldias)
        precio = st.number_input(
        "Ingrese un precio maximo para filtrar", min_value=0.0, max_value=100000.0,value=0.0,step=100.0, placeholder="Ingresar"
        )


        # Llamado a la funcion
        PREGUNTA_5(alcaldia,precio,DATASET)
    
    else:

        PREGUNTA_6(DATASET)

if __name__ == '__main__':
    main()