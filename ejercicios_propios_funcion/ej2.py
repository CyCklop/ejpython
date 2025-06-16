import time
notas = []
def main():
    global notas
    while True:
        try:
            op = int(input("1- Ingresar nota\n2- Borrar nota\n3- Ver notas\n4- Sacar promedio\n5- Salir\n"))
            match op:
                case 1:
                    cant = int(input("Ingrese la cantidad de notas: "))
                    for i in range(cant):
                        op = float(input(f"Ingrese la nota {i+1}: "))
                        notas.append(op)
                case 2:
                    borrar = float(input("Ingrese la nota a borrar: "))
                    if borrar in notas:
                        notas.remove(borrar)
                        print(f"Has borrado la nota {borrar}")
                    else:
                        print(f"La nota {borrar} no se encuentra en la lista")
                case 3:
                    print(f"Las notas actuales son: {notas}")
                case 4:
                    resultado = sum(notas)/cant
                    reresultado = round(resultado)
                    print(f"El promedio es de: {reresultado}")
                case 5:
                    print("Saliendo...")
                    time.sleep(1)
                    break
                case _:
                    print("Error, ingrese una opción valida")
        except Exception:
            print("Error, ingrese un dato númerico")
main()