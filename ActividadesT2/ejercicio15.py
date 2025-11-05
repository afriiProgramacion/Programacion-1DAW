def notas (nota):
    if nota <= 4:
        print ("INSUFICIENTE")
    elif nota == 5:
        print ("SUFICIENTE")
    elif nota == 6:
        print ("BIEN")
    elif nota == 7 or nota == 8:
        print ("NOTABLE")
    elif nota == 9 or nota == 10:
        print ("SOBRESALIENTE")

nota = float(input("INTRODUCE UNA NOTA CON DECIMALES: "))

nota = int(nota)

notas (nota)