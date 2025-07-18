vehiculos = {}

def valipatente(patente):
    if len(patente) != 6:
        return False
    if " " in patente:
        return False
    if not patente.upper():
        return False
    numeros = 0
    caracteres = 0
    for c in patente:
        if c.isnumeric():
            numeros+=1
        else:
            caracteres+=1
    if numeros != 2 and caracteres != 4:
        return False
    return True

def ingresar(vehiculo):
    while True:
        marca = input("Ingresa la marca del vehiculo: ")
        año = input("Ingresa el año del vehiculo: ")
        if len(año) != 4:
            print("El año debe tener 4 digitos obligatoriamente")
            continue
        patente = input("Ingresa la patente de tu vehiculo: ")
        if valipatente(patente):
            print("Añadiendo vehiculo al parking...")
            vehiculo[patente]= {"marca": marca, "año": año}
            break
        else:
            print("Error, la patente debe contener (4 letras mayusculas y 2 números)")

def ver_vehi(vehiculo):
    for key,value in vehiculo.items():
        print(f"Patente: {key} --- Marca: {value["marca"]} --- Año: {value["año"]}")

def retirar(vehiculo):
    op = input("Ingrese la patente del vehiculo a retirar: ")
    if op in vehiculo.keys():
        print(f"Retirando vehiculo patente {op}")
        vehiculos.pop(op)
    else:
        print(f"El vehiculo patente {op}, no se encuentra en el parking...")


def menu():
    while True:
        try:
            print("***PARKING.PY***\n1) Ingresar Vehiculo\n2) Ver vehiculos\n3) Retirar Vehiculo\n4) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresar(vehiculos)
                case 2:
                    ver_vehi(vehiculos)
                case 3:
                    retirar(vehiculos)
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, ingresa una opción correcta")
        except Exception:
            print("Error, ingresa un valor númerico")
menu()