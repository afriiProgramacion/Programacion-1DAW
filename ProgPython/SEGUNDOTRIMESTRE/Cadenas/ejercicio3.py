letra = input("Introduce una letra que quieras que busque: ")
frase = input("Introduceme una frase: ")

posicion = frase.find(letra)


if posicion <= -1:
    print("No se ha encontrado la letra")
else:
    print(f"{letra} se encuentra en la posicion: {posicion}")