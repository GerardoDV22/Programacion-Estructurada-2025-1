#Luis Gerardo Dávalos Velásquez 240278
from funciones import *

#Parte 1
print("Imprimir una matriz 3x3")
matriz = [1,2,3,],[4,5,6],[7,8,9]
imprimir_matriz(matriz)
print("\n~~~~~~~~~~~\n~~~~~~~~~~~\n~~~~~~~~~~~")

#Parte 2 y 4.1
print("\nSuma de matrices:")
a = [1,2,5],[3,4,6]
b = [5,6,9],[7,8,6]
print("\nMatriz A:")
imprimir_matriz(a)
print("\nMatriz B:")
imprimir_matriz(b)
print("\nSuma de A + B:")
sumar_matrices(a,b)
print("\n~~~~~~~~~~~\n~~~~~~~~~~~\n~~~~~~~~~~~")

#Parte 3
print("\nTransponer una matriz")
matriz = [1,2,3,],[4,5,6,]
print("\nMatriz original:")
imprimir_matriz(matriz)
print("\nMatriz transpuesta:")
imprimir_matriz(transponer_matriz(matriz))
print("\n~~~~~~~~~~~\n~~~~~~~~~~~\n~~~~~~~~~~~")

#Parte 4.2
print("\nMultiplicar matrices")
a = [1,2,2],[3,4,5]
b = [1,1,3],[0,2,4],[0,0,0]
print("\nMatriz A:")
imprimir_matriz(a)
print("\nMatriz B:")
imprimir_matriz(b)
print("\nMatriz Resultado:")
multiplicar_matriz(a,b)

#len(a) = filas
#len(a[0]) = columnas