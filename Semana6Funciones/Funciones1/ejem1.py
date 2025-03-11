#Luis Gerardo Dávalos Velásquez 240278
def saludar(nombre):
    """ Esta función recibe un nombre y devuelve un saludo
        Parametros:
         nombre (str): El nombre de la persona a saludar
        
        Retorna:
         str: Un mensaje de saludo personalizado """
    mensaje = (f"¡Hola, {nombre}! Bienvenido/a al mundo de las funciones")
    return mensaje

#Ejemplo de uso de la función
nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)

print(len(nombre_usuario))