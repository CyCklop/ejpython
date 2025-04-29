import random 
import time
bill = ["dinero",5000,10000,20000]
caja = 30

clave = int(input("Cajero Automatico\nCrea una clave númerica para tu usuario: "))
time.sleep(1)
print("¡Clave guardada!")
intento = int(input("Ingresa la clave creada: "))
while intento!=clave:
    intento = int(input("¡Clave incorrecta!\nIntenta nuevamente: "))
else:
    print("¡Bienvenido al cajero automatico!")