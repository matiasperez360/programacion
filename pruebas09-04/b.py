"Desarrolle un programa que permita ingresar un número, si es negativo debemos enviar un mensaje al usuario “Número inválido, reingrese” y debe volver a ingresar otro número, si es positivo enviamos un mensaje “Número correcto” y termina el programa"  

num = ""

num = int(input("ingrese un número: "))

if num >= 0:
    print("número correcto")
else:
    print("número inválido, reingrese")
    num = int(input("ingrese un número: "))
    if num >= 0:
     print("número correcto")
    else:
     print("número invalido")       


