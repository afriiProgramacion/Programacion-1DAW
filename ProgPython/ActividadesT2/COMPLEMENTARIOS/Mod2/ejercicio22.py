numero = int(input("Introduce un número para saber si es par y/o divisible entre 5: "))

if numero % 2 == 0 or numero % 5 == 0:
    print("El número introducido es par y/o divisible entre 5: ")
else:
    print("El numero no es par ni tampoco divisible entre 5")