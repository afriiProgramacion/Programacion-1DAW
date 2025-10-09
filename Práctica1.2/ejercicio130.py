numero = int(input("Introduce un número entero: "))

i = 2
encontrado = False

while (i<(numero//2)) and (not encontrado):
    if (numero%i==0):
        encontrado=True
    i=i+1


if encontrado:
    print("NO ES PRIMO")
else:
    print ("ES PRIMO")
    