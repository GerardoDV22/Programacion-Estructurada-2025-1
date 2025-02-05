#Luis Gerardo Dávalos Velásquez 240278
print("Determinar si dos números tienen signos opuestos")
n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa otro número: "))

if n1 == 0 or n2 == 0:
    print("Por lo menos uno de los números es 0")
elif (n1 > 0 and n2 < 0) or (n2 > 0 and n1 < 0):
    print("Los números tienen signos opuestos")
else:
    print("Los números son del mismo signo")