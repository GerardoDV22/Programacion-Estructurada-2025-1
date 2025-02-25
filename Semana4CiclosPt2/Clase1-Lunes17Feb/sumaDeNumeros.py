#Luis Gerardo Dávalos Velásquez 240278
print("Suma de todos los números positivos hasta que se ingrese uno negativo")
suma = 0
while True:
    try:
        num = float(input("Dame un número positivo para sumar (O uno negativo para salir): "))
        if num > 0:
            suma += num
        elif num < 0:
            break
    except ValueError:
        print("Solo se admiten números")

print(f"La suma de los números ingresados es: {suma}")