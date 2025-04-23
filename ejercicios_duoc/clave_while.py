clave = 2233
intento = [0,3] #inicial,maximo
password = int(input("Ingresa la clave: "))
while clave!=password:
    print(f"Clave incorrecta, intente denuevo (Intentos Restantes: {intento[1]})")
    password = int(input("Ingresa la clave: "))
    intento[1]+=-1
if intento[1]<=0:
    print("Se acabaron los intentos, bloqueando acceso...")
else:
    print("¡Clave correcta!, Accediendo al sistema...")