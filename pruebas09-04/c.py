"C.	Desarrolle un programa que permita ingresar la estatura y peso, si al dividir el peso por la estatura al cuadrado el valor es menor a 25 desplegaremos por pantalla peso normal, si sobrepasa los 25 mostraremos sobrepesoC.	Desarrolle un programa que permita ingresar la estatura y peso, si al dividir el peso por la estatura al cuadrado el valor es menor a 25 desplegaremos por pantalla peso normal, si sobrepasa los 25 mostraremos sobrepeso"

estatura = ""
peso = ""

estatura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

sobrepeso = peso / (estatura * estatura)

if sobrepeso < 25:
    print("peso normal")
else:
    print("usted tiene sobrepeso")
