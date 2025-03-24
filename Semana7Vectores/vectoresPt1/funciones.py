#Luis Gerardo Dávalos Velásquez 240278

def sumar_vector(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

def encontrar_mayor_menor(vector):
    mayor = vector[0]
    menor = vector[0]
    for i in range(1,len(vector)):
        if vector[i] > mayor:
            mayor = vector[i]
        elif vector[i] < menor:
            menor = vector[i]
    return mayor, menor

def filtrar_mayores(vector, numero_filtro):
    vector_filtrado = []
    for i in range(len(vector)):
        if vector[i] > numero_filtro:
            vector_filtrado.append(vector[i])
    return vector_filtrado

def combinar_vectores(vector1, vector2):
    for i in range(len(vector2)):
        vector1.append(vector2[i])
    return vector1

def ordenar_vector(vector):
    for i in range(len(vector)):
        for j in range(i+1, len(vector)):
            if vector[j] < vector[i]:
                aux = vector[i]
                vector[i] = vector[j]
                vector[j] = aux
    return vector