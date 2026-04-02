cajas_de_mouse_compradas = ""   
cantidad_de_mouse_por_caja = ""
valor_de_caja = ""
cantidad_total_de_mouse = ""
valor_de_mouse = ""
recaudo_total = ""
ganancia_total = ""

print("Calculadora de ingresos por venta de mouse")

cajas_de_mouse_compradas = int(input("Ingrese la cantidad de cajas de mouse compradas: "))
cantidad_de_mouse_por_caja = int(input("Ingrese la cantidad de mouse por caja: "))
cantidad_total_de_mouse = int(cajas_de_mouse_compradas * cantidad_de_mouse_por_caja)
valor_de_mouse = int(input("Ingrese el valor de cada mouse: "))
valor_de_caja = int(input("Ingrese el valor de cada caja: "))
recaudo_total = int(cantidad_total_de_mouse * valor_de_mouse)
ganancia_total = int(recaudo_total - (cajas_de_mouse_compradas * valor_de_caja))
print(f"El recaudo total por la venta de mouse es: ${recaudo_total}")
print(f"El valor total de las cajas de mouse es: ${cajas_de_mouse_compradas * valor_de_caja}")
print(f"La ganancia total es: ${ganancia_total}")
print("Gracias por usar la calculadora de ingresos por venta de mouse.")

