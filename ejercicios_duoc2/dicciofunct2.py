personas = {
    1: {"nombre": "Ignacio Flores",
        "numero": [12345678],
        "edad": 19,
        "trabajo": False},
    2: {"nombre": "default",
        "numero": [0],
        "edad": 19,
        "trabajo": False},
    3: {"nombre": "Ignacio Flores",
        "numero": [12345678],
        "edad": 19,
        "trabajo": False}
},


def ingresar(diccio):
    nom = input("Ingresa el nombre de un usuario: ")
    num = int(input("Ingresa el número de telefono del usuario"))
    age = int(input("Ingresa la edad del usuario: "))
    job = input("¿Usted trabaja?: ")
    diccio.insert(0,{"nombre": nom, "numero": num, "edad": age, "trabajo": job})

def mostrar(diccio):
    for i in enumerate(diccio):
        print(i+1)

def borrar():
    pass


def main():
    while True:
        try:
            print("1) Ingresar perfil\n2) Mostrar perfiles\n3) Borrar perfil\n4) Salir")
            op = int(input(""))
            match op:
                case 1:
                    ingresar(personas)
                case 2:
                    mostrar(personas)
                case 3:
                    pass
                case 4:
                    pass
                case _:
                    print("Saliendo...")
                    break
        except Exception:
            print("Error, ingrese un valor valido")
main(personas)