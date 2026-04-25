#Muestra la tabla de multiplicar de un número introducido por teclado.

def tablaMultiplicar(numero):
    for i in range(0,11,1):
        print(f"{numero} x {i} = {numero * i}")

if __name__=="__main__":
    try:
        n = int(input("Dime un número para saber su tabla: "))
    except ValueError:
        print("Valor inválido.")
    else:
        print(tablaMultiplicar(n))