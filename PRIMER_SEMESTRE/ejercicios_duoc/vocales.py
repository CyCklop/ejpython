pa = input("Escribe un texto: ")
cont = [0,0,0]
for i in pa:
    if i.lower() in "aeiou":
        cont[1]+=1
    else:
        cont[2]+=1
    cont[0]+=1
    print(i)
print(f"La cantidad de caracteres es: {cont[0]}")
print(f"La cantidad de vocales son: {cont[1]}")
print(f"La cantidad de consonantes son: {cont[2]}")