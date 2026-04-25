def votar (numero):
    if numero <18:
        return print("NO PUEDES VOTAR AÚN ERES MENOR DE EDAD")
    else:
        return print("ERES VÁLIDO PARA VOTAR, ERES MAYOR DE 18 AÑOS")

edad = int(input("INTRODUCE TU EDAD PARA SABER SI ERES VÁLIDO PARA VOTAR: "))

votar (edad)