import os

def suma(a,b):
    return a+b

def resta(a,b):
    if a==b:
        return 0
    elif a<b:
        return b - a
    else:
        return a-b

def multiplica(a,b):
    return a*b

def divide(a,b):
    if b!= 0:
        return a/b
    else:
        return None
    
def raiz_cuadrada(a,b):
    return a ** b

def potencia(a,b):
    
    if b == 0:
        return 1
    else:
        return  a ** b

def factorial(a):
    resultado = 1

    if a < 0:
        return "NO SIRVEN NUMEROS NEGATIVOS"
    else:
        for i in range (0, a):
            return  resultado * i

def pintaMenu():

    
    print("1. SUMAR")
    print("2. RESTAR")
    print("3. MILTIPLICAR")
    print("4. DIVIDIR")
    print("5. RAÍZ CUADRADA")
    print("6. POTENCIA")
    print("7. FACTORIAL")
    print("0. SALIR DEL PROGRAMA!!")

if __name__ == "main":

    valor1 = 2
    valor2 = 4

    opcion = 1
    while opcion != 0:

        pintaMenu()
        opcion = int(input("ELIGE UNA OPCIÓN: "))

        match opcion:
            case 1: 
                print("LA SUMA ES: ", suma(valor1,valor2))
                os.system('pause')
            case 2: 
                print("LA RESTA ES: ", resta(valor1,valor2))
                os.system('pause')
            case 3: 
                print("LA MULTIPLICACIÓN ES: ", multiplica(valor1,valor2))
                os.system('pause')
            case 4: 
                print("LA DIVISIÓN ES: ", divide(valor1,valor2))
                os.system('pause')
            case 5: 
                print("LA RAÍZ CUADRADA ES: ", raiz_cuadrada(valor1))
                os.system('pause')
            case 6:
                print("LA POTENCIA ES: ", potencia(valor1))
                os.system('pause')
            case 7: 
                print("EL FACTORIAL ES: ", factorial(valor1))
                os.system('pause')
            case 0: print("HASTA LUEGO")
            case _: print("OPCIÓN NO VÁLIDA, POR FAVOR, INTRODUCE UNA OPCIÓN VALIDA: ")

