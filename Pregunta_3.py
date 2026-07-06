
from lector import dataset
import streamlit as st

#Tomas
#falta el diseno de datos 

# funcion de la pregunta 3
# ¿Cuántos alquileres están disponibles en una alcaldía(?)

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
        """
        indice: int
        alcaldia_buscada: str
        DATASET: list

        PREGUNTA_3: int -> int
        #recibe el indice de una alcaldia y muestra un mapa con todas
        #las publicaciones disponibles en esa alcaldia y dice la cantidad
        #de alquileres que se encontraron

        #ejemplos
        # PREGUNTA_3(2) -> 2587
        # PREGUNTA_3(10) -> 4312
        
        """
        alcaldia_buscada = lista_de_alcaldias[indice]

        DATASET = dataset()

        #acumulador 
        lista_posiciones = []
        
        for i in DATASET:
            if i["neighbourhood"] == alcaldia_buscada:
                diccionario_posiciones = {
                                        "longitude": float(i["longitude"]),
                                        "latitude": float(i["latitude"])
                                }
                lista_posiciones.append(diccionario_posiciones)      
        
        st.subheader(alcaldia_buscada)  
        st.map(lista_posiciones,color="#ff5a5f")

        cantidad = len(lista_posiciones)

        st.write("Cantidad de publicaciones:", cantidad)
        print("la cantidad de publicaciones de",alcaldia_buscada, "es:",cantidad)
    
        return cantidad

#PREGUNTA_3(2)


