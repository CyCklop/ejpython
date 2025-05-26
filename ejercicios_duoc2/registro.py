users = []
passwd = []

def main():
    global users, passwd
    while True:
        try:
            op = int(input("1) Iniciar sesión\n2) Registrar usuario\n3) Salir\n"))
            match op:
                case 1:
                    if not users:
                        print("No hay usuarios registrados, debes registrar uno")
                    else:
                        pass
                case 2:
                    user = str(input("Ingresa el nombre de tu usuario: "))
                    users.append(user)
                    print(users)
                    passw = input("Ingresa una contraseña: ")
                    passwd.append(passw)
                    print(passwd)
                case 3:
                    print("Saliendo..")
                    break
                case _:
                    print("Ingrese una opción correcta")
        except Exception:
            print("Error, ingrese un valor correcto")

def submenu():
    while True:
        try:
            op2 = int(input("1) Realizar llamada\n2) Enviar correo electrónico\n3) Cerrar sesión"))
            match op2:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    print("Volviendo...")
                    break
                case _:
                    print("Ingrese una opción correcta")
        except Exception:
            print("Error, ingrese un valor correcto")
main()