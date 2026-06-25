from lector import dataset
import streamlit as st

def PREGUNTA_5(alcaldia:str,precio:int,DATOS:list)->list:
    """
    La función recibe una alcaldía, un precio maximo y la dataset, a partir de
    estos datos la función filtra los hospedajes que se encuentran en la alcaldía
    dada por un monto menor o igual a precio.
    Ejemplo:
    PREGUNTA_5("Álvaro Obregón" , 200.0 , dataset()) == [{"Nombre": "Cómodo y lindo Dpto.", "Precio": 150.0, "Ubicación": (-99.24999814788514, 19.32927732036978)},
                                                         {"Nombre": "cuarto privado con baño propio", "Precio": 154.0, "Ubicación": (-99.27086530036256, 19.314865453550965)},
                                                         {"Nombre": "533 Habitación céntrica en remodelación", "Precio": 189.0, "Ubicación": (-99.1956584278164, 19.372925252214305)},
                                                         {"Nombre": "Habitación no. 9 | Las Almendras", "Precio": 196.0, "Ubicación": (-99.21619, 19.37231)}]
    """
    

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
                    "Ubicación": (float(i["longitude"]), float(i["latitude"]))
                })
    

    # Tabla en streamlit
    st.dataframe(tabla)


    return tabla


