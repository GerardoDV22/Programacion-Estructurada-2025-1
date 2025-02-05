#Luis Gerardo Dávalos Velásquez 240278
print("Programa que solicita la edad de un usuario y muestra un mensaje")
try:
    edad = int(input("Ingresa tu edad: "))
except ValueError:
    print("Error, debes ingresar un número valido (mayor que 0).")
    exit()

#Se verifica que la edad sea mayor o igual a 18
if edad >= 18:
    print("Eres mayor de edad. Puedes votar y conducir")
else:#Sí no se cumple la condicion del "if" se procede a realizar las instrucciones depues del "else"
    print("Eres menor de edad. NO puedes votar ni conducir")