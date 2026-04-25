def puntuacion (puntos):
    if puntos < 0.0:
        raise NameError ("No puedes tener una puntuación por debajo de 0")
    elif puntos == 0.0:
        return 1
    elif puntos == 0.4:
        return 2
    else:
        return 3


#PROGRAMA PRINCIPAL
try:
    puntos = float(input("INTRODUCE TU PUNTUACIÓN: "))
    dinero = (puntos * 2400) + 2400
    resultado = puntuacion(puntos)


# PRUEBA PARA VER SI FUNCIONA CON EL MATCH
    
    match resultado:
        case 1: print(f"Inaceptable, tu puntuación es de {puntos}, por lo tanto tienes {dinero} euros")
        case 2: print(f"Aceptable, tienes una puntuación de {puntos}, por lo tanto tienes {dinero} euros")
        case 3: print(f"Meritorio, tienes una puntuación de {puntos}, por lo tanto tienes {dinero} euros, felicidades")


except Exception as ex:
    print(f"ERROR. {ex}")