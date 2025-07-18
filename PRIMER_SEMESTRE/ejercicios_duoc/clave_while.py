clave = 2233
intento = 3
print(f"Tienes {intento} intentos para ingresar la clave")
while intento>0:
    password = int(input("Ingresa la clave: "))
    if clave==password:
        print("Accediendo al sistema...")
        break
    else:
        intento-=1
        print(f"Clave incorrecta, te quedan {intento} intentos" if intento>0 else "Ya no te quedan más intentos, bloqueando sistema..")