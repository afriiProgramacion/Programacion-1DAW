#Realiza un programa que pida una hora por teclado y que muestre luego buenos días,
# buenas tardes o buenas noches según la hora. Se utilizarán los tramos de 6 a 12, de 13 a 20 y de
# 21 a 5. respectivamente. Sólo se tienen en cuenta las horas, los minutos no se deben introducir por
# teclado.

def saludo(hora):
    if hora <=6 or hora ==12:
        dias = "Buenos días"
        return dias
    elif hora == 13 or hora <=20:
        tardes = "Buenas tardes"
        return  tardes
    else:
        noches = "Buenas noches"
        return noches

try:
    hora = int(input("Dime una hora: "))
except ValueError:
    print("Valor inválido.")
else:
    print(saludo(hora))