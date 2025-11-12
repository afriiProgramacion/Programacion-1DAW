def menu ():
    print("ELIGE TU PIZZA")
    print("1. PIZZA VEGETARIANA")
    print("2. PIZZA NO VEGETARIANA")

def pizzavegetariana ():
    print ("HAS ELEGIDO LA PIZZA VEGETARIANA, ELIGE LOS INGREDIENTES: ")
    print ("1. PIMIENTO")
    print ("2. TOFU")

def no_vegetariana ():
    print ("HAS ELEGIDO PIZZA NO VEGETARIANA, ELIGE LOS INGREDIENTES: ")
    print ("1. PEPPERONI")
    print ("2. JAMÓN")
    print ("3. SALMÓN")

def principal ():
    option = 0
    menu()
    vegetariana = int(input("INTRODUCE UNA OPCIÓN: "))
    match option: 
        case 1:
            return True
        case 2:
            return False

#PROGRAMA PRINCIPAL
try:

    IngredienteEspecial = ""
    vegetariana = principal()
    if vegetariana:
        pizzavegetariana()
        option = int(input("INTRODUCE UN INGREDIENTE VEGETARIANO: "))
        match option:
            case 1:
                IngredienteEspecial = "PIMIENTO"
            case 2: 
                IngredienteEspecial = "TOFU"
            case _:
                print("OPCIÓN NO VÁLIDA")
    else:
        option = int(input("ELIGE ENTRE SOLO UN INGREDIENTE: "))
        no_vegetariana()
        match option:
            case 1:
                IngredienteEspecial = "PEPPERONI"
            case 2: 
                IngredienteEspecial = "JAMON"
            case 3: 
                IngredienteEspecial = "SALMON"
            case _:
                print("OPCIÓN NO VÁLIDA")

    print("LA PIZZA ELEGIDA ES:"+IngredienteEspecial)
except ValueError:
    print("ERROR")