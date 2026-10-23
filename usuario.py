from funciones import consultar_pelicula
from funciones import mostrar_precios
from funciones import comprar_entrada
from funciones import mostrar_factura
from compra_snack import comprar_snack
from funciones import ver_cartelera
import funciones 

def menu_usuario():
    while True:
        print("===== MENU USUARIO =====")
        print("1. Ver cartelera")
        print("2. Buscar pelicula")
        print("3. Comprar Snack")
        print("4. ver precios")
        print("5. Comprar entrada")
        print("6. Mostrar factura")
        print("7. Cerrar sesion")
        opcion = input(
            "Seleccione una opcion: ")
        match opcion:
            case "1":
                ver_cartelera()
            case "2":
                consultar_pelicula()
            case "3":
                comprar_snack()    
            
            case "4":
                mostrar_precios()
            case "5":
                funciones.precio_snack=comprar_entrada()
            case "6":
                mostrar_factura()
            case "7":
                print("Sesion cerrada correctamente")
                break
            case _:
                print("Opcion invalida")