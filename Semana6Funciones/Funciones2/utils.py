#Luis Gerardo Dávalos Velásquez 240278
def leer_numero(i):
    while True:
        try:
            return float(input(f"Ingresa el número {i}: "))
        except ValueError:
            print("El dato ingresado debe ser numérico")

def calcular_media(suma, cantidad):
    return suma/cantidad

def calcular_varianza(suma_cuadrados, suma, cantidad):
    return (suma_cuadrados/3) - (suma/3)**2

def calcular_desviacion_estandar(varianza):
    return varianza**0.5

def comparar_numeros(numero, mayor, menor):
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
    
    return mayor, menor