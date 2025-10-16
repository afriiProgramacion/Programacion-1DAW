
a = float(input("Introduce el lado a: "))
b = float(input("Introduce el lado b: "))
c = float(input("Introduce el lado c: "))


s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
if area==0:
    print("No tengo solución para este triángulo, elige otro")
else:
    # Se muestra el resultado
    print(f"El área del triángulo es: {area:.2f}")