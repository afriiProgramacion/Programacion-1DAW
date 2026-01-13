
#Carne Vacuno

vacuno1 = 10
vacuno2 = 17
vacuno3 = 25

#Carne Cordero

cordero1 = 15
cordero2 = 25
cordero3 = 40

print("Introduce tipo de carne: ")
print("1. Vacuno")
print("2. Cordero")

carne = input("Introduce un tipo de carne: ")

match carne:
    case 1: carne = "vacuno"
    case 2: carne = "cordero"
    case _: print("Lla eleccion de carne ha sido errónea")

print("Introduce el tipo de coccion: ")
print("1. Casi cruda")
print("3. Bien hecha")


punto = int(input("Introduce el modo de coccion (1,2 ó 3) "))
if punto < 1 or punto > 3:
    print("Error de punto de coccion")
else:
    try:
        peso = int(input("Introduce el peso de la carne: "))
        peso = abs(peso)
    except ValueError:
        print("El peso odebe ser numérico")
    else:
        
        
        tiempo = 0
        if carne == "vacuno":
            match punto:
                case 1: 
                    tiempo = (vacuno1 * peso) / 400
                case 2:
                    tiempo = (vacuno2 * peso) / 400
                case 3:
                    tiempo = (vacuno1 * peso) / 400
                case _:
                    print("Valor no válido del punto")
        else:
            print("ERROR. Tipo de carne")
        
        print(f"Se necesita cocer durante {tiempo} minutos")
        print(f"Se necesita cocer durante {tiempo * 60} segundos")