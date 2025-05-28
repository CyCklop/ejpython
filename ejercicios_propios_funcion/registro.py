userpas = []

def main():
    global userpas
    while True:
        try:
            op = int(input("1) Iniciar Sesión\n2) Registrar Usuario\n3) Salir\n"))
            match op:
                case 1:
                    if len(userpas) == 0:
                        print("No hay usuarios creados, debes crear minimo 1")
                        continue 
                    elif len(userpas)>=1:
                        valiname = str(input("Escribe el nombre de un usuario: "))
                        valipass = input("Escribe la contraseña correspondiente al usuario: ")
                        for name,pasw in userpas:
                            if valiname == name and valipass == pasw:
                                print("Ingresando al sistema...")
                                submenu()
                case 2:
                    for i in range(3):
                        name = str(input(f"Crea tu nombre del usuario/a {i+1}: "))
                        pasw = input(f"Crea la contraseña del usuario {i+1}: ")
                        userpas.append([name,pasw])
                        print(userpas)
                case 3:
                    print("Saliendo..")
                    break
                case _:
                    print("Elija una opción valida")
        except Exception:
            print("Error, Ingrese un número")

def submenu():
    while True:
        try:
            op = int(input("1) Realizar llamada\n2) Enviar correo electrónico\n3) Cerrar Sesión\n"))
            match op:
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case _:
                    print("Elija una opción valida")
        except Exception:
            print("Error, Ingrese un número")
main()