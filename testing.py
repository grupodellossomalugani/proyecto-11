from Pregunta_1 import AUX_PREGUNTA_1
from Pregunta_4 import PREGUNTA_4
from Pregunta_5 import PREGUNTA_5
from Pregunta_6 import PREGUNTA_6
from lector import dataset
from Pregunta_2 import PREGUNTA_2
from Pregunta_3 import PREGUNTA_3, lista_de_alcaldias



"""
# test pregunta 1

def test_devuelve_5_elementos():

    resultado = AUX_PREGUNTA_1()
    assert len(resultado) == 5

def test_cada_elemento():
    rta = AUX_PREGUNTA_1()
    for i in rta:
        assert len(i) == 2

def test_promedio_flotante():
    rta = AUX_PREGUNTA_1()

    for i in rta:
        assert type(i[1] ) == float

def test_ordenado_mayor_a_menor():
    rta = AUX_PREGUNTA_1()
    
    for i in range(len(rta)-1):
        assert rta[i][1] >= rta[i+1][1]

#==================================================
#test pregunta 2

def test_PREGUNTA_2_p1():
    assert PREGUNTA_2("Coyoacán") == None

def test_PREGUNTA_2_p2():
    assert PREGUNTA_2("Cuauhtémoc") == None


#==========================================================


#test PREGUNTA 3


def test_PREGUNTA_3():
    rta = PREGUNTA_3(0)

    assert type(rta) == int

def test_PREGUNTA_3_alvaro_obregon():
    cant = 0
    for fila in dataset():
        if fila["neighbourhood"] == "Álvaro Obregón":
            cant += 1
    assert PREGUNTA_3(0) == cant

def test_PREGUNTA_3_coyoacan():
    cant = 0
    for fila in dataset():
        if fila["neighbourhood"] == "Coyoacán":
            cant += 1
    assert PREGUNTA_3(3) == cant
"""

def test_PREGUNTA_4():


    # Dataset vacio
    DATOS1 = ["Xochimilco", "Coyoacán"]

    assert PREGUNTA_4(DATOS1,[]) == (DATOS1, [])


    # Promedio de varios precios
    ALCALDIA2 = ["Coyoacán"]
    DATOS2 = [{"neighbourhood": "Coyoacán", "price": "100"},{"neighbourhood": "Coyoacán", "price": "200"},{"neighbourhood": "Coyoacán", "price": "300"}]
    
    assert PREGUNTA_4(ALCALDIA2, DATOS2) == (["Coyoacán"] , [200.0])


    # Precios validos e invalidos
    ALCALDIAS3 = ["Iztapalapa"]

    DATOS3 = [{"neighbourhood": "Iztapalapa", "price": ""},{"neighbourhood": "Iztapalapa", "price": "100"},{"neighbourhood": "Iztapalapa", "price": ""},{"neighbourhood": "Iztapalapa", "price": "300"}]
    
    assert PREGUNTA_4(ALCALDIAS3, DATOS3) == (["Iztapalapa"],[200.0])


    # Alcaldia sin hospedaje
    ALCALDIAS4 = ["Xochomilco", "Coyoacán"]
    DATOS4 = [
        {"neighbourhood": "Xochomilco", "price": "100"}]

    assert PREGUNTA_4(ALCALDIAS4, DATOS4) == (["Xochomilco", "Coyoacán"],[100.0])




def test_PREGUNTA_5():
    

    # Varios hospedajes en rango
    RESULTADO1 = [{"Nombre": "Cómodo y lindo Dpto.", "Precio": 150.0, "Ubicación": (-99.24999814788514, 19.32927732036978)},
                 {"Nombre": "cuarto privado con baño propio", "Precio": 154.0, "Ubicación": (-99.27086530036256, 19.314865453550965)},
                 {"Nombre": "533 Habitación céntrica en remodelación", "Precio": 189.0, "Ubicación": (-99.1956584278164, 19.372925252214305)},
                 {"Nombre": "Habitación no. 9 | Las Almendras", "Precio": 196.0, "Ubicación": (-99.21619, 19.37231)}]
    assert PREGUNTA_5("Álvaro Obregón" , 200.0 , dataset()) == RESULTADO1

    
    # Dataset vacio
    RESULTADO2 = []

    assert PREGUNTA_5("Álvaro Obregón", 200, RESULTADO2) == RESULTADO2

    
    # Sobreprecio
    DATOS1 = [{"name": "Hotel A","neighbourhood": "Xochimilco","price": "300","longitude": "-99.12000","latitude": "19.43444"}]

    assert PREGUNTA_5("Xochimilco", 200, DATOS1) == []


    # Alcaldia distinta
    RESULTADO3 = [
        {"name": "Hotel B","neighbourhood": "Coyoacán","price": "100","longitude": "-99.12475","latitude": "19.43449"}]

    assert PREGUNTA_5("Benito Juárez", 200, RESULTADO3) == []



def test_PREGUNTA_6():
    
    # Varios hospedajes en rango
    DATOS1 = [{"name": "Hotel Catedral","longitude": "-99.13306","latitude": "19.43444","price": 500},
              {"name": "Hotel Cercano","longitude": "-99.13250","latitude": "19.43400","price": 800},
              {"name": "Hotel Lejano","longitude": "-99.12000","latitude": "19.42000","price": 1200}]
    RESULTADO1 = [{"Nombre": "Hotel Catedral","Distancia(Km)": 0.0,"Precio": 500,"Ubicación": (-99.13306, 19.43444)},
                  {"Nombre": "Hotel Cercano","Distancia(Km)": 0.1,"Precio": 800,"Ubicación":(-99.13250,19.43400)}]

    assert PREGUNTA_6(DATOS1) == RESULTADO1
    

    # Dataset vacio
    DATOS2 = []
    assert PREGUNTA_6(DATOS2) == []


    # Hotel fuera de rango
    DATOS3 = [{"name": "Hotel Fuera de Rango","longitude": "-99.12000","latitude": "19.42000","price": 700}]
    assert PREGUNTA_6(DATOS3) == []


