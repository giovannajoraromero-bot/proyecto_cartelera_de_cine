usuarios = ["hasu", "liz", "asoka", "anahi", "admin"]
contraseñas = [2468, 1433, 8699, 7310, 1234]
peliculas = ["toy story","llorona","chaplin"]
from compra_snack import comprar_snack
precio_snack=0


##Funciones para control de usuarios
def login():
    usuario = input("Usuario: ").strip().lower()
    try:
        contraseña = int(input("Contraseña de 4 digitos: "))
        if contraseña < 1000 or contraseña > 9999:
            print("La contraseña debe tener 4 d├¡gitos")
            return "incorrecto"
    except ValueError:
        print("La contraseña debe ser numerica")
        return "incorrecto"
    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas[i]:
            if usuario == "admin":
                print("Bienvenido Administrador")
                return "administrador"
            else:
                print("Bienvenido Usuario")
                return "usuario"
    print("Usuario o contraseña incorrectos")
    return "incorrecto"
##Falta verificacion de usuario existente...
def registrar_usuario():
    nuevo_usuario = input("Ingrese usuario: ").strip().lower()
    if nuevo_usuario in usuarios:
        print("Ese usuario ya existe")
        return
    try:
        nueva_contraseña = int(input("Ingrese contraseña: "))
        if nueva_contraseña < 1000 or nueva_contraseña > 9999:
            print("La contraseña debe tener 4 digitos")
            return
        if nueva_contraseña in contraseñas:
            print("La contraseña ya existe")
            return
    except ValueError:
        print("La contraseña debe ser numerica")
        return
    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)
    print("Usuario registrado correctamente")
def mostrar_usuarios():
    if len(usuarios) == 0:
        print("No existen usuarios")
        return
    for i in range(len(usuarios)):
        print("----------------")
        print("Usuario:", usuarios[i])
        print("Contraseña:", contraseñas[i])
def buscar_usuario():
    buscar = input("Ingrese usuario a buscar: ").strip().lower()
    if buscar in usuarios:
        posicion = usuarios.index(buscar)
        print("Usuario:", usuarios[posicion])
        print("Contraseña:", contraseñas[posicion])
    else:
        print("Usuario no encontrado")
def modificar_usuario():
    buscar = input("Usuario a modificar: ").strip().lower()
    if buscar in usuarios:
        posicion = usuarios.index(buscar)
        nuevo_usuario = input("Nuevo usuario: ").strip().lower()
        if nuevo_usuario in usuarios and nuevo_usuario != buscar:
            print("Ese usuario ya existe")
            return
        try:
            nueva_contraseña = int(input("Nueva contraseña: "))
            if nueva_contraseña < 1000 or nueva_contraseña > 9999:
                print("La contraseña debe tener 4 digitos")
                return
        except ValueError:
            print("La contraseña debe ser numerica")
            return
        usuarios[posicion] = nuevo_usuario
        contraseñas[posicion] = nueva_contraseña
        print("Usuario modificado correctamente")
    else:
        print("Usuario no encontrado")
def eliminar_usuario():
    buscar = input("Usuario a eliminar: ").strip().lower()
    if buscar == "admin":
        print("No se puede eliminar el administrador")
        return
    if buscar in usuarios:
        posicion = usuarios.index(buscar)
        usuarios.pop(posicion)
        contraseñas.pop(posicion)
        print("Usuario eliminado correctamente")
    else:
        print("Usuario no encontrado")
def cerrar_sesion():
    print("Sesion cerrada correctamente...")
##Funciones para la cartelera....
def registrar_pelicula():
    nueva = input("Ingrese la pelicula: ").strip().lower()
    if nueva in peliculas:
        print("La pelicula ya existe")
        return
    peliculas.append(nueva)
    print("Pelicula registrada")
def mostrar_peliculas():
    if len(peliculas) == 0:
        print("No existen peliculas")
        return
    print("\n===== CARTELERA =====")
    for i in range(len(peliculas)):
        print(i + 1, "-", peliculas[i])
def buscar_pelicula():
    buscar = input("Pelicula a buscar: ").strip().lower()
    if buscar in peliculas:
        print("Pelicula encontrada")
    else:
        print("Pelicula no encontrada")
def modificar_pelicula():
    buscar = input("Pelicula a modificar: ").strip().lower()
    if buscar in peliculas:
        posicion = peliculas.index(buscar)
        nueva = input("Nuevo nombre: ").strip().lower()
        peliculas[posicion] = nueva
        print("Pelicula modificada")
    else:
        print("Pelicula no encontrada")
def eliminar_pelicula():
    buscar = input("Pelicula a eliminar: ").strip().lower()
    if buscar in peliculas:
        posicion = peliculas.index(buscar)
        peliculas.pop(posicion)
        print("Pelicula eliminada")
    else:
        print("Pelicula no encontrada")
    

# FUNCIONES USUARIO
precio_entrada = 30
factura = ""
def ver_cartelera():
    if len(peliculas) == 0:
        print("No hay peliculas registradas")
        return
    print("===== CARTELERA =====")
    for i in range(len(peliculas)):
        print(i + 1, "-", peliculas[i])
def consultar_pelicula():
    buscar = input("Ingrese la pelicula: ").strip().lower()
    if buscar in peliculas:
        print("Pelicula encontrada")
    else:
        print("Pelicula no encontrada")

def mostrar_precios():
    print("===== PRECIOS =====")
    print("Entrada:", precio_entrada, "Bs")
def comprar_entrada():
    
    global factura
    pelicula = input("Ingrese la pelicula: ").strip().lower()
    if pelicula not in peliculas:
        print("Pelicula no disponible")
        return
    try:
        cantidad = int(input("Cantidad de entradas: "))
    except ValueError:
        print("Ingrese solo numeros")
        return
    total = cantidad * precio_entrada
    factura = ("\n===== FACTURA =====\n"
        f"Pelicula: {pelicula}\n"
        f"Cantidad entradas: {cantidad}\n"
        f"Total a pagar: {total} Bs\n"
        f"Total Snack: {precio_snack} Bs\n")
    
    print("Compra realizada correctamente")
def mostrar_factura():
    global factura
    if factura == "":
        print("No existen compras registradas")
    else:
        print(factura)
        input("presione ENTER para continuar")