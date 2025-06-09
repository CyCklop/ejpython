product = []
precio = []
def main():
    global product,precio
    while True:
        try:
            op = int(input("1- Agregar Productos\n2- Comprar\n3- Crear Boleta\n4- Salir\n"))
            match op:
                case 1:
                    prona = input("Ingresa el nombre del producto: ")
                    product.append(prona)
                    propre = int(input("Ingresa el precio del producto: "))
                    precio.append(propre)
                case 2:
                    submenu()
                case 3:
                    boleta()
                case 4:
                    print("Saliendo..")
                    break
                case _:
                    print("Error, Elija una opción válida")
        except Exception:
            print("Debes ingresar un valor númerico")

def submenu():
    global product,precio
    while True:
        try:
            print(f"Lista de productos\n1- {product} ${precio}")
            op = int(input("Seleccione cual producto comprar: "))
            match op:
                case 1:
                    pass
                case 2:
                    pass
        except Exception:
            print("Ingrese un valor númerico")

def boleta():
    pass
main()