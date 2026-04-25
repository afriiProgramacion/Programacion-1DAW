import random

def generar_combinacion_primitiva():
    numeros = []

    while len(numeros) < 6:
        n = random.randint(1, 49)
        if n not in numeros:
            numeros.append(n)
    return numeros

combinacion = generar_combinacion_primitiva()
print(f"Tu combinación de la primitiva es: {combinacion}")