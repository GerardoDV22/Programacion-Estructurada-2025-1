#Luis Gerardo Dávalos Velásquez 240278
print("Calculadora de indice de masa corporal(IMC)")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros(Ej: 0.00): "))

imc = peso/(altura**2)

print(f"Tu IMC es {imc:.2f}")