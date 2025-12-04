# Pedir datos de las tres personas
nombre1 = input("Nombre 1: ")
anio1 = int(input("Año de nacimiento de " + nombre1 + ": "))

nombre2 = input("Nombre 2: ")
anio2 = int(input("Año de nacimiento de " + nombre2 + ": "))

nombre3 = input("Nombre 3: ")
anio3 = int(input("Año de nacimiento de " + nombre3 + ": "))

# Comparaciones
if anio1 == anio2 and anio2 == anio3:
    print("Los tres son de la misma quinta.")
elif anio1 == anio2:
    print(nombre1, "y", nombre2, "son de la misma quinta.")
elif anio1 == anio3:
    print(nombre1, "y", nombre3, "son de la misma quinta.")
elif anio2 == anio3:
    print(nombre2, "y", nombre3, "son de la misma quinta.")
else:
    print("Ninguno es de la misma quinta.")
