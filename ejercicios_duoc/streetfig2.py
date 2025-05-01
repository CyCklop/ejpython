import random
import time

hp, hp2 = 50,50
dmg = random.randint(7,15)
crit = random.randint(1,6)
turno = random.randint(1,2)

ch1 = str(input("Elija nombres para los luchadores\nprimer luchador: "))
ch2 = str(input("segundo luchador: "))

while hp>0 and hp2>0:
    time.sleep(1)
    print("¡La batalla esta por comenzar!")
    if turno % 2==0:
        print(f"¡Es turno de {ch1}!")
        if crit == 3:
            time.sleep(1)
            hp2-=dmg*2
            print(f"¡{ch1} ha lanzado un hadouken a {ch2}!")
            print(f"Vida de {ch2}")
            print("/"*hp2)
        else:
            time.sleep(1)
            hp2-=dmg*2
            print(f"¡{ch1} ha golpeado a {ch2}!")
            print(f"Vida de {ch2}")
            print("/"*hp2 if hp2>0 else "X_X")
    else:
        print(f"¡Es turno de {ch2}!")
        if crit == 3:
            hp-=dmg*2
            time.sleep(1)
            print(f"¡{ch2} ha lanzado un hadouken a {ch1}!")
            print(f"Vida de {ch1}")
            print("/"*hp)
        else:
            time.sleep(1)
            hp-=dmg*2
            print(f"¡{ch2} ha golpeado a {ch1}!")
            print(f"Vida de {ch1}")
            print("/"*hp if hp>0 else "X_X")
if hp>hp2:
    print(f"¡Ha ganado {ch1}!")
else:
    print(f"¡Ha ganado {ch2}!")