personas = {
    1: {"nombre": "Ignacio Flores",
        "numero": [12345678],
        "edad": 19,
        "trabajo": True},
    2: {"nombre": "default",
        "numero": [0],
        "edad": 19,
        "trabajo": True},
    3: {"nombre": "Ignacio Flores",
        "numero": [12345678],
        "edad": 19,
        "trabajo": True}
},


def ingresar(diccio):
    nom = input("Ingresa el nombre de un usuario: ")
    num = int(input("Ingresa el número de telefono del usuario"))
    age = int(input("Ingresa la edad del usuario: "))
    diccio.insert(0,{"nombre": nom, "numero": num, "edad": age})

def mostrar(diccio):
    for i in enumerate(diccio):
        print(i+1)

def borrar():
    pass


def main(diccio):
    while True:
        try:
            print("1) Ingresar perfil\n2) Mostrar perfiles\n3) Actualizar persona\n4) Borrar perfil\n5) Salir")
            op = int(input(""))
            match op:
                case 1:
                    ingresar(diccio)
                case 2:
                    mostrar(diccio)
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, seleccione una opción valida")
        except Exception:
            print("Error, ingrese un valor valido")
main(personas)