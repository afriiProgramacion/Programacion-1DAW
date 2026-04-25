#Escribe un programa que pida por teclado un día de la semana y que diga qué asignatura toca a
# primera hora ese día.

"""
Dependiendo de la opción elegida te dice que hay a primera hora de ese día.
Precondiciones:
    Las opciones deben ser numéricas y enteras.
Postcondición:
    Debe decirte que toca a primera el día elegido.
"""

def diaDeLaSemana():
    print("1.Lunes")
    print("2.Martes")
    print("3.Miércoles")
    print("4.Jueves")
    print("5.Viernes")


def Lunes():
    print("Los Lunes hay base de datos a primera.")

def Martes():
    print("Los Martes hay base de datos a primera.")

def Miercoles():
    print("Los Miercoles hay programación a primera.")

def Jueves():
    print("Los Jueves hay sostenibilidad a primera.")

def Viernes():
    print("Los Viernes hay IPE a primera.")

opcion = -1

try:
    while opcion != 0:
        diaDeLaSemana()
        opcion = int(input("Elige un día de la semana,(0 para salir):"))
        match opcion:
            case 1:
                Lunes()
            case 2:
                Martes()
            case 3:
                Miercoles()
            case 4:
                Jueves()
            case 5:
                Viernes()
            case 0:
                ("Es fin de semana, a descansar.")
            case _:
                print("Opción no válida.")
except ValueError:
    print("Algún valor no era correcto.")