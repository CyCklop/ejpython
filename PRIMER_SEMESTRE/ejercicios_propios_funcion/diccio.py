usuario = {
    1: {"nombre": "Josh Dun", "edad": 37, "casado": True}
}

def ingresar(diccio):
    lista_diccio = list(diccio.keys())[-1]
    print(lista_diccio)
    nom = input("Ingresa el nombre: ")
    age = int(input("Ingresa la edad: "))
    cas = int(input("¿Esta casado/a?\n1) No 2)Si\nSelecciona una opción: "))
    diccio[lista_diccio+1]={"nombre": nom, "edad": age, "casado": bool(cas-1)}

def update(diccio):
    for key,value in diccio.items():
        print(f"{key}-Nombre: {value["nombre"]} Edad: {value["edad"]} Casado: {value["casado"]}")
    op = int(input("Ingrese la llave del usuario a actualizar: "))
    if op in list(diccio.keys()):
        nom = input("Ingresa el nombre: ")
        age = int(input("Ingresa la edad: "))
        cas = int(input("¿Esta casado/a?\n1) No 2)Si\nSelecciona una opción: "))
        diccio[op]={"nombre": nom, "edad": age, "casado": bool(cas-1)}
    else:
        print(f"La llave {op} no existe..")

def show(diccio):
    for key,value in diccio.items():
        print(f"{key}-Nombre: {value["nombre"]} Edad: {value["edad"]} Casado: {value["casado"]}")

def pop(diccio):
    for key,value in diccio.items():
        print(f"{key}-Nombre: {value["nombre"]} Edad: {value["edad"]} Casado: {value["casado"]}")
    op = int(input("Ingrese la llave del usuario a eliminar: "))
    if op in list(diccio.keys()):
        diccio.pop(op)
        print(f"Se ha eliminado el usuario de la llave {op}")
    else:
        print(f"La llave {op} no existe..")

def main():
    while True:
        try:
            op = int(input("1) Agregar usuario\n2) Actualizar usuario\n3) Borrar usuario\n4) Mostrar usuario\n5) Salir\nSelecciona una opcion: "))
            match op:
                case 1:
                    ingresar(usuario)
                case 2:
                    update(usuario)
                case 3:
                    pop(usuario)
                case 4:
                    show(usuario)
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, Selecciona una opcion valida")
        except Exception:
            print("Error, ingresa un número")
main()
