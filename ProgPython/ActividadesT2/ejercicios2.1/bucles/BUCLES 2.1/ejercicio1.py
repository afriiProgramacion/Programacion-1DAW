def suma(a, total):
    return total + a
def CalculoMedia(a, contador):
    return a/contador

numero = ""
contador = 0
total = 0

while numero != "FIN":
        numero = input("INTRODUCE UN NÚMERO: ")
        
        if numero != "FIN":
            try:
                
                numero_int = int(numero)
                total = suma(numero_int, total)
                contador +=1
                media = CalculoMedia(total, contador)
                
            except ValueError:
                print("ERROR. AÑADE NÚMEROS VÁLIDOS")

if numero == "FIN":
                    print("FIN DEL PROGRAMA, HASTA LUEGO :)")
                    print(f"Hay {contador} números")
                    print(f"El total de la suma de los  números es: {total}")
                    print(f"La média de los números es: {media}")                
