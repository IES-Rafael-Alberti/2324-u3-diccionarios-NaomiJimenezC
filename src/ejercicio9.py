"""
Escribir un programa que gestione las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura.
El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. 
Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 
Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
"""

#Entrada
def introducir_opcion()->str:
    opciones_posibles = ["1","2","3"]
    opcion_escogida = input("Escoge una de las opciones que salen en el menú (1,2,3): ")
    
    while opcion_escogida in opciones_posibles != True:
        opcion_escogida = input("Escoge una de las opciones que salen en el menú: ")
    
    return opcion_escogida

def introducir_num_factura()->str:
    num_factura_introducida = input("Introduce el número de factura: ")
    while len(num_factura_introducida.strip()) < 1:
        num_factura_introducida = input("Introduce el número de factura: ")
    return num_factura_introducida

def introducir_coste_factura()->float:
    coste_correcto = False
    while coste_correcto != True:
        try:
            coste_introducido = float(input("Introduce el coste de la factura: "))
            return coste_introducido
            coste_correcto = True
        except:
            pass
        
#Procesado

def crear_factura(carpeta_facturas:dict,num_factura:str,coste:float):
    carpeta_facturas.update({num_factura:coste})

def calcular_pago_pendiente(cantidad_pendiente,facturas:dict)-> float:
    cantidad_pendiente += sum(facturas.values())
    return cantidad_pendiente

def reducir_cantidad_pendiente(cantidad_pendiente,num_factura_pagada:str,facturas:dict):
    return cantidad_pendiente - facturas[num_factura_pagada]

def eliminar_factura(num_factura:str,factura:dict):
    if num_factura in factura:
        factura.pop(num_factura)

#Salida

def menu():
    return f"Escoge alguna de las 3 opciones\n 1-Añadir factura \n 2-Pagar factura \n 3-Salir"

def mostrar_cantidad_pendiente(cantidad_pendiente:float)->str:
    return f"Queda pendiente {cantidad_pendiente} euros"

if __name__ == "__main__":
    #Entrada
    facturas = {}
    cantidad_pendiente = 0
    seguir_usando_programa = True
    
    
    while seguir_usando_programa:
        print(menu())
        opcion_escogida = introducir_opcion()
        
        if opcion_escogida == "1":
            num_factura_a_anadir = introducir_num_factura()
            coste_factura = introducir_num_factura()
            crear_factura(num_factura_a_anadir,coste_factura)
            
            calcular_pago_pendiente(cantidad_pendiente,facturas)
            print(mostrar_cantidad_pendiente(cantidad_pendiente))
        
        if opcion_escogida == 2:
            num_factura_a_pagar = introducir_num_factura() 
            cantidad_actualizada = reducir_cantidad_pendiente(cantidad_pendiente,num_factura_a_pagar,facturas)
            eliminar_factura(num_factura,facturas)
            print(mostrar_cantidad_pendiente(cantidad_actualizada))
            
        if opcion_escogida == 3:
            seguir_usando_programa = False