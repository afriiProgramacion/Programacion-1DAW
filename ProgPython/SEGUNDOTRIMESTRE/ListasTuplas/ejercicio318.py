palabra = input("Dime una palabra")

palabra1 = list(palabra)
palabra2 = list(palabra1)
palabra2.reverse()

if palabra1 == palabra2:
    print("PALÍDROMO")
else:
    print("NO ES PALÍNDROMO")