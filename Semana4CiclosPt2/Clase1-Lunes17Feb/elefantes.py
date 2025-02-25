#Luis Gerardo Dávalos Velásquez 240278
print("Canción de los elefantes que se columpiaban")
elefantes = 1
print(f"¡{elefantes} elefante se columpiaba sobre la tela de una araña!\n¡Como veia que resistia fue a llamar a otro elefante!")
while True:
    try:
        sig = int(input("¿Cuantos elefantes siguen? "))
        if sig == elefantes+1:
            elefantes = sig
            print(f"¡{elefantes} elefantes se columpiaban sobre la tela de una araña!\n¡Como veian que resistia fueron a llamar a otro elefante!")
        else:
            print("No sigue ese número de elefantes ¡Intentalo de nuevo!")
        
        if elefantes == 10:
            print("Pero como ya eran 10 elefantes ¡La canción se termino!")
            break
    except ValueError:
        print("Solo se permiten números")