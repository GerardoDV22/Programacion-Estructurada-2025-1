#Luis Gerardo Dávalos Velásquez 240278
dineroAuto = 0
dineroMoto = 0
dineroCamioneta = 0
tAuto = 0
tMoto = 0
tCamioneta = 0
cVehiculos = 0
hrsAuto = 0
hrsMoto = 0
hrsCamioneta = 0
hrsMayor = 0
vehiculoMayor = 0
print("Control de Estacionamiento")
while True:
    try:
        tipo = int(input("Tipo de vehiculo que ingresa:\n1. Automovil\n2. Moto\n3. Camioneta\n0. Terminar día\nSeleccione número: "))
        if tipo > 0 and tipo < 4:
            hrs = float(input("Ingrese las horas de estancia: "))
            if hrs < 1:
                print("Las horas de estancia deben ser mayores a 1")
                tipo = -99
            elif hrs > hrsMayor:
                hrsMayor = hrs
                vehiculoMayor = tipo
    except ValueError:
        print("Solo se aceptan numeros")
    

    if tipo == 1:
        tAuto += 1
        hrsAuto += hrs
        aux = 20*hrs
        dineroAuto += aux
    elif tipo == 2:
        tMoto += 1
        hrsMoto += hrs
        aux = 10*hrs
        dineroMoto += aux
    elif tipo == 3:
        tCamioneta += 1
        hrsCamioneta += hrs
        aux = 25*hrs
        dineroCamioneta += aux
    elif tipo == 0:
        print("Terminando día.")
        break
    else:
        print("Opción invalida")
    print("-----------------------------")

promHrsAuto = hrsAuto/tAuto
promHrsMoto = hrsMoto/tMoto
promHrsCamioneta = hrsCamioneta/tCamioneta
print("-----------------------------")
print("Resumen del día.\nTotal Recaudado por tipo de vehiculo:")
print(f"Autos: ${dineroAuto}\nMotos: ${dineroMoto}\nCamionetas: {dineroCamioneta}")
print(f"Vehiculos atendidos: {tAuto+tMoto+tCamioneta}\n---------------------\nHoras de estancia promedio:")
print(f"Autos: {promHrsAuto} horas\nMotos: {promHrsMoto} horas\nCamionetas: {promHrsCamioneta} horas")
if vehiculoMayor == 1:
    print(f"El vehiculo que más tiempo tuvo de estancia fue un auto con {hrsMayor} horas")
elif vehiculoMayor == 2:
    print(f"El vehiculo que más tiempo tuvo de estancia fue una moto con {hrsMayor} horas")
elif vehiculoMayor == 3:
    print(f"El vehiculos que más tiempo tuvo de estancia fue una camioneta con {hrsMayor} horas")