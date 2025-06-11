import time
nota = []

def main():
    global nota
    while True:
        try:
            print("Programa manejo de notas\n1.- Ingresar nota\n2.- Borrar nota\n3.- Mostrar notas\n4.- Sacar promedio nota menor y mayor\n5.- Limpiar todas las notas\n6.- Salir")
            op = int(input())
            match op:
                case 1:
                    notas()
                case 2:
                    borrar()
                case 3:
                    show()
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

def borrar():
    global nota
    while True:
        try:
            borrar = int(input(f"Selecciona cual nota borrar de la lista {nota}: "))
            nota.remove(borrar)
            print("Nota borrada excitosamente..")
            time.sleep(1)
            break
        except Exception:
            print("Error, ingrese un valor númerico")

def notas():
    global nota
    while True:
        try:
            cant = int(input("Ingrese la cantidad de notas: "))
            for i in range(cant):
                notsa = int(input(f"Ingresa la nota {i+1}: "))
                nota.append(notsa)
                print("¡Nota agregada!")
            break
        except Exception:
            print("Error, ingrese un valor númerico")

def show():
    global nota
    while True:
        print(f"¡Tus notas son: {nota}!")
        break

main()