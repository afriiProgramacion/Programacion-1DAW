import os


# Menu de una calculadora
def suma (a, b):
    resultado = a + b
    return resultado

def resta (a, b):
    if a==b:
        return 0
    elif a<b:
        return b - a
    else:
        return a - b

def multiplicar (a, b):
    resultado = a * b
    return resultado

def dividir (a, b):
    if b != 0:
        resultado = a / b
        return resultado
    else:
        return "Error: División por cero"
    
def raizCuadrada(a):
    if a >= 0:
        return a ** 0.5
    else:
        return "error: raíz cuadrada e un número negativo."

def factorial(a):
    if a < 0:
        return "Error: no existe el factorial de un número negativo."
    
    resultado = 1
    for i in range(1, a + 1):
        resultado *= i
    return resultado

def potencia(a,b):
    resultado = a ** b
    return resultado

def pintamenu():

    os.system('cls')
    print("Menu calculadora:")
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MULTIPLICAR")
    print("4. DIVIDIR")
    print("5. RAÍZ")
    print("6. FACTORIAL")
    print("7. POTENCIA")
    print("0. SALIR")

# Programa principal
if __name__=="__main__":
    n1 = 2
    n2 = 4

    option = 1
    while option != 0:
    
        pintamenu()

        option = int(input("Elige una opción: "))

        match option:
            case 1: 
                print("La suma es: ", suma(n1, n2))
                os.system ('pause')
            case 2: 
                print("La resta es: ", resta(n1, n2))
                os.system ('pause')
            case 3: 
                print("La multiplicación es: ", multiplicar(n1, n2))
                os.system ('pause')
            case 4: 
                print("La división es: ", dividir(n1, n2))
                os.system ('pause')
            case 5: 
                print("La raíz es: ", raizCuadrada(n1))
            case 6: 
                print("El factorial es: ", factorial(n1))
                os.system ('pause')
            case 7: 
                print("La potencia es: ", potencia(n1, n2))
                os.system ('pause')
            case 0: 
                print("HASTA LUEGO")
            case _: 
                print("Opción no válida")
                os.system ('pause')