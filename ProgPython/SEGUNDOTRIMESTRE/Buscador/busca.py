def extraerEmail(cadena):
    if len(cadena) > 0:
        posicion_arroba = cadena.find('@')
        if posicion_arroba == -1:
            return None
        
        inicio = posicion_arroba
        while inicio > 0 and cadena[inicio] != '':
            inicio = inicio - 1

        fin = posicion_arroba
        while fin < len(cadena) - 1 and cadena[fin+1] != '':
            fin = fin+1

        return cadena[inicio:fin+1] 



nombre = input("Dime un email a ver si lo encuentro: ")
handler = open('mailbox.txt')

for linea in handler:
    palabras = linea.split()
    if len(palabras) > 0 and palabras [0] == 'From':
        email = extraerEmail(linea)
        if (nombre in linea):
            print(f"El día de la semana es: {palabras[2]}")
            print("Email encontrado: ", email)