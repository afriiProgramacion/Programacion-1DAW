lotería = input("Introduce los números de la lotería (en este formato: xxxxx):")
listaloteria = list(lotería)
listaloteria = sorted(listaloteria)

print(f"Los números que has introducido ordenados de menor a mayor: {listaloteria}")