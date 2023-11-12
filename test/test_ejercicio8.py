from src.ejercicio8 import *


def test_anadir_traduccion_al_diccionario():
    p_espanola = "patata"
    p_ingles = "potatoe"
    prueba = {}
    
    copia_prueba = prueba.copy()
    anadir_traduccion(copia_prueba,p_espanola,p_ingles)
    
    assert prueba != copia_prueba
    assert copia_prueba == {"patata":"potatoe"}