def pintacombinacion(c):
    print(c)

combinacion = []

i = 0
while i < 6:
    try:
        numero = int(input(f"Introduce el {i} numero de la combinación: "))
        if (numero > 0) and (numero < 50):
            combinacion.append(numero)
            i+=1
        else:
            raise NameError("Fuera de Rango")
    except ValueError:
        print("Deben ser valores enteros dentro de rango")
    except Exception as e:
        print(e)

combinacion.sort()

if len(combinacion) == 6:
    pintacombinacion(combinacion)
else:
    print("Hubo algún error al introducir los números")