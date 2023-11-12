"""
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en
el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente.
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente,
(2) Eliminar cliente, 
(3) Mostrar cliente, 
(4) Listar todos los clientes, 
(5) Listar clientes preferentes, 
(6) Terminar. 

En función de la opción elegida el programa tendrá que hacer lo siguiente:

    Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    Preguntar por el NIF del cliente y mostrar sus datos.
    Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    Terminar el programa.

"""

#Entrada

def introducir_opcion()->str:
    opciones_disponibles = ["1","2","3","4","5","6"]
    opcion_introducida = input("Introduce una opción que desees hacer (1,2,3,4,5,6): ")
    
    while opcion_introducida not in opciones_disponibles:
        opcion_introducida = input("Introduce una opción que desees hacer (1,2,3,4,5,6): ")

    return opcion_introducida

def introducir_nif() -> str:
    nif_cliente = input("Introduce el nif del cliente: ")
    while len(nif_cliente) != 9:
        nif_cliente = input("Introduce el nif del cliente: ")
    return nif_cliente

def introducir_nombre() -> str:
    nombre_introducido = input("Introduce un nombre: ")
    while len(nombre_introducido.strip()) < 1 or nombre_introducido.isalpha() != True:
        nombre_introducido = input("Introduce un nombre: ")
    return nombre_introducido

def introducir_direccion() -> str:
    direccion_introducida = input("Introduce tu dirección: ")
    while len(nombre_introducido.strip()) < 1:
        direccion_introducida = input("Introduce tu dirección: ")
    return direccion_introducida

def introducir_telefono() -> int:
    telefono_introducido = input("Introduce tu número de teléfono: ")
    while len(telefono_introducido) != 9 or telefono_introducido.isdecimal() != True:
        telefono_introducido = input("Introduce tu número de teléfono: ")
    return int(telefono_introducido)

def introducir_email() -> str:
    correo_introducido = input("Introduce su email: ")
    while len(correo_introducido.strip()) < 1:
        correo_introducido = input("Introduce su email: ")
    return correo_introducido

def es_preferente() -> bool:
    es_preferente = input("¿Es un cliente preferente?")
    while es_preferente.upper() != "S" and es_preferente.upper() != "N":
        es_preferente = input("¿Es un cliente preferente?")
        
    if es_preferente == "S":
        return True
    else:
        return False
        
#Procesado

def crear_contacto(nif:str,nombre:str,direccion:str,tlf:int,email:str,es_vip:bool)->tuple:
    cliente = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": tlf,
        "email": email,
        "es_vip": es_vip
    }
    
    return (nif,cliente)

def anadir_cliente(agenda:dict,info_contacto_a_anadir:tuple):
    agenda.update({info_contacto_a_anadir[0]:info_contacto_a_anadir[1]})
    
def eliminar_cliente(nif_cliente:str,agenda_contacto:dict):
    if nif_cliente in agenda_contacto:
        agenda_contacto.pop(nif_cliente)

def mostrar_info_cliente(nif_cliente,agenda_contacto:dict):
    info_cliente = ""
    if nif_cliente in agenda_contacto:
        for info in agenda_contacto[nif_cliente]:
            info_cliente += info + "\n"
    return info_cliente

def mostrar_info_clientes(agenda_contacto:dict)->str:
    info_contactos= ""
    for info_contacto in agenda_contacto.items():
        info_contactos += info_contacto[0] +","+info_contacto[1]["nombre"]+"\n"
    return info_contacto

def mostrar_clientes_preferentes(agenda_contacto:dict)->str:
    clientes_preferentes = ""
    for nif_cliente,info_cliente in agenda_contacto.items():
        if info_cliente["es_vip"]:
            clientes_preferentes += nif_cliente + "\n"
    return clientes_preferentes
#Salida

def menu():
    return f"Elige algunas de las opciones: \n 1-Añadir Cliente\n2-Eliminar Cliente\n3-Mostrar Cliente\n4-Listar todos los clientes\n5-Listar clientes vip"

if __name__ == "__main__":
    clientes = {}
    seguir_ejecutando_programa = True
    
    while seguir_ejecutando_programa:
        print(menu())
        opcion_escogida = introducir_opcion()
        
        if opcion_escogida == "1":
            nif_cliente = introducir_nif()
            nombre_cliente = introducir_nombre()
            direccion_cliente = introducir_direccion()
            tlf_cliente = introducir_telefono()
            email_cliente = introducir_email()
            preferencia_cliente = es_vip()
            
            cliente_contacto = crear_contacto(nif_cliente,nombre_cliente,direccion_cliente,tlf_cliente,email_cliente,preferencia_cliente)
            anadir_cliente(clientes,cliente_contacto)
            
        if opcion_escogida == "2":
            nif_cliente = introducir_nif()
            eliminar_cliente(nif_cliente,clientes)
            
        if opcion_escogida == "3":
            nif_cliente = introducir_nif()
            
            info_contaco = mostrar_info_cliente(nif_cliente,clientes)
            print(info_contaco)
        
        if opcion_escogida == "4":
            info_clientes = mostrar_info_clientes(clientes)
            print(info_clientes)
        
        if opcion_escogida == "5":
            info_clientes_vip = mostrar_clientes_preferentes(clientes)
            print(info_clientes_vip)
        if opcion_escogida == "6":
            seguir_ejecutando_programa == False