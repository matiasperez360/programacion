pesos_que_tiene = int(input("Ingrese la cantidad de dinero que tiene: "))
inversion_total = int(input("Ingrese la cantidad de dinero que desea invertir: "))
n_meses = int(input("Ingrese el número de meses de inversión: "))
print("********** Interés de inversiones *************")
int_bonos = int(input("Ingrese porcentaje de ganancia en bonos : "))
int_dep = int(input("Ingrese porcentaje interés en depósitos : "))

dinero_dep = pesos_que_tiene - inversion_total

inversion_bonos = inversion_total * (int_bonos / 100)
inversion_deposito = dinero_dep * (int_dep / 100)
ganancia_mensual = inversion_bonos + inversion_deposito
print("************* Detalle de ganacias **********************")
print("Dinero invertido en depósitos :", dinero_dep)
print(f"Inversión {int_bonos}% : {inversion_bonos}")
print(f"Depósitos {int_dep}% : {inversion_deposito}")
print("Total ganacia mensual :", ganancia_mensual)
print("Total período de ", n_meses, "meses")
ganancia_total = ganancia_mensual * n_meses
print(f"{n_meses} meses es: {ganancia_total}")