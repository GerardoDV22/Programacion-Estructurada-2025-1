#Luis Gerardo Dávalos Velásquez 240278
print("Determinar si un número entero de 4 digitos es palíndromo")
try:
    num = int(input("Ingrese un número entero de 4 digitos: "))
except ValueError:
    print("El dato ingresado no es correcto")
    exit()
if num>9999 or num < 1000:
    print("No es un número de 4 digitos")
    exit()

m = num//1000
aux = num%1000
c = aux//100
aux = aux % 100
d = aux //10
u = aux % 10
if m == u and c == d:
    print(f"El número {num} es un palindromo")
else:
    print(f"El número {num} NO es un palindromo")