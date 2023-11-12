from src.ejercicio6 import anadir_info_personal

def test_anadir_info_personal_al_diccionario():
    datos_peter = {}
    anadir_info_personal(datos_peter,"Nombre","Peter")
    assert datos_peter == {"Nombre":"Peter"}