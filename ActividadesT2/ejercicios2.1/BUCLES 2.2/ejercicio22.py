digitosPares = 0
digitosImpares = 0

valor = input("Dame un valor: ")

for i in valor:
    aux = int(i)
    if aux%2 == 0:
        digitosPares += 1
    else:
        digitosImpares += 1

print(f"Has metido {digitosImpares} digitos impares y {digitosPares} digitos pares")