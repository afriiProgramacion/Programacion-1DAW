#El programa debe mostrar un menú con una lista de películas y una opción para salir. Si el
# usuario elige una de las películas, el programa mostrará una cita de esa película. Luego se
# debe mostrar nuevamente el menú para que el usuario elija otra película o decida salir.
# Ejemplo de ejecución:

import os

def menuPeliculas():
    print("1.Una cita de Forrest Gump.")
    print("2.Una cita de James Bond.")
    print("3.Una cita de star wars.")
    print("4.Una cita de El sexto sentido.")
    print("5.Una cita de El padrino.")
    print("6.Salir de la aplicación.")

opcion = -1

while opcion != 6:
    menuPeliculas()
    opcion = int(input("Elige una de las películas:"))
    match opcion:
        case 1:
            print("La vida es como una caja de bombones, nunca sabes que te va a tocar.")
        case 2:
            print("Me llamo Bond, James Bond.")
        case 3:
            print("Que la fuerza te acompañe.")
        case 4:
            print("Hasta luego Lucas.")
        case 5:
            print("Te haré una oferta que no podrás rechazar.")
        case 6:
            print("Saliendo del programa...")
        case _:
            print("Opción no válida.")