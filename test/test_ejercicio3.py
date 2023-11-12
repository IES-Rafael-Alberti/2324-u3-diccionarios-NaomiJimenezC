from src.ejercicio3 import comprobar_stock,calcular_precio,mostrar_precio,mostrar_falta_stock

def test_comprobar_stock_fruta_existente():
    assert comprobar_stock("Plátano") == True
    assert comprobar_stock("Manzana") == True
    assert comprobar_stock("Pera") == True
    assert comprobar_stock("Naranja") == True
    
def test_calcular_precio_kilos():
    assert calcular_precio(1,"Naranja") == 0.7
    
def test_mensaje_de_fruta_existente():
    precio_kilos = 15.75
    assert mostrar_precio(precio_kilos) == "El precio de los kilos solicitados es de 15.75"
    
def test_mensaje_de_fruta_inexistente():
    assert mostrar_falta_stock() == "No nos queda stock de esa fruta"