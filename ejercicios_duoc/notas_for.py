cant = int(input("Ingresa el número de notas: "))
suma = 0
for i in range(cant):
    print(f"Ingrese nota {i+1}")
    nota=float(input())
    suma+=nota #o suma=suma+nota
prom= suma/cant
print(f"El promedio de notas es de {prom}")