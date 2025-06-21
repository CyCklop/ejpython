articulos = {
    1: {"nombre": "Toalla", "precio": 6500}
}

carrito = []

def ingresar(diccio):
    lista_diccio = list(diccio.keys())[-1]
    nom = input("Ingresa el nombre del articulo: ")
    pre = int(input("Ingresa el precio del articulo: "))
    diccio[lista_diccio+1] = {"nombre": nom, "precio": pre}

def comprar(diccio,cart):
    for key,value in diccio.items():
        print(f"{key}.- {value["nombre"]}-{value["precio"]}")
    op = int(input("Selecciona el numero del producto a comprar: "))
    if op in diccio.keys():
        print(f"¡Has agregado al carrito el articulo {op}!")
        cart.append(diccio.keys(op))
    else:
        print(f"El número de articulo {op} no existe..")


def show(diccio):
    for key,value in diccio.items():
        print(f"{key}.- {value["nombre"]}-{value["precio"]}")


def showcarr(cart):
    for i in cart:
        print(f"En el carrito llevas:\n{i}")


def boleta():
    pass

def menu():
    while True:
        try:
            print("*****TIENDA*****\n1) Ingresar Articulo\n2) Comprar Articulo\n3) Ver Articulos\n4) Ver Carrito\n5) Pedir boleta\n6) Salir")
            op = int(input("Elige una opción: "))
            match op:
                case 1:
                    ingresar(articulos)
                case 2:
                    comprar(articulos,carrito)
                case 3:
                    show(articulos)
                case 4:
                    showcarr(carrito)
                case 5:
                    pass
                case 6:
                    print("Saliendo del menú....")
                    break
                case _:
                    print("Error, Ingresa una opción valida")
        except Exception:
            print("Error, ingrese un dato númerico")
menu()