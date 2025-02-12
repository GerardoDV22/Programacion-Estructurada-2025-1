#Luis Gerardo Dávalos Velásquez 240278
print("Determinar si un número entero es multiplo de otro")
try:
    n1 = int(input("Ingrese el primer número: "))
    n2 = int(input("Ingrese el segundo número: "))
except ValueError:
    print("Los valores deben ser números enteros")
    exit()

if n2%n1 == 0:
    print(f"{n1} es multiplo de {n2}")
elif n1%n2 == 0:
    print(f"{n2} es multiplo de {n1}")
else:
    print("Ninguno de los números es multiplo del otro")