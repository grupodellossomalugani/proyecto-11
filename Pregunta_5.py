from lector import dataset
import streamlit as st
from Pregunta_3 import lista_de_alcaldias

def PREGUNTA_5(alcaldia:str,precio:int,DATOS:list)->list:
    
    listaAlcaldia = []

    # Tabla resultante
    tabla = []


    # Ciclo para filtrar lo pedido
    for i in DATOS:
    
    
        if i["neighbourhood"] == alcaldia:


            # Evalua que el precio cumpla la condicion
            if i["price"] != "" and float(i["price"]) <= precio:
            
            
                # Si es valido, se agrega a la tabla
                tabla.append({
                    "Nombre": i["name"],
                    "Precio": float(i["price"]),
                    "Direccion": " "
                })
    

    # Data 
    st.dataframe(tabla)

    return tabla


def test_PREGUNTA_5():
    assert PREGUNTA_5("Álvaro Obregón" , 200.0 , dataset()) == [{"Nombre": "Cómodo y lindo Dpto.", "Precio": 150.0, "Direccion": " "},
                                                                {"Nombre": "cuarto privado con baño propio", "Precio": 154.0, "Direccion": " "},
                                                                {"Nombre": "533 Habitación céntrica en remodelación", "Precio": 189.0, "Direccion": " "},
                                                                {"Nombre": "Habitación no. 9 | Las Almendras", "Precio": 196.0, "Direccion": " "}]

