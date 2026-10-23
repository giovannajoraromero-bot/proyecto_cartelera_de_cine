lista_aperitivos=["Pipocas","Nachos","Hot-Dog","Gomitas"]
lista_bebidas=["Fanta","Coca-Cola","Sprite"]
precio_snack=0

def comprar_snack():
    print("====Bienvenido a los Snacks====")
    print("Elija sus aperitivos para disfrutar con la pelicula")
    print("1.Pipocas")
    print("2.Nachos")
    print("3.Gomitas")
    print("4.Volver")
    eleccion=input("Elija escribiendo el numero: ")
    match eleccion:
        case "1":
            respuesta=input("\nLas va a querer con mantequilla si/No"  ).strip().lower()
            if respuesta=="si":
                print("Las pipocas con mantequilla le sale en 50 bs")
                print("===========================================")
                precio_snack=50
                res_bebida=input("\nDesea algo de beber? si/No " ).strip().lower()
                if res_bebida=="si":
                    print("1.Fanta")
                    print("2.Cola-Cola")
                    print("3.Sprite")
                    bebida=input("Selecione elijiendo un numero: ")
                    match bebida :
                        case "1":
                            print("La fanta en vaso de 1 litro tiene un precio de 15 bs")
                            precio_snack=precio_snack + 15
                            input("\nPresione ENTER para avanzar...")                          
                            return precio_snack
                        case "2":
                            print("La Coca-Cola en vaso de 1 litro tiene un precio de 17 bs")
                            precio_snack=precio_snack + 17
                            input("\nPresione ENTER para avanzar...")
                            return precio_snack
                        case "3":
                            print("La Sprite en vaso de 1 litro tiene un precio de 20 bs")
                            precio_snack=precio_snack + 20
                            input("\nPresioneENTER para avanzar...")
                            return precio_snack
                        case _:
                              print("Opcion incorrecta..no se agregara bebida")
                              return precio_snack
                else:
                    return precio_snack
            else:
                    precio_snack=30
                    res_bebida=input("\nDesea algo de beber? si/No" ).strip().lower()
                    if res_bebida=="si":
                        print("1.Fanta")
                        print("2.Cola-Cola")
                        print("3.Sprite")
                        bebida=input("Selecione elijiendo un numero: ")
                        match bebida :
                            case "1":
                                print("La fanta en vaso tiene un precio de 15 bs")
                                precio_snack=precio_snack + 15
                                input("\nPresione ENTER para avanzar...")
                                return precio_snack
                            case "2":
                                print("La Coca-Cola en vaso de 1 litro tiene un precio de 17 bs")
                                precio_snack=precio_snack + 17
                                input("\nPresioneENTER para avanzar...")
                                return precio_snack
                            case "3":
                                print("La Sprite en vaso de 1 litro tiene un precio de 20 bs")
                                precio_snack=precio_snack + 20
                                input("\nPresione ENTER para avanzar...")
                                return precio_snack
                    else:
                        return precio_snack

        case "2":
            respuesta=input("\nLas va a querer con Queso si/No "  ).strip().lower()
            if respuesta=="si":
                print("Los nachos con queso le sale en 30 bs")
                print("===========================================")
                precio_snack=30
                res_bebida=input("\nDesea algo de beber? si/No" ).strip().lower()
                if res_bebida=="si":
                    print("1.Fanta")
                    print("2.Cola-Cola")
                    print("3.Sprite")
                    bebida=input("Selecione elijiendo un numero: ")
                    match bebida :
                        case "1":
                            print("La fanta en vaso tiene un precio de 15 bs")
                            precio_snack=precio_snack + 15
                            input("\nPresione ENTER para avanzar...")
                            return precio_snack
                        case "2":
                            print("La Coca-Cola en vaso de 1 litro tiene un precio de 17 bs")
                            precio_snack=precio_snack + 17
                            input("\nPresione ENTER para avanzar...")
                            return precio_snack
                        case "3":
                            print("La Sprite en vaso de 1 litro tiene un precio de 20 bs")
                            precio_snack=precio_snack + 20
                            input("\nPresione ENTER para avanzar...")
                            return precio_snack
                else:
                    return precio_snack
            else:
                        precio_snack=30
                        res_bebida=input("\nDesea algo de beber? si/No" ).strip().lower()
                        if res_bebida=="si":
                            print("1.Fanta")
                            print("2.Cola-Cola")
                            print("3.Sprite")
                            bebida=input("Selecione elijiendo un numero: ")
                            match bebida :
                                case "1":
                                    print("La fanta en vaso tiene un precio de 15 bs")
                                    precio_snack=precio_snack + 15
                                    input("\nPresione ENTER para avanzar...")
                                    return precio_snack
                                case "2":
                                    print("La Coca-Cola en vaso de 1 litro tiene un precio de 17 bs")
                                    precio_snack=precio_snack + 17
                                    input("\nPresione ENTER para avanzar...")
                                    return precio_snack
                                case "3":
                                    print("La Sprite en vaso de 1 litro tiene un precio de 20 bs")
                                    precio_snack=precio_snack + 20
                                    input("\nPresione ENTER para avanzar...")
                                    return precio_snack
                        else:
                            return precio_snack


        case "3":
                    print("El kilo de gomitas mixtas le sale en 25 bs")
                    print("===========================================")
                    precio_snack=25
                    res_bebida=input("\nDesea algo de beber? si/No" ).strip().lower()
                    if res_bebida=="si":
                        print("1.Fanta")
                        print("2.Cola-Cola")
                        print("3.Sprite")
                        bebida=input("Selecione elijiendo un numero: ")
                        match bebida :
                            case "1":
                                print("La fanta en vaso tiene un precio de 15 bs")
                                precio_snack=precio_snack + 15
                                input("\nPresione ENTER para avanzar...")
                                return precio_snack
                            case "2":
                                print("La Coca-Cola en vaso de 1 litro tiene un precio de 17 bs")
                                precio_snack=precio_snack + 17
                                input("\nPresione ENTER para avanzar...")
                                return precio_snack
                            case "3":
                                print("La Sprite en vaso de 1 litro tiene un precio de 20 bs")
                                precio_snack=precio_snack + 20
                                input("\nPresione ENTER para avanzar...")
                                return precio_snack        
                    else: 
                        return precio_snack
                
        case "4":  
            print("Volviendo a menu")
            return   
def agregar_snack():
    print("Que snack desea agregar?")
    print("1.Aperitivos")
    print("2.Bebida")
    eleccion=input("Escoja una opcion: ")
    match eleccion:
        case "1":
            print("Aperitivos Actuales",lista_aperitivos)
            aperitivo=input("Que aperitivo desea agregar?: ")
            lista_aperitivos.append(aperitivo)
            print(aperitivo,"  agregado con exito a la lista")
        case "2":
            print("Bebidas Actuales",lista_bebidas)
            bebida=input("Que bebida desea agregar?: ")
            lista_bebidas.append(bebida)
            print(bebida ,"  agregado con exito a la lista")
        case _:
              print("opcion invalida,retornando al menu")
              return
def mostrar_snack():
     
     print("Snack Disponibles:")
     print(lista_aperitivos)
     print(lista_bebidas)
def eliminar_snack():
    print("Que desea eliminar?: ")
    print("1.aperitivos")
    print("2.Bebidas")
    opcion=input("\nElija una opcion: ")
    if opcion=="1":
        print("Aperitivos actuales",lista_aperitivos)
        eliminar=input("Escriba lo que desea eliminar")
        if eliminar in lista_aperitivos:
            lista_aperitivos.remove(eliminar)
            print(eliminar,"a sido eliminado con exito")
        else:
            print("el producto no se encuentra en la lista")
            return
    elif opcion=="2":
        print("Bebidas actuales",lista_bebidas)
        eliminar=input("Escriba lo que desea eliminar")
        if eliminar in lista_bebidas:
                lista_bebidas.remove(eliminar)
                print(eliminar,"a sido eliminado con exito")
        else:
                print("el producto no se encuentra en la lista")
                return
