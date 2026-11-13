def comprar_snack():
    lista_aperitivos = ["Pipocas", "Nachos", "Hot-Dog", "Gomitas"]
    lista_bebidas = ["Fanta", "Coca-Cola", "Sprite"]
    precios_aperitivos = {"Pipocas": 30,"Nachos": 30,"Hot-Dog": 20,"Gomitas": 25}
    precios_bebidas = {"Fanta": 15,"Coca-Cola": 17,"Sprite": 20}
    precio_snack = 0
    cantidad=50
    factura = []
    print("==== Bienvenido a los Snacks ====")
    print("Elija sus aperitivos para disfrutar con la pelicula")
    for i, aperitivo in enumerate(lista_aperitivos, start=1):
        print(i, ".", aperitivo)
    print(len(lista_aperitivos) + 1, ". Volver")
    eleccion = input("Elija escribiendo el numero: ")
    if not eleccion.isdigit():
        print("Opcion incorrecta")
        return 0
    eleccion = int(eleccion)
    if eleccion == len(lista_aperitivos) + 1:
        print("Volviendo al menu")
        return 0
    if eleccion < 1 or eleccion > len(lista_aperitivos):
        print("Opcion incorrecta")
        return 0
    aperitivo = lista_aperitivos[eleccion - 1]
    if aperitivo == "Pipocas":
        while True:
            try:
                cant = int(input("¿Cuantos conos de pipoca va a querer?: "))
                if cant <= 0:
                    print("Cantidad invalida")
                    
                elif cant > cantidad:
                    print("La cantidad ha superado el límite de stock, intente con una cantidad menor")
                    
                else:
                    for i in range(cant):
                        print(f"\nElija el sabor del cono {i + 1}")
                        print("1. Mantequilla")
                        print("2. Dulce")
                        sabor = input("Seleccione el sabor: ")
                        if sabor == "1":
                            precio = 50
                            descripcion = "Pipocas con mantequilla"
                        elif sabor == "2":
                            precio = 30
                            descripcion = "Pipocas dulces"
                        else:
                            print("Opcion incorrecta")
                            return 0
                        precio_snack += precio
                        factura.append({"producto": descripcion,"cantidad": 1,"precio": precio,"subtotal": precio})
                    break
            except ValueError:
                print("Ingrese solo numeros")
                return 0
    elif aperitivo == "Nachos":
        while True:
            try:
                cant = int(input("¿Cuantas porciones de nachos desea?: "))
                if cant <= 0:
                    print("Cantidad invalida")
                
                if cant > cantidad:
                    print("La cantidad ha superado el límite de stock, intente con una cantidad menor")
                else:
                    respuesta = input("¿Desea sus nachos con queso? si/no: ").strip().lower()
                    if respuesta == "si":
                            precio = 30
                            descripcion = "Nachos con queso"
                    else:
                        precio = 25
                        descripcion = "Nachos sin queso"
                        subtotal = cant * precio
                        precio_snack += subtotal
                        factura.append({"producto": descripcion,"cantidad": cant,"precio": precio,"subtotal": subtotal})
                    break
            except ValueError:
                print("Ingrese solo numeros")
                return 0
    elif aperitivo == "Hot-Dog":
        while True:
            try:
                cant = int(input("¿Cuantos Hot-Dog desea?: "))
                if cant <= 0:
                    print("Cantidad invalida") 
                elif cant > cantidad:
                    print("La cantidad ha superado el límite de stock, intente con una cantidad menor")
                else:
                    precio = precios_aperitivos[aperitivo]
                    subtotal = cant * precio
                    precio_snack += subtotal
                    factura.append({"producto": "Hot-Dog","cantidad": cant,"precio": precio,"subtotal": subtotal})
                    break
            except ValueError:
                print("Ingrese solo numeros")
                return 0
    elif aperitivo == "Gomitas":
        while True:
            try:
                cant = int(input("¿Cuantas bolsitas de gomitas desea?: "))
                if cant <= 0:
                    print("Cantidad invalida")
                elif cant > cantidad:
                    print("La cantidad ha superado el límite de stock, intente con una cantidad menor")
                else:
                    precio = precios_aperitivos[aperitivo]
                    subtotal = cant * precio
                    precio_snack += subtotal
                    factura.append({"producto": "Gomitas","cantidad": cant,"precio": precio,"subtotal": subtotal})
                    break
            except ValueError:
                print("Ingrese solo numeros")
                return 0   
    res_bebida = input("\n¿Desea algo de beber? si/no: ").strip().lower()
    if res_bebida == "si":
        while True:
            try:
                cant_bebidas = int(input("¿Cuantos refrescos desea?: "))
                if cant_bebidas <= 0:
                    print("Cantidad invalida")
                elif cant_bebidas > cantidad:
                    print("La cantidad ha superado el límite de stock, intente con una cantidad menor")
                else:
                    for i in range(cant_bebidas):
                        print(f"\nRefresco numero {i + 1}")
                        for j, bebida in enumerate(lista_bebidas, start=1):
                            print(j, ".", bebida)
                        eleccion_bebida = input("Seleccione una bebida: ")
                        if not eleccion_bebida.isdigit():
                            print("Opcion incorrecta")
                            continue
                        eleccion_bebida = int(eleccion_bebida)
                        if 1 <= eleccion_bebida <= len(lista_bebidas):
                            bebida = lista_bebidas[eleccion_bebida - 1]
                            precio = precios_bebidas[bebida]
                            precio_snack += precio
                            factura.append({"producto": bebida,"cantidad": 1,"precio": precio,"subtotal": precio})
                            print(bebida, "agregada con exito")
                        else:
                            print("Opcion incorrecta")
                    break
            except ValueError:
                print("Ingrese solo numeros")
                return precio_snack
    print("\n==========================================")
    print("           FACTURA DE COMPRA")
    print("==========================================")
    for producto in factura:
        print("\nProducto:", producto["producto"])
        print("Cantidad:", producto["cantidad"])
        print("Precio unitario:", producto["precio"], "Bs")
        print("Subtotal:", round(producto["subtotal"], 2), "Bs")
    print("\n==========================================")
    print("TOTAL A PAGAR:", round(precio_snack, 2), "Bs")
    print("==========================================")
    input("\nPresione ENTER para continuar...")
    return precio_snack