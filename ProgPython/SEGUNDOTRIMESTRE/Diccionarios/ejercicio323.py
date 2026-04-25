
frutaprecio = {'Plátano': 1.35, 'Manzana': 0.80, 'Pera': 0.85, 'Naranja': 0.70}
fruta = input("Introduce una fruta (Con la primera letra mayúscula): ")
kilos = int(input("Introduce un número de kilos: "))

if fruta in frutaprecio:
    frutakilo = frutaprecio[fruta] * kilos
    print(f"La fruta cuesta {frutakilo:.2f} €")
else: 
    print("La fruta introducida no se encuentra en la lista")

