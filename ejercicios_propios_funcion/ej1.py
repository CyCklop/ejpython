def main():
    total = 0
    qui1 = int(input("Seleccione su quintil para el bono (1-5)\n"))
    match qui1:
        case 1:
            print("Su quintil es de menor ingreso, recibe bono de $60.000")
            total+=60000
            empleo()
        case 2:
            print("Su quintil es de bajo ingreso, recibe un bono de $60.000")
            total+=60000
            empleo()
        case 3:
            print("Su quintil es de mediano ingreso")
            empleo()
        case 4:
            print("Su quintil es de alto ingreso, no recibe bono")
            empleo()
        case 5:
            print("Su quintil es de maximo ingreso, no recibe bono")
            empleo()
        case _:
            print("Selecciona una opción correcta")

def empleo():
    qui2 = str(input("¿Usted es empleado o desempleado?\n"))
    if qui2.lower() == "empleado":
        print("Usted es empleado")
    elif qui2.lower() == "desempleado":
        print("Usted es desempleado")

def edad():
    age = int(input("Ingrese su edad\n"))
    if age>=65:
        print("Usted recibe un bono de $40.000 por bono de adulto mayor")
    else:
        print("Usted no recibe bono de adulto mayor")

main()