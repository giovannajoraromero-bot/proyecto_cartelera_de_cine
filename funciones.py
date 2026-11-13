usuarios = ["hasu", "liz", "asoka", "anahi",]
contraseñas = [2468, 1433, 8699, 7310]
administradores=["admin"]
contraseña_admin=[1234]
peliculas = ["toy story","llorona","chaplin"]
salas = [1, 2, 3]
horario_tarde = ["15:00", "16:00", "17:00"]
horario_noche = ["20:00", "21:00", "22:00"]
precio_snack=0
asientos_disponibles=[50,50,50,50,50,50,50]
from compra_snack import comprar_snack
def login():
    usuario = input("Usuario (escriba salir para terminar): ").strip().lower()
    if usuario== "salir":
        return "salir"
    try:
        contraseña = int(input("Contraseña de 4 digitos: "))
        if contraseña < 1000 or contraseña > 9999:
            print("La contraseña debe tener 4 dígitos")
            return "incorrecto"
    except ValueError:
        print("La contraseña debe ser numerica")
        return "incorrecto"
    for i in range(len(administradores)):
        if usuario == administradores[i] and contraseña == contraseña_admin[i]:
            print("Bienvenido Administrador")
            return "administrador"
    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas[i]:
            print("Bienvenido Usuario")
            return "usuario"
    print("Usuario o contraseña incorrectos")
    return "incorrecto"
def registrar_usuario():
    nuevo_usuario = input("Ingrese usuario: ").strip().lower()
    if nuevo_usuario in administradores or nuevo_usuario in usuarios:
        print("Usuario existente")
        return
    try:
        nueva_contraseña = int(input("Ingrese contraseña: "))
        if nueva_contraseña < 1000 or nueva_contraseña > 9999:
            print("La contraseña debe tener 4 digitos")
            return
    except ValueError:
        print("La contraseña debe ser numerica")
        return
    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)
    print("Usuario registrado correctamente")
    return
def registrar_administradores():
    nuevo_admin= input("Ingrese el usuario: ").strip().lower()
    if nuevo_admin in administradores or nuevo_admin in usuarios:
        print("Usuario existente")
        return
    try:
        nueva_contraseña = int(input("Ingrese contraseña: "))
        if nueva_contraseña < 1000 or nueva_contraseña > 9999:
            print("La contraseña debe tener 4 digitos")
            return
    except ValueError:
            print("La contraseña debe ser numerica")
            return
    administradores.append(nuevo_admin)
    contraseña_admin.append(nueva_contraseña)
    print("Administrador registrado correctamente")
    return
def mostrar_usuarios():
    if len(usuarios) == 0:
        print("No existen usuarios")
        return
    for i in range(len(usuarios)):
        print("----------------")
        print("Usuario:", usuarios[i])
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
    salas.append(max(salas) + 1)
    horario_tarde.append("15:00")
    horario_noche.append("20:00")
    asientos_disponibles.append(50)
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
        if nueva in peliculas:
            print("La pelicula ya existe")
            return
        peliculas[posicion] = nueva
        print("Pelicula modificada")
    else:
        print("Pelicula no encontrada")
def eliminar_pelicula():
    buscar = input("Pelicula a eliminar: ").strip().lower()
    if buscar in peliculas:
        posicion = peliculas.index(buscar)
        peliculas.pop(posicion)
        asientos_disponibles.pop(posicion)
        salas.pop(posicion)
        horario_tarde.pop(posicion)
        horario_noche.pop(posicion)
        print("Pelicula eliminada")
    else:
        print("Pelicula no encontrada")
precio_entrada = 30
factura = ""
def ver_cartelera():
    if len(peliculas) == 0:
        print("No hay peliculas registradas")
        return
    print("===== CARTELERA =====")
    for i in range(len(peliculas)):
        print(i + 1, "-", peliculas[i])
        print("Sala:", salas[i])
        print("Horario tarde:", horario_tarde[i])
        print("Horario noche:", horario_noche[i])
        print("Asientos disponibles:", asientos_disponibles[i])
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
    global precio_snack
    pelicula = input("Ingrese la pelicula: ").strip().lower()
    if pelicula not in peliculas:
        print("Pelicula no disponible")
        return
    posicion = peliculas.index(pelicula)
    print("\nHorarios disponibles")
    print("1.", horario_tarde[posicion])
    print("2.", horario_noche[posicion])
    opcion_horario = input("Seleccione horario: ")
    if opcion_horario == "1":
        horario = horario_tarde[posicion]
    elif opcion_horario == "2":
        horario = horario_noche[posicion]
    else:
        print("Horario invalido")
        return
    try:
        cantidad = int(input("Cantidad de entradas: "))
        if cantidad > asientos_disponibles[posicion]:
            print("No hay asientos disponibles")
            return
        elif cantidad<=0:
            print("Cantidad inválida")
            return
    except ValueError:
        print("Ingrese solo numeros")
        return
    total = cantidad * precio_entrada
    respuesta = input("\n¿Desea comprar snacks para acompañar su pelicula? (si/no): ").strip().lower()
    if respuesta == "si":
        precio_snack = comprar_snack()
        if precio_snack is None:
            return
    else:
        precio_snack = 0
    factura = (
        "\n===== FACTURA =====\n"
        f"Pelicula: {pelicula}\n"
        f"Sala: {salas[posicion]}\n"
        f"Horario: {horario}\n"
        f"Cantidad entradas: {cantidad}\n"
        f"Total entradas: {total} Bs\n"
        f"Total snack: {precio_snack} Bs\n"
        f"Total general: {total + precio_snack} Bs\n")
    asientos_disponibles[posicion] -=cantidad
    print("Compra realizada correctamente")
def mostrar_factura():
    global factura
    if factura == "":
        print("No existen compras registradas")
    else:
        print(factura)
        input("presione ENTER para continuar")