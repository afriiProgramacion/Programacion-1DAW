numero = int(input("Introduce un número de tres cifras: "))

# Extraer cifras
centenas = numero // 100
unidades = numero % 10

# Comprobar si es capicúa
if centenas == unidades:
    print("El número es capicúa.")
else:
    print("El número NO es capicúa.")
