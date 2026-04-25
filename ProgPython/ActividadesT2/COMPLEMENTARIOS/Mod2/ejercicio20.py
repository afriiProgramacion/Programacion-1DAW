
hora = int(input("Introduce la hora en formato 24h: "))

if hora >= 6 or hora <= 12:
    print("Buenos dias")
elif hora >= 13 or hora <= 20:
    print("Buenas Tardes")
elif hora >= 21 or hora <= 5:
    print("Buenas Noches")