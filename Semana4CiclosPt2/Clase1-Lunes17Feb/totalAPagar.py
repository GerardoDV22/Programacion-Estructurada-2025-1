#Luis Gerardo Dávalos Velásquez 240278
print("Calcular el total a pagar de las compras de un cliente")
subtotal = 0
while True:
    try:
        monto = float(input("Ingresa el monto de la compra (o un 0 para salir): "))
        if monto > 0:
            subtotal += monto
        elif monto < 0:
            print("No se aceptan numeros negativos")
        else:
            print("Calculando total")
            break
    except ValueError:
        print("Solo se permiten numeros")

print("-------------")
if subtotal >= 1000:
    total = subtotal*.9
    print("El monto supera los 1000 pesos, se aplica un descuento de 10%")
else:
    total = subtotal
print(f"El monto total a pagar es de {total} pesos")