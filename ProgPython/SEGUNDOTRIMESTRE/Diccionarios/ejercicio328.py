d = {
    'hola': 'hello',

}

nuevaEntrada = input("Introduce valores para poblar el diccionario: ('esp'0:'ing'): ")
listaEntradas = nuevaEntrada.split(',')

if len(listaEntradas) <1:
    print("Valores no válidos")
else:
    for entrada in listaEntradas:
        subcadena = entrada.split(',')
        d[subcadena[0]] = subcadena[1]

fraseEsp = input("Dime una frase en español: ")
listaPalabras = fraseEsp.split()

for palabra in listaPalabras:
    if palabra in d:
        print(f"{d[palabra]}")
    else:
        print(palabra)