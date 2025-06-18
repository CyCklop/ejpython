list_prod=[
    {"nombre":"zapato", 
     "precio":20000, 
     "categoria": "vestuario",
     "tamaño": "mediano",
     "enOferta": False},

    {"nombre":"pelota", 
     "precio":24000}
]

def mostrar_art(lista):
    for n, p in enumerate(lista):
        print(n+1, ".-", p["nombre"], "$", p["precio"])

# menu
while True:
    try:
        print(f"1- Agregar producto\n2- Mostrar producto\n3- Actualizar producto\n4- Borrar productos\n5- Salir")
        op=int(input("Seleccione una opcion: "))
        match op:
            case 1:
                nom=input("Ingrese el nombre del producto: ")
                pre=int(input("Ingrese el precio: "))
                list_prod.insert(0,{"nombre":nom, "precio":pre})
            case 2:
                mostrar_art(list_prod)
            case 3:
                # for n, p in enumerate(list_prod):
                #     print(n+1, ".- ", p)
                for i in range(len(list_prod)):
                    print(i+1, ".-", list_prod[i])
                opc=int(input("Seleccione el producto a actualizar"))
                print(list_prod[opc-1])
                nn=input("Ingrese nuevo Nombre")
                np=int(input("Ingrese nuevo Precio"))
                list_prod[opc-1]["nombre"]=nn
                list_prod[opc-1]["precio"]=np
                print("Articulo actualizado!")
            case 4:
                pass
            case 5:
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo numeros enteros")