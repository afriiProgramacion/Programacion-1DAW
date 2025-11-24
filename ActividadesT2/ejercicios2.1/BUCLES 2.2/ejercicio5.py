def CapitalObtenido (c, interes, a):
    ganancia = 0
    for i in range (0, a):
        ganancia = c +((c * interes)/ 100)
    return (ganancia)


cantidad_invertir =  float(input("Introduce la cantidad que quieres invertir: "))
interes_anual = float(input("Introduce el interés anual: "))
num_años = int(input("Introduce el número de años que vas a invertir: "))
for i in range (0, num_años):
    cantidad_invertir = CapitalObtenido(cantidad_invertir, interes_anual, num_años)
    print(f"EL CAPITAL FINAL ES {CapitalObtenido(cantidad_invertir, interes_anual, num_años)}")

