from funciones import (consultar_pelicula,comprar_entrada,mostrar_factura,ver_cartelera)
def menu_usuario():
    while True:
        print("\n===== MENU USUARIO =====")
        print("1. Ver cartelera y horarios")
        print("2. Buscar pelicula")
        print("3. Comprar entrada")
        print("4. Mostrar factura")
        print("5. Cerrar sesion")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                ver_cartelera()
            case "2":
                consultar_pelicula()
            case "3":
                comprar_entrada()
            case "4":
                mostrar_factura()
            case "5":
                print("Sesion cerrada correctamente")
                break
            case _:
                print("Opcion invalida")