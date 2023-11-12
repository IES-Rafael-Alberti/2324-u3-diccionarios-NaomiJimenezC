from src.ejercicio7 import *

def test_anadir_cosas_a_la_lista_de_la_compra():
    lista_compra = {"8GB RAM":1.50}
    articulo_prueba = "Ryzen 5600X"
    precio_prueba = 2.50
    
    copia_lista_compra = lista_compra.copy()
    
    anadir_lista_compra(copia_lista_compra,articulo_prueba,precio_prueba)
    
    assert copia_lista_compra != lista_compra
    
    

    
def test_sumar_precios_lista_de_la_compra():
    precios_articulos = {
        'Camiseta': 19.99,
        'Pantalones': 29.99,
        'Zapatos': 59.99,
        'Sombrero': 9.99,
        'Bufanda': 14.99
    }   
    assert calcular_precio_final(precios_articulos) == 134.95
