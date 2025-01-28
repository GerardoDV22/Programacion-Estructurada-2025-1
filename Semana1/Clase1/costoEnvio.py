#Luis Gerardo Dávalos Velásquez 240278
print("Calcular coste de envio de Payasos y Muñecas")
p = float(input("Ingrese el número de payasos a enviar: "))
m = float(input("Ingrese el número de muñecas a enviar: "))

pp = p*112
mp = m*75
pesoT = pp+mp
costo = 120*(pesoT/600)

print(f"Resumen de envio:\n\tPayasos. Cantidad: {p}. Peso en conjunto: {pp} gramos")
print(f"\n\tMuñecas. Cantidad: {m}. Peso en conjunto: {mp} gramos")
print(f"Peso total: {pesoT} gramos.\nCosto total del envío: {costo}")