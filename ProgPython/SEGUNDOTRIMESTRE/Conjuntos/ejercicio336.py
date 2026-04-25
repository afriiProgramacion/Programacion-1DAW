def pintaConjunto(c):
    resultado = ""

    for elemento in c:
        resultado += elemento + ','
    
    print(resultado)

def pintaConjuntoSort(c):
    uno = list(c)
    uno.sort()

    resultado = ""
    for elemento in uno:
        resultado+str(elemento) + ","
    if (len(resultado) > 0):
        print(resultado[:-1])


vocales = {'a', 'e', 'i', 'o', 'u'}
consonantes = ("bcdfghjklmnpqrstvwxyz")
consonantes = set(consonantes)

letras_comunes = vocales.intersection(consonantes)
pintaConjunto(vocales)
pintaConjunto(letras_comunes)
