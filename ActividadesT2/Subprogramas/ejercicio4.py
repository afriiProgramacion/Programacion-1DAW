def par(num):
    if num % 2 == 0:
        return print("ES PAR")
    else:
        return print("NO ES PAR / ES IMPAR")

numero = int(input("INTRODUCE UN NÚMERO PARA SABER SI ES PAR: "))

par(numero)