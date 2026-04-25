def ParImpar (num):

    if num % 2 == 0:
        return True
    else: 
        return False

#PROGRAMA PRINCIPAL
try:
    num = int(input("Introduce un número entero: "))

    if ParImpar(num):
        print(f"{num} ES UN NÚMERO PAR")
    else:
        print(f"{num} ES UN NÚMERO IMPAR")

except ValueError:
    print("ERROR. Debes introducir un número entero, sin decimales")