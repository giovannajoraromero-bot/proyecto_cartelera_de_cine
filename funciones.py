usuarios=["hasu","liz","asoka","anahi","admin"]
contraseñas=[2468,1433,8699,7310,1234]
peliculas=["Toy story","llorona","Claplin","Alicia y el pais de las maravillas","miky mouse","scream"]
##Funciones para control de usuarios
def login():
    usuario = input("Ingrese su usuario: ").strip().lower()
    try:
        contraseña = int(input("Ingrese la contraseña de cuatro dígitos: "))
        if contraseña < 1000 or contraseña > 9999:
            print("La contraseña debe tener cuatro dígitos")
            return "incorrecto"
    except ValueError:
        print("La contraseña debe ser numérica")
        return "incorrecto"
    for i in range(len(usuarios)):
        if usuario == usuarios[i] and contraseña == contraseñas[i]:
            if usuario == "admin":
                print("--- Acceso concedido ---")
                print("Bienvenido como administrador")
                return "administrador"
            else:
                print("--- Acceso concedido ---")
                print("Bienvenido como usuario")
                return "usuario"
    print("Contraseña o usuario incorrecto")
    return "incorrecto"
##Falta verificacion de usuario existente...
def registrar_usuario():
    nuevo_usuario = input("Ingrese el usuario nuevo: ").strip().lower()
    if nuevo_usuario in usuarios:
        print("El usuario ya existe")
        return
    try:
        nueva_contraseña = int(input("Ingrese la contraseña de cuatro dígitos: "))
        if nueva_contraseña < 1000 or nueva_contraseña > 9999:
            print("La contraseña debe tener cuatro dígitos")
            return
    except ValueError:
        print("La contraseña debe ser numérica")
        return
    usuarios.append(nuevo_usuario)
    contraseñas.append(nueva_contraseña)
    print("Nuevo usuario registrado exitosamente...")
def mostrar_usuarios():
    print("--- USUARIOS REGISTRADOS ---")
    for i in range(len(usuarios)):
        print("Usuario:", usuarios[i])
        print("Contraseña:", contraseñas[i])
def buscar_usuario():
    buscar_u=input("Ingrese el nombre de usuario que desea buscar: ").strip().lower()
    if buscar_u in usuarios:
        posicion=usuarios.index(buscar_u)
        print(f"Usuario: ",usuarios[posicion])
        print("Contraseña: ",contraseñas[posicion])
    else:
        print("Usuario no encontrado...")
def modificar_usuario():
    buscar_u = input("Ingrese el usuario que desea modificar: ").strip().lower()
    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)
        nuevo_usuario = input("Ingrese el nuevo usuario: ").strip().lower()
        try:
            nueva_contraseña = int(input("Ingrese la nueva contraseña de cuatro dígitos: "))
            if nueva_contraseña < 1000 or nueva_contraseña > 9999:
                print("La contraseña debe tener cuatro dígitos")
                return
        except ValueError:
            print("La contraseña debe ser numérica")
            return
        usuarios[posicion] = nuevo_usuario
        contraseñas[posicion] = nueva_contraseña
        print("Usuario modificado correctamente...")
    else:
        print("Usuario no encontrado...")
def eliminar_usuario():
    buscar_u = input("Ingrese el usuario que desea eliminar: ").strip().lower()
    if buscar_u in usuarios:
        posicion = usuarios.index(buscar_u)
        usuarios.pop(posicion)
        contraseñas.pop(posicion)
        print("Usuario eliminado correctamente...")
    else:
        print("Usuario no encontrado...")
def cerrar_sesion():
    print("Sesión cerrada correctamente...")
##Funciones para la cartelera....
def registrar_pelicula():
    nueva_pelicula=input("Ingrese el nombre de la nueva película: ").strip().lower()
    if nueva_pelicula not in peliculas:
        print("Película agregada exitosamente..")
        peliculas.append(nueva_pelicula)
        return
    else:
        print("La película ya existe...")
def consultar_pelicula():
    buscar_p=input("Ingrese la película que desea buscar:").strip().lower()
    if buscar_p in peliculas:
        buscar=peliculas.index(buscar_p)
        print("Película encontrada...")
def modificar_pelicula():
    buscar_pelicula=input("Ingrese la pelicula que desea modificar: ").strip().lower()
    if buscar_pelicula in peliculas:
        posicion=peliculas.index(buscar_pelicula)
        nueva_pelicula=input("Ingrese el nombre de la nueva película: ").strip().lower()
        peliculas[posicion]=nueva_pelicula
        print("Pelicula modificada correctamente...")
    else:
        print("Película no encontrada...")
def eliminar_pelicula():
    buscar_pelicula=input("Ingrese el nombre de la película que desea eliminar: ").strip().lower()
    if buscar_pelicula in peliculas:
        posicion=peliculas.index[buscar_pelicula]
        peliculas.pop[posicion]
        print("Película eliminada correctamente....")
    else:
        print("Película no encontrada...")
    ##Funciones de horario, salas