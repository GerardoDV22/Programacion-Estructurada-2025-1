#Luis Gerardo Dávalos Velásquez 240278
contador = 0 #Contará cuantos números positivos hay
acumulador = 0 #Acumulará la suma de los números positivos
#Pedir 5 números al usuario
for i in range(5):
    num = float(input(f"Ingrese el número {i+1}: "))
    #Si el número es positivo, lo sumamos y contamos
    if num>0:
        acumulador += num #Suma el número positivo
        contador += 1 #Incrementa el contador
#Calcular el promedio si hubo números positivos
if contador>0:
    promedio = acumulador/contador
    print(f"El promedio de los números positivos es: {promedio:.2f}")