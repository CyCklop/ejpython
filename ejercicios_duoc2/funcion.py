import time

def suma():
    num = int(input("Seleccione el primer número: "))
    num2 = int(input("Seleccione el segundo número: "))
    print(f"El resultado de la suma es {num+num2}")

def resta():
    num = int(input("Seleccione el primer número: "))
    num2 = int(input("Seleccione el segundo número: "))
    print(f"El resultado de la suma es {num-num2}")

def mult():
    num = int(input("Seleccione el primer número: "))
    num2 = int(input("Seleccione el segundo número: "))
    print(f"El resultado de la suma es {num*num2}")

def div():
    try:
        num = int(input("Seleccione el primer número: "))
        num2 = int(input("Seleccione el segundo número: "))
        print(f"El resultado de la suma es {num/num2}")
    except ZeroDivisionError:
        return print("ERROR,no se puede dividir por cero")
        

def calcu():
    op = int(input("Seleccione una opcion\n1- Suma\n2- Resta\n3- Multiplicación\n4- Division\n5- Salir\n"))
    while True:
        match op:
            case 1:
                print("Usted ha elegido suma")
                suma()
            case 2:
                print("Usted ha elegido resta")
                resta()
            case 3:
                print("Usted ha elegido Multiplicacion")
                mult()
            case 4:
                print("Usted ha elegido Division")
                div()
            case 5 :
                print("Saliendo..")
                break
            case _:
                print("Opcion no valida")
                break
calcu()