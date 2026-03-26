cantidad_de_buses = ""
cantidad_de_pasajeros_por_bus = ""
valor_pasaje = ""
recaudo_total = ""

print("Calculadora de ingresos por venta de pasajes")

cantidad_de_buses = int(input("Ingrese la cantidad de buses: "))
cantidad_de_pasajeros_por_bus = int(input("Ingrese la cantidad de pasajeros por bus: "))
valor_pasaje = int(input("Ingrese el valor del pasaje: "))
recaudo_total = int(cantidad_de_buses * cantidad_de_pasajeros_por_bus * valor_pasaje)
print(f"El recaudo total por la venta de pasajes es: ${recaudo_total}")      