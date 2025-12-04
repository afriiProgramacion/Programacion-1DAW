def CalculoNeto (Horas, Tarifa):
    if Horas <= 35:
        bruto = Horas * Tarifa
    else:
        bruto = 35 * Tarifa + (Horas - 35) * 1.5 * Tarifa
    
    if bruto < 500:
        neto = bruto
    elif bruto > 900:
        tasas = 400 * 0.25 + (bruto - 900) * 0.45
        neto = 500 + 400 * 0.75 + (bruto - 900) * 0.55
    else: 
        neto = 500 + (bruto - 500) * 0.25
        tasas = (bruto - 500) * 0.25

    return neto


# PROGRAMA PRINCIPAL

nombre = input("¿Cómo te llamas?: ")

try:
    horas = int(input("¿Cuántas horas has trabajado?: "))
    tarifa = float(input("Dime el precio por hora: "))
    
except ValueError:
    print("Valores no válidos, deben ser numéricos.")

else:
    neto = CalculoNeto(horas, tarifa)
    print(f"El empleado es: {nombre}")
    print(f"El salario neto es: {neto}")
    print(f"Las tasas han sido: {horas * tarifa - neto}")