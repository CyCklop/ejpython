import time
import random
cate = ["Categoria",200,400,600]
prod = [
    "Deporte",8000,8500,38000,
    "Enlatados",4500,5000,4000,
    "Carnes",13000,7000,7500
]
total = 0

opcion = int(input("Selecione una categoria\n1- Deporte\n2- Enlatados\n3- Carnes\n"))
if opcion == 1:
    opcion2 = int(input("Categoria Deportes\n1- Pelota BasketBall $8.000\n2- Pelota Fútbol $8.500\n3- Zapatillas Deportivas $38.000\n"))
    if opcion2 ==1:
        print("Has comprado 1 Pelota de BasketBall")
        total+=8000
    elif opcion2 ==2:
        pass
    elif opcion2 ==3:
        pass
    else:
        print("Selecciona una opcion valida")
elif opcion == 2:
    opcion2 = int(input("Categoria Enlatados\n1- Atún al agua $4.500\n2- Jurel en medallon $5.000\n3- Salsa de tomate $4.000\n"))
    if opcion2 ==1:
        print("Has comprado 1 Atún al agua")
        total+=4500
    elif opcion2 ==2:
        pass
    elif opcion2 ==3:
        pass
    else:
        print("Selecciona una opcion valida")
elif opcion == 3:
    opcion2 = int(input("Categoria Carnes\n1- Posta paleta $13.000\n2- Carne molida especial $7.000\n3- Pechuga de pollo $7.500\n"))
    if opcion2 ==1:
        print("Has comprado 1 Posta paleta")
        total+=13000
    elif opcion2 ==2:
        pass
    elif opcion2 ==3:
        pass
    else:
        print("Selecciona una opcion valida")
else:
    print("Seleccione una opcion valida")

if total<=1000:
    total = total*3/100