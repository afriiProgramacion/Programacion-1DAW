
# DEFINICIÓN DE VARIABLES

def Renta (ingreso):
    if ingreso < 0:
        raise NameError("La renta no puede estar por debajo de 0")
    else:
        if ingreso < 10000:
            return 5
        elif ingreso < 20000:
            return 15
        elif ingreso < 35000:
            return 20
        elif ingreso < 60000:
            return 30
        else:
            return 45

# PROGRAMA PRINCIPAL

try:
    ingresos = int(input("INTRODUCE TU RENTA ANUAL: "))
    resultado = Renta(ingresos)
    if Renta(ingresos):
        print(f"Según tu renta anual te pertenece un {resultado}% de Tipo Impositivo")

except Exception as ex:
    print(f"ERROR. {ex}")