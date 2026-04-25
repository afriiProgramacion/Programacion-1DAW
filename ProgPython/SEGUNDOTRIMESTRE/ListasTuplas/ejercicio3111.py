vector1 = [1, 2, 3]
vector2 = [-1, 0, 2]
producto_escalar = 0

for i in range (0, len(vector1)):
    producto_escalar += vector1[i] * vector2[i]

print(f"El producto escalar es: {producto_escalar}")