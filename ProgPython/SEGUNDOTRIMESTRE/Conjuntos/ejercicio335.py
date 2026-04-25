def pintaConjunto(c):
    resultado = ""

    for elemento in c:
        resultado += elemento + ','
    
    print(resultado)

def conjuntoPares(c):
    pares = set()
    for elemento in c:
        if elemento%2 == 0:
            pares.add(elemento)
    if len(pares) > 0:
        return pares
    else:
        raise NameError ("No existen elementos")

def multiplos_de_3(numeros):
    resultado = []
    for numero in numeros:
        if numero % 3 == 0:
            resultado.append(numero)
    return resultado

def paresY3 (x, y):
    z = x&y
    if len(z) > 0:
        return z
    else:
        raise NameError ("No existen elementos")
    

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

pares = conjuntoPares(numeros)
print(f"Números pares dentro del conjunto: {pares}")

multiplos_de_tres = multiplos_de_3(numeros)
print(f"Múltiplos de 3: {multiplos_de_tres}")

pares_y_multiplos_de_3 = paresY3(numeros, pares)

print("Números pares y múltiplos de 3: ", pares_y_multiplos_de_3)

if numeros.issuperset(pares) == True:
    print("Números es un super conjunto de Pares")
else:
    print("Números no es un super conjunto de Pares")