import time
deuda = 100000

def main():
    global deuda
    print(f"BANCO NO ESTADO\nTu saldo actual es de: {deuda}")
    while True:
        try:
            op = int(input(f"Deuda actual: {deuda}\n1- Pagar deuda actual\n2- Comprar\n3- Salir\n"))
            match op:
                case 1:
                    valor = int(input("Ingrese el monto a pagar: "))
                    if valor>=deuda:
                        print("No puede exceder el total de su saldo")
                    elif valor<=deuda:
                        deuda-=valor
                        print(f"Has pagado {valor} de una deuda actual de {deuda} pesos")
                    else:
                        print("El valor ingresado debe ser mayor a 0")
                case 2:
                    print("Entrando a menú de compras...")
                    time.sleep(1)
                    compras()
                case 3:
                    print("Saliendo...")
                    break
                case _:
                    print("Ingresa un opción correcta")
        except Exception:
            print("Ingrese un valor númerico")

def compras():
    global deuda
    compra = 0
    while True:
        try:
            op2 = int(input("Ingresa la cantidad de objetos a comprar: "))
            if op2<=0:
                print("Debes ingresar un monto mayor a 0")
            else:
                for i in range(op2):
                    op3 = int(input(f"Cuanta cantidad del objeto {i+1} desea comprar?: "))
                    if op3<=0:
                        print("Debes ingresar un monto mayor a 0")
                    else:
                        compra+=op3
                deuda+=compra
                print("Volviendo...")
                time.sleep(1)
                break
        except Exception:
            print("Ingresa un valor númerico")
main()