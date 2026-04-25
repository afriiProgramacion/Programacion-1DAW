cesta = input("Introduce los productos de tu cesta de compra separados por coma: ")

coma = cesta.split(",")

for cesta in coma:
    print(cesta.strip())