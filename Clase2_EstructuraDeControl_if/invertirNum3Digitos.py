#Luis Gerardo Dávalos Velásquez 240278
print("Invertir un número entero de 3 digitos")
num = 0
num = int(input("Ingresa el número: "))

if num > 999 or num < 100:
    print("No es un número de 3 digitos")
else:
    c = num//100
    aux = num%100
    d = aux//10
    d = d*10
    u = aux%10
    u = u*100
    numI = c+d+u
    print(f"El número {num} invertido es {numI}")