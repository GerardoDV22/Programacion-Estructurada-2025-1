#Luis Gerardo Dávalos Velásquez 240278
print("Calcular su sueldo en base al coste por hora")

hrs = int(input("Ingrese las horas trabajadas: "))
pxh = int(input("Ingrese el cobro que realiza por hora: "))

sueldo = hrs * pxh

print(f"Tras trabajar un total de {hrs} a un precio de {pxh} pesos")
print(f"El sueldo que le corresponde es de {sueldo} pesos")