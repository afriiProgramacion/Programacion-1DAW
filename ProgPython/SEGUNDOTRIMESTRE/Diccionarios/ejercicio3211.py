def pintaDiccionario(d):
    for i in d.items():
        print(i)

cadena ="nif;nombre;email;teléfono;descuento\n01234567L;LuisGonzález;luisgonzalez@mail.com;656343576;12.5\n71476342J;MacarenaRamírez;macarena@mail.com;692839321;8\n63823376M;Juan JoséMarínez;juanjo@mail.com;664888233;5.2\n98376547F;CarmenSánchez;carmen@mail.com;667677855;15.7"
cadenaLineas = cadena.split('\n')
campos = cadenaLineas[0].split(';')

diccionario = {}

for i in range (1, len(cadenaLineas)):
    valores = cadenaLineas[i].split(';')
    diccionario[valores[0]] = {campos[1]: valores[1], campos[2]: valores[2], campos[3]: valores[3]}

pintaDiccionario(diccionario)