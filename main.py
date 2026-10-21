from funciones import login
from administrador import menu_administrador
def main():
    print(" SISTEMA CARTELERA DE CINE ")
    tipo_usuario = login()
    if tipo_usuario == "administrador":
        menu_administrador()
    elif tipo_usuario == "usuario":
        print("Bienvenido usuario")
    else:
        print("Acceso denegado")
main()