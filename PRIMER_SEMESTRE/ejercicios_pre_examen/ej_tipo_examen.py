autos = {}
stock = {}


def ver(stock):
    print("Stock Disponible:")
    for key,value in stock.items():
        print(f"Modelo: {key} -- Unidades: {value[0]} --- Valor por unidad: {value[1]}")

def buscar(stock):
    pass

def actualizar(stock):
    while True:
        pat = input("Ingrese la patente del vehiculo: ")
        if verificar_patente(pat):
            input_stock = input("Ingrese el stock del vehiculo: ")
            try:
                stock_auto,precio_auto = stock[pat]
                if input_stock == stock_auto:
                    print("***No se puede ingresar un número de stock existente***\nEscriba un stock valido: ")
                    continue
                stock[pat][0] = input_stock
            except KeyError:
                precio = input("***No existe stock para esta patente, ingrese el precio: ")
                stock[pat] = [input_stock,precio]
            print(f"Has agregado el stock y precio del vehiculo: {pat}")
            break
        else:
            print("***Error, ingrese una patente valida (4 letras mayusculas y 2 números)***")

def borrar(auto,stock):
    pass

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
    elif letras != 4:
        return False
    return True


def actualizar_datos(auto):
    while True:
        pat = input("Ingrese la patente del vehiculo: ")
        if verificar_patente(pat):
            marca = input("Ingresa la marca del vehiculo: ")
            año = input("Ingresa el año del vehiculo: ")
            if len(año) != 4:
                print("***Error, ingrese un año valido***")
                continue
            com = input("Ingrese que tipo de combustible usa: ")
            lit = input("Ingrese cuanta capacidad tiene el estanque: ")
            auto[pat] = [marca,año,com,lit]
            print(f"¡Auto patente {pat} añadido al sistema!")
            break
        else:
            print("***Error, ingrese una patente valida (4 letras mayusculas y 2 números)***")

def menu():
    while True:
        print(autos)
        print(stock)
        try:
            print("1.- Ver Stock\n2.- Buscar precio más alto\n3.- Actualizar Stock\n4.- Borrar un Modelo\n5.- Actualizar Datos\n6.- Salir")
            op = int(input("Ingresa una opción: "))
            match op:
                case 1:
                    ver(stock)
                case 2:
                    pass
                case 3:
                    actualizar(stock)
                case 4:
                    pass
                case 5:
                    actualizar_datos(autos)
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("***Error, ingrese una opción válida***")
        except Exception:
            print("***Error, ingrese un dato válido***")
menu()