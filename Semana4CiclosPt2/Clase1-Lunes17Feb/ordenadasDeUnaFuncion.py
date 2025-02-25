#Luis Gerardo Dávalos Velásquez 240278
print("Ordenadas pares de la función f(x) = x*x*x+1")
x = 0
while x <=30:
    if x%2 == 0:
        resultado = x*x*x+1
        print(f"f({x}) = {x} x {x} x {x} + 1 = {resultado}")
    x += 1