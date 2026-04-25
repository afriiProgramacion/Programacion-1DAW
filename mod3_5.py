n = int(input("Introduce un número positivo: "))
factorial = 1
while (n>0):
    factorial = factorial * n
    n = n-1
print ("Resultado:", factorial)