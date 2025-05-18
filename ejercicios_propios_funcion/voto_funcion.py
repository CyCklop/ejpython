cant = int(input("Selecciona la cantidad de votantes: "))
vo1,vo2 = 0,0
def lista():
    print("ELECCIONES 2025 PRIMERA VUELTA\n1- Huevito rey\n2- Choche")

def acción():
    for i in range(cant):
        lista()
        global vo1,vo2
        op = int(input("Selecciona por quien votar: "))
        match op:
            case 1:
                print("Votaste por Huevito Rey")
                vo1+=1
            case 2:
                print("Votaste por Choche")
                vo2+=1
            case _:
                print("Selecciona un número valido")
acción()
if vo1>vo2:
    print(f"Las elecciones las gano Huevito Rey con {vo1} votos")
elif vo1==vo2:
    print("Las elecciones han sido empatadas hasta segunda vuelta")
else:
    print(f"Las elecciones las gano Choche con {vo2} votos")