from src.ejercicio2 import crear_contacto


def test_guardar_info_contacto():
    nombre = "Naomi"
    edad = 19
    direccion = "Avenida Tercera Agudo 8, 1A"
    num_tlf = 615611087
    
    assert crear_contacto(nombre,edad,direccion,num_tlf) == {"nombre":"Naomi","edad":19,"direccion":"Avenida Tercera Agudo 8, 1A","tlf":615611087}
