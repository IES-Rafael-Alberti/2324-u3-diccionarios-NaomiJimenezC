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
#Salida

if __name__ == "__main__":
    #Entrada
    #Procesado
    #Salida
    print()