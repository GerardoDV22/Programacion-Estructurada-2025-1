#Luis Gerardo Dávalos Velásquez 240278
# ===============================================================
# PRÁCTICA DE VECTORES Y MATRICES EN PYTHON
# ===============================================================

"""
INSTRUCCIONES:

1. Lee atentamente cada ejercicio antes de empezar a resolverlo.
2. Escribe tu código en los espacios indicados con "Tu código aquí".
3. Guarda este archivo como "practica_vectores2_tunombre.py".
4. Ejecuta tu código para comprobar que funciona correctamente.
5. Asegúrate de que cada ejercicio produce el resultado esperado.

¡Buena suerte!
"""

# ===============================================================
# PARTE 1: MANIPULACIÓN BÁSICA DE VECTORES
# ===============================================================

print("\n=== PARTE 1: MANIPULACIÓN BÁSICA DE VECTORES ===\n")

# --------------------------
# Ejercicio 1: Crear y modificar un vector
# --------------------------
print("\n--- Ejercicio 1: Crear y modificar un vector ---")

# Tu código aquí
ciudades = ["Mexicali","Tijuana","Tecate","Ensenada","Rosarito"]
print(ciudades)
ciudades.append("Calexico")
print(ciudades)

# 1. Crea un vector llamado "ciudades" con 5 nombres de ciudades
# 2. Muestra el vector completo
# 3. Agrega una ciudad más al final del vector usando append()
# 4. Muestra el vector actualizado

# --------------------------
# Ejercicio 2: Recorrer un vector
# --------------------------
print("\n--- Ejercicio 2: Recorrer un vector ---")

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Vector de números:", numeros)

# Tu código aquí
print("\nNumeros en lista:")
for numero in numeros:
    print(numero)
print("\nNumeros en posiciones pares:")
for i in range(0,len(numeros),2):
        print(numeros[i])
print("\nNumeros a la inversa:")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])

# 1. Recorre el vector usando un ciclo for y muestra cada número
# 2. Muestra solo los números en posiciones pares (0, 2, 4...)
# 3. Muestra los números en orden inverso


# --------------------------
# Ejercicio 3: Operaciones con vectores de temperaturas
# --------------------------
print("\n--- Ejercicio 3: Operaciones con vectores de temperaturas ---")

temperaturas = [22.5, 19.8, 25.1, 28.0, 27.5, 30.2, 18.5]
print("Temperaturas de la semana:", temperaturas)

# Tu código aquí
temperatura_max = temperaturas[0]
temperatura_min = temperaturas[0]
suma_temperaturas = 0
dias_mayores_a_25 = 0
for temperatura in temperaturas:
    suma_temperaturas += temperatura
    if temperatura > temperatura_max:
        temperatura_max = temperatura
    elif temperatura < temperatura_min:
        temperatura_min = temperatura
    if temperatura > 25:
         dias_mayores_a_25 += 1
promedio_temperaturas = suma_temperaturas/len(temperaturas)
print(f"La temperatura máxima fue de {temperatura_max} grados")
print(f"La temperatura mínima fue de {temperatura_min} grados")
print(f"El promedio de las temperaturas es: {promedio_temperaturas:.2f}")
print(f"{dias_mayores_a_25} días tuvieron temperaturas mayores a 25 grados")

# 1. Calcula y muestra la temperatura máxima
# 2. Calcula y muestra la temperatura mínima
# 3. Calcula y muestra el promedio de temperaturas
# 4. Cuenta cuántos días tuvieron temperaturas superiores a 25 grados

# --------------------------
# Ejercicio 4: Eliminar elementos de un vector
# --------------------------
print("\n--- Ejercicio 4: Eliminar elementos de un vector ---")

materias = ["Matemáticas", "Español", "Historia", "Ciencias", "Arte", "Educación Física"]
print("Lista de materias:", materias)

# Tu código aquí
del materias[0]
print("Tras eliminar la primera materias: ", materias)
materias.remove("Historia")
print("Tras eliminar \"Historia\" de las materias: ", materias)
materias.pop()
print("Lista de materias final: ", materias)

# 1. Elimina la primera materia del vector
# 2. Elimina "Historia" del vector (usando remove)
# 3. Elimina la última materia del vector
# 4. Muestra el vector final

# --------------------------
# Ejercicio 5: Filtrar elementos de un vector
# --------------------------
print("\n--- Ejercicio 5: Filtrar elementos de un vector ---")

estaturas = [1.65, 1.80, 1.58, 1.75, 1.90, 1.72, 1.68]
print("Estaturas (en metros):", estaturas)

# Tu código aquí
altos = []
medios = []
for estatura in estaturas:
    if estatura >= 1.70:
         altos.append(estatura)
    if estatura >= 1.65 and estatura <=1.75:
         medios.append(estatura)
print("Estaturas altas (mayores a 1.70): ", altos)
print("Estaturas medias (entre 1.65 y 1.75): ", medios)

# 1. Crea un nuevo vector llamado "altos" que contenga solo las estaturas mayores a 1.70m
# 2. Crea un nuevo vector llamado "medios" que contenga solo las estaturas entre 1.65m y 1.75m
# 3. Muestra ambos vectores resultantes