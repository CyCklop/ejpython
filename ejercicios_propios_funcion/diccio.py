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

def show(diccio):
    for key,value in diccio.items():
        print(f"{key}-{value["nombre"]}")




def main():
    while True:
        try:
            op = int(input("1) Agregar usuario\n2) Actualizar usuario\n3) Borrar usuario\n4) Mostrar usuario\n5) Salir\nSelecciona una opcion: "))
            match op:
                case 1:
                    ingresar(usuario)
                case 2:
                    pass
                case 3:
                    pass
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
