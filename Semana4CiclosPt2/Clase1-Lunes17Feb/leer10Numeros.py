#Luis Gerardo Dávalos Velásquez 240278
print("Se leeran 10 números y se contaran positivos, negativos y ceros")
pos = 0
neg = 0
ceros = 0
i = 10
while i > 0:
    try:
        num = float(input("Dame un número: "))
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            ceros += 1
        i -= 1
    except:
        print("Solo se aceptan numeros")

print("---------------------")
print(f"Ingresaste:\n{pos} numeros positivos\n{neg} numeros negativos\n{ceros} ceros")