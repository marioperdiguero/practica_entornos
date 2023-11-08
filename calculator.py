def add(a, b):
    return a + b

def subtract(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def menu_choice():
    funciones = ["sumar", "restar", "multiplicar", "dividir"]

    for i in range(len(funciones)):
        print(str(i + 1) + "-", funciones[i])
    
    return int(input(" Elige opción: "))


menu_choice()