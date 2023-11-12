"""
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 
el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se 
debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
"""

#Entrada

def ingresar_nombre_articulo()->str:
    articulo_ingresado = input("Ingrese el nombre del artículo: ")
    while len(articulo_ingresado.strip()) < 1:
        articulo_ingresado = input("Ingrese el nombre del artículo: ")
    return articulo_ingresado

def ingresar_precio_articulo()->float:
    es_un_precio_valido = False
    while es_un_precio_valido != True:
        try:
             articulo_ingresado = float(input("Ingrese el precio del artículo: "))
             es_un_precio_valido = True
        except:
            pass
        
def seguir_anadiendo_productos()-> bool:
    confirmacion = input("¿Quieres seguir añadiendo productos?(S/N)")
    while confirmacion.upper() != "S" and confirmacion.upper() != "N":
        confirmacion = input("¿Quieres seguir añadiendo productos?(S/N)")
    if confirmacion.upper() == "S":
        return True
    else:
        return False

#Procesado

def anadir_lista_compra(lista_compra:dict,nombre_del_articulo:str,precio_del_articulo:float):
    lista_compra.update({nombre_del_articulo:precio_del_articulo})

def calcular_precio_final(lista_de_la_compra:dict):
    return sum(lista_de_la_compra.values())

#Salida

def mostrar_lista_de_la_compra(lista_compra:dict)->str:
    contenido_lista_de_la_compra= "La lista de la compra está hecho de: \n"
    for articulo in lista_compra.keys():
        contenido_lista_de_la_compra += articulo +"\n"
    return contenido_lista_de_la_compra

def mostrar_precio_final(precio_final:float)->str:
    return f"El coste total es de {precio_final} euros"

if __name__ == "__main__":
    #Entrada
    lista_compra = {}
    seguir_comprando = True
    
    while seguir_comprando:
        articulo_a_anadir = ingresar_nombre_articulo()
        precio_articulo = ingresar_precio_articulo()
        anadir_lista_compra(lista_compra,articulo_a_anadir,precio_articulo)
        seguir_comprando = seguir_anadiendo_productos()
    #Procesado
    precio_final = calcular_precio_final(lista_compra)
    #Salida
    articulos_pedidos = mostrar_lista_de_la_compra(lista_compra)
    mensaje_final = mostrar_precio_final(precio_final)
    
    print(articulos_pedidos)
    print(mensaje_final)