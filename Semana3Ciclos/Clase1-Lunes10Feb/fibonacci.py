#Luis Gerardo Dávalos Velásquez 240278
print("Calcular la secuencia fibonacci hasta el termino que se indique")
n = int(input("Ingrese hasta que termino desea que se imprima la secuencia: "))
fib1 = 0
fib2 = 1
for i in range(n):
    print(fib1, end=", ")
    aux = fib1 + fib2
    fib1 = fib2
    fib2 = aux