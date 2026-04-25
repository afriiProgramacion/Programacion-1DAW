numeros = [1,2,3,4,5,6,7,8,9]
pares = []
for i in range (len(numeros)):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])  
    else:
        print(f"El número {numeros[i]} es impar")
print(f"Los números pares son: {pares}")