x = 0
cant = 0
positivos = 0
suma = 0
promedio = 0

cant = int(input("cuantos números quiere ingresar: "))

while x < cant:
    num = float(input(f"Ingrese el número {x + 1} de {cant}: "))
    if num > 0:
        suma = suma + num
        positivos = positivos + 1
    
    x = x + 1

promedio = suma / positivos

promedio = round(promedio, 1)


print(f"el promedio de los números positivos es: {promedio}")