personas = {}
registro = {}

def validar_rut(rut):
    if len(rut) != 10:
        return False
    if " " in rut:
        return False
    numeros = 0
    caracter = 0
    for c in rut:
        if c.isnumeric():
            numeros+=1
        else:
            caracter+=1
    if numeros != 9:
        return False
    if caracter != 1:
        return False
    return True

def ingresar_datos(persona,registro):
    while True:
        rut = input("Ingrese su RUT (Sin puntos y con guión): ")
        if validar_rut(rut):
            if rut in persona.keys():
                print("**Error, no puedes ingresar un RUT ya existente en el sistema**")
                continue
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            comuna = input("Ingrese su comuna: ")
            sueldo = int(input("ingrese su sueldo: "))
            persona[rut] = {"nombre": nombre, "edad": edad}
            registro[rut] = {"comuna": comuna, "sueldo": sueldo}
            print("¡Ha ingresado excitosamente sus datos en el sistema!")
            break
        else:
            print("**Error, ingrese un RUT válido**")


def ver_lista(registro):
    if not registro:
        print("**Error, no existen datos en el sistema para mostrar**")
    else:
        print("--Lista actual del sistema--")
        for key,value in registro.items():
            print(f"RUT: {key} --- Comuna: {value["comuna"]} --- Sueldo: ${value["sueldo"]}")

def borrar_datos(personas,registro):
    while True:
        rut = input("Ingrese el RUT a borrar sus datos: ")
        if validar_rut(rut):
            if rut in personas and rut in registro:
                del personas[rut]
                del registro[rut]
                print(f"¡Se ha eliminado el RUT: {rut} de todo el sistema!")
                break
            else:
                print(f"**Error, el rut: {rut} no se encuentra registrado en ninguna parte del sistema...**")
        else:
            print("**Error, ingrese un RUT válido**")

#parte con ayuda de chatgpt
def buscar_mayor_sueldo(registro):
    if not registro:
        print("**Error, no existen datos en el sistema para buscar**")
        return
    mayor_sueldo = -1
    mayor_rut = ""
    for rut in registro:
        sueldo = registro[rut]["sueldo"]
        if sueldo > mayor_sueldo:
            mayor_sueldo = sueldo
            mayor_rut = rut
    print(f"El RUT con el mayor sueldo es: {mayor_rut} --- Comuna: {registro[mayor_rut]['comuna']} --- Sueldo: ${mayor_sueldo}")


def menu():
    while True:
        try:
            print("--Registro Social--\n1) Ingrese sus datos\n2) Ver lista del registro social\n3) Borrar datos\n4) Buscar mayor sueldo\n5) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    ingresar_datos(personas,registro)
                case 2:
                    ver_lista(registro)
                case 3:
                    borrar_datos(personas,registro)
                case 4:
                    buscar_mayor_sueldo(registro)
                case 5:
                    print("Saliendo del registro social de hogares...")
                    break
                case _:
                    print("**Error, ingrese una opción válida...**")
        except Exception:
            print("**Error, ingrese un tipo de dato válido..**")
menu()