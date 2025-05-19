import time

def opcion():
    total = 0
    totventa= 0
    print("LAVADO DE AUTOS\n1- Cursar pago del lavado\n2- Ver ventas diarias\n3- Salir")
    while True:
        time.sleep(1)
        op = int(input())
        match op:
            case 1:
                print("MENU DE LAVADOS\n1- Lavado Full $15.000\n2- Standard $10.000\n3- Básico $7.000\n4- Volver al menú anterior")
                op2 = int(input())
                while op2!=4:
                    if op2 == 1:
                        print("Usted ha elegido el Lavado Full")
                        total+=15000
                        totventa+=1
                    elif op2 == 2:
                        print("Usted ha elegido el Lavado Standard")
                        total+=10000
                        totventa+=1
                    elif op2 == 3:
                        print("Usted ha elegido el Lavado Básico")
                        total+=7000
                        totventa+=1
            case 2:
                print(f"El total de las ventas diarias es de {totventa}")
            case 3:
                print("Saliendo del lavado...")
                break
            case _:
                print("Selecciona una opción valida")
opcion()