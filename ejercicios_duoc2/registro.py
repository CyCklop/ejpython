users = []
passwd = []
##CODIGO SIN TERMINAR
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
                        op2 = str(input("Ingresa tu nombre de usuario: "))
                        pas2 = input("Ingresa tu contraseña: ")
                        if op2 and pas2 in users or passwd:
                            print("Has iniciado sesión correctamente")
                            submenu()
                case 2:
                    user = str(input("Ingresa el nombre de tu usuario: "))
                    users.append(user)
                    passw = input("Ingresa una contraseña: ")
                    passwd.append(passw)
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
            op2 = int(input("1) Realizar llamada\n2) Enviar correo electrónico\n3) Cerrar sesión\n"))
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