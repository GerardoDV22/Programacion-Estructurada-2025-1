#Luis Gerardo Dávalos Velásquez 240278
#Ejemplo de ciclo wjile, contar de 1 a 5
""" contador = 1

while contador < 6:
    print(f"Contador: {contador}")
    contador += 1

print("¡Fin del ciclo!") """

#Ejemplo de ciclo while con entrada del usuario, pedira y sumara los numeros 
total = 0

while True:
    try:
        numero = input("Ingresa un número (o escribe \"fin\" para terminar): ")
        if numero.lower() == "fin":
            break
        numero = int(numero)
        total += numero
    except ValueError:
        print("Error: Ingrese un número valido o escribe \"fin\" para terminar")

print(f"La suma total es: {total}")