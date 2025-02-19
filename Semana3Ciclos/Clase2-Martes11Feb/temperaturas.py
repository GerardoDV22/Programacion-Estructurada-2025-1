#Luis Gerardo Dávalos Velásquez 240278
semana = ["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]
print("Registrar temperaturas de una semana y determinar mayor, menor y promedio")
mayor = 0
menor = 0
acumulador = 0
for i in range(7):
    temp = float(input(f"Ingrese la temperatura del día {semana[i]}: "))
    acumulador += temp
    if i==0:
        mayor = temp
        menor = temp
        diaM = 0
        diam = 0
    elif temp>mayor:
        mayor = temp
        diaM = i
    elif temp<menor:
        menor = temp
        diam = i
promedio = acumulador/7
print(f"Resumen de las semana:\nLa temperatura promedio fue de {promedio:.2f} grados")
print(f"El día con mayor temperaatura fue el {semana[diaM]} con {mayor} grados")
print(f"El día con menor temperatura fue el {semana[diam]} con {menor} grados")