from src.ejercicio4 import extractor_fecha,comprobar_formato_dia
import pytest 

def test_extractor_componentes_fecha():
    fecha_prueba = "08/05/2004"
    assert extractor_fecha(fecha_prueba) == ["08","05","2004"]

def test_comprobar_formato_dia_correcto():
    fecha_rota = ["08","05","2004"]
    assert comprobar_formato_dia(fecha_rota) == 8

def test_comprobar_formato_dia_incorrecto():
    fecha_rota = ["aa","05","2004"]
    with pytest.raises(ValueError):
        comprobar_formato_dia(fecha_rota) 