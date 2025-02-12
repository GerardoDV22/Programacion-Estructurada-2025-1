#Luis Gerardo Dávalos Velásquez 240278
print("Determinar el signo zodiacal")
try:
    m = int(input("Ingrese el número de mes en el que nacio : "))
    d = int(input("Ingrese el dia en que nacio: "))
except ValueError:
    print("Solo se admiten números")
    exit()
if m>12 or m<1:
    print("El més solo puede ser del 1 al 12")
    exit()
elif d>31 or d<1:
    print("El dia debe ir de 1 a 31")
    exit()
elif m==2 and d>29:
    print("Febrero solo puede tener maximo 29 dias")
    exit()

if (m==3 and d>20) or (m==4 and d<20):
    print("Su signo zodiacal es Aries")
elif (m==4 and d>19) or (m==5 and d<21):
    print("Su signo zodiacal es Tauro")
elif (m==5 and d>20) or (m==6 and d<21):
    print("Su signo zodiacal es Geminis")
elif (m==6 and d>20) or (m==7 and d<23):
    print("Su signo zodiacal es Cancer") 
elif (m==7 and d>22) or (m==8 and d<23):
    print("Su signo zodiacal es Leo")
elif (m==8 and d>22) or (m==9 and d<23):
    print("Su signo zodiacal es Virgo")
elif (m==9 and d>22) or (m==10 and d<23):
    print("Su signo zodiacal es Libra")
elif (m==10 and d>22) or (m==11 and d<22):
    print("Su signo zodiacal es Escorpio")
elif (m==11 and d>21) or (m==12 and d<22):
    print("Su signo zodiacal es Sagitario")
elif (m==12 and d>21) or (m==1 and d<20):
    print("Su signo zodiacal es Capricornio")
elif (m==1 and d>19 ) or (m==2 and d<19):
    print("Su signo zodiacal es Acuario")
elif (m==2 and d>18) or (m==3 and d<21):
    print("Su signo zodiacal es Piscis")