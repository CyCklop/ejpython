vehiculos = {}
stock = {}

def validación_patente(patente):
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

def ingresar_vehiculo(auto):
    while True:
        patente = input("Ingrese la patente del vehiculo: ")
        if validación_patente(patente):
            marca = input("Ingrese la marca del vehiculo: ")
            año = input("Ingrese el año del vehiculo: ")
            if len(año) != 4:
                print("***Error, ingrese un año válido***")
                continue
            capacidad = float(input("Ingrese la capacidad del estanque: "))
            auto[patente] = [marca,año,capacidad]
            print(f"¡Vehiculo marca {marca} añadido exitosamente!")
            break
        else:
            print("***Error, ingrese una patente válida (4 Letras mayusculas y 2 números)***")

def ingresar_stock(stock):
    while True:
        patente = input("Ingrese la patente del vehiculo: ")
        if validación_patente(patente):
            input_stock = int(input(f"Ingrese el stock disponible para el vehiculo {patente}: "))
            try:
                stock_auto,precio_auto = stock[patente]
                if input_stock == stock_auto:
                    print(f"El vehiculo {patente} no puede tener el mismo stock...")
                    continue
                stock[patente][0] = input_stock
            except KeyError:
                print(f"¡Se ha agregado o actualizado el stock del vehiculo {patente}!")
                input_precio = int(input(f"Ingrese el precio del vehiculo {patente}: "))
                stock[patente] = [input_stock,input_precio]
            print("¡Stock añadido correctamente!")
            break
        else:
            print("Error, ingrese una patente válida (4 Letras mayusculas y 2 números)")

def borrar_patente(auto,stock):
    while True:
        patente = input("Ingrese la patente a eliminar: ")
        if validación_patente(patente):
            if patente in auto:
                del auto[patente]
            if patente in stock:
                del stock[patente]
                print(f"Se ha eliminado los datos de la patente {patente} del sistema...")
                break
        else:
            print("Error, ingrese una patente válida (4 Letras mayusculas y 2 números)")

def lista_stock(stock):
    print("El Stock disponible de vehiculos es de:")
    for key,value in stock.items():
        print(f"Patente: {key} --- Stock: {value[0]} --- Precio c/u: {value[1]}")

def menu():
    while True:
        try:
            print("1) Ingresar un vehiculo\n2) Ingresar Stock\n3) Borrar una patente\n4) Lista de stock\n5) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresar_vehiculo(vehiculos)
                case 2:
                    ingresar_stock(stock)
                case 3:
                    borrar_patente(vehiculos,stock)
                case 4:
                    lista_stock(stock)
                case 5:
                    print("Saliendo del sistema...")
                    break
                case _:
                    print("***Error, ingrese una opción válida***")
        except Exception:
            print("***Error, ingrese un tipo de dato válido***")
menu()