def notas():
    op = int(input("Ingresa cuantas notas tienes: "))
    notas = []
    for i in range(op):
        op2 = int(input(f"Ingresa la {i+1} nota "))
        notas.append(op2) #agrega un valor al final de la lista "notas[]"
    resultado = sum(notas)/op #sum suma todos los elementos int y float de la lista "notas[]"
    if resultado>=4:
        print("Usted aprobo el ramo")
    else:
        print("Usted reprobo el ramo")
    print(f"El promedio de tus notas es: {resultado}")
notas()