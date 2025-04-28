import random
ran = random.randint(1,100)
inte = 5
num = int(input("¡Adivina el número aleatorio de el 1 al 100!: "))
while num!=ran and inte == 0:
    if num < ran:
        print("¡Estas cerca del número!")
        print(f"Te quedan: {inte} intentos")
        num = int(input("Intentalo denuevo: "))
        inte-=1
    else:
        print("¡Estas lejos del número!")
        print(f"Te quedan: {inte} intentos")
        num = int(input("Intentalo denuevo:"))
        inte-=1
if inte<=0:
    print("Se te han acabado los intentos")
print(f"¡Has acertado!, el número era: {ran}") 