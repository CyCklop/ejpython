import random
import time
hp1,hp2 = 50,50
turno = random.randint(1,2)

ch1 = str(input("Ingresa el nombre del primer luchador: "))
ch2 = str(input("Ingresa el nombre del segundo luchador: "))

while hp1>0 and hp2>0:
    if turno % 2==0:
        daño = random.randint(3,15)
        time.sleep(1)
        print(f"¡es el turno de {ch1}!")
        time.sleep(1)
        print(f"¡{ch1} golpea a {ch2} (DMG: {daño})")
        print(f"Vida de {ch2}")
        hp2-=daño
        print("/"*hp2)
    else:
        daño = random.randint(3,15)
        time.sleep(1)
        print(f"¡es el turno de {ch2}!")
        time.sleep(1)
        print(f"¡{ch2} golpea a {ch1} (DMG: {daño})")
        print(f"Vida de {ch1}")
        hp1-=daño
        print("/"*hp1)
    turno+=1
if hp1>hp2:
    print(f"Ha ganado {ch1}")
else:
    print(f"Ha ganado {ch2}")