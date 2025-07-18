import time 
comuna = ["Comunas",20,30,25,15]
grufam = ["Grupo familiar",2,3,4]
arancel = 200000

print("El arancel a pagar es de 200.000 por semestre, pero puede acceder a beneficios depende de la comuna en la que viva y con cuantas personas")
user = int(input("Selecciona en cual de estas comunas vives:\n1- La florida\n2- La pintana\n3- Puente alto\n4- San Joaquin\n"))
if user == 1:
    print("Usted vive en la florida")
    arancel-=arancel * comuna[1]/100
elif user == 2:
    print("Usted vive en La pintana")
    arancel-=arancel * comuna[2]/100
elif user == 3:
    print("Usted vive en Puente alto")
    arancel-=arancel * comuna[3]/100
elif user == 4:
    print("Usted vive en San Joaquin")
    arancel-=arancel * comuna[4]/100
else:
    print("Seleccione una opcion valida")
time.sleep(1)
grupfam = int(input("Con cuantas personas vives:\n1- una persona\n2- dos a cuatro personas\n3- cinco o más personas\n"))
if grupfam == 1:
    print("Usted vive con 1 persona")
    arancel-=arancel * grufam[1]/100
elif grupfam == 2:
    print("Usted vive con 2 o 4 personas")
    arancel-=arancel * grufam[2]/100
elif grupfam == 3:
    print("Usted vive con 5 o más personas")
    arancel-= arancel * grufam[3]/100
else:
    print("Selecciona una opción valida")
print(f"El total a pagar de su arancel actual es: {arancel}")