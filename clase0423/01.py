

contador = 0
positivos = 0
negativos = 0
numero = 0
cuantos = 0

cuantos = int(input("¿Cuántos números desea ingresar? "))

while contador < cuantos:
    numero = int(input(f"Ingrese el número {contador + 1} de {cuantos}: "))
    if numero > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
    contador = contador + 1    


print(f"La cantidad de números negativos es: {negativos}")
print(f"La cantidad de números positivos es: {positivos}")