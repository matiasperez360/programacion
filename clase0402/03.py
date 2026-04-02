nota=""

nota = float(input("Ingrese su nota: "))

if nota <= 1:
     nota_valida = True
else:
    nota_valida = False

if nota > 7:
    nota_valida = False
else:
    nota_valida = True



if nota_valida:
    print("La nota ingresada es válida")
else:   
    print("La nota ingresada no es válida")