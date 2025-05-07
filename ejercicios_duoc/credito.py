total = 0

ingre = int(input("BANCO ESTADO\nPara sacar un credito debe ingresar sus ingresos, nivel educacional y nacionalidad\nEscriba sus ingresos: "))
if ingre<=1000001:
    print("Puede sacar un credito inicial de 300.000$")
    total+=300000
elif ingre<=1500000:
    print("Puede sacar un credito inicial de 650.000$")
    total+=650000
elif ingre>=1500000:
    print("Puede sacar un credito inicial de 1.000.000$")
    total+=1000000

edu = int(input("Escriba su nivel de educacion\n1- Basica\n2- Media\n3- Superior\n"))
if edu == 1:
    print("Usted tuvo estudios hasta educacion basica")
    total*=1
elif edu ==2:
    print("Usted tuvo estudios hasta educacion media")
    total*=1.3
elif edu == 3:
    print("Usted tuvo estudios hasta educacion superior")
    total*=1.5
else:
    print("Seleccione una opción valida")

nacio = int(input("Escriba cual es su nacionalidad\n1- Chilena\n2- Extranjera\n"))
if nacio == 1:
    print("Usted es de nacionalidad chilena")
    total+=300000
elif nacio == 2:
    print("Usted es extranjero")

print(f"El total de su credito es de: {total}")