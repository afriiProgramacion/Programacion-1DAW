numeros = [1,1,1,2,3,4,5,6,7,8,8,8,5,9]

sin_duplicar = []

for i in numeros:
    if i not in sin_duplicar:
        sin_duplicar.append(i)

duplicados = []
for i in numeros:
    if numeros.count(i) > 1 and i not in duplicados:
        duplicados.append(i)
duplicados = tuple(duplicados)

conjunto = set()
for i in numeros:
    if numeros.count(i) == 1:
       conjunto.add(i)

print(f"Sin duplicar: {sin_duplicar}")
print(f"Duplicados: {duplicados}")
print(f"Elementos únicos: {conjunto}")
