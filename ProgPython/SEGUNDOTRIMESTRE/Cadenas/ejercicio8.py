frase = input("Introduceme una frase: ")

try:
    print(f"Mayúsculas: {frase.upper()}")
    print(f"Minúsculas: {frase.lower()}")
except AttributeError:
    print("ERROR. Asegúrate de que la frase sea una cadena")
