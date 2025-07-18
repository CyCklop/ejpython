import time 

print("¡Bienvenido a Pystore!")
name = str(input("Escribe tu nombre: "))


def product():
    time.sleep(1)
    print("Lista de productos\n1- Lavadora $35.000\n2- Guitarra $380.000\n3- Parlante $25.000\n4- Amplificador $65.000\n5- Recibir boleta")

def carrito():
    total = 0
    while True:
        try:
            product()
            time.sleep(1)
            op = int(input())
            match op:
                case 1:
                    print("Has comprado una lavadora")
                    total+=35000
                    print(f"Su subtotal es de {total}")
                case 2:
                    print("Has comprado una guitarra")
                    total+=380000
                    print(f"Su subtotal es de {total}")
                case 3:
                    print("Has comprado un parlante")
                    total+=25000
                    print(f"Su subtotal es de {total}")
                case 4:
                    print("Has comprado un amplificador")
                    total+=65000
                    print(f"Su subtotal es de {total}")
                case 5:
                    time.sleep(1)
                    print(f"¡Gracias por comprar en Pystore {name}!, su total neto es de {total}")
                    print(f"¡Gracias por comprar en Pystore {name}!, su total más IVA es de {total*1.19}")
                    break
                case _:
                    print("Selecciona una opcion valida")
        except Exception:
            print("Escribe un número")
carrito()