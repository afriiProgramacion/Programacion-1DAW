texto = input("Introduce un texto: ")

try:
    nuevo_texto = texto.replace("Java", "Python")
    print(nuevo_texto)
except AttributeError:
    print("ERROR. Asegurate de que el texto sea una cadena")
