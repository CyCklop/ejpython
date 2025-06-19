# MEMORIZA TODOOOO ESTO O CAGASTE
users = {
    1: {"nombre": "Ignacio Flores","edad": 19,"numero":  [12345678],"trabajo": False},
    2: {"nombre": "Ignacio Flores","edad": 19,"numero":  [12345678],"trabajo": False},
    3: {"nombre": "Ignacio Flores","edad": 19,"numero":  [12345678],"trabajo": False}
}

def ingresar():
    largo_dic = list(users.keys())[-1]
    print(largo_dic)
    nom = input("Ingresa el nombre: ")
    age = int(input("Ingresa la edad: "))
    num = int(input("Ingresa el número telefonico: "))
    job = int(input("¿Usted trabaja?\n1) No\n2) Si\nSeleccione una opción: "))
    users[largo_dic+1]={"nombre": nom, "edad": age, "numero": [num], "trabajo": bool(job-1)}

def update():
    for key,value in users.items():
        print(f"{key}-{value["nombre"]}")
    op = int(input("Ingresa el número de usuario a actualizar: "))
    usuario = users[op]
    usuario["nombre"] = input("Ingresa el nombre: ")
    usuario["edad"] = int(input("Ingresa la edad: "))
    usuario["numero"] = int(input("Ingresa el número telefonico: "))
    usuario["trabajo"] = int(input("¿Usted trabaja?\n1) No\n2) Si\nSeleccione una opción: "))



def borrar():
    for key,value in users.items():
        print(f"{key}-{value["nombre"]}")
    op = int(input("Ingresa el numero del usuario a borrar: "))
    users.pop(op)
    print(f"Se ha borrado el usuario {op}")


def show():
    for key,value in users.items():
        print(f"{key}-{value}")



def main():
    while True:
        try:
            op = int(input("1) Ingresar usuario\n2) Actualizar usuario\n3) Borrar usuario\n4) Mostrar usuarios\n5) Salir\n"))
            match op:
                case 1:
                    ingresar()
                case 2:
                    update()
                case 3:
                    borrar()
                case 4:
                    show()
                case 5:
                    print("Saliendo..")
                    break
                case _:
                    print("Error ingresa una opción correcta")
        except Exception:
            print("Error, ingresa un número")
main()