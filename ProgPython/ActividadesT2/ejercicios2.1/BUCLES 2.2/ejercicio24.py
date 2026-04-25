def primo(numero):
    for i in range (2, numero):
        if (numero%i) == 0:
            return False
        else:
            return True

numero = 1
numeros = []
cant_primos = 0

while numero != 0:
    numero = int(input("Introduce un número mayor que 1 (0 para finalizar): "))
    
    if primo(numero) == True:
        numeros.append(numero)

cant_primos = len(numeros)

print(f"La cantidad de números primos introducidos son: {cant_primos}")


