cajas_de_mouse_compradas = ""   
cantidad_de_mouse_por_caja = ""
cantidad_total_de_mouse = ""
valor_de_mouse = ""
recaudo_total = ""

print("Calculadora de ingresos por venta de mouse")

cajas_de_mouse_compradas = int(input("Ingrese la cantidad de cajas de mouse compradas: "))
cantidad_de_mouse_por_caja = int(input("Ingrese la cantidad de mouse por caja: "))
cantidad_total_de_mouse = int(cajas_de_mouse_compradas * cantidad_de_mouse_por_caja)
valor_de_mouse = int(input("Ingrese el valor de cada mouse: "))
recaudo_total = int(cantidad_total_de_mouse * valor_de_mouse)
print(f"El recaudo total por la venta de mouse es: ${recaudo_total}")
