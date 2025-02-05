#Luis Gerardo Dávalos Velásquez 240278
print("Se determinara el tipo de triangulo en base a el valor de sus lados")

l1 = float(input("Ingrese el primer lado: "))
if l1 <= 0:
    print("El valor debe ser mayor que cero")
    exit()
else:
    l2 = float(input("Ingrese el segundo lado: "))
    if l2 <= 0:
        print("El valor debe ser mayor que cero")
        exit()
    else:
        l3 = float(input("Ingrese el tercer lado: "))
        if l3 <= 0:
            print("El valor debe ser mayor que cero")
            exit()

if l1 == l2 and l1 == l3:
    print("Es un triangulo equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("Es un triangulo isosceles")
else:
    print("Es un triangulo escaleno")