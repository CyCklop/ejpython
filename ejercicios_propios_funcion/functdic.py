users = {
    1: {"nombre": "Ignacio Flores",
        "edad": 19,
        "numero":  [12345678],
        "trabajo": False},
    2: {"nombre": "Ignacio Flores",
        "edad": 19,
        "numero":  [12345678],
        "trabajo": False},
    3: {"nombre": "Ignacio Flores",
        "edad": 19,
        "numero":  [12345678],
        "trabajo": False}
}

def ingresar(diccio):
    nom = input("Ingresa el nombre: ")
    age = int(input("Ingresa la edad: "))
    num = int(input("Ingresa el número telefonico: "))
    job = int(input("¿Usted trabaja?\n1) Si\n2) No\nSeleccione una opción: "))
    if job == 1:
        diccio.insert(0,{"nombre": nom, "edad": age, "numero": ["numero"].append(num),"trabajo": True})
    else:
        diccio.insert(0,{"nombre": nom, "edad": age, "numero": ["numero"].append(num),"trabajo": False})


def update():
    pass
def borrar():
    pass
def show():
    pass



def main():
    global users
    while True:
        try:
            op = int(input("1) Ingresar usuario\n2) Actualizar usuario\n3) Borrar usuario\n4) Mostrar usuarios\n5) Salir\n"))
            match op:
                case 1:
                    ingresar(users)
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print("Saliendo..")
                    break
                case _:
                    print("Error ingresa una opción correcta")
        except Exception:
            print("Error, ingresa un número")
main()