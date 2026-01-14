frase = input("Dime una frase para analizar: ")
vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
contador = 0

try:
    for letra in frase:
        if letra in vocales:
            contador +=1
        print(f"Número de vocales: {contador}")
except TypeError:
    print("ERROR. La frase debe ser texto")
