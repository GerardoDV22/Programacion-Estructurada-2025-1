#Luis Gerardo Dávalos Velásquez 240278
print("Calculadora para convertir kilometros a:\n\tMetros\n\tCentimetros\n\tMilimetros")
kilo = float(input("Ingrese la cantidad de kilometros: "))

mtrs = kilo*1000
cm = mtrs*100
mlm = cm*10

print(f"{kilo} kilometros son equivalentes a:\n\t{mtrs} metros\n\t{cm} centimetros\n\t{mlm} milimetros")