palabra = input("Dime una palabra: ")

palabra = list(palabra)
for vocal in "aeiou":
    if vocal in palabra:
        print(f"La vocal {vocal} está en {palabra.count(vocal)} veces repetida")