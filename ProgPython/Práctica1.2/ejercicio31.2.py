# mostrar la descomposición factorial


from sympy import isprime
num = int(input("Dame un número: "))

# Comprueba que no es un número primo
if isprime(num):
    print(f"Es un número primo y no tiene divisores, el único es el mismo: {num}")
else:
    if (num < 4):
        print("Demasiado pequeño para descomponer, por favor, mayor que 4.")
    else:
        i = 2
        while (i <= num):
            if(num %i == 0):
                print("{:3d} Es un divisor" .format(i))
                num = num // i
            else:
                i = i + 1