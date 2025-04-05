#Luis Gerardo Dávalos Velásquez 240278
#Parte 1. Crear y escribir el archivo
with open("datos.txt","w") as archivo:
    archivo.write("Nombre: Luis Gerardo\n")
    archivo.write("Edad: 26\n")
    archivo.write("Lenguaje favorito: Java\n")

#Parte 2. Leer y mostrar el contenido del archivo
print("\nContenido del archivo:")
with open("datos.txt","r") as archivo:
    for linea in archivo:
        print(linea, end="")

#Parte 3. Agregar más información al archivo
with open("datos.txt","a+") as archivo:
    archivo.write("Ciudad: Mexicali\n")
    archivo.write("Pasatiempo: Jugar videojuegos\n")
    archivo.seek(0)
    contenido = archivo.read()
    print("\nNuevo contenido.")
    print(contenido)

#Parte 4. Contar las lineas del archivo
with open("datos.txt","r") as archivo:
    num_lineas = 0
    for linea in archivo:
        num_lineas += 1
    print(f"\nEl archivo tiene {num_lineas} lineas")

#Parte 5.Buscar palabra en el archivo
with open("datos.txt","r") as archivo:
    palabra = input("\nIngresa la palabra a buscar: ")
    for linea in archivo:
        linea = linea.replace(":","").replace("\n","")
        if palabra in linea:
            print(f"La palabra \"{palabra}\" esta en el archivo")
            exit()
    print(f"La palabra \"{palabra}\" NO esta en el archivo")