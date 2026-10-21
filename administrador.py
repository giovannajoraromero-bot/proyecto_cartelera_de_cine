#usuario
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
from funciones import registrar_snack
from funciones import mostrar_snacks
from funciones import buscar_snack
from funciones import modificar_snack
from funciones import eliminar_snack
from funciones import cerrar_sesion
def menu_administrador():
    while True:
        print("===== MENU ADMINISTRADOR =====")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Películas")
        print("3. Gestionar Snacks")
        print("4. Cerrar Sesión")
        opcion = input("Seleccione una opción: ")
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
                print("Opción inválida")
def menu_usuarios():
    while True:
        print("===== GESTIÓN DE USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Buscar usuario")
        print("4. Modificar usuario")
        print("5. Eliminar usuario")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
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
                print("Opción inválida")
def menu_peliculas():
    while True:
        print("===== GESTIÓN DE PELÍCULAS =====")
        print("1. Registrar película")
        print("2. Mostrar películas")
        print("3. Buscar película")
        print("4. Modificar película")
        print("5. Eliminar película")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
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
                print("Opción inválida")
def menu_snacks():
    while True:
        print("===== GESTIÓN DE SNACKS =====")
        print("1. Registrar snack")
        print("2. Mostrar snacks")
        print("3. Buscar snack")
        print("4. Modificar snack")
        print("5. Eliminar snack")
        print("6. Volver")
        opcion = input("Seleccione una opción: ")
        match opcion:
            case "1":
                registrar_snack()
            case "2":
                mostrar_snacks()
            case "3":
                buscar_snack()
            case "4":
                modificar_snack()
            case "5":
                eliminar_snack()
            case "6":
                break
            case _:
                print("Opción inválida")