edad = int(input("Introduce tu edad: "))
ingresos = int(input("Introduce tus ingresos: "))

if edad >= 16 and ingresos >= 1000:
    print("Tiene que tributar")
else:
    print("No tiene que tributar")
