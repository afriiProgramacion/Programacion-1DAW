def invertir(d):
  
    invertido = {}               
    for clave, valor in d.items():   
        invertido[valor] = clave    
    return invertido             


d = {'hello': 'hola'}

nuevaEntrada = input("Introduce valores para poblar el diccionario: ('ing':'esp'): ")
listaEntradas = nuevaEntrada.split(',')

for entrada in listaEntradas:
    partes = entrada.split(':')           
    if len(partes) == 2:
        d[partes[0].strip()] = partes[1].strip()
    else:
        print(f"entrada inválida: {entrada}")

d1 = invertir(d)

fraseEsp = input("Dime una frase en español: ")
for palabra in fraseEsp.split():
    print(d.get(palabra, palabra))