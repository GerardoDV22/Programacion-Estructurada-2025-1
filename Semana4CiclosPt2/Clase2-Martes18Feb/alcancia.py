#Luis Gerardo Dávalos Velásquez 240278
print("Bienvenido al sistema de alcancia digital")
saldo = 0
tdep = 0
tret = 0
mayor = 0
opMayor = 0
ope = int(0)
try:
    opc = int(input("Que desea hacer:\n1. Depositar\n2. Retirar\n3. Salir\nOpcion: "))
except ValueError:
    print("Solo se permiten numeros enteros")
    opc = int(4)
while opc != 3:
    if opc == 1:
        aux = float(input("Ingrese la cantidad que desea ingresar: "))
        saldo += aux
        tdep += aux
        print("Deposito realizado con exito")
        ope += 1
        if aux > mayor:
            mayor = aux
            opMayor = 1
    elif opc == 2:
        aux = float(input("Ingrese la cantidad que quiere retirar: "))
        if saldo >= aux:
            saldo -= aux
            tret += aux
            print("El reitro se realizo con exito")
            if aux > mayor:
                mayor = aux
                opMayor = 2
        else:
            print("No cuenta con fondos suficientes")
        ope += 1
    elif opc == 3:
        print("Saliendo del sistema, preparando resumen")
    else:
        print("Opcion no valida")
    print("-------------------------------")
    print(f"Saldo actual: {saldo}")
    try:
        opc = int(input("Que desea hacer:\n1. Depositar\n2. Retirar\n3. Salir\nOpcion: "))
    except ValueError:
        print("Solo se permiten numeros enteros")
        opc = int(4)

print(f"Resumen:\nSaldo final: {saldo}\nOperaciones realizadas: {ope}")
print(f"Monto total de depositos: {tdep}\nMonto total de retiros: {tret}")
if opMayor == 0:
    print("No se realizaron operaciones")
elif opMayor == 1:
    print(f"La operación más alta fue un deposito por el siguiente monto: {mayor}")
elif opMayor == 2:
    print(f"La operación más alta fue un retiro por el siguiente monto: {mayor}")