#Luis Gerardo Dávalos Velásquez 240278
print("Determinar el número con el valor central (ni mayor ni menor) de 3 números")
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))
except ValueError:
    print("Los datos capturados deben ser numeros enteros")
    exit()

if (num1>num2 and num1<num3) or (num1<num2 and num1>num3):
    print("El primer número ingresado es el que esta en medio")
elif (num2>num1 and num2<num3) or (num2<num1 and num2>num3):
    print("El segundo número ingresado es el que esta en medio")
elif (num3>num1 and num3<num2) or (num3<num1 and num3>num2):
    print("El tercer número ingresado es el que esta en medio")
else:
    print("Al haber ingresado números repetidos no exite número central")