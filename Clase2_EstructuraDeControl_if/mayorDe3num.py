#Luis Gerardo Dávalos Velásquez 240278
print("Comparar 3 números y determinar el mayor")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 > num2 and num1 > num3:
    max = num1
elif num2 > num3:
    max = num2
else:
    max = num3

print(f"El número mayor es: {max}")