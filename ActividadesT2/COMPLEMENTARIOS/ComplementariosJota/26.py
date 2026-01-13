#Diseñe un algoritmo que lea un número de tres cifras y determine si es capicúa.

numero = int(input("Ingrese un número de tres cifras: "))

if 100 <= numero <= 999:
    num_str = str(numero)
    if num_str[0] == num_str[2]:
        print(f"El número {numero} es capicúa.")
    else:
        print(f"El número {numero} NO es capicúa.")
else:
    print("El número ingresado no tiene tres cifras.")
