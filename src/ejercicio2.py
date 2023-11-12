"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
"""

#Entrada

def solicitar_edad()->int:
    edad_ingresada = input("Ingrese su edad: ")
    while edad_ingresada.isdecimal() != True:
      edad_ingresada = input("Ingrese su edad: ")
    return int(edad_ingresada)  

def solicitar_nombre()->str:
    nombre_ingresado = input("Ingrese su nombre: ")
    while len(nombre_ingresado.strip()) < 1 or nombre_ingresado.isalpha() != True:
        nombre_ingresado = input("Ingrese su nombre: ")
    return nombre_ingresado

def solicitar_direccion()->str:
    direccion_ingresada = input("Ingrese su dirección: ")
    while len(direccion_ingresada.strip()) < 1:
        direccion_ingresada = input("Ingrese su dirección: ")
    return direccion_ingresada

def solicitar_tlf()->int:
    tlf_ingresado = input("Ingrese su número de teléfono: ")
    while len(tlf_ingresado) != 9 or tlf_ingresado.isdecimal() != True:
        tlf_ingresado = input("Ingrese su número de teléfono: ")
    return int(tlf_ingresado)

#Procesado
def crear_contacto(nombre:str,edad:int,direccion:str,tlf:int)->dict:
    contacto = {"nombre":nombre,"edad":edad,"direccion":direccion,"tlf":tlf}
    return contacto

#Salida
def mostrar_info_contacto(contacto:dict)->str:
    return f"{contacto['nombre']} tiene {contacto['edad']} años, vive en {contacto['direccion']} y su número de teléfono es {contacto['tlf']}"
    
    return ""
if __name__ == "__main__":
    #Entrada
    nombre = solicitar_nombre()
    edad = solicitar_edad()
    direccion = solicitar_direccion()
    telefono = solicitar_tlf()
    #Procesado
    contacto = crear_contacto(nombre,edad,direccion,telefono)
    revelar_info_contacto = mostrar_info_contacto(contacto)
    #Salida
    print(revelar_info_contacto)