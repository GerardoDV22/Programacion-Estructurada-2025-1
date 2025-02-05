#Luis Gerardo Dávalos Velásquez 240278
print("Identificar su grupo etario dada su edad")
edad = int(input("Ingresaa tu edad: "))

if edad >= 60:
    print("Usted se encuentra en la etapa de la ANCIANIDAD")
elif edad >= 25:
    print("Usted se encuentra en la etapa de la ADULTEZ")
elif edad >= 20:
    print("Usted se encuentra en la etapa de la JUVENTUD")
elif edad >= 12:
    print("Usted se encuentra en la etapa de la ADOLESCENCIA")
elif edad >= 6:
    print("Usted se encuentra en la etapa de la NIÑEZ")
else:
    print("Usted se encuentra en la etapa de la INFANCIA")