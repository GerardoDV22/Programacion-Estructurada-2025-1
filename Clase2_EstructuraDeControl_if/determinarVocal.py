#Luis Gerardo Dávalos Velásquez 240278
print("Determinar si la vocal ingresada es una vocal cerrada (tónica)")
vocal = str()

vocal = str(input("Ingrese una vocal: "))
if len(vocal) != 1:
    print("Solo se acepta un unico caracter")
    exit()

if vocal == 'a' or vocal == 'e' or vocal ==  'o':
    print("Es una vocal abierta")
elif vocal == 'i' or vocal == 'u':
    print("Es una vocal cerrada")
else:
    print("El caracter ingresado no es una vocal")