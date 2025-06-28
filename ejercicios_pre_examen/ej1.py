entradas = {}

def añadir(diccio):
    nom = input("Ingrese el nombre del comprador: ")
    age = int(input("Ingrese la edad: "))
    code = input("Ingrese el codigo verificador: ")
    diccio[nom]={"edad": age, "codigo": code}

def menu():
    while True:
        print(entradas)
        try:
            print("***TICKETMASPY***\n1) Comprar Entrada\n2) Buscar comprador\n3) Borrar Compra\n4) Salir")
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    añadir(entradas)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un dato válido")
menu()