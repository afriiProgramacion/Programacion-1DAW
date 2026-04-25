lista=["a","e","i","o","u"]
def contar(p):
    contador = 0
    for i in p.lower():
        if i in lista:
            contador = contador+1
    return print(contador)
palabra=input("Introduce una palabra: ")
contar(palabra)