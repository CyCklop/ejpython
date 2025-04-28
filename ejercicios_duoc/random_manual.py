import random
n1 = int(input("Selecciona el primer número: "))
n2 = int(input("Selecciona el segundo número: "))
while n2<=n1:
    print("El número debe ser mayor al primero")
    n2 = int(input("Selecciona el segundo número: "))
numran = random.randint(n1,n2)
print(f"El número aleatorio es: {numran}")