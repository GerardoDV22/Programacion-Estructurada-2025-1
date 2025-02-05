#Luis Gerardo Dávalos Velásquez 240278
print("Juego de preguntas. Responde si o no.")

a = int(input("¿Colon descubrio América?\n1. Si\n2. No\n"))
if a == 2:
    print("Respuesta equivocada. Fin del juego")
elif a == 1:
    a = int(input("¿La independecia de México comenzo en el año 1810?\n1. Si\n2. No\n"))
    if a == 2:
        print("Respuesta incorrecta. Fin del juego")
    elif a == 1:
        a = int(input("¿The Doors fue un grupo de rock Americano?\n1. Si\n2. No\n"))
        if a == 2:
            print("Respuesta incorrecta, perdiste")
        elif a == 1:
            print("Ganaste el Juego. Felicidades!!!")