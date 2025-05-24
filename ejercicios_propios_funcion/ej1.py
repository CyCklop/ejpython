total = 0

def main():
    global total
    qui1 = int(input("Seleccione su quintil para el bono (1-5)\n"))
    match qui1:
        case 1:
            print("Su quintil es de menor ingreso, recibe bono de $60.000")
            total+=60000
            empleo()
            edad()
        case 2:
            print("Su quintil es de bajo ingreso, recibe un bono de $60.000")
            total+=60000
            empleo()
            edad()
        case 3:
            print("Su quintil es de mediano ingreso")
            empleo()
            edad()
        case 4:
            print("Su quintil es de alto ingreso, no recibe bono")
            empleo()
            edad()
        case 5:
            print("Su quintil es de maximo ingreso, no recibe bono")
            empleo()
            edad()
        case _:
            print("Selecciona una opción correcta")

def empleo():
    global total
    qui2 = str(input("¿Usted es empleado o desempleado?\n"))
    if qui2.lower() == "empleado":
        print("Usted es empleado, recibe bono de trabajador $30.000")
        total+=30000
    elif qui2.lower() == "desempleado":
        print("Usted es desempleado")

def edad():
    global total
    age = int(input("Ingrese su edad\n"))
    if age>=65:
        print("Usted recibe un bono de $40.000 por bono de adulto mayor")
        total+=40000
    else:
        print("Usted no recibe bono de adulto mayor")

main()
print(f"El total de su bono es de {total}")