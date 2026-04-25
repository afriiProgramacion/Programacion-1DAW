def multiplica (num1, num2):
    resultado = 0
    for i in range (0, num2):
        resultado += num1
    return print(resultado)

n1 = int(input("INTRODUCE UN NÚMERO: "))
n2 = int(input("INTRODUCE OTRO NÚMERO: "))

multiplica(n1,n2)
