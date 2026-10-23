from funciones import registrar_usuario
from funciones import mostrar_usuarios
from funciones import buscar_usuario
from funciones import modificar_usuario
from funciones import eliminar_usuario
#peliculas
from funciones import registrar_pelicula
from funciones import mostrar_peliculas
from funciones import buscar_pelicula
from funciones import modificar_pelicula
from funciones import eliminar_pelicula
#Snaks
from compra_snack import agregar_snack
from compra_snack import mostrar_snack
from compra_snack import eliminar_snack

from funciones import cerrar_sesion
def menu_administrador():
    while True:
        print("===== MENU ADMINISTRADOR =====")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Peliculas")
        print("3. Gestionar Snacks")
        print("4. Cerrar Sesion")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                menu_usuarios()
            case "2":
                menu_peliculas()
            case "3":
                menu_snacks()
            case "4":
                cerrar_sesion()
                break
            case _:
                print("Opcion invílida")
def menu_usuarios():
    while True:
        print("===== GESTION DE USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Volver")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                mostrar_usuarios()
            case "3":
                buscar_usuario()
            case "4":
                modificar_usuario()
            case "5":
                eliminar_usuario()
            case "6":
                break
            case _:
                print("Opcion invalida")
def menu_peliculas():
    while True:
        print("===== GESTI├ôN DE PEL├ìCULAS =====")
        print("1. Registrar pel├¡cula")
        print("2. Mostrar pel├¡culas")
        print("3. Buscar pel├¡cula")
        print("4. Modificar pel├¡cula")
        print("5. Eliminar pel├¡cula")
        print("6. Volver")
        opcion = input("Seleccione una opci├│n: ")
        match opcion:
            case "1":
                registrar_pelicula()
            case "2":
                mostrar_peliculas()
            case "3":
                buscar_pelicula()
            case "4":
                modificar_pelicula()
            case "5":
                eliminar_pelicula()
            case "6":
                break
            case _:
                print("Opci├│n inv├ílida")
def menu_snacks():
    while True:
        print("===== GESTI├ôN DE SNACKS =====")
        print("1. Agregar snack")
        print("2. Mostrar snacks")
        print("3. Eliminar snack")
        print("4. Volver")
        opcion = input("Seleccione una opci├│n: ")
        match opcion:
            case "1":
                agregar_snack()
            case "2":
                mostrar_snack()
            case "3":
                eliminar_snack()
            case "4":
                break
            case _:
                print("Opci├│n inv├ílida")