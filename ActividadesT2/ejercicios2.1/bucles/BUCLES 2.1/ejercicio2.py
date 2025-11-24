def suma(a, total):
    return total + a

numero = ""
contador = 0
total = 0
maximo = None
minimo = None

while numero != "FIN":

    numero = input("INTRODUCE UN NÚMERO: ")

    if numero != "FIN":
        try:
            numero_int = int(numero)

            # Suma
            total = suma(numero_int, total)
            contador += 1

            # Máximo
            if maximo is None or numero_int > maximo:
                maximo = numero_int

            # Mínimo
            if minimo is None or numero_int < minimo:
                minimo = numero_int

        except ValueError:
            print("Error: introduce un número válido.")

# FIN DEL PROGRAMA
print("FIN DEL PROGRAMA, HASTA LUEGO :)")
print(f"Has introducido {contador} números")
print(f"La suma total es: {total}")
print(f"El número máximo es: {maximo}")
print(f"El número mínimo es: {minimo}")
