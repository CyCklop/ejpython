# ejercicio par/impar con bucle for
num = int(input("Ingresa un número: "))

for i in range(num):
    if i % 2==0:
        print(f"El número {i+1} es par")
    else:
        print(f"El número {i+1} es impar")
