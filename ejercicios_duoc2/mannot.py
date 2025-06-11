nota = []

def main():
    global nota
    while True:
        try:
            print("Programa manejo de notas\n1.- Ingresar nota\n2.- Borrar nota\n3.- Mostrar notas\n4.- Sacar promedio nota menor y mayor\n5.- Limpiar todas las notas\n6.- Salir")
            op = int(input())
            match op:
                case 1:
                    nota()
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, seleccione una opción valida")
        except Exception:
            print("Error, ingrese un valor númerico")


def nota():
    global nota
    while True:
        try:
            cant = int(input("Ingrese la cantidad de notas: "))
            for i in range(cant):
                notsa = int(input(f"Ingresa la nota {i+1}: "))
                nota.append(notsa)
            print(nota)
        except Exception:
            print("Error, ingrese un valor númerico")
main()