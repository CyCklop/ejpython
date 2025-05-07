import random
digit = int(input("Escriba el primer digito\n"))
digit2 = int(input("Escriba el segundo digito\n"))
while digit2<=digit:
    print("El segundo numero no puede ser menor o igual al primero")
    digit2 = int(input("Escriba denuevo el segundo digito\n"))
random_digit = random.randint(digit,digit2)
for i in range(random_digit):
    print("▄")