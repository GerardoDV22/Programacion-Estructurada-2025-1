#Luis Gerardo Dávalos Velásquez 240278

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def sumar_matrices(a,b):
    c = a
    for i in range(len(a)):
        for j in range(len(a[i])):
            c[i][j] = a[i][j] + b[i][j]
    return c

def transponer_matriz(matriz):
    transpuesta = [[0 for _ in range(len(matriz))] for _ in range(len(matriz[0]))]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

def multiplicar_matriz(a,b):
    if len(a[0]) == len(b):
        c = [[0 for _ in range(len(b[0]))] for _ in range(len(a))] #columnas/filas
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
        imprimir_matriz(c)
    else:
        print("No se pueden multiplicar")
    