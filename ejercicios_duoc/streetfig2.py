import random
import time

hp, hp2 = 50,50
dmg = random.randint(7,15)
crit = random.randint(1,5)
turno = 1

ch1 = str(input("Elija nombres para los luchadores\nprimer luchador: "))
ch2 = str(input("segundo luchador: "))

while hp>0 and hp2>0:
    time.sleep(1)
    print("¡La batalla esta por comenzar!")
    if turno % 2==0:
        pass
    
