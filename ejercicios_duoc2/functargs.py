def promedio(lista):
    return sum(lista)/len(lista)
cant = int(input("Ingresa la cantidad de notas: "))
notas = []
for i in range(cant):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    notas.append(nota)
resultado = promedio(notas)
resultado_round = round(resultado)
print(f"El promedio es de: {resultado_round}")