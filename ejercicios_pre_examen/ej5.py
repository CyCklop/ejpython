autos = {}
stock = {}

def verificar_patente(patente):
    if len(patente) != 6:
        return False
    if " " in patente:
        return False
    if not patente.isupper():
        return False
    numeros = 0
    letras = 0
    for c in patente:
        if c.isnumeric():
            numeros+=1
        else:
            letras+=1
    if numeros != 2:
        return False
    if letras != 4:
        return False
    return True

def agregar_vehiculo(auto):
    while True:
        try:
            patente = input("Ingresa la patente del vehiculo: ")
            if verificar_patente(patente):
                marca = input("Ingresa la marca del vehiculo: ")
                año = input("Ingresa el año del vehiculo: ")
                if len(año) != 4:
                    print("***Error, ingrese un año valido***")
                    continue
                gas = input("Ingresa el tipo de combustible: ")
                capacidad = input("Ingresa la capacidad del estanque: ")
                auto[patente] = [marca,año,gas,capacidad]
                print(f"Has añadido el vehiculo patente {patente}")
                break
            else:
                print("***Error, ingresa una patente valida (4 Letras Mayusculas y 2 Numeros)***")
        except Exception:
            print("***Error, ingresa un tipo de dato valido***")

def agregar_stock(stock):
    while True:
        patente = input("Ingresa la patente del vehiculo: ")
        if verificar_patente(patente):
            input_stock = input("Ingresa el stock del vehiculo: ")
            try:
                input_stock,input_precio = stock[patente]
                stock[patente][0] = input_stock
            except KeyError:
                input_stock = input("***No existe un stock para este vehiculo, ingrese uno: ")
                stock[patente] = [input_stock,input_precio]
            input_precio = int(input("ingresa el precio del vehiculo"))
            stock[patente] = [input_stock,input_precio]
            print(f"Has agregado stock y precio al vehiculo patente {patente}")
            break
        else:
            print("***Error, ingresa una patente valida (4 Letras Mayusculas y 2 Numeros)***")


def mostrar_stock(stock):
    print("La lista de stock disponible es de: ")
    for key,value in stock.items():
        print(f"Patente: {key} --- Stock: {value[0]} --- Precio: {value[1]}")

def menu():
    while True:
        print(autos)
        print(stock)
        try:
            print("1) Agregar vehiculo\n2) Agregar Stock\n3) Borrar Vehiculo/Stock\n4) Buscar Precio Más Alto\n5) Mostrar Stock\n6) Salir")
            op = int(input("Ingresa una opción: "))
            match op:
                case 1:
                    agregar_vehiculo(autos)
                case 2:
                    agregar_stock(stock)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    mostrar_stock(stock)
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("***Error, ingresa una opción valida***")
        except Exception:
            print("***Error, ingresa un tipo de dato valido***")
menu()