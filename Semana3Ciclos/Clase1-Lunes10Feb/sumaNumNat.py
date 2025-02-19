#Luis Gerardo Dávalos Velásquez 240278
suma = 0
print("Suma de números naturales hasta \"n\"")
n = int(input("Ingrese el número entero positivo hasta donde llegara la suma: "))
for i in range(n):
    suma = i + suma + 1
print(f"La suma de 1 hasta {n} es igual a {suma}")