"""
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción>
separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones.
Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
"""

#Entrada
def introducir_palabra_espanol()->str:
    palabra_espanola = input("Ingrese una palabra en español: ")
    while len(palabra_espanola.strip()) < 1:
        palabra_espanola = input("Ingrese una palabra en español: ")
    return palabra_espanola
    
def introducir_traduccion_en_ingles(palabra_espanola:str)->str:
    traduccion_en_ingles = input("Ingrese la traducción de {palabra_espanola}: ")
    while len(traduccion_en_ingles.strip()) <1:
        traduccion_en_ingles = input('Ingrese la traducción de {palabra_espanola}: ')
    return traduccion_en_ingles
    
def seguir_introduciendo_traducciones()->bool:
    confirmar_continuacion = input("¿Quieres seguir añadiendo traducciones?(S/N)")
    while confirmar_continuacion.upper() != "S" and confirmar_continuacion != "N":
        confirmar_continuacion = input("¿Quieres seguir añadiendo traducciones?(S/N)")
        
    if confirmar_continuacion == "S":
        return True
    else:
        return False

def introducir_frase()->str:
    frase_introducida = input("Ingrese una frase que quieras traducir: ")
    while len(frase_introducida.split()) <1:
        frase_introducida = input("Ingrese una frase que quieras traducir: ")
    return frase_introducida

#Procesado
def anadir_traduccion(diccionario:dict,palabra_espanol:str,traduccion_ingles:str):
    diccionario.update({palabra_espanol:traduccion_ingles})
def traducir_frase(frase:str,diccionario_traducciones:dict)->str:
    frase_por_palabra = frase.split()
    frase_traducida = ""
    for palabra_a_traducir in frase_por_palabra:
        if palabra_a_traducir in diccionario_traducciones:
            frase_traducida += diccionario_traducciones[palabra_a_traducir] + " "
        else:
            frase_traducida += palabra_a_traducir
    return frase_traducida
    
#Salida
    
def mostrar_traduccion(traduccion:str):
    return traduccion
    
if __name__ == "__main__":
    #Entrada
    diccionario_traduccion = {}
    seguir_traduciendo = True
    
    while seguir_traduciendo:
        palabra_espanola = introducir_palabra_espanol()
        traduccion_inglesa = introducir_traduccion_en_ingles(palabra_espanola)
        
        anadir_traduccion(diccionario_traduccion,palabra_espanola,traduccion_inglesa)
        
        seguir_traduciendo = seguir_introduciendo_traducciones()

    frase_a_traducir = introducir_frase()
    
    #Procesado
    
    frase_traducida = traducir_frase(frase_a_traducir,diccionario_traduccion)

    #Salida
    
    traduccion_final = mostrar_traduccion(frase_traducida)
    print(traduccion_final)