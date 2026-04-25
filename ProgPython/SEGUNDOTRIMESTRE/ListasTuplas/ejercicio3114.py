letrasDni = list("TRWAGMYFPDXBNJ")

dni = input("Introduce tu DNI completo sin espacios: ")
dni = dni.upper()

if len(dni) < 2 or not dni[:-1].isdigit() or not dni[-1].isalpha():
    print("Formato incorrecto. Debes introducir el numero seguido de la letra.")

else:
    try:
        numero = int(dni[:-1])
        letraUsuario = dni[-1]
        letraCorrecta = letrasDni[numero%23]
    except ValueError:
        print("Fallo en la conversión")
    except IndexError:
        print("Has meado fuera de tiesto")

    if letraUsuario == letraCorrecta:
        print("El DNI es correcto")
    else:
        print(f"La letra es incorrecta. Debería ser {letraCorrecta}")
    