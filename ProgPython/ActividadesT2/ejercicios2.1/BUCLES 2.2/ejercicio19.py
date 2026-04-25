def MuestraMenu():
    print("1. Comenzar Programa")
    print("2. Imprimir listado")
    print("3. Finalizar Programa")

    opcion = 1

    while opcion != 3:
        MuestraMenu()
        opcion = int(input("ELIGE UNA OPCION: "))
        match opcion:
            case 1:
                print("EL PROGRAMA HA INICIADO")
            case 2:
                print("Listado")
            case 3:
                print("Adiós")
            case _:
                print("Valor no válido, introduce otro")


    