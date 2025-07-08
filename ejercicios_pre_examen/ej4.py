users = {}

def numer(numero):
    if len(numero) > 11:
        return False
    if " " in numero:
        return False
    for c in numero:
        if numero.isnumeric():
            pass
        else:
            return False
    return True

def ingresar(usuario):
    while True:
        nom = input("Ingresa un nombre: ")
        age = int(input("Ingresa tu edad: "))
        if age <= 12:
            print("***Debes ser mayor de 12 años para ingresar***")
            continue
        num = input("Ingresa un número de telefono: ")
        if numer(num):
            usuario[nom] = {"edad": age, "numero": [num]}
            print(f"***Usuario {nom} Agregado Al Sistema***")
            break
        else:
            print("***Error, ingrese un número válido y sin espacios en blanco***")

def eliminar(usuario):
    user = input("Ingresa el nombre del usuario a eliminar: ")
    if user in usuario.keys():
        print(f"Eliminando usuario {user} ...")
        usuario.pop(user)
    else:
        print(f"El usuario {user}, no esta en el sistema...")

def ver(usuario):
    print("La lista de usuarios en el sistema es de:")
    for key,value in usuario.items():
        print(f"Usuario: {key} --- Edad: {value["edad"]} --- Numeros de contacto: {value["numero"]}")

def menu():
    while True:
        try:
            print("*****Ejemplo 4*****\n1) Ingresar usuario\n2) Eliminar usuario\n3) Ver usuarios\n4) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresar(users)
                case 2:
                    eliminar(users)
                case 3:
                    ver(users)
                case 4:
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Error, ingrese una opción válida")
        except Exception:
            print("Error, ingrese un tipo de dato correcto")
menu()