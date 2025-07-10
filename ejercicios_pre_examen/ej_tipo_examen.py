autos = {
    'ABC123': ['Nissan', 2000, 'Gasolina', '1.7L']
}
stock = {
    'ABC123': [10, 6500000]
}



def ver(stock):
    print("Stock Disponible:")
    for key,value in stock.items():
        print(f"Modelo: {key} -- {value}")

def buscar(stock):
    pass

def actualizar(stock):
    pass

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
            ben = input("Ingrese que tipo de combustible usa: ")
            lit = input("Ingrese cuanta capacidad tiene el estanque: ")
            auto[pat] = [marca,año,ben,lit]
            print(f"¡Auto patente {pat} añadido al sistema!")
            break
        else:
            print("***Error, ingrese una patente valida (4 letras mayusculas y 2 números)***")

def menu():
    while True:
        try:
            print("1.- Ver Stock\n2.- Buscar precio más alto\n3.- Actualizar Stock\n4.- Borrar un Modelo\n5.- Actualizar Datos\n6.- Salir")
            op = int(input("Ingresa una opción: "))
            match op:
                case 1:
                    ver(stock)
                case 2:
                    pass
                case 3:
                    pass
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