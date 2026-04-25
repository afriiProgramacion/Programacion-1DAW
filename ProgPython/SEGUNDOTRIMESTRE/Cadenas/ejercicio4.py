frase = input("Introduceme una frase: ")
letra = input("Introduce una letra que quieras que busque: ")

try:
    cantidad = frase.count(letra)
    print(f"la letra {letra} aparece {cantidad} veces")
except Exception as e:
    print(f"ERROR INESPERADO {e}")