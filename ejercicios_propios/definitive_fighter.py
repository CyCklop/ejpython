import random
import time
hp, hp2 = 50,50
en1, en2 = 25,25
atq = random.randint(6,15)
atq2 = random.randint(1,2)
atqmor = random.randint(4,20)
crit_chance = random.randint(1,5)
turno = random.randint(1,2)

ch1 = str(input("BIENVENIDO A DEFINITIVE FIGHTER\nSelcciona el nombre de tú luchador: "))
time.sleep(1)
print("Te enfrentarás contra Sub-Zero")
time.sleep(1)
print("¡La batalla está por comenzar!")

while hp>0 and hp2>0:
    if turno % 2==0:
        time.sleep(1)
        print(f"¡Es turno de {ch1}!")
        elec = int(input("Decide que hacer este turno\n1- Atacar\n2- Recuperar Energia\n"))
        if elec == 1:
            atac = int(input("Elige cual ataque usar\n1- Golpe Basico (-10 energia)\n2- Golpe Mortal (-15 energia)\n"))
            if atac == 1:
                print(f"¡{ch1} ha usado golpe basico en sub-zero!")
                en1-=10
                hp2-=atq
                print("Vida restante de Sub-Zero")
                print("▄"*hp2 if hp2>0 else "X_X")
            elif atac == 2:
                print(f"¡{ch1} ha usado golpe mortal en sub-zero!")
                en1-=15
                hp2-=atqmor
                print("Vida restante de Sub-Zero")
                print("▄"*hp2 if hp2>0 else "X_X")
        elif elec == 2:
            if en1<15:
                en1+=10
                print("¡Has recuperado 10 puntos de energia!")
                print("Tu energia actual es de")
                print("▄"*en1)
            else:
                print("Aun tienes mucha energia")
        else:
            print("Elige una opción adecuada")
    else:
        time.sleep(1)
        print("¡Es turno de Sub-Zero!")
        if atq2 == 1:
            print(f"¡Sub-Zero ha usado Golpe Basico contra {ch1}!")
            hp-=atq
            en2-=10
            print(f"Vida restante de {ch1}")
            print("▄"*hp if hp>0 else "X_X")
        elif atq2 == 2:
            print(f"¡Sub-Zero ha usado Golpe Congelante contra {ch1}!")
            hp-=atqmor
            en2-=15
            print(f"Vida restante de {ch1}")
            print("▄"*hp if hp>0 else "X_X")
    turno+=1
if hp>hp2:
    print(f"Ha ganado {ch1}")
else:
    print("¡Ha ganado Sub-Zero!")