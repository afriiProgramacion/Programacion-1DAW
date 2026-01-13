#Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras.
# El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el
# mensaje “Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se
# ha abierto satisfactoriamente”. Tendremos cuatro oportunidades para abrir la caja fuerte.

contraseña = 1234

i = 0
acertado = False

while (1<4) and (not acertado):
    print(f"Introduce la contraseña (intento {i}): ")
    
    intento = int(input())
    
    if (intento<1000) or (intento>9999):
        print("ERROR: Debe ser un número de 4 cifras.")
    else:
        if intento == contraseña:
            print("La caja se ha abierto satisfactoriamente.")
            acertado = True
        else:
            print("Lo siento esa no es la combinación.")
    i = i + 1