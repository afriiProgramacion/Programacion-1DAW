#Escribe un programa que solicite dos números por teclado y nos diga si son primos gemelos
# o no. Dos números primos son gemelos cuando son primos, y además están separados por
# dos unidades. Por ejemplo, 3 y 5, 11 y 13, etc.

# import sympy

from sympy import isprime

n1 = int(input("Introduce valor 1: "))
n2 = int(input("Introduce valor 2: "))

if isprime(n1) and isprime(n2) and abs(n1 - n2)==2:
    print("Son primos gemelos.")
else:
    print("No son primos gemelos.")