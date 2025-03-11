#Luis Gerardo Dávalos Velásquez 240278
from random import *
def saludar(nombre):
    """ Esta función recibe un nombre y devuelve un saludo
        Parametros:
         nombre (str): El nombre de la persona a saludar
        
        Retorna:
         str: Un mensaje de saludo personalizado """
    mensaje = (f"¡Hola, {nombre}! Bienvenido/a al mundo de las funciones")
    return mensaje

def contar_vocales(palabra):
    """
    Esta función recibe una palabra y cuenta cuántas vocales contiene.
   
    Parámetros:
    palabra (str): La palabra de la que se contarán las vocales
   
    Retorna:
    int: La cantidad de vocales que contiene la palabra
    """
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in palabra:
        if letra.lower() in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

def longitud_nombre(nombre):
    return len(nombre)

def juego(nombre):
    cpu = randint(1,3)
    print("\nJuguemos piedra, papel y tijeras")
    print("1. Piedra\n2. Papel\n3. Tijeras")
    try:
        player = int(input("Escoge su jugada (1, 2 o 3): "))
    except ValueError:
        print("Solo se aceptan números")
        return
    if player > 3 or player < 1:
        print("Opción invalida")
        return

    if cpu == 1:
        print("Yo juego: Piedra")
    elif cpu == 2:
        print("Yo juego: Papel")
    else:
        print("Yo juego: Tijeras")

    if player == cpu:
        print("Empate")
    elif (player==1 and cpu==3) or (player==2 and cpu == 1) or (player==3 and cpu == 2):
        print(f"Ganaste {nombre}, eres bueno")
    else:
        print("Perdiste, mejor suerte la proxima")
    return

def edad():
    try:
        nacimiento = int(input("\nIngresa el año en el que naciste: "))
    except ValueError:
        print("Solo se aceptan números")
        return
    
    if nacimiento > 2025:
        print("Año de nacimiento invalido")
        return
    
    edad = 2025 - nacimiento
    print(f"Tienes {edad} años")

def suma():
    try:
        num1 = float(input("\nIngresa un número: "))
        num2 = float(input("Ingresa otro número: "))
        return num1 + num2
    except ValueError:
        print("Solo se permiten números")
        return None

def imprimir_piramide(nombre):
    print(f"\n Aqui tienes tu pirámide {nombre}:\n")
    for i in range(1,6):
        for k in range(5,i,-1):
            print(" ",end="")
        for j in range(i*2):
            print("*",end="")
        print("")