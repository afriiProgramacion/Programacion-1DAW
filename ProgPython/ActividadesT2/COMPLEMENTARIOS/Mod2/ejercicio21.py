

hora = int(input("Teclea una hora: "))
minutos = int(input("Teclea los minutos de esa hora: "))

segundos_transcurridos = hora * 3600 + minutos * 60
segundos_totales_dia = 24 * 3600
segundos_faltan = segundos_totales_dia - segundos_transcurridos

print("Segundos que faltan para la medianoche:", segundos_faltan)