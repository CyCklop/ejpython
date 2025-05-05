import random
digit = int(input("Escriba el primer digito\n"))
digit2 = int(input("Escriba el segundo digito\n"))
random_digit = random.randint(digit,digit2)
if digit2<=digit:
    print("El segundo numero no puede ser menor o igual al primero")
else:
    for i in range(random_digit):
        print("*")
