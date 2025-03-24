#Luis Gerardo Dávalos Velásquez 240278
from funciones import *
# ===============================================================
# PRÁCTICA DE VECTORES (ARREGLOS) EN PYTHON PARA PRINCIPIANTES
# ===============================================================

"""
INSTRUCCIONES PARA LOS ALUMNOS:

1. Lee atentamente cada ejercicio antes de empezar a resolverlo.
2. Escribe tu código en los espacios indicados con "Tu código aquí".
3. Guarda este archivo como "practica_vectores_tunombre.py".
4. Ejecuta tu código para comprobar que funciona correctamente.
5. Asegúrate de que cada ejercicio produce el resultado esperado.

¡Buena suerte!
"""

# ===============================================================
# PARTE 1: EJERCICIOS BÁSICOS CON VECTORES
# ===============================================================

print("\n=== PARTE 1: EJERCICIOS BÁSICOS CON VECTORES ===\n")

# Recordatorio: Un vector en Python es simplemente una lista de elementos

# --------------------------
# Ejercicio 1: Crear y mostrar un vector de números del 1 al 10
# --------------------------
print("\n--- Ejercicio 1: Crear y mostrar un vector ---")

# Tu código aquí
numeros = [1,2,3,4,5,6,7,8,9,10]
print(numeros)

# Crea un vector llamado "numeros" que contenga los números del 1 al 10
# Luego muestra el vector completo usando print()

# --------------------------
# Ejercicio 2: Acceder y modificar elementos de un vector
# --------------------------
print("\n--- Ejercicio 2: Acceder y modificar elementos de un vector ---")

# Usamos este vector para el ejercicio
colores = ["rojo", "verde", "azul", "amarillo", "morado"]
print("Vector original:", colores)
# Tu código aquí
print("El primer color es: ", colores[0])
print("El ultimo color es: ", colores[-1])
colores[1] = "naranja"
print("Vector modificado: ", colores)

# 1. Muestra el primer color del vector
# 2. Muestra el último color del vector
# 3. Cambia "verde" por "naranja"
# 4. Muestra el vector modificado

# --------------------------
# Ejercicio 3: Operaciones con vectores de números
# --------------------------
print("\n--- Ejercicio 3: Operaciones con vectores de números ---")

edades = [15, 18, 21, 14, 17, 20, 16]
print("Vector de edades:", edades)

# Tu código aquí
suma_edades = 0
edad_mayor = edades[0]
edad_menor = edades[0]
for edad in edades:
    suma_edades += edad
    if edad > edad_mayor:
        edad_mayor = edad
    elif edad < edad_menor:
        edad_menor = edad
promedio_edades = suma_edades/len(edades)
print("La suma de las edades es: ", suma_edades)
print(f"El promedio de las edades es: {promedio_edades:.2f}")
print(f"La edad mayor es {edad_mayor} y la menor es {edad_menor}")

# 1. Calcula y muestra la suma de todas las edades
# 2. Calcula y muestra el promedio de las edades (suma dividida por cantidad)
# 3. Muestra la edad más alta
# 4. Muestra la edad más baja

# --------------------------
# Ejercicio 4: Buscar un elemento en un vector
# --------------------------
print("\n--- Ejercicio 4: Buscar un elemento en un vector ---")

frutas = ["manzana", "banana", "pera", "naranja", "uva", "fresa"]
print("Vector de frutas:", frutas)

# Tu código aquí
buscar = "pera"
bandera = 0
for i in range(len(frutas)):
    if frutas[i] == buscar:
        print(f"Fruta encontrada en la posición {i+1}")
        bandera = 1
if bandera == 0:
    print("Fruta no encontrada")

# 1. Define una variable buscar = "pera"
# 2. Recorre el vector de frutas con un ciclo for
# 3. Si encuentras la fruta buscada, muestra "Fruta encontrada en la posición X"
# 4. Si no la encuentras, muestra "Fruta no encontrada"

# --------------------------
# Ejercicio 5: Contar elementos que cumplan una condición
# --------------------------
print("\n--- Ejercicio 5: Contar elementos que cumplan una condición ---")

calificaciones = [85, 90, 75, 95, 70, 60, 80, 65, 88, 92]
print("Vector de calificaciones:", calificaciones)

# Tu código aquí
mayores_a_80 = 0
menores_que_70 = 0
for calificacion in calificaciones:
    if calificacion >= 80:
        mayores_a_80 += 1
    elif calificacion < 70:
        menores_que_70 += 1
print(f"Hay {mayores_a_80} calificaciones mayores o iguales a 80")
print(f"Mientras que hay {menores_que_70} menores de 70")

# 1. Cuenta cuántas calificaciones son mayores o iguales a 80
# 2. Cuenta cuántas calificaciones son menores a 70
# 3. Muestra ambos resultados


# ===============================================================
# PARTE 2: EJERCICIOS CON FUNCIONES Y VECTORES
# ===============================================================

print("\n=== PARTE 2: EJERCICIOS CON FUNCIONES Y VECTORES ===\n")

# --------------------------
# Ejercicio 6: Función para sumar elementos de un vector
# --------------------------
print("\n--- Ejercicio 6: Función para sumar elementos de un vector ---")

# Tu código aquí
vector = [10,20,30,40,50]
print(vector)
print("La suma del vector es: ", sumar_vector(vector))

# 1. Define una función llamada "sumar_vector" que reciba un vector como parámetro
# 2. La función debe calcular y retornar la suma de todos los elementos
# 3. Prueba la función con el vector [10, 20, 30, 40, 50]
# 4. Muestra el resultado

# --------------------------
# Ejercicio 7: Función para encontrar el mayor y el menor
# --------------------------
print("\n--- Ejercicio 7: Función para encontrar el mayor y el menor ---")

# Tu código aquí
vector = [35, 15, 42, 98, 23, 7, 61]
mayor, menor = encontrar_mayor_menor(vector)
print(vector)
print(f"El número mayor del arreglo es {mayor} y el menor {menor}")

# 1. Define una función llamada "encontrar_mayor_menor" que reciba un vector como parámetro
# 2. La función debe retornar dos valores: el mayor y el menor elemento del vector
# 3. Prueba la función con el vector [35, 15, 42, 98, 23, 7, 61]
# 4. Muestra los resultados

# --------------------------
# Ejercicio 8: Función para filtrar elementos
# --------------------------
print("\n--- Ejercicio 8: Función para filtrar elementos ---")

# Tu código aquí
vector = [12, 5, 8, 15, 3, 7, 10]
print("Vector original: ", vector)
print("Vector filtrado: ", filtrar_mayores(vector, 7))

# 1. Define una función llamada "filtrar_mayores" que reciba un vector y un número como parámetros
# 2. La función debe retornar un nuevo vector que contenga solo los elementos mayores que el número dado
# 3. Prueba la función con el vector [12, 5, 8, 15, 3, 7, 10] y el número 7
# 4. Muestra el vector resultante

# --------------------------
# Ejercicio 9: Función para combinar dos vectores
# --------------------------
print("\n--- Ejercicio 9: Función para combinar dos vectores ---")

# Tu código aquí
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
print("Vetores iniciales:\n", vector1,"\n", vector2)
print("Vectores combinados:\n", combinar_vectores(vector1, vector2))

# 1. Define una función llamada "combinar_vectores" que reciba dos vectores como parámetros
# 2. La función debe retornar un nuevo vector que contenga todos los elementos de ambos vectores
# 3. Prueba la función con los vectores [1, 2, 3] y [4, 5, 6]
# 4. Muestra el vector resultante

# --------------------------
# Ejercicio 10: Función para ordenar un vector
# --------------------------
print("\n--- Ejercicio 10: Función para ordenar un vector ---")

# Tu código aquí
vector = [64, 25, 12, 22, 11]
print("Vector original: ", vector)
print("Vector ordenado: ", ordenar_vector(vector))

# 1. Define una función llamada "ordenar_vector" que reciba un vector como parámetro
# 2. La función debe ordenar el vector de menor a mayor sin usar .sort() (usa un algoritmo simple)
# 3. Prueba la función con el vector [64, 25, 12, 22, 11]
# 4. Muestra el vector ordenado


# ===============================================================
# EJEMPLO DE SOLUCIÓN PARA UN EJERCICIO SIMILAR
# ===============================================================
# Este es un ejemplo para que entiendan la estructura esperada

print("\n--- Ejemplo de solución: ---")

def contar_letras(palabras):
    """
    Función que cuenta cuántas letras tiene cada palabra en un vector.
    Retorna un nuevo vector con los conteos.
    """
    resultado = []
    for palabra in palabras:
        resultado.append(len(palabra))
    return resultado

# Probamos la función
nombres = ["Ana", "Juan", "Carolina", "Miguel"]
conteo = contar_letras(nombres)
print("Nombres:", nombres)
print("Número de letras:", conteo)