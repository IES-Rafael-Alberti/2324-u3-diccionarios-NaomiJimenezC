from src.ejercicio5 import sacar_asignatura_creditos

def test_sacar_asignatura_creditos():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    assert sacar_asignatura_creditos(asignaturas) == [("Matemáticas",6),("Física",4),("Química",5)]