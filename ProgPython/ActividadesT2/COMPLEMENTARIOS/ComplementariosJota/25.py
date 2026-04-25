#Diseña un algoritmo en el que se solicite un número por teclado y nos diga si es múltiplo de
# 2, de 3, de ambos o de ninguno. Por ejemplo, 6 es múltiplo de 2 y de 3; 4 es múltiplo de 2, 9
# es múltiplo de 3 y 5 no es múltiplo de ninguno.

def multiplo(a):
    if a % 2 == 0 and a % 3 == 0:
        print("Es múltiplo de ambos.")
    elif a % 2 == 0:
        print("Es múltiplo de 2.")
    elif a % 3 == 0:
        print("Es múltiplo de 3.")
    else:
        print("No es múltiplo de ninguno.")

try:
    numero = int(input("Dime un número y te digo si es múltiplo de 2, de 3, de ambos o de ninguno:"))
    print(multiplo(numero))
except ValueError:
    print("Valor no válido.")
