from src.ejercicio1 import comprobar_divisa,mostrar_divisa

def test_comprobacion_divisa_correcta():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert comprobar_divisa(divisas,"Euro") == True
    assert comprobar_divisa(divisas,"Dollar") == True
    assert comprobar_divisa(divisas,"Yen") == True
    
def test_comprobacion_divisa_incorrecto():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert comprobar_divisa(divisas,"as") == None

def test_mostrar_divisa_correcta():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert mostrar_divisa(divisas,"Euro",True) == "La divisa que ingresó es el Euro,cuyo símbolo es €"

def test_mostrar_divisa_incorrecta():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert mostrar_divisa(divisas,"as",None) == "La divisa que ingresó no es correcta"