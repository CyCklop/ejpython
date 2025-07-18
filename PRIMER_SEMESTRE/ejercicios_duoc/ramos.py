total = 0
print("Bono Estudios/////")
cant = int(input("Que tipo de carrera estudias\n1- Tecnico\n2- Ingenieria\n3- Diplomado\n"))
if cant == 1:
    total+=60
elif cant == 2:
    total+=40
elif cant == 3:
    total+=20
else:
    print("Seleccione una opción valida")

cantra = int(input("Cuanta cantidad de ramos tiene\n"))
ramos = []
for i in range(cantra):
    ramo = float(input(f"Escriba el promedio de el ramo {i+1}: "))
    ramos.append(ramos)
promedio = (ramos[])/3
if promedio>=5:
    total+=300
elif promedio>=6:
    total+=500
elif promedio>6.9:
    total+=800
print(f"El total de sus creditos por bono estudiantil es de {total}")