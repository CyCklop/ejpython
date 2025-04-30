import time
plata = ["dinero",5000,10000,20000]
cancaja = ["cantidad",30,30,30]

#Creacion de clave
clave = int(input("Cajero Automatico\nCrea una clave númerica para tu usuario: "))
time.sleep(1)
print("¡Clave guardada!")
intento = int(input("Ingresa la clave creada: "))
while intento!=clave:
    intento = int(input("¡Clave incorrecta!\nIntenta nuevamente: "))
else:
    print("¡Bienvenido al cajero automatico!")
time.sleep(1)

#bucle de seleccion de billetes
opcion = int(input("Seleccione la cantidad de billetes que desea sacar: "))
for i in range(opcion):
    opcion2 = int(input(f"Seleccione cual tipo de billete desea sacar\n1- {plata[1]}\n2- {plata[2]}\n3- {plata[3]}\n"))
    if opcion2 == 1:
        cancaja[1]-=1
        print("Has seleccionado 1 billete de 5.000")
    elif opcion2 == 2:
        cancaja[2]-=1
        print("Has seleccionado un billete de 10.000")
    elif opcion2 == 3:
        cancaja[3]-=1
        print("Has seleccionado un billete de 20.000")
    else:
        print("Selecciona un número valido")