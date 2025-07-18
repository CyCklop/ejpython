import random
ran = random.randint(1,100)
num = int(input("¡Adivina el número aleatorio de el 1 al 100!: "))
while num!=ran:
    if num < ran:
        print("¡Estas cerca del número!")
        num = int(input("Intentalo denuevo: "))
    else:
        print("¡Estas lejos del número!")
        num = int(input("Intentalo denuevo: "))
print(f"¡Has acertado!, el número era: {ran}")