juegos = {}
ventas = {}

def validar_codigo(codigo):
    if len(codigo) != 7:
        return False
    if " " in codigo:
        return False
    if not codigo.isupper():
        return False
    numeros = 0
    letras = 0
    for c in codigo:
        if c.isnumeric():
            numeros+=1
        else:
            letras+=1
    if numeros != 3:
        return False
    if letras != 4:
        return False
    return True

def ingresar_datos(juego,ventas):
    while True:
        codigo = input("Ingresa el codigo de licencia del videojuego (4 LETRAS MAYUSCULAS Y 3 NUMEROS): ")
        if codigo in juego.keys():
            print(f"//Error, el juego codigo {codigo} ya esta en el sistema, ingresa otro codigo//")
            continue
        if validar_codigo(codigo):
            nombre = input("Ingresa el nombre del videojuego: ")
            developer = input("Ingresa el nombre del grupo desarrollador del videojuego: ")
            presupuesto = int(input("Ingresa el presupuesto del videojuego: "))
            input_ventas = int(input("Ingresa las ventas del videojuego: "))
            juego[codigo] = {"nombre": nombre, "developer": developer,}
            ventas[codigo] = {"presupuesto": presupuesto, "ventas": input_ventas}
            print(f"¡Videojuego {nombre} agregado al sistema con exito!")
            break
        else:
            print("//Error, ingresa un codigo válido//")


def ver_lista(ventas):
    if not ventas:
        print("//Error, no hay datos de ventas en el sistema//")
        return
    else:
        print("--Lista de ventas--")
        for key,value in ventas.items():
            print(f"Codigo: {key} --- Presupuesto: ${value["presupuesto"]} --- Ventas: {value["ventas"]}")

def eliminar_datos(juego,ventas):
    if not ventas and not juego:
        print("//Error, no hay datos para eliminar en el sistema//")
        return
    else:
        codigo = input("Ingrese el codigo del videojuego a borrar: ")
        if validar_codigo(codigo):
            if codigo in juego and codigo in ventas:
                del juego[codigo]
                del ventas[codigo]
            else:
                print(f"//Error, el codigo {codigo} no se encuentra en los datos del sistema//")
        else:
            print("//Error, ingresa un codigo válido//")

def buscar_jg_exitoso(ventas):
    if not ventas:
        print("//Error, no hay datos de ventas en el sistema//")
        return
    mayor_venta = -1
    mayor_codigo = ""
    for codigo in ventas:
        venta = ventas[codigo]["ventas"]
        if venta > mayor_venta:
            mayor_venta = venta
            mayor_codigo = codigo
    print(f"--El juego con mayor ventas es--\nCodigo: {mayor_codigo} --- Ventas: {mayor_venta}")

def menu():
    while True:
        try:
            print("--GAMESTOP--\n1) Ingresa datos de un juego\n2) Ver lista de ventas\n3) Eliminar datos de un juego\n4) Buscar juego más exitoso\n5) Salir")
            op = int(input("Ingresa una opción: "))
            match op:
                case 1:
                    ingresar_datos(juegos,ventas)
                case 2:
                    ver_lista(ventas)
                case 3:
                    eliminar_datos(juegos,ventas)
                case 4:
                    buscar_jg_exitoso(ventas)
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("//Error, ingresa una opción válida//")
        except Exception:
            print("//Error, ingresa un tipo de dato válido//")
menu()