import random 
import time 

intentos = 3
num = int(input("ADIVINADOR DE NÚMERO\nSelecciona el número menor: "))
num2 = int(input("Selecciona el número mayor: "))
ranum = random.randint(num,num2)

while num2<=num:
    print("El número mayor no puede ser igual o menor al primer número: ")
    num2 = int(input("ADIVINADOR DE NÚMERO\nSelecciona el número mayor: "))
    if num2>num:
        break

adiv = int(input(f"Tienes {intentos} intento/s Adivina el número aleatorio: "))
intentos-=1
while adiv!=ranum:
    if adiv < ranum:
        print("El número es mayor")
        adiv = int(input(f"Te quedan {intentos} intento/s Adivina el número aleatorio: "))
        intentos-=1
    else:
        print("El número es menor")
        adiv = int(input(f"Te quedan {intentos} intento/s Adivina el número aleatorio: "))
        intentos-=1
    if intentos<=0:
        print(f"Se te han acabado los intentos, el número era {ranum}")
        break
if adiv == ranum:
    print("Felicidades has acertado")