from src.ejercicio9 import *


def test_crear_factura():
    facturas = {}
    num_factura_prueba = "num_factura"
    coste = 25.25
    
    crear_factura(facturas,num_factura_prueba,coste)
    
    assert len(facturas) == 1
    
def test_calcular_cantidad_pendiente_de_pago():
    facturas_prueba = {"a":50.00,"b":50.00}
    cantidad_pendiente = 0
    
    assert calcular_pago_pendiente(cantidad_pendiente,facturas_prueba) == 100.00
    
def test_recalcular_cantidad_pendiente():
    cantidad_pendiente = 500
    factura = {"a":50}
    
    nueva_cantidad_pendiente = reducir_cantidad_pendiente(cantidad_pendiente,"a",factura)
    
    assert nueva_cantidad_pendiente == 450