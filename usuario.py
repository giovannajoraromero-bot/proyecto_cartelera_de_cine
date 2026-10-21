from funciones import ver_cartelera
from funciones import consultar_pelicula
from funciones import ver_snacks
from funciones import consultar_snack
from funciones import mostrar_precios
from funciones import comprar_entrada
from funciones import mostrar_factura
def menu_usuario():
    while True:
        print("===== MENU USUARIO =====")
        print("1. Ver cartelera")
        print("2. Buscar pelicula")
        print("3. Ver snacks")
        print("4. Buscar snack")
        print("5. Ver precios")
        print("6. Comprar entrada")
        print("7. Mostrar factura")
        print("8. Cerrar sesion")
        opcion = input(
            "Seleccione una opcion: ")
        match opcion:
            case "1":
                ver_cartelera()
            case "2":
                consultar_pelicula()
            case "3":
                ver_snacks()
            case "4":
                consultar_snack()
            case "5":
                mostrar_precios()
            case "6":
                comprar_entrada()
            case "7":
                mostrar_factura()
            case "8":
                print("Sesion cerrada correctamente")
                break
            case _:
                print("Opcion invalida")