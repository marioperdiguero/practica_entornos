def add(a, b):
    """"
        Función que retorna la suma de dos números
    """
    return a + b

def subtract(a, b):
    """"
        Función que retorna la resta de dos números
    """
    return a - b

def multiply(a, b):
    """"
        Función que retorna la multiplicación de dos números
    """
    return a * b

def divide(a, b):
    """"
        Función que retorna la división de dos números
    """
    return a / b

def menu_choice():
    """"
        Función que muestra el menú de la aplicación
    """
    funciones = ["sumar", "restar", "multiplicar", "dividir"]

    for i in range(len(funciones)):
        print(str(i + 1) + "-", funciones[i])
    
    return int(input(" Elige opción: "))


menu_choice()