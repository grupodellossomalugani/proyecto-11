from lector import dataset
import streamlit as st
from Dashboard import alcaldia

def PREGUNTA_5():
    
    listaAlcaldia = []


    # Tabla resultante
    tabla = []


    DATOS = dataset()


    # Pide al usuario que ingrese una alcaldia y un precio maximo
    alcaldiaSeleccionada = st.selectbox("Seleccione una alcaldía", alcaldia)
    
    precio = st.number_input(
    "Ingrese un precio maximo para filtrar", min_value=0.0, max_value=100000.0,value=0.0,step=100.0, placeholder="Ingresar"
    )


    # Ciclo para filtrar lo pedido
    for i in DATOS:
    
    
        if i["neighbourhood"] == alcaldiaSeleccionada:


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
