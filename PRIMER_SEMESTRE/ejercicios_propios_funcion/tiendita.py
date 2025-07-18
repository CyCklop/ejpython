import time
articulos = {
    1: {"nombre": "Audifonos", "precio": 15000}
}

carrito = []

def ingresar(diccio):
    lista_diccio = list(diccio.keys())[-1]
    nom = input("Ingresa el nombre del articulo: ")
    pre = int(input("Ingresa el precio del articulo: "))
    diccio[lista_diccio+1] = {"nombre": nom,"precio": pre}
    print("Articulo añadido excitosamente..")
    time.sleep(1)

def agregar(diccio,cart):
    for key,value in diccio.items():
        print(f"{key}.- {value["nombre"]}-${value["precio"]}")
    op = int(input("Ingresa el número del articulo a agregar: "))
    if op in diccio.keys():
        cart.append(diccio[op])
        diccio.pop(op)
        print(f"¡Has agregado el articulo número {op} al carrito!")
        time.sleep(1)
    else:
        print(f"El número {op} no esta en la lista de articulos...")

def vercart(cart):
    for i,a in enumerate(cart):
        nombre,precio = a.values()
        print(f"Articulos en carrito:\n{i+1}-{nombre}-${precio}")

def verart(diccio):
    for key,value in diccio.items():
        print(f"{key}.- {value["nombre"]}-${value["precio"]}")

def boleta(cart):
    for i,a in enumerate(cart):
        nombre,precio = a.values()
        print(f"Tu boleta:\n{i+1}-{nombre}-${precio}")

def menu():
    while True:
        try:
            print("1) Ingresar Articulo\n2) Agregar al carrito\n3) Ver Carrito\n4) Ver Articulos\n5) Ver Boleta\n6) Salir")
            op = int(input("Selecciona una opción: "))
            match op:
                case 1:
                    ingresar(articulos)
                case 2:
                    agregar(articulos,carrito)
                case 3:
                    vercart(carrito)
                case 4:
                    verart(articulos)
                case 5:
                    boleta(carrito)
                case 6:
                    print("Saliendo...")
                    break
                case _:
                    print("Error, ingresa una opción valida")
        except Exception:
            print("Error, ingrese un valor númerico")
menu()