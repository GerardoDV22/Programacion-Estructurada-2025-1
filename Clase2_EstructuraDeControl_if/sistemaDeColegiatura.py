#Luis Gerardo Dávalos Velásquez 240278
print("Ponduka State University. Sistema de colegiaturas")

ctgr = str(input("Ingrese su categoria (vet/reg): "))
if ctgr != "vet" and ctgr != "reg":
    print("No ingreso una categoria")
    exit()

try:
    mat = int(input("Ingrese el número de asignaturas que va a pagar: "))
except ValueError:
    print("No ingreso un número valido")
    exit()
if mat <=0:
    print("Las materias no puden ser menores de 1")
    exit()

if ctgr == "vet":
    print(f"Resumen\nEstudiante veterano solicita {mat} asignaturas")
    total = mat * 30
    print(f"Coste: 30 dolares por asignatura\nTotal a pagar: {total}")
else:
    print(f"Resumen\nEstudiante regular solicita {mat} asignaturas")
    total = mat * 50
    print(f"Coste: 50 dolares por asignatura\nTotal a pagar: {total} dolares")