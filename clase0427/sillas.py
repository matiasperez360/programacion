trabajadores = 10
tra_con_bono = 0
sillas = 0
sueldo = 0
bono = 0
x = 0
adicional = 20
pago = 0
total_sueldo = 0
total_sillas = 0
total_bono = 0
promedio_sillas = 0



while x < trabajadores:
    sillas = int(input(f"Cuantas sillas hizo el trabajador {x + 1} de {trabajadores}: "))
    pago = sillas * 1000
    if sillas > 2000:
        bono = (sillas - 2000) * adicional
        tra_con_bono = tra_con_bono + 1
    else:
        bono = 0

    sueldo = pago + bono
    total_sueldo = total_sueldo + sueldo
    total_sillas = total_sillas + sillas
    total_bono = total_bono + bono
    promedio_sillas = total_sillas / trabajadores

    x = x + 1


print(f"El total a pagar a los trabajadores es de ${total_sueldo} pesos")
print(f"El total de sillas construidas por los trabajadores es de {total_sillas} sillas")
print(f"El total de bono pagado a los trabajadores es de ${total_bono} pesos")
print(f"El número de trabajadores que hicieron más de 2000 sillas es de {tra_con_bono} trabajadores")
print(f"El promedio de sillas por trabajador es de {promedio_sillas} sillas")   