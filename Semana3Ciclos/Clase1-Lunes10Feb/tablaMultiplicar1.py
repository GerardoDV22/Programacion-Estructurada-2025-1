#Luis Gerardo Dávalos Velásquez 240278
print("Mostrar en pantalla la tabla de multiplicar del 1 al 10 del número solicitado")
n = int(input("Ingrese el número cuya tabla desea ver: "))
for i in range(1,11):
    multi = n*i
    print(f"{n}*{i} = {multi}")