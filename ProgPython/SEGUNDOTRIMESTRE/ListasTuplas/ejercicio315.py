numeros = [12345678910]
numeros.reverse()

salida = ""
for elemento in numeros:
    salida = salida + str(elemento) + ","

print(salida[:-1])