frase = input("Introduceme una frase: ")
palabra = input("Introduce la palabra que quieres buscar: ")
try:
    if palabra in frase:
        print("La palabra está dentro de la frase")
    else:
        print("La palabra que has introducido no está dentro de la frase")

except TypeError:
    print("ERROR. La frase debe ser texto")