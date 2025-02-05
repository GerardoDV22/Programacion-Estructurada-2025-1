#Luis Gerardo Dávalos Velásquez 240278
print("Fruteria. Manzanas con descuento por gramaje")
precio = float()

precio = float(input("Ingrese el precio por kilogramo de manzana: "))
if precio <= 0:
    print("El precio por kilo debe ser mayor a 0")
    exit()

kilo = float(input("Ingrese el gramaje de manzanas que comprara el cliente: "))
descuento = 0
if kilo > 0:
    subtotal = (precio*kilo)
    if kilo >= 10.01:
        descuento = .2
        total = subtotal-(subtotal*descuento)
    elif kilo >= 5.01:
        descuento = .15
        total = subtotal-(subtotal*descuento)
    elif kilo >= 2.01:
        descuento = .1
        total = subtotal-(subtotal*descuento)
    else:
        total = subtotal
else:
    print("Los kilogramos de manzanas deben ser mayores a 0")
    exit()

descuento = descuento*100
print(f"Su compra de {kilo} kilogramos de manzanas da un subtotal de: {subtotal}")
print(f"Con el descuento aplicado del {descuento:.0f}% pasa a ser un total de: {total}")