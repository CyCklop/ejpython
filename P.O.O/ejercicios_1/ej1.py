class persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    def datos(self):
        print(f"Nombre: {self.nombre} --- Edad: {self.edad}")

while True:
    try:
        input_nombre = str(input("Ingresa tu nombre: "))
        input_edad = int(input("Ingresa tu edad: "))
        break
    except Exception:
        print("Ingresa un dato valido...")

datos1 = persona(input_nombre,input_edad)

datos1.datos()
