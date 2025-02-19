#Luis Gerardo Dávalos Velásquez 240278
print("A continuación se mostraran las tablas de multiplicar del 1, 2 y 3")
for i in range(1,4):
    print(f"Tabla del {i}")
    for j in range(1,11):
        multi = i*j
        print(f"{i}*{j} = {multi}")
    print("-------------")