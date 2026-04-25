
#DEFINICIÓN DE VARIABLES

def MayorEdad (edad):
    if edad < 0 or edad > 120:
        raise NameError("IMPOSIBLE, ESA EDAD ESTÁ FUERA DEL RANGO")
    if edad >= 18:
        return  True
    else:
        return False

#MAIN

try: 
    edad = int(input("INTRODUCE TU EDAD: "))
    if MayorEdad(edad):
        print("Eres mayor de edad puedes pasar a  la discoteca")
    else:
        print("Toma un zumito de piña...")
except ValueError:
    print("DEBES INTRODUCIR UN VALOR ENTERO")
except Exception as ex:
    print(f"Ha ocurrido un error: {ex}")



