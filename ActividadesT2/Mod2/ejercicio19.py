
import os

def MenuSemana():
    print("1. Lunes")
    print("2. Martes")
    print("3. Miercoles")
    print("4. Jueves")
    print("5. Viernes")


# PROGRAMA PRINCIPAL


try:
    semana = 1

    while semana != 0:
        MenuSemana()
        
        semana = int(input("Selecciona un número para elegir un día de la semana (0. Para terminar): "))
        
        match semana:
            case 1:
                print("Has elegido Lunes, los lunes toca: Base de datos, IPE y programación")
                os.system ('pause')
            case 2:
                print("Has elegido el martes, los martes tenemos: Base de datos, Entornos de desarrollo y Sistemas Informáticos")
                os.system ('pause')
            case 3: 
                print("Has elegido el miercoles, los miercoles tenemos: programación, digitalización, lenguaje de marcas, base de datos y sistemas informáticos")
                os.system ('pause')
            case 4:
                print("Has elegido el jueves, los jueves tenemos: Sostenibilidad, Lenguaje de marcas y Programación")
                os.system ('pause')
            case 5:
                print("Has elegido el viernes, porfin el último día de la semana, los viernes tenemos: IPE, Sistemas Informáticos y Entornos de Desarrollo")
                os.system ('pause')
            case 0:
                print("Adioooossss")

except ValueError:
    print("ERROR. Deben ser números enteros")