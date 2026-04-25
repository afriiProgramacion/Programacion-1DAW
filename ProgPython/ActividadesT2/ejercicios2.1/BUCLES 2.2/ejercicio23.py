titulos = ""
total_lineas = 0
linea_actual = ""
while titulos != "*":
    titulos = input("Introduce títulos de libros (* para finalizar y / cuando termine linea): ")

if titulos == "/":
    total_digitos = 0

    for titulo in linea_actual:
        for caracter in titulo:
            if caracter in "0123456789":
                total_digitos +=1
    print(f"Dígitos numéricos en esta línea: {total_digitos}")

    total_lineas +=1
    linea_actual = ""

else:
    linea_actual = linea_actual + titulos

print("\n Total de líneas completas ingresadas: ", total_lineas)
