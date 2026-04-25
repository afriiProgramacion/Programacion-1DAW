def grupos (sexo, nombre):
    lista = ["H", "M"]
    if len(sexo)>1 or sexo not in lista:
        raise NameError("DEBES INTRODUCIR UN SEXO VÁLIDO") 
    else:
        if sexo == "M" and nombre[0]<"M":
            return True
        elif sexo == "H" and nombre[0]>"N":
            return True
        else:
            return False


# PROGRAMA PRINCICPAL

try:
    sexo = input("INTRODUCE TU SEXO ((H), PARA HOMBRE, (M), PARA MUJER): ")
    nombre = input ("INTRODUCE TU NOMBRE: ")

    if grupos(sexo, nombre):
        print("PERTENECES AL GRUPO A")
    else:
        print("PERTENECES AL GRUPO B")

except Exception as ex:
    print(f"ERROR. {ex}")

    