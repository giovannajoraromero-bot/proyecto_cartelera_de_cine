from funciones import login
from administrador import menu_administrador
from usuario import menu_usuario
def main():
        while True:
            tipo_usuario = login()
            if tipo_usuario == "salir":
                print("Programa finalizado")
                break
            elif tipo_usuario == "administrador":
                menu_administrador()
            elif tipo_usuario == "usuario":
                menu_usuario()
            else:
                print("Acceso denegado")
main()