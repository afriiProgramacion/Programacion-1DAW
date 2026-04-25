
import os

def MenuPelis():
    print("1. Una cita de Forrest Gump")
    print("2. Una cita de James Bond")
    print("3. Una cita de Star Wars")
    print("4. Una cita del Sexto Sentido")
    print("5. Una cita del padrino")
    print("6. Salir de la aplicación")


opcion = 0


while opcion != 6:
    
    MenuPelis()
    opcion = int(input("Introduce que cita quieres ver: "))
    match opcion:
        case 1:
            print("La vida es como una caja de bombones, nunca  sabes lo que te va a tocar...")
            os.system ('pause')
        case 2:
            print("Ponga las dos manos en el volante, soy un pasajero muy nervioso.")
            os.system ('pause')
        case 3:
            print("Que la fuerza te acompañe lucas")
            os.system ('pause')
        case 4:
            print("Solo ven lo que quieren ver")
            os.system ('pause')
        case 5:
            print("Voy a hacerle una oferta que no podrá rechazar")
            os.system ('pause')
        case 6:
            print("Hasta luego, Lucas")


