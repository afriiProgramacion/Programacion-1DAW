frase = input("Dime una frase: ")
letra = input("Dime una letra: ")

encontrado = False
i = 0

while i <len(frase) and (not encontrado):
    if frase[i] == letra:
        print(f"La letra {letra} ha sido encontrada dentro de la frase en la posicion {i}")
        encontrado = True
    i += 1

if not encontrado:
    print("La letra no se encuentra en la frase...")