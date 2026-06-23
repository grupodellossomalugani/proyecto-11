from lector import dataset
import streamlit as st
from Pregunta_3 import lista_de_alcaldias

def PREGUNTA_5():
    
    listaAlcaldia = []


    # Tabla resultante
    tabla = []


    DATOS = dataset()


    # Pide al usuario que ingrese una alcaldia y un precio maximo
    alcaldia = st.selectbox("Seleccione una alcaldía", lista_de_alcaldias)
    
    precio = st.number_input(
    "Ingrese un precio maximo para filtrar", min_value=0.0, max_value=100000.0,value=0.0,step=100.0, placeholder="Ingresar"
    )


    # Ciclo para filtrar lo pedido
    for i in DATOS:
    
    
        if i["neighbourhood"] == alcaldia:


            # Evalua que el precio cumpla la condicion
            if i["price"] != "" and float(i["price"]) <= precio:
            
            
                # Si es valido, se agrega a la tabla
                tabla.append({
                    "Nombre": i["name"],
                    "Precio": i["price"],
                    "Direccion": " "
                })
    

    # Data 
    st.dataframe(tabla)
