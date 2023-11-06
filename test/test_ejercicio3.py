from src.ejercicio3 import comprobar_stock,calcular_precio,mostrar_precio

def test_comprobar_stock_fruta_existente():
    assert comprobar_stock("Plátano") == True
    assert comprobar_stock("Manzana") == True
    assert comprobar_stock("Pera") == True
    assert comprobar_stock("Naranja") == True
    
def test_calcular_precio_kilos():
    assert calcular_precio(1,0.70) == 0.70
    
def test_mensaje_de_fruta_existente():
    queda_stock_fruta = True
    precio_kilos = 15.75
    assert mostrar_precio(queda_stock_fruta,precio_kilos) == "El precio de los kilos solicitados es de 15.75"
    
def test_mensaje_de_fruta_inexistente():
    queda_stock_fruta = False
    precio_kilos = 15.75
    assert mostrar_precio(queda_stock_fruta,precio_kilos) == "Lo siento no queda stock de esa fruta"