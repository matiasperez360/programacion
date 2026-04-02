

anio_de_nacimiento = ""
anio_actual = ""
edad = ""

print("Calculadora de edad")
print("Ingrese su año de nacimiento y el año actual para calcular su edad.")

anio_de_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_actual = int(input("Ingrese el año actual: "))
edad = int(anio_actual - anio_de_nacimiento)
print(f"Su edad es: {edad}")

