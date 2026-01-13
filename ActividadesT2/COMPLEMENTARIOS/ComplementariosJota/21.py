#Escribe un programa que dada una hora determinada (horas y minutos), calcule los
# segundos que faltan para llegar a la medianoche.

def cuentaMinutos(hora,minuto):
    segundosEnDía = 24 * 60 * 60
    segundosPasados = (hora * 60 * 60) + (minuto * 60)
    segundosRestante = segundosEnDía - segundosPasados
    return segundosRestante

try:
    hora = int(input("Dame una hora (0-23): "))
    if hora > 23 or hora < 0:
        print("La hora debe estar entre 0 y 23.")
    else:
        minuto = int(input("Ahora los minutos (0-59): "))
        if minuto < 0 or minuto > 59:
            print("Los minutos deben estar entre 0 y 59.")
        else:
            segundos = cuentaMinutos(hora, minuto)
except ValueError:
    print("Algún valor inválido.")
print(f"Faltan {segundos} restantes.")