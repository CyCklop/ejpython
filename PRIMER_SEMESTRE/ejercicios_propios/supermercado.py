cant = int(input("Selecciona la cantidad de articulos que llevaras: "))
contot = [0,0]
articulos = [0,0,0]
for a in range(cant):
    obj = int(input("1- pan $450 c/u 2- queso $350 c/u 3- salame $500 c/u: "))
    if obj==1:
        contot[0]+=1
        articulos[0]+=1
        contot[1]+=450
        print("Has comprado 1 pan")
    elif obj ==2:
        contot[0]+=1
        articulos[1]+=1
        contot[1]+=350
        print("Has comprado 1 queso")
    elif obj ==3:
        contot[0]+=1
        articulos[2]+=1
        contot[1]+=500
        print("Has comprado 1 salame")
    else:
        print("Selecciona una opción valida")
print(f"Has llevado {contot[0]} articulo/s")
print(f"Dentro de los cuales fueron: {articulos[0]} pan/es, {articulos[1]} queso/s, {articulos[2]} salame/s")
print(f"El total de tu boleta es de: {contot[1]*1.19}")