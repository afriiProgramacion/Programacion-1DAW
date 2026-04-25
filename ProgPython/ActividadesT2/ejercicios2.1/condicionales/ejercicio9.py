def pago(n):
    if n<4:
        return("entras gratis")
    elif n>=4 and n<=18:
        return("pagas 5 euros")
    else:
        return("pagas 10 euros")

#PROGRAMA PRINCIPAL

try:
    edad=int(input("Introduce tu edad: "))
    resultado=pago(edad)
    print(f"Segun tu edad {resultado}")
except ValueError:
    print("ERROR: valor no valido")