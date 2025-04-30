import time 
comuna = ["Comunas",20/100,30/100,25/100,15/100]
grufam = ["Grupo familiar",2/100,3/100,4/100]
arancel = 200000

print("El arancel a pagar es de 200.000 por semestre, pero puede acceder a beneficios depende de la comuna en la que viva y con cuantas personas")
user = int(input("Selecciona en cual de estas comunas vives:\n1- La florida\n2- La pintana\n3- Puente alto\n4- San Joaquin\n"))
if user == 1:
    print("Usted vive en la florida")
    arancel-=comuna[1]
elif user == 2:
    print("Usted vive en La pintana")
    arancel-=comuna[2]
elif user == 3:
    print("Usted vive en Puente alto")
    arancel-=comuna[3]
elif user == 4:
    print("Usted vive en San Joaquin")
    arancel-=comuna[4]
else:
    print("Seleccione una opcion valida")
time.sleep(1)
grupfam = int(input("Con cuantas personas vives:\n1- una persona\n2- dos a cuatro personas\n3- cinco o más personas\n"))
if grupfam == 1:
    print("Usted vive con 1 persona")
    arancel-=grufam[1]
elif grupfam == 2:
    print("Usted vive con 2 o 4 personas")
    arancel-=grufam[2]
elif grupfam == 3:
    print("Usted vive con 5 o más personas")
    arancel-=grufam[3]
else:
    print("Selecciona una opción valida")
time.sleep(1)
print(f"El total a pagar del arancel actual es: {arancel}")