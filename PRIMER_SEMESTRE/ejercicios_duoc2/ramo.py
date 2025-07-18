import time
while True:
    try:
        cant = int(input("Ingresa la cantidad de rojos en el curso: "))
        tall = int(input("Ingrese a cuantos de los 4 talleres asistió: "))

        while tall>4:
            print("Solo hubieron 4 talleres, ingrese la cantidad correcta")
            tall = int(input("Ingrese a cuantos de los 4 talleres asistió: "))

        decimas = 0

        for i in range(tall):
            print(f"Has asistido al taller {i+1}, has obtenido 0.3 decimas")
            time.sleep(1)
            decimas+=0.3
        if decimas>=1:
            print("Usted tiene la bendicion del profesor")
            nota = float(input("Ingresa la nota que quieres subir: "))
            resultado = nota+decimas
            print(f"El total de su nota con las decimas aplicadas es de: {resultado}")
        else:
            print("No se le puede ayudar")
            break

        if nota>=4:
            print("Usted Aprobo")
            break
        else:
            print("Usted reprobo")
            break
    except Exception:
        print("Ingrese un dato valido")