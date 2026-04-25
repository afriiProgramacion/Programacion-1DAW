mayor = 0
menor = 0
lista = [50, 75, 46, 22, 80, 65, 8]

for i in lista:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

print(f"El mayor es: {mayor}")
print(f"El menor es: {menor}")