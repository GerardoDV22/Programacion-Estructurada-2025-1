#Luis Gerardo Dávalos Velásquez 240278
#Inicializar una variable para almacenar el número mayor
mayor = 0 #Se inicializa un valor muy pequeño como referencia inicial
#pedir 5 números al usuario
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    #Comprobar y actualizar el mayor si el número ingresado es mayor
    if i == 0:
        mayor = num
    elif num>mayor:
        mayor = num
#Imprimir el número mayor
print(f"El número mayor es: {mayor}")