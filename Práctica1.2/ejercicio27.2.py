nombre = input("Introduce el nombre del producto: ")                                            # Se piden los datos al usuario
precio = float(input("Introduce el precio unitario del producto: "))
unidades = int(input("Introduce el número de unidades: "))

coste_total = precio * unidades                                                                 # Se calcula el coste total

print(f"{nombre} - Precio unitario: {precio:06.2f} €, Unidades: {unidades:03d}, Coste total: {coste_total:08.2f} €")