import random
while True:
    try:
        cant = int(input("CAZA PY\nIngresa un número de perros: "))
        cuota = 3
        cumple = 0
        for i in range(cant):
            con = random.randint(0,5)
            print(f"El perro número {i+1} cazó {con} conejo/s")
            if con>=cuota:
                print(f"El perro {i+1} ganó un filete")
                meta+=1
            else:
                print(f"El perro {i+1} se quedo sin filete")
        print(f"La cantidad de perros que cumplieron la cuota es de {cuota}")
        print(f"La cantidad de perros que no cumplieron la cuota fueron {cant-cuota}")
    except Exception:
        print("Se debe ingresar un número entero")