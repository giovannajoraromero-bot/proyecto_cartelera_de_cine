from funciones import registrar_usuario
from funciones import registrar_administradores
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
from funciones import cerrar_sesion
def menu_administrador():
    while True:
        print("===== MENU ADMINISTRADOR =====")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Peliculas")
        print("3. Cerrar sesion")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                menu_usuarios()
            case "2":
                menu_peliculas()
            case "3":
                cerrar_sesion()
                break
            case _:
                print("Opcion invílida")
def menu_usuarios():
    while True:
        print("===== GESTION DE USUARIOS =====")
        print("1. Registrar usuario")
        print("2. Registrar administrador")
        print("3. Mostrar usuarios")
        print("4. Buscar usuario")
        print("5. Modificar usuario")
        print("6. Eliminar usuario")
        print("7. Volver")
        opcion = input("Seleccione una opcion: ")
        match opcion:
            case "1":
                registrar_usuario()
            case "2":
                registrar_administradores()
            case "3":
                mostrar_usuarios()
            case "4":
                buscar_usuario()
            case "5":
                modificar_usuario()
            case "6":
                eliminar_usuario()
            case "7":
                break
            case _:
                print("Opcion invalida")
def menu_peliculas():
    while True:
        print("===== GESTIóN DE PELíCULAS =====")
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