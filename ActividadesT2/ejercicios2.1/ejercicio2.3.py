dividendo = int(input("Introduce un número para el dividendo: "))
divisor = int(input("Introduce otro número para el divisor: "))
division = dividendo / divisor

if divisor == 0:
    print("Error, el divisor no puede ser 0")
else:
    print(f"El resultado de la division es {division}")