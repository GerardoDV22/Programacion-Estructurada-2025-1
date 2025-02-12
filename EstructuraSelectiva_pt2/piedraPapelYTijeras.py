#Luis Gerardo Dávalos Velásquez 240278
from random import *
cpu = randint(1,3)
print("Juguemos piedra, papel y tijeras")
print("1. Piedra\n2. Papel\n3. Tijeras")
try:
    player = int(input("Escoga su jugada (1, 2 o 3): "))
except ValueError:
    print("Solo se aceptan números")
    exit()
if player > 3 or player < 1:
    print("Opción invalida")
    exit()

if cpu == 1:
    print("Computadora juega: Piedra")
elif cpu == 2:
    print("Computadora juega: Papel")
else:
    print("Computadora juega: Tijeras")

if player == cpu:
    print("Empate")
elif (player==1 and cpu==3) or (player==2 and cpu == 1) or (player==3 and cpu == 2):
    print("Ganaste, eres bueno")
else:
    print("Perdiste, mejor suerte la proxima")