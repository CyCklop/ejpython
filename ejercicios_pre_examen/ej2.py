usuarios = {}

def validar(code):
    if len(code)!= 6:
        return False
    if " " in code:
        return False
    return True

def ingresar(diccio):
    while True:
        nom = input("Ingresa tu nombre: ")
        code = input("Ingresa tu codigo: ")
        if validar(code):
            diccio[nom] = {"codigo": code}
            print("¡Usuario y clave añadidos con exito!")
            break
        else:
            print("Clave invalida intente denuevo...")

def ver(diccio):
    print("La lista de usuarios en sistema es de:")
    for key,value in diccio.items():
        print(f"Usuario: {key} --- {value["codigo"]}")


def menu():
    while True:
        try:
            print("****TicketMas.PY****\n1) Ingresar usuario al sistema\n2) Ver Sistema\n3) Borrar Usuario\n4) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresar(usuarios)
                case 2:
                    ver(usuarios)
                case 3:
                    pass
                case 4:
                    print("Saliendo del sistema....")
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un dato valido")
menu()