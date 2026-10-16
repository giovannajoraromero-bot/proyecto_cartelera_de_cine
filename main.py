from funciones import login
from administrador import menu_administrador
def main():
    print("--- BIENVENIDO/A AL SISTEMA ---")
    tipo_usuario = login()
    if tipo_usuario == "administrador":
        menu_administrador()
    else:
        print("Error... Acceso denegado...")
main()