def contar_palabras(texto):
    palabras = texto.split()  # separa por espacios
    conteo = {}
    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

# Ejemplo
t = "hola mundo hola python mundo"
print(contar_palabras(t))
# {'hola': 2, 'mundo': 2, 'python': 1}
