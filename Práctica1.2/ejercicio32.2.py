# Calcula la serie de Fibonacci hasta un número dado

num = int(input("Hasta que número de la secuencia?: "))

i = 0
j=1
punta=i+j

print (i)
print (j)
print (punta)

while (punta<=num):
    i=j
    j=punta
    punta=i+j
    if punta<=num:
        print(punta)