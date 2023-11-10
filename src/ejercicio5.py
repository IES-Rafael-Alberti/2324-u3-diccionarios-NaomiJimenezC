"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una 
de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número
total de créditos del curso.
"""

#Procesado
def sacar_asignatura_creditos(asignaturas_con_sus_creditos:dict)->list:
    """Saca de un diccionario una lista de asignaturas con sus creditos

    Parameters
    ----------
    asignaturas_con_sus_creditos : dict
        El diccionario que contiene la asignatura y sus créditos correspondientes

    Returns
    -------
    list
        Una lista de tuplas, cada tupla tendrá asignatura y su credito
    """
    
    asignaturas_extraidas = []
    for asignatura in asignaturas_con_sus_creditos.items():
        asignaturas_extraidas.append(asignatura)
    return asignaturas_extraidas

#Salida
def mostrar_credito_por_asignatura(lista_de_asignaturas:list)->str:
    """
    Una función que muestra los creditos de cada asignatura.

    Parameters
    ----------
    lista_de_asignaturas : list
        lista de tuplas, cada tupla tiene una asignatura y sus créditos

    Returns
    -------
    str
        Devuelve la cadena mostrando los créditos por asignatura
    """
    mensaje_credito = ""
    for asignatura_con_su_credito in lista_de_asignaturas:
        mensaje_credito += f"{asignatura_con_su_credito[0]} tiene {asignatura_con_su_credito[1]} créditos\n"
    return mensaje_credito


if __name__ == "__main__":
    #Entrada
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    #Procesado
    asignatuas_extraidas = sacar_asignatura_creditos(asignaturas)
    #Salida
    mensaje_creditos = mostrar_credito_por_asignatura(asignatuas_extraidas)
    print(mensaje_creditos)