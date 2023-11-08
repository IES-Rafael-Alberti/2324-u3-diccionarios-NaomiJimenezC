"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, 
un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario 
debe mostrar un mensaje informando de ello
"""

#Entrada
def solicitar_fruta()->str:
    fruta_ingresada = input("Ingrese una fruta: ")
    while len(fruta_ingresada.strip()) < 1 or fruta_ingresada.isalpha() != True:
        fruta_ingresada = input("Ingrese una fruta: ")
    return fruta_ingresada.capitalize()

def solicitar_kilos()->int:
    kilos_deseados = input("Ingrese cuantos kilos de fruta desea: ")
    while kilos_deseados.isdecimal() != True:
        kilos_deseados = input("Ingrese cuantos kilos de fruta desea: ")
    return int(kilos_deseados)
    
#Procesado

def comprobar_stock(fruta_deseada:str)->bool:
    frutas_disponibles = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    if fruta_deseada in frutas_disponibles.keys():
        return True

def calcular_precio(kilos_solicitados:int,fruta_deseada:str)->float:
    precios_por_kilo = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    precio_por_kilo = precios_por_kilo[fruta_deseada]
    return kilos_solicitados * precio_por_kilo

#Salida
    
def mostrar_precio(precio_kilos:float)->str:
    return f"El precio de los kilos solicitados es de {precio_kilos}"
    
def mostrar_falta_stock()->str:
    return "No nos queda stock de esa fruta"

if __name__ == "__main__":

    fruta_deseada = solicitar_fruta()
    kilos_deseados = solicitar_kilos()
    queda_stock = comprobar_stock(fruta_deseada)
    
    if queda_stock:
        precio_kilos = calcular_precio(kilos_deseados,fruta_deseada)
        mensaje_precio = mostrar_precio(precio_kilos)
        print(mensaje_precio)
    else:
        mensaje_no_stock = mostrar_falta_stock()
        print(mensaje_no_stock)