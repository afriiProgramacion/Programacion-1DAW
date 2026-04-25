#Realiza un programa que diga si un número introducido por teclado es par y/o divisible entre 5.

def Par(num):
    if num % 5 == 0:
        print("Es divisible entre 5.")
    elif num % 2 == 0:
        print("Es par.")
    else:
        print("Es impar.")

try:
    numero = int(input("Dime un número entero: "))
except ValueError:
    print("Valor erroneo.")
else:
    print(Par(numero))