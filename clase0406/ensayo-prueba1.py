"La empresa “Sito Man Boy” vende sillas al por mayor, sus ventas han bajado y elaboraron un plan para incentivar la producción, al trabajador se le cancela 120 pesos por cada silla construida, si en el mes supera las 1000 unidades se le cancelará un adicional de 20 pesos adicional por cada silla sobre las 1000."

pago_por_silla = 120
adicional_por_silla = 20
sillas = "" 
pago = ""
pago_total = ""
bonus = ""

sillas = int(input("Ingrese la cantidad de sillas construidas al mes: "))
pago = sillas * pago_por_silla
bonus = (sillas - 1000) * adicional_por_silla

if sillas > 1000:
    pago_total = pago + bonus
    print(f"El pago por las sillas construidas es de ${pago} pesos")
    print(f"El bonus por las sillas adicionales es de ${bonus} pesos")
    print(f"El pago total es de ${pago_total} pesos")
else:
    pago_total = pago
    print(f"El pago total es de ${pago_total} pesos")
    print("No se ha ganado el bonus")