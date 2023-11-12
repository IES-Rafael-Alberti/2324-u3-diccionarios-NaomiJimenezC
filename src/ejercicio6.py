"""
Escribir un programa que cree un diccionario vacío y lo vaya llenado con 
información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, 
correo electrónico, etc.) que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

#Entrada
def introducir_campo_de_informacion_persona()->str:
    """Permite introducir por consola un campo de información personal

    Returns
    -------
    str
        devuelve el campo que desea ser introducido
    """
    campo_introducido = input("Añade sobre que campo de información personal quieres guardar: ")
    while len(campo_introducido.strip()) < 1:
        campo_introducido = input("Añade sobre que campo de información personal quieres guardar: ")
    return campo_introducido

def introducir_info_personal(campo:str)->str:
    """Permite introducir la información relacionada con un campo de información concreto

    Parameters
    ----------
    campo : str
        Es el campo del que se quiere añadir información

    Returns
    -------
    str
        Devuelve la información de dicho campo
    """
    informacion_introducida = input(f"¿Qué información quieres añadir sobre {campo}?")
    while len(informacion_introducida.strip()) < 1:
        informacion_introducida = input(f"¿Qué información quieres añadir sobre {campo}?")
    return informacion_introducida

#Procesado



def anadir_info_personal(contacto:dict,campo:str,info_del_campo:str):
    """Actualiza la información de un diccionario con un campo y su respectiva info

    Parameters
    ----------
    contacto:dict
        Diccionario que contiene toda la información personal de la persona
    campo : str
        Tema del que se quiere añadir información
    info_del_campo : str
        Información del campo
    """
    contacto.update({campo:info_del_campo})

#Salida
def mostrar_contenido_del_contacto(info_contacto:dict)->str:
    return f"Los campos del contacto son: \n {info_contacto}"

if __name__ == "__main__":
    #Entrada
    contacto_nuevo = {}
    campo_a_querer_anadir = introducir_campo_de_informacion_persona()
    info_del_campo = introducir_info_personal(campo_a_querer_anadir)
    
    #Procesado
    seguir_anadiendo_info = True
    while seguir_anadiendo_info:
        anadir_info_personal(contacto_nuevo,campo_a_querer_anadir,info_del_campo)
        contenido_actual_contacto = mostrar_contenido_del_contacto(contacto_nuevo)
        print(contenido_actual_contacto)        
    