usuarios = ["anahi", "asoka", "liz","hasu" ,"admin"]
contraseñas = [7310, 8699, 1433, 1234,1234]
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
login()