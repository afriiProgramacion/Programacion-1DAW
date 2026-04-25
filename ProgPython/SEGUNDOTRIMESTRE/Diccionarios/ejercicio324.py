meses = {'01': 'Enero', 
         '02': 'Febrero', 
         '03': 'Marzo', 
         '04': 'Abril', 
         '05': 'Mayo', 
         '06': 'Junio', 
         '07': 'julio',
         '08': 'agosto',
         '09': 'septiembre',
         '10': 'octubre',
         '11': 'noviembre',
         '12': 'diciembre'
         }

print("Introduce una fecha en formato dd/mm/aaaa")

dia = int(input("Introduce el día: "))
mes = input("Introduce el mes: ")
año = int(input("Introduce el año: "))

print(f"La fecha es: {dia} de {meses[mes]} del {año}")