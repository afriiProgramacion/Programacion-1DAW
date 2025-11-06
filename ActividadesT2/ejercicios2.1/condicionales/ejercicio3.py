def division (num1, num2):
    if num2 == 0:
        raise NameError("ERROR. EL DIVISOR NO PUEDE SER NUNCA 0")
    else:
        resultado = num1 / num2
        return print(f"El resultado es {resultado}")

#PROGRAMA PRINCIPAL

try:
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))

    division(num1,num2)

except Exception as ex:
    print(f"{ex} Debes introducir un divisor distinto de 0")