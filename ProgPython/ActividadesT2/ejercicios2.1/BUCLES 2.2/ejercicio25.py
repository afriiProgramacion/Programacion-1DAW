frase = input("Ingresa una frase: ")

palabras = frase.split(" ")

cantidad_palabras = 0
palabra_mas_larga = ""
longitud_maxima = 0

for palabra in palabras:
    cantidad_palabras += 1
    if len(palabras) > longitud_maxima:
        longitud_maxima = len(palabra)
        palabra_mas_larga = palabra

print(f"Cantidad de palabras: {cantidad_palabras}")
print(f"Palabra mas larga: {palabra_mas_larga}")