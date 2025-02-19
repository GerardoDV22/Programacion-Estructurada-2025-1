#Luis Gerardo Dávalos Velásquez 240278
print("Calcular el factorial e un número entero positivo")
n = int(input("Ingrese un número: "))
facto = 1
for i in range(2,n+1):
    facto *= i
print(f"El factorial de {n} es igual a {facto}")