#Luis Gerardo Dávalos Velásquez 240278
productos = []
unidades = []
operaciones = []
print("Sistema de control de inventario del día")
opc = 0
while opc != 4:
    print("------------------------------------")
    print("1. Agregar producto\n2. Modificar productos\n3. Resumen de inventario\n4. Salir")
    try:
        opc = int(input("Selecciona una opción: "))
    except ValueError:
        print("Solo se permiten números")

    if opc == 1:
        print("------------------------------------")
        p = input("Ingrese el nombre del nuevo producto: ")
        try:
            u = int(input("Ingrese las unidades iniciales (0 en caso de no haber): "))
            productos.append(p)
            unidades.append(u)
            operaciones.append(0)
            print("Inventario actualizado correctamente")
        except ValueError:
            print("Se debe ingresar solo números en las unidades")
    elif opc == 2:
        print("------------------------------------")
        if len(productos) == 0:
            print("No hay productos registrados en el inventario")
        else:
            print("Articulos en inventario:")
            n = 1
            for i in productos:
                print(f"{n}. {i}")
                n+=1
            try:
                opc2 = int(input("Seleccione el número de una opción: "))
            except ValueError:
                print("Solo se permiten números")
            if opc2<=len(productos) and opc2>0:
                print("------------------------------------")
                print(f"Producto: {productos[opc2-1]}\nUnidades en inventario: {unidades[opc2-1]}")
                print("Desea:\n1. Agregar unidades\n2. Eliminar unidades")
                try: 
                    opc3 = int(input("Selecciona una opción: "))
                    if opc3 == 1:
                          try:
                              aux = int(input("Ingrese las unidades entrantes: "))
                              unidades[opc2-1] += aux
                              operaciones[opc2-1] += 1
                          except ValueError:
                              print("Solo se permiten números")
                    elif opc3 == 2:
                        try:
                              aux = int(input("Ingrese las unidades que van a salir: "))
                              if unidades[opc2-1] < aux:
                                  print("No hay suficiente inventario")
                              else:
                                  unidades[opc2-1] -= aux
                                  operaciones[opc2-1] += 1
                        except ValueError:
                            print("Solo se permiten numeros")
                    else:
                        print("Opción invalida")
                except ValueError:
                    print("Solo se permiten numeros")
            else:
                print("No existe tal opción")
    elif opc == 3:
        print("------------------------------------")
        if len(productos) == 0:
            print("El inventario esta vacio")
        else:
            print("Resumen del inventario: ")
            for i in range(len(productos)):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(f"Producto: {productos[i]}\nUnidades en inventario: {unidades[i]}")
                print(f"Entradas/Salidas de inventario del día de hoy: {operaciones[i]}")
    elif opc == 4:
        print("Saliendo del sistema.\nHasta luego")
    else:
        print("Opción no valida")