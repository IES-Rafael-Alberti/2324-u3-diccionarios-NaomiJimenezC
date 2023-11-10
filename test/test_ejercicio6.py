
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

def test_anadir_info_personal_al_diccionario():
    datos_peter = {}
    anadir_info_personal(datos_peter,"Nombre","Peter")
    assert datos_peter == {"Nombre":"Peter"}