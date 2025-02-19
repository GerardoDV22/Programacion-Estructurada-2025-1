#Luis Gerardo Dávalos Velásquez 240278
print("Contador de números pares, impares y ceros")
pares = 0
impares = 0
ceros = 0
for i in range(10):
    num = float(input(f"Ingrese el número {i+1}: "))
    if num == 0:
        ceros += 1
    elif num%2 == 0:
        pares += 1
    else:
        impares += 1
print(f"Se ingresaron:\n{pares} números pares\n{impares} números impares\n{ceros} ceros")