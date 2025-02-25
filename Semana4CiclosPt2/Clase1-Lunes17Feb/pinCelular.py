#Luis Gerardo Dávalos Velásquez 240278
pinSecreto = 1234
print("Pantalla de bloqueo de celular")
intentos = 3
while True:
    try:
        pin = int(input("Ingresa tu pin: "))
        if pin == pinSecreto:
            print("Login correcto. Bienvenido de nuevo")
            exit()
        else:
            print("Pin incorrecto")
            intentos -= 1
            if intentos == 0:
                print("Ubicación encendida. Llamando a la policia...")
                exit()
    except ValueError:
        print("Solo se permiten números")