usuarios = {}

def val_contra(contraseña):
    numeros = 0
    mayus = 0
    if len(contraseña) != 6:
        return False
    for c in contraseña:
        if c.isnumeric():
            numeros+=1
        elif c.isupper():
            mayus+=1
    if mayus != 1:
        return False
    if numeros != 2:
        return False
    return True


def crear(usuario):
    while True:
        nom = input("Ingresa el nombre de tu usuario: ")
        age = int(input("Ingresa tu edad: "))
        if age <= 12:
            print("¡Debes ser nayor de 12 años para crear un usuario!")
            continue
        contra = input("**Tu contraseña debe contener 2 números y 1 letra mayuscula y un maximo de 6 caracteres**\nCrea tu contraseña: ")
        if val_contra(contra):
            print(f"¡Has creado el usuario {nom}!")
            usuario[nom]  = {"edad": age, "contraseña": contra}
            break
        else:
            print("Error, verifica que tu contraseña contenga lo pedido")


def ver(usuario):
    print("La cantidad de usuarios en el sistema es de: ")
    for key,value in usuario.items():
        print(f"Usuario: {key} --- Edad: {value["edad"]} --- Contraseña: {value["contraseña"]}")

def borrar(usuario):
    op = input("Ingresa el nombre del usuario a borrar: ")
    if op in usuario.keys():
        usuario.pop(op)
        print(f"¡Se ha borrado el usuario {op}!")
    else:
        print(f"El usuario {op} no se encuentra en el sistema...")

def menu():
    while True:
        try:
            print("*****RED SOCIAL*****\n1) Crear usuario\n2) Ver lista de usuarios\n3) Eliminar Usuario\n4) Salir")
            op = int(input("Ingresa una opción: "))
            match op:
                case 1:
                    crear(usuarios)
                case 2:
                    ver(usuarios)
                case 3:
                    borrar(usuarios)
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, ingresa una opción válida")
        except Exception:
            print("Error, ingrese un dato correcto")
menu()