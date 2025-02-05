#Luis Gerardo Dávalos Velásquez 240278
operacion = str()
print("Calculaora de operaciónes básicas")
print("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir")
try:
    opc = int(input("¿Que operación desea realizar? (1, 2, 3 o 4): "))
except ValueError:
    print("Solo se admiten números enteros")
    exit()

try:
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
except ValueError:
    print("Solo se admiten números")
    exit()

if opc == 1:
    r = a+b
    operacion = "suma"
elif opc == 2:
    r = a-b
    operacion = "resta"
elif opc == 3:
    r = a*b
    operacion = "multiplicación"
elif opc == 4:
    r = a/b
    operacion == "división"
else:
    print("Opción invalida")
    exit()

print(f"Su operación de {operacion} de {a} y {b} da como resultado: {r:.2f}")