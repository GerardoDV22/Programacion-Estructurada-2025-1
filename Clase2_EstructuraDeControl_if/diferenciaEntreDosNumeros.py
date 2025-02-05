#Luis Gerardo Dávalos Velásquez 240278
print("Calcular la diferencia entre dos enteros positivos")
try:
    n1 = int(input("Ingresa un número positivo: "))
    n2 = int(input("Ingresa otro número positivo: "))
except n1 < 0 or n2 < 0:
    print("Los números deben ser positivos")
    exit()

if n1 > n2:
    dif = n1 - n2
else:
    dif = n2 - n1

print(f"La diferencia entre los numeros es de: {dif}")