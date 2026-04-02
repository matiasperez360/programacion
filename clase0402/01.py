nota01 = ""
nota02 = ""
nota03 = ""
numero_notas = ""
promedio = ""


nota01 = float(input("Ingrese la primera nota: "))
nota02 = float(input("Ingrese la segunda nota: "))
nota03 = float(input("Ingrese la tercera nota: "))
numero_notas = 3
promedio = (nota01 + nota02 + nota03) / numero_notas


promedio_redondeado = round(promedio, 1)

if promedio_redondeado >= 4.0: 
    aprobado = True
else: 
    aprobado = False


if aprobado:
    print("El estudiante ha aprobado con un promedio de", promedio_redondeado)
else:
    print("El estudiante no ha aprobado con un promedio de", promedio_redondeado)
