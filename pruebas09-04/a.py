"Realizar un programa que solicite ingresar 3 valores enteros y luego muéstrelos siempre negativos"

num1 = ""
num2 = ""
num3 = ""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))

if num1 > 0:
    num1 = num1 * -1
else:
    num1 = num1

if num2 > 0:
    num2 = num2 * -1
else:
    num2 = num2

if num3 > 0:
    num3 = num3 * -1
else:
    num3 = num3


print(f"Los números son: {num1}, {num2} y {num3}")            
