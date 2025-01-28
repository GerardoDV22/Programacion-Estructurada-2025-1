#Luis Gerardo Dávalos Velásquez, 240278
print("Bienvenido a la Casa de Cambio")
print("Cambiamos pesos(mxn) a dolares")

peso = float(input("¿Cuantos dolares desea comprar? "))

TC = 20.77
dolares = peso/TC

print(f"Tus {peso} pesos, son equivalentes a {dolares:.2f}") #El ".2f" permite delimitar la cantidad de decimales a mostrar