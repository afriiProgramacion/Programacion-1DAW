frase = input("Introduceme una frase: ")

try:
    limpia = frase.strip()
    print(f"Frase sin espacios {limpia}")

except AttributeError:
    print("ERROR. La variable no es una cadena")