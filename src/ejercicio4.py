"""
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por 
pantalla la misma fecha en formato <dd de <mes> de aaaa> donde <mes> es el nombre del mes.
"""

#Entrada
def solicitar_fecha()->str:
    fecha_ingresada = input("Ingrese una fecha con el siguiente formato (dd/mm/aaaa): ")
    while fecha_ingresada.count("/") != 2 or len(fecha_ingresada) != 10: #10 es la longitud de una fecha en ese formato
        fecha_ingresada = input("Ingrese una fecha con el siguiente formato (dd/mm/aaaa): ")
    return fecha_ingresada
#Procesado
def extractor_fecha(fecha_a_romper:str)->list:
    return fecha_a_romper.split("/")

def comprobar_formato_dia(fecha:str)->int:
    try:
        dia = int(fecha[0])
        return dia
    except ValueError as e:
        raise(ValueError,"Este número no es válido")


#Salida

if __name__ == "__main__":
    #Entrada
    fecha_ingresada = solicitar_fecha()
    #Procesado
    #Salida
    print(fecha_ingresada)