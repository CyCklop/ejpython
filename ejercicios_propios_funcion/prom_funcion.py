def notas():
    op = int(input("Ingresa cuantas notas tienes: "))
    notas = []
    for i in range(op):
        op2 = int(input(f"Ingresa la {i+1} nota "))
        notas.append(op2)
    resultado = sum(notas)/op
    if resultado>=4:
        print("Usted aprobo el ramo")
    else:
        print("Usted reprobo el ramo")
    print(f"El promedio de tus notas es: {resultado}")
notas()