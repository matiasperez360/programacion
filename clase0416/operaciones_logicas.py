numA = ""
numB = ""
resultado = "" 


numA = int(input("Ingrese el primer numero: "))
numB = int(input("Ingrese el segundo numero: "))

resultado = numA * numB

if numA > numB or numA % 2 == 0:
    print(f"El resultado de la multiplicacion es: {resultado}")
else:
    print("Error en formula")