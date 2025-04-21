cant = int(input("Ingresa la cantidad de votantes: "))
candi1 = 0
candi2 = 0

for i in range(cant):
    voto = int(input("Ingresa un voto (1- vardoc 2- xoda): "))
    if voto == 1:
        candi1=candi1+1
        print("¡Has votado por vardoc!")
    elif voto == 2:
        candi2=candi2+1
        print("¡Has votado por xoda!")
    else:
        print("Error seleccione un número valido")

if candi1>candi2:
    print(f"Las elecciones las ha ganado vardoc, con {candi1} votos")
elif candi1==candi2:
    print(f"Las elecciones han sido empatadas hasta la segunda vuelta")
else:
    print(f"Las elecciones las ha ganado xoda, con {candi2} votos")