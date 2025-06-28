perfiles = {}

def iniciar(perfil):
    nom = input("Ingrese el nombre de su perfil: ")
    pas = input("Ingrese su contraseña: ")
    if nom or pas not in perfil.items():
        print(f"El perfil {nom}, no esta creado o la contraseña es incorrecta")
    else:
        print("¡Se accedido correctamente!")

def registrar(perfil):
    nom = input("Ingrese un nombre de perfil: ")
    age = int(input("Ingrese su edad: "))
    pas = input("Ingrese su contraseña: ")
    perfil[nom]={"edad": age, "contraseña": pas}

def show(perfil):
    print("Los usuarios registrados son:")
    for key,value in perfil.items():
        print(f"Usuario: {key} -Edad: {value["edad"]} -Contraseña:{value["contraseña"]}")


def menu():
    while True:
        print(perfiles)
        try:
            print("Red Social.PY\n1) Iniciar Sesión\n2) Registrarse\n3) Ver usuarios registrados\n4) Salir del sistema")
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    iniciar(perfiles)
                case 2:
                    registrar(perfiles)
                case 3:
                    show(perfiles)
                case 4:
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un valor valido")
menu()