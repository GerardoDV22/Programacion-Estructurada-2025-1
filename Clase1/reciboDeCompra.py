#Luis Gerardo Dávalos Velásquez 240278
print("Imprimir recibo de compra de 3 articulos")
a1 = float(input("Ingrese el precio del primer articulo: "))
a2 = float(input("Ingrese el precio del segundo articulo: "))
a3 = float(input("Ingrese el precio del tercer articulo: "))

subt = a1+a2+a3
iva = subt*.16
total = subt + iva

print(f"Resumen de compra:\n\tArticulo 1:\t{a1} pesos\n\tArticulo 2:\t{a2} pesos\n\tArticulo 3:\t{a3} pesos")
print(f"Subtotal: {subt} pesos\nIVA (16%): {iva} pesos\nTotal: {total} pesos")