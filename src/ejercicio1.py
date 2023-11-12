"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre 
su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

#ENtrada
def ingresar_divisa()->str:
    divisa_ingresada = input("Ingrese una divisa (Euro,Dollar,Yen) : ")
    while len(divisa_ingresada.strip()) < 1:
        divisa_ingresada = input("Ingrese una divisa (Euro,Dollar,Yen) : ")
    return divisa_ingresada.capitalize()
#Procesado
def comprobar_divisa(divisas:dict,divisa_ingresada:str):
    """
    comprobar_divisa 

    Args:
        divisas (dict): Diccionario que guarda las divisas que se están trabajando
        divisa_ingresada (str): Le pasas la divisa que quieras comprobar

    Returns:
        True: Devuelve True si la divisa es correcta
    """
   
    if divisa_ingresada in divisas.keys():
        return True

#Salida

def mostrar_divisa(divisas:dict,divisa_ingresada:str,resultado_comprobacion):
    if resultado_comprobacion:
        return f"La divisa que ingresó es el {divisa_ingresada},cuyo símbolo es {divisas[divisa_ingresada]}"
    else:
        return "La divisa que ingresó no es correcta"
    
if __name__ == "__main__":
    #Entrada
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa_ingresada = ingresar_divisa()
    #Procesado
    comprobacion_divisa_ingresada = comprobar_divisa(divisas,divisa_ingresada)
    
    mensaje_divisa= mostrar_divisa(divisas,divisa_ingresada,comprobacion_divisa_ingresada)
    #Salida
    print(mensaje_divisa)