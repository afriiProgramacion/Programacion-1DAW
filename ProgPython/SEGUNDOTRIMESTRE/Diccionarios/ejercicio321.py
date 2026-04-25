diccionario = {'Euro': '€','Dollar': '$', 'Yen': '¥'}
divisa = input("Introduce una divisa: ")


if divisa in diccionario:
    print(diccionario[divisa])
else:
    print("La divisa no está en el diccionario")