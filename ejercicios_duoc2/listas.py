cant = int(input("Ingrese la cantidad de números que quiere añadir a la lista: "))
list = []
for i in range(cant):
    num = int(input(f"Ingrese el número {i} de la lista: "))
    list.append(num)
print(f"La lista quedo con estos datos: {list}")