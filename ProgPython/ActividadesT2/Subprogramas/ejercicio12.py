def resolver_segundo_grado(a, b, c):
    discriminante = b*2 - 4*a*c

    if discriminante < 0:
        return print("No tiene soluciones reales")

    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)

    return print(x1, x2)


num1 = int(input("Introduce un número: "))
num2 = int(input("Introduce otro número: "))
num3 = int(input("Introduce un último número: "))

resolver_segundo_grado(num1, num2, num3)