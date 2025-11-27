def sumaDigito (a):
    while numero>0:
        suma+=a%10
        a = a//10
    return suma

def isPar (a):
    if a % 2 == 0:
        return True
    else:
        return False

numero = 0
pares = 0

while numero != -1:
    numero = int(input("Introduce un número: "))
    print(f"La suma de los digitos de este número es: {sumaDigito(numero)}")
    if isPar(numero):
        pares += 1

print(f"El numero de pares ha sido {pares}")

