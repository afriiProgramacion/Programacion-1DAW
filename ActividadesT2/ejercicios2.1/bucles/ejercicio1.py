def suma(a, total):
    return total + a
def CalculoMedia(a):
    return a/contador

try:
    numero = ""
    contador = 0
    total = 0

    while numero != "FIN":
        numero = input("INTRODUCE UN NÚMERO: ")
        numero = int(numero)
        total = suma(numero)
        contador +=1
        media = CalculoMedia(total)

except:
    if numero == "FIN":
        print("FIN DEL PROGRAMA, HASTA LUEGO :)")
        print(f"Hay {contador} números")
        print(f"El total de la suma de los  números es: {total}")
        print(f"La média de los números es: {media}")
