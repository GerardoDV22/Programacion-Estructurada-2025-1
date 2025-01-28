#Luis Gerardo Dávalos Velásquez 240278
num = int(input("Ingrese un número de dos digitos: "))
u = num%10
d = num//10
print(f"{u} y {d}")
u = u*10
num = u+d
print(num)