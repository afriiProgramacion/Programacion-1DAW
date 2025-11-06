def tributa (edad, ingresos):
    if edad < 0 or edad > 120:
        raise NameError ("La edad está fuera del rango")
    else:
        if ingresos >= 1000 and edad >= 16:
            return True
        else:
            return False

try:
    edad = int(input("Introduce tu edad: "))
    
    if edad < 0 or edad > 120:
        raise NameError ("La edad está fuera del rango")
    
    ingresos = int(input("Introduce tu nivel de ingresos: "))

    if tributa (edad, ingresos):
        print(f"Tienes {edad} años y unos ingresos de {ingresos} euros, por lo tanto, tienes que tributar")
    else:
        print("No puedes Tributar aún, no cumples con los requisitos")

except Exception as ex:
    print(f"HA OCURRIDO UN ERROR {ex}")
