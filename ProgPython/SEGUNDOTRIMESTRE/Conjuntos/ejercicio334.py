frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

set_frutas1 = set(frutas1)
set_frutas2 = set(frutas2)


frutasComunes = set_frutas1.intersection(set_frutas2)
print("Frutas Comunes: ", frutasComunes)

frutas_solo_en_frutas1 = set_frutas1.difference(set_frutas2)
print(f"\nFrutas que solo están en frutas 1: {frutas_solo_en_frutas1}")

frutas_solo_en_frutas2 = set_frutas2.difference(set_frutas1)

print(f"\nFrutas que solo están en frutas 2: {frutas_solo_en_frutas2}")


frutas_raras = frutas_solo_en_frutas1.union(frutas_solo_en_frutas2)
print(f"\nFrutas raras: {frutas_raras}")