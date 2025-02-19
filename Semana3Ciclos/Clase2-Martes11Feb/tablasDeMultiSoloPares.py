#Luis Gerardo Dávalos Velásquez 240278
print("A continuación se mostraran solo los números pares de las tablas de multiplicar del 1, 2 y 3")
for i in range(1,4):
    print(f"Tabla del {i}")
    for j in range(2,11,2):
        multi = i*j
        print(f"{i}*{j} = {multi}")
    print("-------------")