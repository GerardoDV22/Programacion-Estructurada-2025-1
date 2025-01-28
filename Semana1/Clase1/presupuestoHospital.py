#Luis Gerardo Dávalos Velásquez 240278
print("Presupuesto anual del Hopital para sus tres áreas")

presupuesto = float(input("Ingrese el presupuesto total: "))

preGine = presupuesto*.4
preTrau = presupuesto*.3
prePedi = preTrau

print(f"Al ser el presupuesto total de {presupuesto} pesos")
print("se reparte a las áreas de la siguiente manera:")
print(f"\tGinecología(40%): {preGine:.2f}\n\tTraumatología(30%): {preTrau:.2f}\n\tPediatría(30%): {prePedi:.2f}")