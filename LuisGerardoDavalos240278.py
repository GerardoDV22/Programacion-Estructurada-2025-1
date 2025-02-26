#Luis Gerardo Dávalos Velásquez 240278
#Sistema de votación escolar
votosHugo = 0
votosPaco = 0
votosLuis = 0
estudiantes = 15
n = 1
while estudiantes > 0:
    while True:
        print("--------------------------------")
        print("Bienvenidos a las elecciones de jefe de grupo\nLos candidatos son:")
        print("1. Hugo\n2. Paco\n3. Luis")
        print(f"Estudiante número {n}")
        try:
            voto = int(input("¿Por quien votas? Escoge un número: "))
            if voto == 1:
                votosHugo += 1
                estudiantes -= 1
                n += 1
                break
            elif voto == 2:
                votosPaco += 1
                estudiantes -= 1
                n += 1
                break
            elif voto == 3:
                votosLuis += 1
                estudiantes -= 1
                n += 1
                break
            else:
                print("Opción invalida, intenta de nuevo")
        except ValueError:
            print("Solo se permite ingresar numeros")

    if estudiantes == 0:
        if votosHugo == votosPaco or votosHugo == votosLuis or votosLuis == votosPaco:
            print("--------------------------------")
            print(f"Votos:\nHugo: {votosHugo}\nPaco: {votosPaco}\nLuis: {votosLuis}")
            print("Ocurrio un empate por alguno de los puestos, las votaciones deben repetirse.")
            estudiantes = 15
            votosHugo = 0
            votosPaco = 0
            votosLuis = 0
            n = 1

print("--------------------------------")
print("Resultados de la votaciones")
porcentajeHugo = (votosHugo/15)*100
porcentajePaco = (votosPaco/15)*100
porcentajeLuis = (votosLuis/15)*100
if votosHugo > votosPaco and votosHugo > votosLuis:
    print(f"El jefe de grupo es Hugo con {votosHugo} votos, es decir un {porcentajeHugo:.2f}% de los votos.")
    if votosPaco > votosLuis:
        print(f"El tesorero es Paco con {votosPaco} votos, es decir un {porcentajePaco:.2f}% de los votos.")
        print(f"Luis recibio {votosLuis} votos, un {porcentajeLuis}% de los votos. Gracias por participar.")
    else:
        print(f"El tesorero es Luis con {votosLuis} votos, es decir un {porcentajeLuis:.2f}% de los votos.")
        print(f"Paco recibio {votosPaco} votos, un {porcentajePaco:.2f}% de los votos. Gracias por participar.")
elif votosPaco > votosLuis:
    print(f"El jefe de grupo es Paco con {votosPaco} votos, es decir un {porcentajePaco:.2f}% de los votos.")
    if votosHugo > votosLuis:
        print(f"El tesorero es Hugo con {votosHugo} votos, es decir un {porcentajeHugo:.2f}% de los votos.")
        print(f"Luis recibio {votosLuis} votos, un {porcentajeLuis}% de los votos. Gracias por participar.")
    else:
        print(f"El tesorero es Luis con {votosLuis} votos, es decir un {porcentajeLuis:.2f}% de los votos.")
        print(f"Hugo recibio {votosHugo} votos, un {porcentajeHugo:.2f}% de los votos. Gracias por participar.")
else:
    print(f"El jefe de grupo es Luis con {votosLuis} votos, es decir un {porcentajeLuis:.2f}% de los votos.")
    if votosHugo > votosPaco:
        print(f"El tesorero es Hugo con {votosHugo} votos, es decir un {porcentajeHugo:.2f}% de los votos.")
        print(f"Paco recibio {votosPaco} votos, un {porcentajePaco:.2f}% de los votos. Gracias por participar.")
    else:
        print(f"El tesorero es Paco con {votosPaco} votos, es decir un {porcentajePaco:.2f}% de los votos.")
        print(f"Hugo recibio {votosHugo} votos, un {porcentajeHugo:.2f}% de los votos. Gracias por participar.")