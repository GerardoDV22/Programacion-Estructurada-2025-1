# ARREGLOS EN PYTHON: INTRODUCCIÓN BÁSICA

# 1. Crear un arreglo (lista)
print("\n--- CREAR ARREGLOS ---")
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "fresa"]

print("Arreglo de números: ", numeros)
print("Arreglo de frutas: ", frutas)

# 2. Acceder a elementos
print("\n--- ACCEDER A ELEMENTOS ---")
print("Primer número:", numeros[0])     # Los índices empiezan en 0
print("Segunda fruta:", frutas[1])
print("Último número:", numeros[4])     # También se puede usar numeros[-1]

# 3. Modificar elementos
print("\n--- MODIFICAR ELEMENTOS ---")
print("Arreglo original:", numeros)
numeros[0] = 10                        # Cambiar el primer elemento
print("Después de cambiar:", numeros)

# 4. Añadir elementos
print("\n--- AÑADIR ELEMENTOS ---")
frutas.append("naranja")               # Añadir al final
print("Después de añadir:", frutas)

numeros.insert(0, 7)                    # Añadir en una posición específica
print("Después de insertar:", numeros)

# 5. Longitud del arreglo
print("\n--- LONGITUD DEL ARREGLO ---")
print("Cantidad de números:", len(numeros))
print("Cantidad de frutas:", len(frutas))

# 6. Recorrer un arreglo
print("\n--- RECORRER UN ARREGLO ---")
print("Todos los números:")
for numero in numeros:
    print(numero)

# Recorrer un arreglo inversamente
print("\nTodos los números (inverso):")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])

print("\nTodas las frutas:")
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}")

# 7. Ejemplo simple: encontrar el número mayor
print("\n--- ENCONTRAR EL NÚMERO MAYOR ---")
numeros_mezclados = [15, 8, 23, 6, 42, 12]
print("Arreglo:", numeros_mezclados)

mayor = numeros_mezclados[0]
for numero in numeros_mezclados:
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)