usuarios = ["hasu", "liz", "asoka", "anahi", "admin"]
contraseñas = [2468, 1433, 8699, 7310, 1234]
def login():
    usuario = input("Usuario: ").strip().lower()
    try:
        contraseña = int(input("Contraseña de 4 dígitos: "))
        if contraseña < 1000 or contraseña > 9999:
            print("La contraseña debe tener 4 dígitos")
            return "incorrecto"
    except ValueError:
        print("La contraseña debe ser numérica")
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
login()