autos = {
    1: {"marca": "Nissan", "Año": 2000, "Patente": "wdrt23"}
}


def ingresar(diccio):
    lista_vehiculo = list(diccio.keys())[-1]
    mar = str(input("Ingrese la marca del vehiculo: "))
    year = int(input("Ingrese el año del vehiculo (MAXIMO 4 CARACTERES): "))
    pat = input("Ingrese la patente del vehiculo: ")
    diccio[lista_vehiculo+1] = {"marca": mar, "año": year, "patente": pat}

def ver(diccio):
    print("Los vehiculos estacionados son: ")
    for key,value in diccio.items():
        print(f"{key}. {value["marca"]} Año {value["Año"]} Patente {value["Patente"]}")

def sacar(diccio):
    op = input("Seleccione el número del vehiculo a sacar: ")
    if op in diccio.items():
        print(f"¡Has sacado el vehiculo {op}!")
        diccio.pop(op)
    else:
        print(f"El vehiculo {op} no se encuentra en el parking...")


def menu():
    while True:
        try:
            print("****Parking Py*****\n1) Ingresar vehiculo\n2) Ver vehiculos\n3) Sacar vehiculo\n4) Salir")
            op = int(input("Seleccione una opción: "))
            match op:
                case 1:
                    ingresar(autos)
                case 2:
                    ver(autos)
                case 3:
                    sacar(autos)
                case 4:
                    print("Saliendo del menú principal...")
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un valor númerico")
menu()