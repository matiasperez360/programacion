"Desarrolle un programa que permita ingresar 3 números al usuario y despliegue el mayor de los números ingresados."

num1 = ""
num2 = ""
num3 = ""
num_mayor = ""

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 > num2 and num1 > num3:
    num_mayor = num1
if num2 > num1 and num2 > num3:
    num_mayor = num2
if num3 > num1 and num3 > num2:
    num_mayor = num3

print(f"El numero mayor es el {num_mayor}")
