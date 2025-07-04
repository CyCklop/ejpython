usuarios = {}

def validar(code):
    if len(code)!= 6:
        return False
    if " " in code:
        return False
    if not code.isupper():
        return False
    return True

def ingresar(diccio):
    while True:
        nom = input("Ingresa tu nombre: ")
        area = input("Ingresa que area compraste (G/V): ")
        if area != "G" and area != "V":
            print("Selecciona un area valida (Incluyendo Mayusculas)")
            continue
        code = input("Ingresa tu codigo: ")
        if validar(code):
            diccio[nom] = {"codigo": code, "area": area}
            print("¡Usuario, area y clave añadidos con exito!")
            break
        else:
            print("Clave invalida intente denuevo...")

def ver(diccio):
    print("La lista de usuarios en sistema es de:")
    for key,value in diccio.items():
        print(f"Usuario: {key} --- Codigo: {value["codigo"]} --- Area: {value["area"]}")

def pop(diccio):
    op = input("Ingresa el nombre de usuario a borrar: ")
    if op in diccio.keys():
        diccio.pop(op)
        print(f"Has borrado el usuario {op}")
    else:
        print(f"El usuario {op} no se encuentra en el sistema...")

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
                    pop(usuarios)
                case 4:
                    print("Saliendo del sistema....")
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un dato valido")
menu()