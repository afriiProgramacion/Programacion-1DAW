puntos = float(input("Introduce tu puntuación:  "))
salario = 2400
dinero = puntos * salario

if puntos <= 0.0:
    print(f"Inaceptable, tu puntuación es {puntos}, tu cantidad de dinero ahora mismo es {dinero}€")
elif puntos == 0.4:
    print(f"Aceptable, tu puntuación es de {puntos}, tu cantidad de dinero es de {dinero}€")
else:
    print(f"Meritorio, tu puntuación es de {puntos}, así que tu cantidad de dinero es {dinero}€")
