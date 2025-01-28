#Luis Gerardo Dávalos Velásquez 240278

print("La suma de 3 numeros y el promedio") #Permite mostrar un mensaje en pantalla
n1 = float(input("Ingrese el primer número: ")) #Recibe una entrada y puede mostrar un mensaje para solicitar
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: ")) #Se recomienda usar datos tipo float por las operaciones matematicas

#Operaciónes matematicas
suma = n1+n2+n3 
prom = suma/3

print(f"La suma es {suma} y el promedio es {prom:.2f}") #Se agrega una "f" al inicio del print para incluir variables