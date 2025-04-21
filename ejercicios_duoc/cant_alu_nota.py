alum = int(input("Ingresa la cantidad total de alumnos: "))
suma = 0

for j in range(alum):
    cnotas = int(input(f"Ingresa la cantidad de notas del alumno {j+1}: "))
    for i in range(cnotas):
        nota = float(input(f"Ingresa la nota número {i+1} del alumno {j+1}: "))
        suma=suma+nota 
prom=suma/cnotas
print(f"El promedio del alumno {j} es: {prom}")

if prom>=4:
    print("Usted aprobo")
else:
    print("Usted reprobo")