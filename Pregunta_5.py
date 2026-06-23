from lector import DATASET
import streamlit as st


def PREGUNTA_5():
    
    listaAlcaldia = []


    # Tabla resultante
    tabla = []


    DATOS = DATASET


    # Crea la lista de las alcaldias
    for i in DATOS:


        if i["neighbourhood"] not in listaAlcaldia:
            listaAlcaldia.append(i["neighbourhood"])    


    # Pide al usuario que ingrese una alcaldia y un precio maximo
    alcaldia = st.selectbox("Seleccione una alcaldía", listaAlcaldia)
    
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
