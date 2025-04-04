#Luis Gerardo Dávalos Velásquez 240278

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print()

def sumar_matrices(a,b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = a
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[i][j] = a[i][j] + b[i][j]
        imprimir_matriz(c)
    else:
        print("No se pueden sumar")

def transponer_matriz(matriz):
    transpuesta = []
    for i in range(len(matriz[0])):
        lista = [0,0,0]
        for j in range(len(matriz)):
            lista.append(0)
        transpuesta.append(lista)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            transpuesta[j][i] = matriz[i][j]
    return transpuesta

def multiplicar_matriz(a,b):
    if len(a[0]) == len(b):
        c = []
        for i in range(len(a)):
            lista = []
            for j in range(len(b[0])):
                lista.append(0)
            c.append(lista)
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]
        imprimir_matriz(c)
    else:
        print("No se pueden multiplicar")
    