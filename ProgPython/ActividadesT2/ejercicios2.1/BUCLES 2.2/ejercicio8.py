def triangulo (num):
    for i in range (1, num +1):
        linea = ""
        for j in range(2*i-1, 0, -2):
            linea = linea + str(f" {j}")
        print (linea)

num = int(input("Introduce un número positivo: "))
triangulo(num)