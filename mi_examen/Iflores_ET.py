#Examen Transversal Ignacio Flores
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
            '2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
            'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
            'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
            'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
            '123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
            '342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
            'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
        'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
        'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0] 
}


def stock_marca(producto,stock):
    while True:
        input_modelo = input("Ingrese modelo del producto: ")
        if input_modelo in producto.keys() and input_modelo in stock.keys():
            input_marca = input("Ingrese marca a consultar: ")
            if input_marca in producto[input_modelo]:
                print(f"El stock es de: {stock[input_modelo][1]}")
                break
            else:
                print(f"//Error, la marca {input_marca} no existe en el modelo {input_modelo}...//")
        else:
            print(f"//Error, el modelo {input_modelo} no existe...//")

def busqueda_por_precio(stock):
    precio_minimo = int(input("Ingrese precio minimo: "))
    precio_maximo = int(input("Ingrese precio máximo: "))
    for i in range(precio_minimo,precio_maximo):
        pass

def actualizar_precio(productos,stock):
    while True:
        input_modelo = input("Ingrese el modelo a actualizar: ")
        if input_modelo in productos.keys() and input_modelo in stock.keys():
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            stock[input_modelo][1] = [nuevo_precio]
            print(f"¡Precio del modelo '{input_modelo}' actualizado correctamente!")
            input_actualizar = input("¿Desea actualizar otro precio (s/n)?: ")
            if input_actualizar == "s":
                continue
            if input_actualizar == "n":
                print("Volviendo al menú principal...")
                break
            while input_actualizar != "s" and input_actualizar != "n":
                print("//Error, debes ingresar 's' o 'n'//")
                input_actualizar = input("¿Desea actualizar otro precio (s/n)?: ")
        else:
            print(f"//Error, el modelo {input_modelo}, no existe...//")

def menu():
    while True:
        try:
            print("--Menú Principal--\n1) Stock marca\n2) Búsqueda por precio\n3) Actualizar precio\n4) Salir")
            op = int(input("Ingrese una opción: "))
            match op:
                case 1:
                    stock_marca(productos,stock)
                case 2:
                    busqueda_por_precio(stock)
                case 3:
                    actualizar_precio(productos,stock)
                case 4:
                    print("Programa finalizado....")
                    break
                case _:
                    print("//Error, debes ingresar una opción válida//")
        except Exception:
            print("//Error, debes ingresar un número entero//")
menu()