"Desarrolle un programa que permita ingresar 3 números y desplegarlos de forma descendente"

num1 = ""
num2 = ""
num3 = ""
numeromayor = ""
numeromedio = ""
numeromenor = ""

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
num3 = int(input("Ingrese un tercer número: "))

if num1 > num2:
   if num1 > num3:
        numeromayor = num1
if num2 > num1:
    if num2 > num3:
        numeromayor = num2
if num3 > num1:
    if num3 > num2:
        numeromayor = num3


if num1 < num2:
    if num1 < num3:
        numeromenor = num1
if num2 < num1:
    if num2 < num3:
        numeromenor = num2
if num3 < num1:
    if num3 < num2:
        numeromenor = num3

numeromedio = (num1 + num2 + num3) - (numeromayor + numeromenor)

print(f"Los números en orden descendente son: {numeromayor}, {numeromedio} y {numeromenor}")