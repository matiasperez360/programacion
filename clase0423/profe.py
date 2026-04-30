positivos = 0
x = 1
z = int(input("Cuantos números desea ingresar: "))
while x <= z:
   num = int(input(f"Ing. número [{x} de {z}]: "))
   if num > 0:
      positivos = positivos + 1

   x = x + 1

print(f"Positivos ingresados = {positivos}")