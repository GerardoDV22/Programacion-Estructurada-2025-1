#Luis Gerardo Dávalos Velásquez 240278
num = int(input("Ingrese un número de tres digitos: "))
c = num//100
du = num%100
d = du//10
u = du%10
print(f"{u} - {d} - {c}")
u = u*100
d = d*10
num = u+d+c
print(num)