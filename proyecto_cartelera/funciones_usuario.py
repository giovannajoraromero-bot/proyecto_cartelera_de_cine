def funcion_usuario():
    print("bienvenid@ al sistema")
    nombre=input("ingrese su nombre: ")
    print("\n¿desea comprar algo?")
    respuesta=input("escriba si/no: ")
    respuesta=respuesta.lower().strip()
    if respuesta  in ["si","si"]:
        print("\n MENU ")
        print("1. PIPOCAS")
        print("2. REFRESCOS")
        print("3. GOLOSINAS")
        opcion=input("elige un numero: ")
        pedido=""
        match opcion:
            case"1":
                pedido="pipocas"
            case"2":
                pedido="refrescos"
            case"3":
                pedido="golosinas"
            case "1,2":
                pedido="pipocas y refresco"
            case"1,3":
                pedido="pipocas y golosinas"
            case"2,3":
                pedido="refresco y golosinas"
            case _:
                "opcion invalida"
        print(f"\n listo a nomdre de {nombre}, su pedido es: {pedido} ")
        print("Listo.")
    elif respuesta == "no":
        print("Volver")
    else: 
        print("opcion invalida")

funcion_usuario()

                        