#Escribe un programa que calcule el salario neto semanal de un trabajador en función del
# número de horas trabajadas y la tasa de impuestos de acuerdo a las siguientes hipótesis:
# • Las primeras 35 horas se pagan a tarifa normal.
# • Las horas que pasen de 35 se pagan a 1,5 veces la tarifa normal.
# • Las tasas de impuestos son:
# • Los primeros 500 euros son libres de impuestos.
# • Los siguientes 400 tienen un 25% de impuestos.
# • Los restantes un 45% de impuestos.
# Escribir nombre, salario bruto, tasas y salario neto.

"""
Calcula salario neto en funcion de las horas y el precio hora.
Parametros
    horas: tiempo en horas que se trabaja.
    tarifa: precio por hora que se debe cobrar.
Precondiciones
    horas y tarifas deben ser datos numéricos.
    tarifa tiene que pertenecer al rango [10-100]
PostCondición
    Se calcula el salario neto en función de horas extras y tasas de impuestos.
Return
    Devuelve el salario neto en formato decimal.
"""

def calculaNeto(horas,tarifa):
    if horas <= 35:
        bruto=horas * tarifa
    else:
        bruto= 35 * tarifa + (horas - 35) * 1.5 * tarifa

    if bruto < 500:
        neto = bruto
    else:
        if bruto > 900:
            tasas = 400 * 0.25 + (bruto - 900) * 0.45
            neto = 500 + 400 * 0.75 + (bruto-900)*0.55
        else:
            neto = 500 + (bruto -500)*0.25
            tasas = (bruto - 500) * 0.25
    return neto, tasas

nombre = input("Dime tu nombre: ")
try:
    hora=int(input("Dime las horas que has trabajado: "))
    tarifa=float(input("Dime el precio por hora: "))
except ValueError:
    print("Valores no válidos.")
else:
    tasas, neto=calculaNeto(hora,tarifa)
    print(f"El empleado es: {nombre}")
    print(f"El salario neto es: {neto}")
    print(f"Las tasas han sido: {tasas}")
