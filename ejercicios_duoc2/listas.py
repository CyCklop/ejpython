nombre = []
apelli = []
while True:
    print("1- Ingresar un nombre\n2- Mostrar nombres y apellidos\n3- Buscar nombre\n4- Salir")
    op = int(input())
    match op:
        case 1:
            nom = input("Ingrese su nombre: ")
            nombre.append(nom)
            ape = input("Ingrese su apellido: ")
            apelli.append(ape)
        case 2:
            c = 0
            for i in nombre:
                print(nombre[c], apelli[c])
                c+=1
        case 3:
            busca = input("Indique que nombre buscar: ")
            if busca in nombre:
                print(f"el nombre {busca} esta en la lista")
            else:
                print(f"el nombre {busca} no se encuentra en la lista")
        case 4:
            print("Saliendo..")
            break
        case _:
            print("Error, Seleccione una opción valida")