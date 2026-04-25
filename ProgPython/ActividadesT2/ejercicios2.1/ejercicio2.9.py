edad = int(input("Introduce tu edad: "))

if edad <= 4:
    precio = 0
    print("Puede entrar gratis")
elif edad >= 4 and edad <= 18:
    precio = 5
    print(f"Tiene que pagar {precio}€")
else:
    precio = 10
    print(f"Tiene que pagar {precio}€")