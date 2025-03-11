#Luis Gerardo Dávalos Velásquez 240278
from funciones import *

def mostrar_menu():
    print("\n===== MENÚ DE OPCIONES =====")
    print("1. Saludar")
    print("2. Número de letras en su nombre")
    print("3. Piedra, papel o tijeras")
    print("4. Determinar edad")
    print("5. Sumar 2 numeros")
    print("6. Mostrar piramide")
    print("0. Salir")
    return input("\nSelecciona una opción: ")

def main():
    nombre_usuario = input("Por favor, ingresa tu nombre: ")
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            print(saludar(nombre_usuario))
        elif opcion == "2":
            print(f"\n{nombre_usuario} tiene {longitud_nombre(nombre_usuario)} letras")
        elif opcion == "3":
            juego(nombre_usuario)
        elif opcion == "4":
            edad()
        elif opcion == "5":
            num = suma()
            if num != None:
                print(f"\nLa suma de los números es: {num:.2f}")
        elif opcion == "6":
            imprimir_piramide(nombre_usuario)
        elif opcion == "0":
            print(f"¡Hasta pronto, {nombre_usuario}!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
        
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()