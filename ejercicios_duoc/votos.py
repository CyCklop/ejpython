cant = int(input("Ingresa la cantidad de votantes: "))
candid = [0,0]

for i in range(cant):
    voto = int(input("Ingresa un voto (1- vardoc 2- xoda): "))
    if voto == 1:
        candid[0]+=1
        print("¡Has votado por vardoc!")
    elif voto == 2:
        candid[1]+=1
        print("¡Has votado por xoda!")
    else:
        print("Error seleccione un número valido")

if candid[0]>candid[1]:
    print(f"Las elecciones las ha ganado vardoc, con {candid[0]} votos")
elif candid[0]==candid[1]:
    print(f"Las elecciones han sido empatadas hasta la segunda vuelta")
else:
    print(f"Las elecciones las ha ganado xoda, con {candid[1]} votos")