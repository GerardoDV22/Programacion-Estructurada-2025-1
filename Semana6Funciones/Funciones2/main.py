#Luis Gerardo Dávalos Velásquez 240278
from utils import *
print("Bienvenido al sistema de calculo estadistico")
while True:
    try:
        n = int(input("Ingresa de que tamaño es tu muestra de datos: "))
        break
    except ValueError:
        print("Solo se permiten numeros")
mayor = 0
menor = 0
suma = 0
suma_cuadrada = 0
for i in range(n):
    numero = leer_numero(i+1)
    if i == 0:
        mayor = numero
        menor = numero
    else:
        mayor, menor = comparar_numeros(numero, mayor,menor )
    suma += numero
    suma_cuadrada += numero**2

media = calcular_media(suma,n)
varianza = calcular_varianza(suma_cuadrada, suma, n)
desviacion_estandar = calcular_desviacion_estandar(varianza)
print("Resultados:")
print(f"Media: {media:.2f}\nVarianza: {varianza:.2f}\nDesviación estandar: {desviacion_estandar:.2f}")
print(f"Dato mayor ingresado: {mayor}\nDato menor ingresado: {menor}")