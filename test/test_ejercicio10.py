from src.ejercicio10 import *



def test_anadir_clientes():
    clientes = {}
    nif_cliente = "87654321K"
    nombre = "Nora"
    direccion = "avenida prueba 11"
    email = "prueba@gmail.com"
    tlf = 615611097
    cliente_preferente = True
    cliente = crear_contacto(nif_cliente,nombre,direccion,tlf,email,cliente_preferente)
    
    anadir_cliente(clientes,cliente)
 
    assert len(clientes) == 1