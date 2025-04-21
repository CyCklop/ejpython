cant = int(input("Selecciona la cantidad de articulos que llevaras: "))
cont = 0
total = 0
pan = 0
que = 0
sa = 0
for a in range(cant):
    obj = int(input("1- pan $450 c/u 2- queso $350 c/u 3- salame $500 c/u: "))
    if obj==1:
        cont+=1
        pan+=1
        total+=450
        print("Has comprado 1 pan")
    elif obj ==2:
        cont+=1
        que+=1
        total+=350
        print("Has comprado 1 queso")
    elif obj ==3:
        cont+=1
        sa+=1
        total+=500
        print("Has comprado 1 salame")
    else:
        print("Selecciona una opción valida")
print(f"Has llevado {cont} articulo/s")
print(f"Dentro de los cuales fueron: {pan} pan/es, {que} queso/s, {sa} salame/s")
print(f"El total de tu boleta es de: {total*1.19}")