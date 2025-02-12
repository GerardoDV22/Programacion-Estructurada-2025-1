#Luis Gerardo Dávalos Velásquez 240278
print("Se calculara el mayor de 5 números ingresados")
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    num3 = float(input("Ingrese el tercer número: "))
    num4 = float(input("Ingrese el cuarto número: "))
    num5 = float(input("Ingrese el quinto número: "))
except ValueError:
    print("Solo se aceptan números")

if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print(f"El primer número \"{num1}\" es el más grande")
elif num2>num3 and num2>num4 and num2>num5:
    print(f"El segundo número \"{num2}\" es el más grande")
elif num3>num4 and num3>num5:
    print(f"El tercer número \"{num3}\" es el más grande")
elif num4>num5:
    print(f"El cuarto número \"{num4}\" es el más grande")
else:
    print(f"El quinto número \"{num5}\" es el más grande")