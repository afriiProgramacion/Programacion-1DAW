def EliminaRepes(lista):
    salida = []
    for elemento in lista:
        if elemento not in lista:
            lista.append(elemento)
    return lista


lista1 = []
entrada = input("Introduce numeros repetidos: ")
numeros = entrada.split(',')


for i in lista1:
    lista1.append(int(i))
eliminar = EliminaRepes(lista1)

print(eliminar)